#!/usr/bin/env python3
"""
OSINT Pipeline — Digital Finance Frontier
Automated multi-source OSINT collection and correlation.

Usage:
    python3 osint_pipeline.py --seed 0x1234... --sources telegram,twitter,darkweb
    python3 osint_pipeline.py --seed admin@scam.com --sources all
    python3 osint_pipeline.py --seed-file seeds.json --output report.json

Requires:
    pip install requests aiohttp beautifulsoup4 lxml spacy
    # Optional:
    # pip install telethon (Telegram)
    # pip install tweepy (Twitter)
    # pip install discord.py (Discord)
"""

import argparse
import asyncio
import json
import re
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class Indicator:
    value: str
    type: str  # address, domain, email, ip, username, phone
    source: str = "seed"
    confidence: float = 1.0
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class Finding:
    indicator: Indicator
    source: str
    data: dict
    confidence: float
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class OSINTPipeline:
    """Multi-source OSINT collection and correlation pipeline.
    
    LEGAL BOUNDARIES:
    - Only collect PUBLIC data
    - No access behind login without valid credentials
    - No private groups/channels without invitation
    - No purchasing of stolen data
    - No social engineering
    - See legal-framework.md for full details
    """

    def __init__(self, api_keys: Optional[dict] = None):
        self.api_keys = api_keys or {}
        self.findings: list[Finding] = []
        self.indicators: list[Indicator] = []
        self.rate_limit = 10  # requests per second (be respectful)

    async def run(self, seed: str, seed_type: str = "auto",
                  sources: list[str] = None) -> dict:
        """Run full OSINT pipeline on a seed indicator.
        
        Args:
            seed: The starting indicator (address, domain, email, etc.)
            seed_type: Type of seed (auto-detected if not specified)
            sources: List of sources to query (default: all available)
        """
        if seed_type == "auto":
            seed_type = self._detect_type(seed)

        self.indicators.append(Indicator(value=seed, type=seed_type))
        print(f"[INFO] Starting OSINT pipeline")
        print(f"[INFO] Seed: {seed} ({seed_type})")
        print(f"[INFO] Sources: {sources or 'all available'}")
        print()

        # Phase 1: Infrastructure
        if not sources or "infrastructure" in sources:
            await self._query_infrastructure(seed)

        # Phase 2: Blockchain
        if not sources or "blockchain" in sources:
            await self._query_blockchain(seed)

        # Phase 3: Social Media
        if not sources or "social" in sources:
            await self._query_social(seed)

        # Phase 4: Dark Web
        if not sources or "darkweb" in sources:
            await self._query_darkweb(seed)

        # Phase 5: Correlation
        results = self._correlate()

        print(f"\n[INFO] Pipeline complete")
        print(f"[INFO] Total findings: {len(self.findings)}")
        print(f"[INFO] Indicators discovered: {len(self.indicators)}")
        return results

    def _detect_type(self, seed: str) -> str:
        """Auto-detect indicator type."""
        if re.match(r'^0x[a-fA-F0-9]{40}$', seed):
            return "address_eth"
        if re.match(r'^bc1[a-z0-9]{6,87}$', seed):
            return "address_btc"
        if re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', seed):
            return "address_btc"
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', seed):
            return "email"
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', seed):
            return "ip"
        if re.match(r'^[a-z0-9.-]+\.[a-z]{2,}$', seed, re.I):
            return "domain"
        if re.match(r'^\+?\d{10,15}$', seed.replace("-", "")):
            return "phone"
        return "username"

    async def _query_infrastructure(self, seed: str):
        """Query infrastructure sources (DNS, WHOIS, Shodan, Censys)."""
        print("[PHASE 1] Infrastructure")
        # DNS lookup
        # WHOIS / RDAP
        # Shodan (if API key)
        # Censys (if API key)
        # Certificate Transparency (crt.sh)
        # SecurityTrails (if API key)
        pass

    async def _query_blockchain(self, seed: str):
        """Query blockchain sources."""
        print("[PHASE 2] Blockchain")
        # Etherscan / Blockscout (public)
        # Dune Analytics (if API key)
        # Nansen (if API key)
        # Arkham (if API key)
        # Token transfers
        # Contract interactions
        # Exchange deposit/withdrawal detection
        pass

    async def _query_social(self, seed: str):
        """Query social media (PUBLIC data only)."""
        print("[PHASE 3] Social Media")
        # Twitter/X (public posts via API)
        # Telegram (public channels via API)
        # Discord (public servers via bot)
        # Reddit (public via API)
        # GitHub (public repos, issues)
        # Maigret / Sherlock (username search)
        pass

    async def _query_darkweb(self, seed: str):
        """Query dark web (PUBLIC .onion sites only)."""
        print("[PHASE 4] Dark Web")
        # DarkSearch API
        # Flashpoint (if subscription)
        # ZeroFOX (if subscription)
        # Public .onion marketplaces (monitoring only, NO purchasing)
        # Leak site monitoring
        pass

    def _correlate(self) -> dict:
        """Correlate findings across sources."""
        print("[PHASE 5] Correlation")
        # Cross-source entity linking
        # Temporal correlation
        # Infrastructure overlap
        # Financial flow analysis
        # Generate entity profile
        results = {
            "entity_profile": {
                "seed": self.indicators[0].value if self.indicators else None,
                "linked_indicators": [i.value for i in self.indicators[1:]],
                "platforms": set(),
                "risk_score": 0.0,
                "first_seen": None,
                "last_seen": None
            },
            "findings": [
                {
                    "indicator": f.indicator.value,
                    "source": f.source,
                    "data": f.data,
                    "confidence": f.confidence
                }
                for f in self.findings
            ],
            "recommendations": []
        }
        return results

    def export(self, output: str, format: str = "json"):
        """Export findings."""
        data = {
            "pipeline": "digital-finance-frontier/osint",
            "timestamp": datetime.now().isoformat(),
            "seed": self.indicators[0].value if self.indicators else None,
            "findings": [
                {
                    "indicator": f.indicator.value,
                    "type": f.indicator.type,
                    "source": f.source,
                    "data": f.data,
                    "confidence": f.confidence,
                    "timestamp": f.timestamp
                }
                for f in self.findings
            ]
        }
        if format == "json":
            with open(output, "w") as f:
                json.dump(data, f, indent=2, default=str)
        elif format == "md":
            self._export_markdown(output, data)
        print(f"[INFO] Exported to {output} ({format})")

    def _export_markdown(self, output: str, data: dict):
        """Export as Markdown report."""
        md = f"""# OSINT Report
**Date:** {data['timestamp']}
**Seed:** `{data['seed']}`
**Total Findings:** {len(data['findings'])}

## Findings

| # | Indicator | Source | Confidence | Timestamp |
|---|---|---|---|---|
"""
        for i, f in enumerate(data['findings'], 1):
            md += f"| {i} | `{f['indicator']}` | {f['source']} | {f['confidence']:.2f} | {f['timestamp']} |\n"
        md += "\n## Legal Notice\n\nThis report was generated using publicly available data only. All collection methods comply with CFAA, Wiretap Act, and applicable platform Terms of Service.\n"
        with open(output, "w") as f:
            f.write(md)


def main():
    parser = argparse.ArgumentParser(description="OSINT Pipeline — Digital Finance Frontier")
    parser.add_argument("--seed", required=True, help="Starting indicator")
    parser.add_argument("--seed-type", default="auto", help="Type of seed")
    parser.add_argument("--sources", default="all", help="Comma-separated sources")
    parser.add_argument("--output", help="Output file")
    parser.add_argument("--format", default="json", choices=["json", "md"])
    args = parser.parse_args()

    sources = args.sources.split(",") if args.sources != "all" else None
    pipeline = OSINTPipeline()

    results = asyncio.run(pipeline.run(args.seed, args.seed_type, sources))

    if args.output:
        pipeline.export(args.output, args.format)

    print(json.dumps(results, indent=2, default=str))


if __name__ == "__main__":
    main()   