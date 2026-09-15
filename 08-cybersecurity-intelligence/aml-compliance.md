# AML/CFT Compliance in Digital Assets (Expanded)

## Regulatory Framework

### US

| Regulation | Scope | Key Requirements |
|---|---|---|
| **BSA** (31 U.S.C. § 5311) | All financial institutions | SAR, CTR, record-keeping |
| **FinCEN VASP Rule** | Crypto exchanges, custodians, money transmitters | Registration, AML program, CIP |
| **Travel Rule** (31 C.F.R. § 1010.100) | VASPs | Sender/receiver info for transfers >$3,000 |
| **GENIUS Act** (2025) | Stablecoin issuers | 1:1 reserves; AML; CIP; SAR |
| **OFAC** | All entities | Sanctions screening; 50% ownership rule |
| **SEC** | Securities | Anti-fraud; market manipulation |
| **CFTC** | Commodities | Digital commodities; CIP |

### EU

| Regulation | Scope | Key Requirements |
|---|---|---|
| **MiCA** (EU 2023/1114) | All crypto-asset service providers | Licensing; AML; consumer protection |
| **AMLD6** (EU 2024/1624) | VASPs; crypto | CDD; beneficial ownership; SAR |
| **TFR** (Transfer of Funds Reg.) | VASPs | Travel Rule (same as US) |
| **DORA** (EU 2022/2554) | Financial entities | Operational resilience; incident reporting |

### International

| Framework | Scope | Key Requirements |
|---|---|---|
| **FATF Recommendations** | All jurisdictions | 40 recommendations; Travel Rule; VASP regulation |
| **FATF 2026 Update** | VASPs | Allow-listing; freeze/burn functions; DeFi |
| **UNODC** | All | Cybercrime; money laundering |

## AI-Enhanced AML (Deep Dive)

### Current Production Systems

| System | Technology | Accuracy | False Positive Rate |
|---|---|---|---|
| Chainalysis KYT | ML + rules + expert labels | 92-95% | 5-10% |
| TRM Labs Screening | Glass-box ML + rules | 93-96% | 3-8% |
| Elliptic Lens | ML + cross-chain | 91-94% | 5-12% |
| CoSemiGNN (research) | Dynamic GNN | **94.7%** | <5% |
| PrivChain-AI (research) | Federated + blockchain | **94.7%** | <5% |
| ZKP-enhanced (research) | ZK + DL | **96.7%** | <3% |
| Rule-based (baseline) | Thresholds + patterns | 70-80% | 20-40% |

### GNN Architecture for AML
INPUT: Transaction graph
Nodes: Addresses (features: degree, volume, velocity, age)
Edges: Transactions (features: amount, time, token, gas)

MODEL: Graph Attention Network (GAT)
Layer 1: GATConv(16 → 256, heads=8)
Layer 2: GATConv(2048 → 256, heads=8)
Layer 3: GATConv(2048 → 256, heads=8)
Output: Risk score per node + per edge

TRAINING:
Positive: Confirmed illicit (law enforcement, Chainalysis reports)
Negative: Random normal transactions
Ratio: ~1:100 (focal loss)
Data: 30+ days of transactions (millions of edges)

EVALUATION:
AUC-ROC: 0.97+
Precision@1000: 85%+
F1: 0.89+
False positive rate: <5% at 95% recall

DEPLOYMENT:
Real-time: Score each new transaction <100ms
Batch: Re-score full graph daily
Alert: Score > 0.947 → flag for review
SAR: Score > 0.99 + pattern match → auto-file SAR

### ZKP-Enhanced AML (Research → Production)

| Component | Function | Status |
|---|---|---|
| ZK proof of compliance | "I am not sanctioned" without revealing identity | Mandala Phase 2 |
| ZK proof of reserves | "My reserves are sufficient" without revealing balance | Decker-ZKP (2025) |
| ZK + GNN | Privacy-preserving fraud detection | Research (96.7% accuracy) |
| SDAS | Selective disclosure authorization | arXiv 2026 |
| Production target | US banks by end 2026 | "Unremarkable rather than experimental" |

## Key Challenges (2026)

| Challenge | Detail | Mitigation |
|---|---|---|
| Cross-border | Different AML regimes per jurisdiction | FATF convergence; bilateral agreements |
| Cross-chain | Assets move across 450+ chains | CCIP tracking; multi-chain analytics |
| DeFi | No central entity to monitor | Protocol-level compliance (Mandala); ZK proofs |
| Privacy | ZK vs. regulatory transparency | ZK proofs (prove compliance without revealing) |
| Speed | Real-time at blockchain speed | <100ms scoring; edge computing |
| Volume | 500M+ daily transactions | ML (not rules); distributed processing |
| Adversarial | Actors evade detection | Adversarial training; continuous retraining |
| Regulatory | GENIUS vs. MiCA vs. national | FSB convergence; cross-border cooperation |

## SAR Filing (US)

| Trigger | Threshold | Deadline |
|---|---|---|
| Suspicious activity | >$5,000 (any type) | 30 days (60 max) |
| Money laundering | Any amount | 30 days |
| Terrorist financing | Any amount | **24 hours** |
| Sanctions evasion | Any amount | **24 hours** |
| Structuring | >$10,000 split to avoid CTR | 30 days |

### Crypto-Specific SAR Triggers

| Pattern | Example |
|---|---|
| Rapid movement | >$10K through 5+ wallets in <1 hour |
| Round numbers | Repeated $10K, $50K, $100K transfers |
| New counterparty | First transaction with unknown entity >$100K |
| Mix/tumbler use | Deposit into Tornado Cash, CoinJoin |
| Cross-chain bridge | Move across 3+ chains in <10 min |
| Exchange deposit | Large deposit followed by immediate withdrawal |
| Dark web link | Address linked to dark web marketplace |
| Sanctions proximity | Address within 2 hops of OFAC-listed entity |
| Velocity anomaly | 10x normal transaction velocity |
| Time anomaly | Activity at unusual hours for entity type |   