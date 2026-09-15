#!/usr/bin/env python3
"""
Dark Web Monitor — Digital Finance Frontier
Monitors public .onion sites for financial crime indicators.

Usage:
    python3 darknet_monitor.py --keywords "ransom,bitcoin,exchange" --output alerts.json
    python3 darknet_monitor.py --monitor --interval 3600

LEGAL BOUNDARIES:
    - ONLY access public .onion sites
    - DO NOT purchase any data or services
    - DO NOT interact with marketplaces (no orders, no messages)
    - DO NOT download illegal content
    - Monitor only: listings, announcements, ransom notes
    - See legal-framework.md for full details

Requires:
    pip install requests aiohttp beautifulsoup4 lxml
    # Tor: Install system-wide (tor, torsocks)
"""

import argparse
import asyncio
import json
import re
import time
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class DarkWebAlert:
    source: str
    title: str
    content: str
    indicators: list
    risk_level: str  # low, medium, high, critical
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    url: str = ""
    keywords_matched: list = field(default_factory=list)


class DarkWebMonitor:
    """Monitors public .onion sites for financial crime indicators.
    
    LEGAL: Only accesses public data. No interaction, no purchase,
    no private content access.
    """

    # High-value keywords for financial crime
    FINANCIAL_KEYWORDS = [
        "ransom", "bitcoin", "btc", "ethereum", "eth", "usdt", "usdc",
        "exchange", "binance", "coinbase", "kraken", "wallet",
        "stolen", "leaked", "compromised", "exploit", "hack",
        "money laundering", "mixer", "tumbler", "tornado",
        "phishing", "scam", "ponzi", "rug pull",
        "api key", "private key", "seed phrase", "mnemonic",
        "for sale", "for hire", "zero day", "exploit kit",
        "darknet", "marketplace", "vendor", "buyer",
        "sanctions", "ofac", "lazarus", "north korea",
    ]

    # Risk indicators (regex)
    RISK_PATTERNS = [
        (re.compile(r'\d+\.?\d*\s*(?:BTC|ETH|USDT|USDC)\b', re.I), "crypto_amount"),
        (re.compile(r'0x[a-fA-F0-9]{40}', re.I), "eth_address"),
        (re.compile(r'bc1[ac-hj-np-z02-9]{6,87}', re.I), "btc_address"),
        (re.compile(r'\$[\d,]+', re.I), "usd_amount"),
        (re.compile(r'(?:deadline|pay within|hours|days)\b', re.I), "urgency"),
        (re.compile(r'(?:victim|target|company|bank|exchange)\b', re.I), "target"),
    ]

    def __init__(self, tor_proxy: str = "socks5://127.0.0.1:9050"):
        self.tor_proxy = tor_proxy
        self.alerts: list[DarkWebAlert] = []
        self.monitored_sources: list[str] = []

    def add_source(self, url: str, name: str):
        """Add a public .onion source to monitor."""
        self.monitored_sources.append({"url": url, "name": name})
        print(f"[INFO] Added source: {name} ({url})")

    async def scan_source(self, url: str, name: str) -> list[DarkWebAlert]:
        """Scan a public .onion source for indicators.
        
        LEGAL: Public access only. No interaction.
        """
        alerts = []
        print(f"[SCAN] {name} ({url})")

        try:
            # In production: use torsocks or PySocks with Tor
            # import aiohttp
            # from aiohttp_socks import Connector
            #
            # connector = Connector.from_url(self.tor_proxy)
            # async with aiohttp.ClientSession(connector=connector) as session:
            #     async with session.get(url) as resp:
            #         html = await resp.text()
            #         text = self._extract_text(html)
            #         alerts = self._analyze(text, url, name)
            #
            # NOTE: This is a scaffold. Production requires:
            # 1. Running Tor daemon
            # 2. PySocks/aiohttp-socks for routing
            # 3. Rate limiting (be respectful)
            # 4. Error handling (sites go down frequently)
            # 5. Content filtering (skip illegal content pages)
            pass

        except Exception as e:
            print(f"[ERROR] {name}: {e}")

        return alerts

    def _extract_text(self, html: str) -> str:
        """Extract text from HTML."""
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, "lxml")
            for tag in soup(["script", "style", "nav", "footer"]):
                tag.decompose()
            return soup.get_text(separator="\n", strip=True)
        except ImportError:
            return re.sub(r'<[^>]+>', ' ', html)

    def _analyze(self, text: str, url: str, source: str) -> list[DarkWebAlert]:
        """Analyze text for financial crime indicators."""
        alerts = []
        lines = text.split("\n")

        for line in lines:
            matched_keywords = [
                kw for kw in self.FINANCIAL_KEYWORDS
                if kw in line.lower()
            ]
            if not matched_keywords:
                continue

            # Check risk patterns
            risk_indicators = []
            for pattern, label in self.RISK_PATTERNS:
                if pattern.search(line):
                    risk_indicators.append(label)

            # Determine risk level
            if len(risk_indicators) >= 3 or "ransom" in line.lower():
                risk = "critical"
            elif len(risk_indicators) >= 2:
                risk = "high"
            elif len(risk_indicators) >= 1:
                risk = "medium"
            else:
                risk = "low"

            if risk in ("high", "critical"):
                alerts.append(DarkWebAlert(
                    source=source,
                    title=line[:100],
                    content=line[:500],
                    indicators=risk_indicators,
                    risk_level=risk,
                    url=url,
                    keywords_matched=matched_keywords
                ))

        return alerts

    async def run_monitor(self, interval: int = 3600):
        """Continuous monitoring loop."""
        print(f"[INFO] Starting dark web monitor (interval: {interval}s)")
        print(f"[INFO] Sources: {len(self.monitored_sources)}")
        print(f"[INFO] LEGAL: Public data only. No interaction.")
        print()

        while True:
            for source in self.monitored_sources:
                alerts = await self.scan_source(source["url"], source["name"])
                self.alerts.extend(alerts)

            critical = [a for a in self.alerts if a.risk_level == "critical"]
            if critical:
                print(f"\n[ALERT] {len(critical)} critical alerts!")
                for a in critical:
                    print(f"  [{a.risk_level.upper()}] {a.title}")
                    print(f"    Source: {a.source}")
                    print(f"    Indicators: {a.indicators}")
                    print()

            await asyncio.sleep(interval)

    def export(self, output: str):
        """Export alerts to JSON."""
        data = {
            "monitor": "digital-finance-frontier/darknet",
            "timestamp": datetime.now().isoformat(),
            "total_alerts": len(self.alerts),
            "critical": sum(1 for a in self.alerts if a.risk_level == "critical"),
            "high": sum(1 for a in self.alerts if a.risk_level == "high"),
            "alerts": [
                {
                    "source": a.source,
                    "title": a.title,
                    "risk_level": a.risk_level,
                    "indicators": a.indicators,
                    "keywords": a.keywords_matched,
                    "timestamp": a.timestamp,
                    "url": a.url
                }
                for a in self.alerts
            ]
        }
        with open(output, "w") as f:
            json.dump(data, f, indent=2)
        print(f"[INFO] Exported {len(self.alerts)} alerts to {output}")


