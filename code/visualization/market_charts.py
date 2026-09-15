#!/usr/bin/env python3
"""
Market Charts — Digital Finance Frontier
Generates key market data visualizations.

Usage:
    python3 market_charts.py --output assets/charts/
    python3 market_charts.py --chart tokenization-growth
    python3 market_charts.py --chart all

Requires:
    pip install matplotlib numpy pandas
"""

import argparse
from pathlib import Path


def chart_tokenization_growth(output_dir: str):
    """Tokenized RWA market growth chart."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np

    # Data points (mid-2025 → mid-2026, with projections)
    periods = ["Q1'25", "Q2'25", "Q3'25", "Q4'25", "Q1'26", "Q2'26", "Q1'27*", "Q1'28*", "Q1'30*"]
    rwa_b = [3.5, 8.2, 15.0, 22.0, 28.0, 37.0, 55.0, 120.0, 500.0]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(periods, rwa_b, 'o-', color='#0f3460', linewidth=2, markersize=8)
    ax.fill_between(range(len(periods)), rwa_b, alpha=0.1, color='#0f3460')

    # Annotations
    ax.annotate('$37B\n(mid-2026)', xy=(5, 37), xytext=(5.5, 50),
                fontsize=9, fontweight='bold', color='#0f3460',
                arrowprops=dict(arrowstyle='->', color='#0f3460'))
    ax.annotate('$500B+\n(2030 proj.)', xy=(8, 500), xytext=(6.5, 400),
                fontsize=9, fontweight='bold', color='#e94560',
                arrowprops=dict(arrowstyle='->', color='#e94560'))

    ax.set_ylabel("Tokenized RWA (excl. stablecoins) — $B")
    ax.set_title("Tokenized Real-World Asset Market Growth", fontsize=12, fontweight='bold')
    ax.set_yscale('log')
    ax.grid(True, alpha=0.3)
    ax.axvline(x=5, color='#999', linestyle='--', alpha=0.5)
    ax.text(5.1, 2, "← ACTUAL | PROJECTED →", fontsize=8, color='#999')

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/tokenization_growth.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] tokenization_growth.png")


def chart_stablecoin_market(output_dir: str):
    """Stablecoin market cap chart."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    periods = ["Q1'24", "Q2'24", "Q3'24", "Q4'24", "Q1'25", "Q2'25", "Q3'25", "Q4'25", "Q1'26", "Q2'26"]
    usdc_b = [30, 35, 38, 42, 45, 50, 55, 58, 62, 65]
    usdt_b = [70, 75, 80, 85, 90, 95, 100, 105, 110, 115]
    other_b = [5, 8, 12, 15, 20, 25, 30, 35, 40, 45]

    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(periods))
    ax.bar(x, usdt_b, label='USDT (Tether)', color='#26a17b', alpha=0.8)
    ax.bar(x, usdc_b, bottom=usdt_b, label='USDC (Circle)', color='#2775ca', alpha=0.8)
    ax.bar(x, other_b, bottom=[a+b for a, b in zip(usdt_b, usdc_b)],
           label='Other (PYUSD, DAI, GENIUS Act, etc.)', color='#9b59b6', alpha=0.8)

    total = [a+b+c for a, b, c in zip(usdt_b, usdc_b, other_b)]
    ax.plot(x, total, 'k-', linewidth=1.5, label='Total')

    ax.set_xticks(x)
    ax.set_xticklabels(periods)
    ax.set_ylabel("Market Cap — $B")
    ax.set_title("Stablecoin Market Cap by Issuer (2024–2026)", fontsize=12, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/stablecoin_market.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] stablecoin_market.png")


def chart_defi_tvl(output_dir: str):
    """DeFi TVL by region."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    regions = ['North America', 'Asia-Pacific', 'Europe', 'Other']
    tvl = [86, 48, 40, 26]
    growth = [12, 52, 7.3, 15]
    colors = ['#0f3460', '#e94560', '#533483', '#2c3e50']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # TVL
    bars = ax1.bar(regions, tvl, color=colors, alpha=0.8)
    ax1.set_ylabel("TVL — $B")
    ax1.set_title("DeFi TVL by Region (mid-2026)", fontweight='bold')
    for bar, val in zip(bars, tvl):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'${val}B', ha='center', fontsize=9)

    # Growth
    bars2 = ax2.bar(regions, growth, color=colors, alpha=0.8)
    ax2.set_ylabel("YTD Growth — %")
    ax2.set_title("YTD Growth by Region", fontweight='bold')
    for bar, val in zip(bars2, growth):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'+{val}%', ha='center', fontsize=9)

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/defi_tvl.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] defi_tvl.png")


def chart_pqc_timeline(output_dir: str):
    """PQC migration timeline."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    events = [
        ("Aug 2024", "NIST FIPS 203/204/205 Final", 0),
        ("Mar 2025", "HQC Selected (backup KEM)", 1),
        ("May 2026", "Microsoft ML-DSA in Active Directory", 2),
        ("2026", "White House PQC Executive Order", 3),
        ("Dec 2026", "EU National PQC Strategies Due", 4),
        ("Dec 2030", "Federal HVA: PQC Key Establishment", 5),
        ("Dec 2031", "Federal HVA: PQC Digital Signatures", 6),
        ("2035", "NIST Full Migration / NSA CNSA 2.0", 7),
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    y_positions = range(len(events))

    for i, (date, event, _) in enumerate(events):
        color = '#e94560' if i < 4 else '#0f3460'
        ax.scatter(0, i, color=color, s=100, zorder=5)
        ax.text(0.1, i, f"{date}: {event}", va='center', fontsize=9)

    ax.axvline(x=0, color='#999', linewidth=2)
    ax.set_xlim(-0.3, 3.5)
    ax.set_ylim(-0.5, len(events) - 0.5)
    ax.set_yticks([])
    ax.set_title("Post-Quantum Cryptography Migration Timeline", fontsize=12, fontweight='bold')
    ax.legend(handles=[
        plt.Line2D([0], [0], color='#e94560', marker='o', markersize=8, label='Completed / In Progress'),
        plt.Line2D([0], [0], color='#0f3460', marker='o', markersize=8, label='Upcoming'),
    ], loc='lower right')

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/pqc_timeline.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] pqc_timeline.png")


def main():
    parser = argparse.ArgumentParser(description="Market Charts — Digital Finance Frontier")
    parser.add_argument("--output", default="assets/charts/")
    parser.add_argument("--chart", default="all",
                        choices=["all", "tokenization-growth", "stablecoin-market",
                                 "defi-tvl", "pqc-timeline"])
    args = parser.parse_args()

    if args.chart in ("all", "tokenization-growth"):
        chart_tokenization_growth(args.output)
    if args.chart in ("all", "stablecoin-market"):
        chart_stablecoin_market(args.output)
    if args.chart in ("all", "defi-tvl"):
        chart_defi_tvl(args.output)
    if args.chart in ("all", "pqc-timeline"):
        chart_pqc_timeline(args.output)


if __name__ == "__main__":
    main()   