#!/usr/bin/env python3
"""
Architecture Diagram Generator — Digital Finance Frontier
Generates the six-layer architecture diagram.

Usage:
    python3 architecture_diagram.py --output assets/diagrams/architecture.png
    python3 architecture_diagram.py --output assets/diagrams/architecture.svg --format svg

Requires:
    pip install matplotlib numpy
"""

import argparse
from pathlib import Path


def generate_diagram(output: str = "assets/diagrams/architecture.png",
                     fmt: str = "png"):
    """Generate the six-layer architecture diagram."""
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        from matplotlib.patches import FancyBboxPatch

        fig, ax = plt.subplots(1, 1, figsize=(14, 11))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 11)
        ax.axis('off')

        # Title
        ax.text(7, 10.5, "DIGITAL FINANCE FRONTIER",
                fontsize=16, fontweight='bold', ha='center', color='#1a1a2e')
        ax.text(7, 10.1, "Six-Layer Architecture (2026)",
                fontsize=11, ha='center', color='#555')

        layers = [
            ("L6: REGULATION & GOVERNANCE",
             "G20 · FSB · IOSCO · IMF · BIS CPMI · GENIUS Act · MiCA · FATF",
             "#1a1a2e", "#e8e8f0", 9.2),
            ("L5: DISTRIBUTION & ACCESS",
             "Schwab · Fidelity · Vanguard · Coinbase · Kraken · PayPal · MetaMask",
             "#16213e", "#dce6f1", 7.8),
            ("L4: ISSUANCE & TOKENIZATION",
             "BlackRock BUIDL · JPMorgan Kinexys · DTCC · NYSE · Ondo · Kraken xStocks",
             "#0f3460", "#d1e7dd", 6.4),
            ("L3: SETTLEMENT & ACCEPTANCE",
             "Visa · Mastercard · SWIFT · Canton · TCH · Agorá · mBridge",
             "#533483", "#fff3cd", 5.0),
            ("L2: PROTOCOL & INFRASTRUCTURE",
             "Ethereum L2s · Solana · Chainlink · Fireblocks · Aave · Lido · LayerZero",
             "#e94560", "#f8d7da", 3.6),
            ("L1: MONETARY FOUNDATION",
             "Central Bank Reserves · wCBDCs · Tokenized Deposits · Stablecoins ($315B+)",
             "#2c3e50", "#d4edda", 2.2),
        ]

        for title, actors, color, bg, y in layers:
            # Background box
            box = FancyBboxPatch((0.5, y - 0.4), 13, 1.1,
                                  boxstyle="round,pad=0.1",
                                  facecolor=bg, edgecolor=color, linewidth=2)
            ax.add_patch(box)

            # Layer title
            ax.text(1.0, y + 0.35, title, fontsize=10, fontweight='bold',
                    color=color, va='center')

            # Actors
            ax.text(1.0, y - 0.15, actors, fontsize=8.5,
                    color='#333', va='center')

        # Arrows between layers
        for y in [8.8, 7.4, 6.0, 4.6, 3.2]:
            ax.annotate('', xy=(7, y - 0.15), xytext=(7, y + 0.05),
                        arrowprops=dict(arrowstyle='->', color='#888', lw=1.5))

        # Value capture annotation
        ax.text(13.5, 8.2, "← 2026\n   Value\n   Capture",
                fontsize=8, color='#e94560', ha='center', fontstyle='italic')
        ax.text(13.5, 6.6, "← 2030\n   Value\n   Capture",
                fontsize=8, color='#0f3460', ha='center', fontstyle='italic')

        # Footer
        ax.text(7, 1.2, "Digital Finance Frontier v1.0 | September 2026",
                fontsize=8, ha='center', color='#999')
        ax.text(7, 0.8, "CC BY-NC 4.0",
                fontsize=7, ha='center', color='#bbb')

        Path(output).parent.mkdir(parents=True, exist_ok=True)
        plt.tight_layout()
        plt.savefig(output, format=fmt, dpi=150, bbox_inches='tight',
                    facecolor='white')
        plt.close()
        print(f"[OK] Diagram saved to {output}")

    except ImportError as e:
        print(f"[ERROR] Missing dependency: {e}")
        print("[INFO] Install: pip install matplotlib numpy")


def main():
    parser = argparse.ArgumentParser(description="Architecture Diagram — Digital Finance Frontier")
    parser.add_argument("--output", default="assets/diagrams/architecture.png")
    parser.add_argument("--format", default="png", choices=["png", "svg", "pdf"])
    args = parser.parse_args()
    generate_diagram(args.output, args.format)


if __name__ == "__main__":
    main()   