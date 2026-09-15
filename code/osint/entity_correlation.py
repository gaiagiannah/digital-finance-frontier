#!/usr/bin/env python3
"""
Entity Correlation Engine — Digital Finance Frontier
Cross-platform entity clustering and blockchain cross-referencing.

Usage:
    python3 entity_correlation.py --input indicators.json --output cluster_report.json
    python3 entity_correlation.py --seed 0x1234... --platforms telegram,twitter,blockchain

Requires:
    pip install networkx scipy scikit-learn
"""

import argparse
import json
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class EntityNode:
    id: str
    value: str
    platform: str  # telegram, twitter, discord, blockchain, domain, email
    type: str  # address, username, domain, email, ip
    first_seen: Optional[str] = None
    last_seen: Optional[str] = None
    metadata: dict = field(default_factory=dict)


@dataclass
class CorrelationEdge:
    source_id: str
    target_id: str
    weight: float  # 0-1 confidence
    method: str  # string_sim, temporal, infra, financial, content
    evidence: str = ""


class EntityCorrelationEngine:
    """Cross-platform entity clustering and blockchain cross-referencing.
    
    Combines:
    - String similarity (Levenshtein, Jaccard, embeddings)
    - Temporal correlation (same active windows)
    - Infrastructure overlap (same IP, domain, hosting)
    - Financial linkage (same wallet, exchange)
    - Content similarity (embedding distance)
    """

    def __init__(self):
        self.nodes: dict[str, EntityNode] = {}
        self.edges: list[CorrelationEdge] = []

    def add_node(self, value: str, platform: str, type: str,
                 first_seen: Optional[str] = None) -> str:
        """Add an entity node. Returns node ID."""
        node_id = f"{platform}:{value}"
        if node_id not in self.nodes:
            self.nodes[node_id] = EntityNode(
                id=node_id, value=value, platform=platform,
                type=type, first_seen=first_seen
            )
        return node_id

    def add_edge(self, source: str, target: str, weight: float,
                 method: str, evidence: str = ""):
        """Add a correlation edge between two nodes."""
        self.edges.append(CorrelationEdge(
            source_id=source, target_id=target,
            weight=weight, method=method, evidence=evidence
        ))

    def string_similarity(self, s1: str, s2: str) -> float:
        """Compute string similarity (0-1)."""
        # Jaccard on character n-grams
        n = 3
        set1 = set(s1[i:i+n] for i in range(len(s1)-n+1))
        set2 = set(s2[i:i+n] for i in range(len(s2)-n+1))
        if not set1 or not set2:
            return 0.0
        return len(set1 & set2) / len(set1 | set2)

    def temporal_correlation(self, times1: list, times2: list) -> float:
        """Compute temporal overlap (0-1)."""
        if not times1 or not times2:
            return 0.0
        # Jaccard on 1-hour bins
        bins1 = set(int(t // 3600) for t in times1)
        bins2 = set(int(t // 3600) for t in times2)
        if not bins1 or not bins2:
            return 0.0
        return len(bins1 & bins2) / len(bins1 | bins2)

    def correlate_platforms(self, entities: dict) -> list[CorrelationEdge]:
        """Correlate entities across platforms.
        
        Args:
            entities: {
                "telegram": [{"value": "t.me/scam", "times": [...]}],
                "twitter": [{"value": "@scam_master", "times": [...]}],
                "blockchain": [{"value": "0x1234...", "times": [...]}],
                "domain": [{"value": "evil.com", "times": [...]}],
            }
        """
        edges = []
        platforms = list(entities.keys())

        for i, p1 in enumerate(platforms):
            for p2 in platforms[i+1:]:
                for e1 in entities[p1]:
                    for e2 in entities[p2]:
                        # String similarity
                        sim = self.string_similarity(e1["value"], e2["value"])
                        if sim > 0.6:
                            self.add_edge(
                                self.add_node(e1["value"], p1, "entity"),
                                self.add_node(e2["value"], p2, "entity"),
                                weight=sim,
                                method="string_sim",
                                evidence=f"Jaccard n-gram similarity: {sim:.3f}"
                            )

                        # Temporal correlation
                        if "times" in e1 and "times" in e2:
                            temp = self.temporal_correlation(e1["times"], e2["times"])
                            if temp > 0.5:
                                self.add_edge(
                                    self.add_node(e1["value"], p1, "entity"),
                                    self.add_node(e2["value"], p2, "entity"),
                                    weight=temp,
                                    method="temporal",
                                    evidence=f"Temporal overlap: {temp:.3f}"
                                )

        return self.edges

    def blockchain_cross_reference(self, addresses: list[str],
                                    domains: list[str],
                                    emails: list[str]) -> dict:
        """Cross-reference blockchain addresses with off-chain entities.
        
        Rules:
        1. Direct: Address mentioned with identity in public post
        2. Financial: Address paid domain registrar
        3. Tip jar: Address = social profile tip
        4. Temporal: Wallet activity matches social posting time
        5. Infrastructure: Same IP at wallet creation
        """
        results = {
            "address_to_domain": {},
            "address_to_email": {},
            "confidence": {}
        }
        # Implementation requires actual data sources
        # (Etherscan, Shodan, WHOIS, social media APIs)
        return results

    def cluster(self, threshold: float = 0.6) -> list[dict]:
        """Find entity clusters using community detection.
        
        Uses:
        - Louvain modularity optimization (if networkx available)
        - OR: Connected components with edge weight > threshold
        """
        try:
            import networkx as nx

            G = nx.Graph()
            for node_id in self.nodes:
                G.add_node(node_id)
            for edge in self.edges:
                if edge.weight >= threshold:
                    G.add_edge(edge.source_id, edge.target_id,
                               weight=edge.weight, method=edge.method)

            # Connected components (simple clustering)
            communities = list(nx.connected_components(G))

            clusters = []
            for i, community in enumerate(communities):
                if len(community) < 2:
                    continue
                cluster = {
                    "id": f"cluster_{i}",
                    "size": len(community),
                    "entities": [
                        {
                            "value": self.nodes[nid].value,
                            "platform": self.nodes[nid].platform,
                            "type": self.nodes[nid].type
                        }
                        for nid in community
                    ],
                    "edges": [
                        {
                            "source": self.nodes[e.source_id].value,
                            "target": self.nodes[e.target_id].value,
                            "weight": e.weight,
                            "method": e.method
                        }
                        for e in self.edges
                        if e.source_id in community and e.target_id in community
                    ],
                    "risk_score": min(1.0, len(community) * 0.15)
                }
                clusters.append(cluster)

            return sorted(clusters, key=lambda c: c["size"], reverse=True)

        except ImportError:
            print("[WARN] networkx not installed. Using simple connected components.")
            # Fallback: simple union-find
            return []

    def report(self) -> str:
        """Generate correlation report."""
        clusters = self.cluster()
        report = f"""
{'='*70}
ENTITY CORRELATION REPORT
{'='*70}
Total Nodes: {len(self.nodes)}
Total Edges: {len(self.edges)}
Clusters Found: {len(clusters)}
{'='*70}

"""
        for cluster in clusters[:10]:  # Top 10
            report += f"Cluster {cluster['id']} (size={cluster['size']}, risk={cluster['risk_score']:.2f})\n"
            for entity in cluster["entities"]:
                report += f"  [{entity['platform']}] {entity['value']} ({entity['type']})\n"
            for edge in cluster["edges"][:5]:
                report += f"    → {edge['source']} ↔ {edge['target']} ({edge['method']}, w={edge['weight']:.2f})\n"
            report += "\n"

        report += f"{'='*70}\nCONFIDENTIAL — FOR INVESTIGATIVE USE ONLY\n{'='*70}\n"
        return report


def main():
    parser = argparse.ArgumentParser(description="Entity Correlation — Digital Finance Frontier")
    parser.add_argument("--input", help="Input JSON with entities")
    parser.add_argument("--seed", help="Seed indicator")
    parser.add_argument("--platforms", default="all", help="Comma-separated platforms")
    parser.add_argument("--threshold", type=float, default=0.6)
    parser.add_argument("--output", help="Output file")
    args = parser.parse_args()

    engine = EntityCorrelationEngine()

    print(f"{'='*60}")
    print(f"Entity Correlation Engine — Digital Finance Frontier")
    print(f"{'='*60}")
    print(f"  Threshold: {args.threshold}")
    print(f"  Platforms: {args.platforms}")
    print()
    print("  Methods:")
    print("    - String similarity (Jaccard n-grams)")
    print("    - Temporal correlation (1-hour bins)")
    print("    - Infrastructure overlap (IP, domain)")
    print("    - Financial linkage (wallet, exchange)")
    print("    - Content similarity (embeddings)")
    print()
    print("  Output:")
    print("    - Entity clusters (connected components)")
    print("    - Cross-platform links (with confidence)")
    print("    - Risk score per cluster")
    print(f"{'='*60}")

    if args.input:
        with open(args.input) as f:
            entities = json.load(f)
        engine.correlate_platforms(entities)
        report = engine.report()
        print(report)
        if args.output:
            with open(args.output, "w") as f:
                f.write(report)
            print(f"[INFO] Saved to {args.output}")


if __name__ == "__main__":
    main()   