# Code

Python tools for the Digital Finance Frontier project.

## Structure
code/
├── requirements.txt # All dependencies
├── forensics/
│ ├── chain_analysis.py # On-chain tracing + cross-referencing
│ ├── graph_analysis.py # GNN-based AML detection
│ └── osint_pipeline.py # Multi-source OSINT collection
├── visualization/
│ ├── architecture_diagram.py # Six-layer stack diagram
│ └── market_charts.py # Market data visualizations
├── ml-models/
│ ├── gnn_aml.py # Production GNN AML model
│ ├── ner_model.py # Crypto NER (regex + transformer)
│ └── anomaly_detection.py # Autoencoder + Isolation Forest
├── quantum-sim/
│ ├── portfolio_qaoa.py # QAOA portfolio optimization
│ └── pqc_demo.py # PQC (ML-KEM, ML-DSA) demo
└── osint/
├── darknet_monitor.py # Dark web monitoring (public only)
└── entity_correlation.py # Cross-platform entity clustering

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run NER on a sample
python3 ml-models/ner_model.py --text "0x1234... sent 100 BTC to bc1q..."

# Run chain analysis
python3 forensics/chain_analysis.py --chain ethereum --address 0x...

# Run OSINT pipeline
python3 forensics/osint_pipeline.py --seed admin@scam.com --output report.json

# Run PQC demo
python3 quantum-sim/pqc_demo.py --operation all

# Generate diagrams
python3 visualization/architecture_diagram.py --output assets/diagrams/arch.png
python3 visualization/market_charts.py --chart all   

Legal Notice
All tools operate within legal boundaries. Only publicly available data is collected. See 08-cybersecurity-intelligence/legal-framework.md for the full legal analysis.

---

## `06-ai-finance/research/university-labs.md` (expanded)

```markdown
# University Research Labs (AI + Finance)

## MIT

### Digital Currency Initiative (DCI)

| Researcher | Focus | 2025-2026 Work |
|---|---|---|
| Neha Narula | Stablecoin risk, payment token design | "Stablecoin Risk" series; payment token architecture (2025) |
| Joseph Bonneau | Blockchain security, consensus | PoS attack vectors; smart contract vulnerabilities |
| Tadayoshi Kohno | Blockchain security, ZK proofs | ZK-based payment privacy; CBDC design |

### CSAIL (Computer Science & AI Lab)

| Focus | Key Work |
|---|---|
| Adversarial ML | Detecting AI-generated phishing; adversarial robustness for financial models |
| Blockchain security | Smart contract verification; formal methods |
| Cryptography | PQC implementation; ZK proof systems |

### Network Coding Group (RLNC)

| Focus | Key Work |
|---|---|
| Random Linear Network Coding | Quantum-safe data encoding for blockchain |
| Hardware synthesis | RLNC synthesized in silicon (2026) |
| Application | Embeddable in blockchain node cores for long-term resilience |

**Key 2025-2026 Contributions:**
- Stablecoin risk framework (Narula)
- Payment token design for CBDCs
- RLNC hardware synthesis (quantum-safe blockchain)
- ZK proofs for financial privacy
- FHE for confidential computing
- Adversarial ML for financial fraud detection

---

## Stanford

### Tse Lab (David Tse)

| Focus | Key Work |
|---|---|
| Blockchain consensus | Three attacks on PoS Ethereum (2025) |
| Error-correcting codes | Ebb-and-flow protocols for data availability |
| Quantum + blockchain | Co-authored Google Quantum AI whitepaper (Mar 2026) |
| RLNC | Random Linear Network Coding for quantum safety |

### CS Department (Cryptography)

| Focus | Key Work |
|---|---|
| PQC | ML-DSA implementation; blockchain migration |
| Smart contracts | Formal verification; bug detection |
| ZK proofs | ZK-STARKs for financial compliance |

### Blockchain Center

| Focus | Key Work |
|---|---|
| Tokenization | Institutional tokenization research |
| DeFi | Protocol design; MEV analysis |
| Industry bridge | Partnerships with BlackRock, JPMorgan, Fidelity |

**Key 2025-2026 Contributions:**
- PoS security: three novel attack vectors on Ethereum
- Error-correcting codes for blockchain data availability
- Quantum attacks on ECC (with Google + Ethereum Foundation)
- RLNC for quantum-safe blockchain (with MIT)
- Tokenization architecture for institutional use

---

## ETH Zürich

### Blockchains Group

| Focus | Key Work |
|---|---|
| Protocol design | Smart contract verification; consensus mechanisms |
| Quantum finance | QAOA, VQE for financial optimization |
| ZK proofs | ZK-SNARK/STARK implementations for compliance |

### Quantum Computing Center

| Focus | Key Work |
|---|---|
| Quantum algorithms | Amplitude estimation; portfolio optimization |
| Quantum error correction | Fault-tolerant QC for finance |
| Quantum ML | Hybrid quantum-classical for AML |

---

## Carnegie Mellon

### CyLab

| Focus | Key Work |
|---|---|
| AI forensics | GNNs for AML; adversarial ML detection |
| Cybersecurity | Blockchain security; smart contract auditing |
| OSINT | Automated intelligence collection; NLP for dark web |

### ML Department

| Focus | Key Work |
|---|---|
| GNNs for finance | Transaction graph analysis; entity resolution |
| Adversarial robustness | Detecting AI-generated social engineering |
| Federated learning | Cross-institution ML without data sharing |

---

## Columbia

### Data Science Institute

| Focus | Key Work |
|---|---|
| GNNs for AML | Transaction graph analysis; community detection |
| Financial networks | Systemic risk; contagion modeling |
| NLP for finance | Regulatory document analysis; sentiment |

---

## Tsinghua (China)

### Fintech Research Center

| Focus | Key Work |
|---|---|
| Quantum finance | QAOA, VQE (China perspective) |
| CBDC design | e-CNY architecture; cross-border (mBridge research) |
| AI + AML | AI-driven AML (China regulatory context) |
| Cross-border payments | mBridge research; trade finance tokenization |

---

## NUS Singapore

| Focus | Key Work |
|---|---|
| CBDC | Project Guardian research; cross-border payments |
| mBridge | Technical architecture; compliance |
| Quantum | NUS Quantum; optimization for finance |
| AML | AI-driven AML (Singapore regulatory context) |

---

## Oxford

### Quantum Technology Institute

| Focus | Key Work |
|---|---|
| Quantum optimization | QAOA for financial portfolios |
| PQC | Implementation for financial infrastructure |
| Quantum cybersecurity | PQC migration strategy |

---

## Cambridge

### Quantum (merged with Xanadu)

| Focus | Key Work |
|---|---|
| Quantum-enhanced cybersecurity | PQC implementation; QKD |
| Photonic quantum computing | Xanadu partnership; long-term |
| Financial optimization | Quantum portfolio management |

---

## Lviv Polytechnic (Ukraine)

### Cryptography

| Researcher | Focus |
|---|---|
| Solomka & Liubinskyy | ZKP for financial compliance (KYC MVP, 2025) |

**Key Contribution:**
- ZKP-based KYC verification: 97% reduction in exposed user data
- MVP demonstrated (2025)
- Open-source implementation   