def main():
    parser = argparse.ArgumentParser(description="Dark Web Monitor — Digital Finance Frontier")
    parser.add_argument("--keywords", help="Comma-separated keywords")
    parser.add_argument("--monitor", action="store_true", help="Continuous monitoring")
    parser.add_argument("--interval", type=int, default=3600, help="Scan interval (seconds)")
    parser.add_argument("--output", help="Output file")
    args = parser.parse_args()

    monitor = DarkWebMonitor()

    # Default sources (public .onion sites for monitoring)
    # In production, add specific sources relevant to your investigation
    # monitor.add_source("http://example.onion", "Example Source")

    print(f"{'='*60}")
    print(f"Dark Web Monitor — Digital Finance Frontier")
    print(f"{'='*60}")
    print(f"  Mode: {'Continuous' if args.monitor else 'One-shot'}")
    print(f"  Interval: {args.interval}s")
    print(f"  Keywords: {args.keywords or 'default financial crime set'}")
    print()
    print(f"  LEGAL BOUNDARIES:")
    print(f"    - Public .onion sites ONLY")
    print(f"    - NO purchasing, NO interaction")
    print(f"    - NO downloading illegal content")
    print(f"    - NO accessing private/hidden content")
    print(f"    - Monitor: listings, announcements, ransom notes")
    print(f"  See: 08-cybersecurity-intelligence/legal-framework.md")
    print(f"{'='*60}")

    if args.monitor:
        asyncio.run(monitor.run_monitor(args.interval))
    else:
        print(f"\n[INFO] One-shot mode. Add sources and run scan.")
        if args.output:
            monitor.export(args.output)


if __name__ == "__main__":
    main()   
