#!/usr/bin/env python3
"""
Chain Analysis Tool — Digital Finance Frontier
On-chain transaction tracing, clustering, and cross-referencing.

Usage:
    python3 chain_analysis.py --chain ethereum --address 0x...
    python3 chain_analysis.py --chain ethereum --address 0x... --depth 3 --min-eth 100
    python3 chain_analysis.py --chain ethereum --address 0x... --cross-reference --seed-file seeds.json

Requires:
    pip install web3 requests pandas numpy
"""

import argparse
import json
import hashlib
import time
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from pathlib import Path


@dataclass
class Transaction:
    hash: str
    from_address: str
    to_address: str
    value: float
    timestamp: int
    block: int
    gas_used: int
    status: int
    token_transfers: list = field(default_factory=list)


@dataclass
class Entity:
    address: str
    label: str = "unknown"
    confidence: float = 0.0
    first_seen: Optional[int] = None
    last_seen: Optional[int] = None
    total_in: float = 0.0
    total_out: float = 0.0
    tx_count: int = 0
    links: list = field(default_factory=list)


class ChainAnalyzer:
    """On-chain analysis with cross-referencing capability.
    
    Production deployment would connect to:
    - Alchemy / Infura / Etherscan API (Ethereum)
    - Helius / Solana RPC (Solana)
    - Chainalysis / TRM Labs / Elliptic (entity resolution)
    - Neo4j (graph storage)
    """

    def __init__(self, chain: str = "ethereum", api_key: Optional[str] = None):
        self.chain = chain
        self.api_key = api_key
        self.transactions: list[Transaction] = []
        self.entities: dict[str, Entity] = {}
        self.graph_edges: list[tuple[str, str, float]] = []

    def get_transactions(self, address: str, start_block: int = 0,
                         end_block: Optional[int] = None) -> list[Transaction]:
        """Fetch transactions for an address."""
        print(f"[INFO] Fetching transactions for {address} on {self.chain}")
        print(f"[INFO] Block range: {start_block} to {end_block or 'latest'}")
        print(f"[NOTE] Connect to Alchemy/Infura/Etherscan for live data")
        print(f"[NOTE] For entity resolution: Chainalysis/TRM Labs/Elliptic")
        return self.transactions

    def trace_flow(self, address: str, depth: int = 2,
                   min_value: float = 0) -> dict:
        """BFS fund flow tracing."""
        print(f"[INFO] Tracing flow from {address} (depth={depth}, min={min_value})")
        visited = set()
        queue = [(address, 0)]
        nodes = []
        edges = []

        while queue:
            current, current_depth = queue.pop(0)
            if current in visited or current_depth > depth:
                continue
            visited.add(current)
            nodes.append({"address": current, "depth": current_depth})

            for tx in self._get_txs_for(current):
                if tx.value < min_value:
                    continue
                edges.append({
                    "from": tx.from_address,
                    "to": tx.to_address,
                    "value": tx.value,
                    "timestamp": tx.timestamp
                })
                if current_depth + 1 <= depth:
                    queue.append((tx.to_address, current_depth + 1))
                    queue.append((tx.from_address, current_depth + 1))

        return {"start": address, "depth": depth, "nodes": nodes, "edges": edges}

    def _get_txs_for(self, address: str) -> list[Transaction]:
        """Get transactions for an address (placeholder)."""
        return [tx for tx in self.transactions
                if tx.from_address == address or tx.to_address == address]

    def cluster_addresses(self, addresses: list[str]) -> dict[str, list[str]]:
        """Heuristic clustering."""
        print(f"[INFO] Clustering {len(addresses)} addresses")
        clusters = {}
        # Heuristic 1: Common input (Bitcoin)
        # Heuristic 2: Sequential funding
        # Heuristic 3: Common destination
        # Heuristic 4: Temporal proximity
        # Production: Use Chainalysis/Elliptic/TRM Labs
        return clusters

    def cross_reference(self, seed_file: str) -> dict:
        """Cross-reference on-chain entities with off-chain data.
        
        Args:
            seed_file: JSON file with off-chain indicators:
                {
                    "addresses": ["0x..."],
                    "domains": ["evil.com"],
                    "emails": ["admin@evil.com"],
                    "social": {"twitter": ["@scam"], "telegram": ["t.me/scam"]},
                    "ips": ["1.2.3.4"]
                }
        """
        print(f"[INFO] Cross-referencing with seeds from {seed_file}")
        with open(seed_file) as f:
            seeds = json.load(f)

        results = {
            "address_to_domain": {},
            "address_to_email": {},
            "address_to_social": {},
            "address_to_ip": {},
            "domain_to_address": {},
            "confidence_scores": {}
        }

        # Rule 1: Domain payment (address paid registrar)
        # Rule 2: Tip jar (address = social profile tip)
        # Rule 3: Temporal correlation
        # Rule 4: Infrastructure (same IP)
        # Rule 5: Direct mention (address in post with identity)

        return results

    def temporal_analysis(self, address: str) -> dict:
        """Detect temporal patterns."""
        print(f"[INFO] Temporal analysis for {address}")
        patterns = []
        anomalies = []
        # Burst detection: >5 txs in 60 seconds
        # Round-number detection: 1.0, 10.0, 100.0
        # Time-of-day patterns
        # Velocity anomalies
        return {"patterns": patterns, "anomalies": anomalies}

    def generate_report(self, address: str, output: Optional[str] = None) -> str:
        """Generate forensic report."""
        report = f"""
{'='*70}
FORENSIC ANALYSIS REPORT
{'='*70}
Address: {address}
Chain: {self.chain}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
Analyst: [YOUR_NAME]
Classification: CONFIDENTIAL
{'='*70}

1. TRANSACTION SUMMARY
   Total Transactions: {len(self.transactions)}
   Total Flow: {sum(t.value for t in self.transactions):.4f} {self.chain.upper()}
   Unique Counterparties: {len(set(t.to_address for t in self.transactions))}
   First Transaction: {min((t.timestamp for t in self.transactions), default='N/A')}
   Last Transaction: {max((t.timestamp for t in self.transactions), default='N/A')}

2. ENTITY RESOLUTION
   Clusters Identified: {len(self.entities)}
   High-Confidence Labels: {sum(1 for e in self.entities.values() if e.confidence > 0.8)}
   Medium-Confidence: {sum(1 for e in self.entities.values() if 0.5 < e.confidence <= 0.8)}
   Unresolved: {sum(1 for e in self.entities.values() if e.confidence <= 0.5)}

3. TEMPORAL PATTERNS
   (Populated by temporal_analysis)

4. ANOMALIES
   (Populated by temporal_analysis)

5. CROSS-REFERENCES
   (Populated by cross_reference)

6. RISK ASSESSMENT
   Overall Risk Score: [TO BE CALCULATED]
   Risk Factors: [TO BE LISTED]

7. RECOMMENDATIONS
   - Verify with entity resolution (Chainalysis/Elliptic/TRM)
   - Check against OFAC sanctions list
   - Correlate with off-chain OSINT
   - Document chain of custody
   - File SAR if suspicious activity identified
   - Preserve evidence in WORM storage

{'='*70}
CHAIN OF CUSTODY
{'='*70}
Collected: {datetime.now().isoformat()}
Hash (SHA-256): {hashlib.sha256(address.encode()).hexdigest()}
Storage: WORM
Analyst: [YOUR_NAME]
Supervisor: [SUPERVISOR]
{'='*70}
CONFIDENTIAL — FOR LAW ENFORCEMENT / REGULATORY USE ONLY
{'='*70}
"""
        if output:
            with open(output, "w") as f:
                f.write(report)
            print(f"[INFO] Report saved to {output}")
        return report


def main():
    parser = argparse.ArgumentParser(description="Chain Analysis Tool — Digital Finance Frontier")
    parser.add_argument("--chain", default="ethereum", choices=["ethereum", "solana", "bitcoin"])
    parser.add_argument("--address", required=True)
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument("--min-value", type=float, default=0)
    parser.add_argument("--api-key", help="RPC API key")
    parser.add_argument("--cross-reference", action="store_true")
    parser.add_argument("--seed-file", help="JSON file with off-chain indicators")
    parser.add_argument("--output", help="Output report file")
    args = parser.parse_args()

    analyzer = ChainAnalyzer(chain=args.chain, api_key=args.api_key)
    analyzer.get_transactions(args.address)
    analyzer.trace_flow(args.address, depth=args.depth, min_value=args.min_value)

    if args.cross_reference and args.seed_file:
        analyzer.cross_reference(args.seed_file)

    report = analyzer.generate_report(args.address, output=args.output)
    print(report)


if __name__ == "__main__":
    main()   