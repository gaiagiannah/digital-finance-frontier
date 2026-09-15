#!/usr/bin/env python3
"""
Anomaly Detection — Digital Finance Frontier
Autoencoder + Isolation Forest for on-chain transaction anomalies.

Usage:
    python3 anomaly_detection.py --data data/transactions.csv --method autoencoder
    python3 anomaly_detection.py --data data/transactions.csv --method isolation

Requires:
    pip install torch pandas numpy scikit-learn
"""

import argparse
import json
from pathlib import Path

"""
APPROACHES:

1. Autoencoder:
   - Train on "normal" transactions
   - Reconstruction error > threshold = anomaly
   - Features: amount, velocity, time-of-day, counterparty count, gas

2. Isolation Forest:
   - Unsupervised (no labels needed)
   - Anomalies are "isolated" faster in random splits
   - Good for high-dimensional transaction features

3. Hybrid (recommended):
   - Isolation Forest for initial flagging
   - Autoencoder for scoring
   - GNN for graph-level anomalies (see gnn_aml.py)

TARGET:
   - Detect: Burst patterns, round-number transfers, velocity anomalies,
     new counterparty spikes, unusual time-of-day activity
   - False positive rate: <5% at 95% recall
"""


def build_autoencoder():
    """Build anomaly detection autoencoder."""
    try:
        import torch
        import torch.nn as nn

        class TransactionAutoencoder(nn.Module):
            def __init__(self, input_dim=16, hidden_dim=64, latent_dim=8):
                super().__init__()
                self.encoder = nn.Sequential(
                    nn.Linear(input_dim, hidden_dim),
                    nn.ReLU(),
                    nn.Linear(hidden_dim, hidden_dim // 2),
                    nn.ReLU(),
                    nn.Linear(hidden_dim // 2, latent_dim),
                )
                self.decoder = nn.Sequential(
                    nn.Linear(latent_dim, hidden_dim // 2),
                    nn.ReLU(),
                    nn.Linear(hidden_dim // 2, hidden_dim),
                    nn.ReLU(),
                    nn.Linear(hidden_dim, input_dim),
                )

            def forward(self, x):
                z = self.encoder(x)
                return self.decoder(z), z

        return TransactionAutoencoder()
    except ImportError:
        print("[ERROR] torch not installed. pip install torch")
        return None


def build_isolation_forest():
    """Build Isolation Forest anomaly detector."""
    try:
        from sklearn.ensemble import IsolationForest
        model = IsolationForest(
            n_estimators=200,
            max_samples="auto",
            contamination=0.05,  # Assume 5% anomalies
            random_state=42
        )
        return model
    except ImportError:
        print("[ERROR] scikit-learn not installed. pip install scikit-learn")
        return None


def extract_features(transactions: list[dict]) -> list[list[float]]:
    """Extract feature vector per transaction.
    
    Features (16-dim):
    0: Amount (log-scaled)
    1: Velocity (txs/min for sender)
    2: Time-of-day (sin)
    3: Time-of-day (cos)
    4: Day-of-week (sin)
    5: Day-of-week (cos)
    6: Unique counterparties (sender, log-scaled)
    7: Is round number (0/1)
    8: Amount z-score (sender's history)
    9: Time since sender's last tx (log-scaled)
    10: Time since receiver's first tx (log-scaled)
    11: Is new counterparty (0/1)
    12: Gas used (log-scaled)
    13: Is contract call (0/1)
    14: Token type (0=native, 1=ERC20, 2=stablecoin)
    15: Burst score (txs in last 60s / 5)
    """
    import math
    import time

    features = []
    for tx in transactions:
        amount = tx.get("amount", 0)
        timestamp = tx.get("timestamp", 0)
        hour = (timestamp % 86400) / 3600.0
        dow = (timestamp % 604800) / 86400.0

        features.append([
            math.log1p(amount) if amount > 0 else 0,
            tx.get("velocity", 0),
            math.sin(2 * math.pi * hour / 24),
            math.cos(2 * math.pi * hour / 24),
            math.sin(2 * math.pi * dow / 7),
            math.cos(2 * math.pi * dow / 7),
            math.log1p(tx.get("counterparties", 1)),
            1.0 if _is_round_number(amount) else 0.0,
            tx.get("amount_zscore", 0),
            math.log1p(tx.get("time_since_last", 0)),
            math.log1p(tx.get("receiver_age", 0)),
            1.0 if tx.get("is_new_counterparty", False) else 0.0,
            math.log1p(tx.get("gas_used", 0)),
            1.0 if tx.get("is_contract", False) else 0.0,
            tx.get("token_type", 0),
            tx.get("burst_score", 0),
        ])
    return features


def _is_round_number(amount: float) -> bool:
    """Check if amount is a 'round' number (1.0, 10.0, 100.0, etc.)"""
    if amount == 0:
        return False
    log_val = int(round(__import__('math').log10(amount)))
    round_base = 10 ** log_val
    return abs(amount / round_base - round(amount / round_base)) < 0.001


def main():
    parser = argparse.ArgumentParser(description="Anomaly Detection — Digital Finance Frontier")
    parser.add_argument("--data", required=True, help="Input CSV with transactions")
    parser.add_argument("--method", default="hybrid", choices=["autoencoder", "isolation", "hybrid"])
    parser.add_argument("--threshold", type=float, default=0.95, help="Anomaly threshold (percentile)")
    parser.add_argument("--output", help="Output file for flagged transactions")
    args = parser.parse_args()

    print("=" * 60)
    print("Anomaly Detection — Digital Finance Frontier")
    print("=" * 60)
    print(f"  Data: {args.data}")
    print(f"  Method: {args.method}")
    print(f"  Threshold: {args.threshold}")
    print()
    print("Features (16-dim):")
    print("  amount, velocity, time-of-day (sin/cos), day-of-week (sin/cos),")
    print("  counterparties, round-number, z-score, time-since-last,")
    print("  receiver-age, new-counterparty, gas, contract, token-type, burst")
    print()
    print("Production Notes:")
    print("  - Train on 30+ days of 'normal' transactions")
    print("  - Retrain weekly (concept drift)")
    print("  - Monitor false positive rate in production")
    print("  - Alert on: burst > 5 txs/min, round numbers > $10K,")
    print("    new counterparty + high amount, unusual time-of-day")


if __name__ == "__main__":
    main()    