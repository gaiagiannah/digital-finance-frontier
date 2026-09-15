# AI in Financial Forensics

## Applications

| Application | Technology | Status |
|---|---|---|
| Fraud Detection | GNN on transaction graphs | 94.7% accuracy (CoSemiGNN, 2025); production at Chainalysis, Elliptic |
| AML Monitoring | ML + rule-based hybrid | Standard at all major exchanges; ZKP-enhanced: 96.7% accuracy |
| Chain Clustering | LLMs + graph algorithms | Research → early production |
| Anomaly Detection | Autoencoders, isolation forests | Production at TRM Labs, Chainalysis |
| Phishing Detection | NLP + behavioral analysis | Production at all major wallets |
| Adversarial AI Detection | Detecting AI-generated social engineering | Emerging (2026) |
| Dark Web Correlation | NLP + graph matching | Research → pilot |

## Key Research

- **CoSemiGNN (2025)**: Dynamic GNNs for illicit transaction detection under label scarcity — 94.7% accuracy with ZK privacy
- **PrivChain-AI (2025)**: Federated learning + blockchain for fraud detection — 94.7% accuracy
- **ZKP + Deep Learning (ICISPD 2024, Springer 2026)**: Privacy-preserving DeFi verification

## Tool Stack

| Tool | Purpose |
|---|---|
| PyTorch Geometric | GNN training/inference |
| Neo4j | Graph database for entity resolution |
| HuggingFace | NLP for OSINT, phishing detection |
| Scikit-learn | Classical ML baselines |
| Dune / Nansen | On-chain data for training |   