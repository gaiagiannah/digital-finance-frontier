# OSINT Framework for Crypto Investigations

## Pipeline
1. INDICATOR INGESTION
├── On-chain addresses
├── Domain names / IP addresses
├── Social media handles
├── Dark web market listings
└── Email addresses / phone numbers
2. ENRICHMENT
├── Etherscan / Blockscout (transaction history)
├── Nansen / Arkham (entity labels)
├── Shodan / Censys (infrastructure)
├── TheHarvester / Maltego (correlation)
└── Social media archives (Wayback, GitHub)
3. CORRELATION
├── Cross-chain linking
├── Temporal pattern matching
├── Infrastructure overlap
├── Behavioral fingerprinting
└── Financial flow analysis
4. ATTRIBUTION
├── TTP mapping (MITRE ATT&CK)
├── Actor profiling
├── Confidence scoring
└── Legal validation
5. REPORTING
├── Incident report
├── Regulatory filing
├── Law enforcement handoff
└── Intelligence product

## Tool Stack

| Category | Tools |
|---|---|
| Chain Analysis | Chainalysis Reactor, Elliptic, TRM Labs, Arkham, Nansen, Dune |
| OSINT | Maltego, SpiderFoot, TheHarvester, Shodan, Censys |
| Dark Web | Tor, I2P, specialized crawlers, NLP pipelines |
| On-chain | Etherscan, Blockscout, Tenderly, Alchemy, Infura |
| Visualization | Gephi, Cytoscape, D3.js, Plotly, Neo4j Bloom |   