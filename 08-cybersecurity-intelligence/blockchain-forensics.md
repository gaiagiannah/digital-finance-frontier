# Blockchain Forensics

## Investigation Pipeline

### Phase 1: Detection
- On-chain alerts (exchange monitoring, anomaly detection)
- Off-chain OSINT triggers (social media, forums)
- Dark web monitoring
- AI anomaly detection (GNNs, autoencoders)

### Phase 2: Collection
- On-chain: Etherscan, Dune, Nansen, Arkham, blockchain explorers
- Off-chain: Social media, forums, dark web, KYC data (with warrant)
- Network: PCAP, API logs, exchange metadata
- Preservation: Hash verification, timestamped snapshots, WORM storage

### Phase 3: Analysis
- Chain tracing (follow the money)
- Graph analysis (GNN, community detection)
- Clustering (entity resolution)
- Temporal pattern analysis

### Phase 4: Attribution
- TTP mapping (MITRE ATT&CK Crypto Tactics)
- OSINT correlation (social, forums, dark web)
- KYC/Identity linking (exchange records, legal process)
- Threat actor profiling (Lazarus, Scam Group, Insider)

### Phase 5: Response & Reporting
- Asset freezing/seizure
- Regulatory reporting (FinCEN, FATF, ECB)
- Law enforcement (FBI, SEC, Europol)
- Intelligence sharing (ISACs, industry)

## Key Techniques

| Technique | Description | Tool |
|---|---|---|
| Heuristic clustering | Group wallets by transaction patterns | Chainalysis, Elliptic |
| Exchange tagging | Identify known exchange hot wallets | TRM Labs, Arkham |
| Mix analysis | De-anonymize Tornado Cash, CoinJoin | Specialized |
| Cross-chain tracking | Follow assets across bridges | LayerZero, CCIP analytics |
| Temporal analysis | Identify timing patterns in laundering | Custom ML |
| Graph community detection | Find connected entity clusters | GNN, Neo4j |   