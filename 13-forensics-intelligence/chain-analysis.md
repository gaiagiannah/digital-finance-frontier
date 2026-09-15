# Chain Analysis Techniques

## Fundamentals

### Transaction Tracing

| Step | Action | Tool |
|---|---|---|
| 1 | Start with known address | Etherscan, Blockscout |
| 2 | Follow outputs (where money went) | Chainalysis, TRM, Elliptic |
| 3 | Follow inputs (where money came from) | Same |
| 4 | Identify exchange deposits/withdrawals | VASP labels |
| 5 | Track across chains (bridges) | CCIP analytics, LayerZero |
| 6 | Identify final destination (cash-out) | CEX, OTC, mixer |

### Heuristic Clustering

| Heuristic | Rule | Confidence | Limitation |
|---|---|---|---|
| Common Input (Bitcoin) | Two outputs share an input → same entity | **High** | Bitcoin only (UTXO model) |
| Sequential Funding | New wallet funded immediately after creation → same entity | Medium | Timing can be coincidental |
| Common Destination | Multiple wallets send to same address → same entity | Medium | Could be exchange hot wallet |
| Change Detection | Identify change address (heuristic) | Medium | Heuristic can fail |
| Exchange Pattern | Deposit → trade → withdrawal → same user | High | Requires exchange KYC |
| Temporal Proximity | Two wallets active within seconds → same entity | Low-Medium | Bots, MEV |
| Amount Pattern | Same amount split across wallets → same entity | Medium | Could be coincidence |
| Gas Pattern | Same gas price + nonce sequence → same entity | Medium-High | Mempool visibility |

### Mix/Tumbler Analysis

| Mixer | Chain | De-anonymization Approach |
|---|---|---|
| Tornado Cash | Ethereum | Input/output correlation; timing; amount matching; ZK pool analysis |
| CoinJoin | Bitcoin | Input clustering; timing; amount; participant overlap |
| Wasabi Wallet | Bitcoin | CoinJoin analysis; timing; amount |
| Samourai (defunct) | Bitcoin | Historical analysis; known addresses |
| Privacy pools (DeFi) | Various | Pool entry/exit timing; amount correlation |

**Key insight**: Mixers reduce but don't eliminate traceability. With sufficient data (timing, amounts, exchange deposits), most mixer users can be re-identified. Chainalysis claims 90%+ de-anonymization rate for Tornado Cash.

### Cross-Chain Tracking

| Bridge Type | Tracking Method |
|---|---|
| Lock-and-mint (e.g., WBTC) | Track lock on source chain → mint on destination |
| Liquidity pool (e.g., Wormhole) | Track deposit → pool → withdrawal |
| Validator-based (e.g., LayerZero) | Track message → validator confirmation → execution |
| CCIP (Chainlink) | Track CCIP message → router → destination execution |
| Native bridges (e.g., Optimism) | Track L1 deposit → L2 credit |

**Key challenge**: Each bridge has different data availability. Some are fully transparent (on-chain); others are opaque (off-chain validators). CCIP and native bridges are most trackable.

## Advanced Techniques

### Graph Neural Network (GNN) Analysis
INPUT: Transaction graph (nodes = addresses, edges = transactions)
Node features: degree, volume, velocity, age, token diversity
Edge features: amount, time, token, gas, contract call

MODEL: GAT (Graph Attention Network)
3 layers × 256 hidden × 8 heads
Edge features included
Temporal encoding

OUTPUT:

Node risk score (0-1)
Edge risk score (0-1)
Community detection (cluster = potential entity)
Anomaly flag (deviation from learned norm)
TRAINING:

Semi-supervised (few labeled illicit + many normal)
Contrastive learning (positive/negative pairs)
Adversarial training (evasion resistance)
PERFORMANCE (target):

AUC-ROC: 0.97+
Precision@1000: 85%+
False positive: <5% at 95% recall

### Temporal Graph Analysis

| Technique | Description | Use Case |
|---|---|---|
| Time-respecting traversal | Only follow edges forward in time | Fund flow (no "time travel") |
| Burst detection | >5 txs in 60 seconds | Laundering velocity |
| Cyclic patterns | Regular intervals (daily, weekly) | Salary, subscription, or structured laundering |
| Decay analysis | Activity decay after initial burst | One-time exploit vs. ongoing operation |
| Seasonal patterns | Time-of-day, day-of-week | Geographic inference |
| Velocity anomaly | 10x normal speed for entity | Alert trigger |

### Behavioral Fingerprinting

| Feature | What It Reveals | Reliability |
|---|---|---|
| Transaction size distribution | Individual vs. institutional | High |
| Time-of-day activity | Geographic location (time zone) | Medium |
| Gas price sensitivity | Cost consciousness (individual) | Low-Medium |
| Token diversity | Portfolio strategy | Low |
| Address reuse | Individual (sloppy) vs. institutional (systematic) | High |
| Contract interaction pattern | Technical sophistication | Medium |
| Bridge usage pattern | Cross-chain strategy | Medium |
| Exchange preference | Jurisdiction, trust | Medium |
| Mixer usage | Anonymization intent | High |
| Round-number usage | Individual (less sophisticated) | Medium |

### Entity Resolution Pipeline
┌─────────────────────────────────────────────────────────────────┐
│ ENTITY RESOLUTION PIPELINE │
├─────────────────────────────────────────────────────────────────┤
│ 1. COLLECT │
│ - All transactions for target address (all chains) │
│ - All counterparty addresses │
│ - All token transfers │
│ - All contract interactions │
│ - All bridge crossings │
├─────────────────────────────────────────────────────────────────┤
│ 2. CLUSTER │
│ - Apply heuristic rules (common input, sequential, etc.) │
│ - GNN community detection │
│ - Temporal clustering (activity windows) │
│ - Amount correlation (split/merge patterns) │
├─────────────────────────────────────────────────────────────────┤
│ 3. LABEL │
│ - Match clusters against known labels (Chainalysis, TRM) │
│ - Exchange identification (hot wallets) │
│ - Mixer identification │
│ - DeFi protocol identification │
│ - Cross-reference with off-chain data (OSINT) │
├─────────────────────────────────────────────────────────────────┤
│ 4. RESOLVE │
│ - Cluster → Entity (if confident) │
│ - Entity → Identity (if KYC available via legal process) │
│ - Entity → Infrastructure (IP, domain, social) │
│ - Assign confidence score per link │
├─────────────────────────────────────────────────────────────────┤
│ 5. REPORT │
│ - Entity profile (all linked identifiers) │
│ - Transaction summary (in, out, net) │
│ - Risk score │
│ - Recommendations (further investigation, legal process) │
└─────────────────────────────────────────────────────────────────┘

## Tools for Chain Analysis

| Tool | Type | Cost | Best For |
|---|---|---|---|
| **Chainalysis Reactor** | Commercial | Enterprise | Full investigation; law enforcement; court evidence |
| **TRM Labs** | Commercial | Enterprise | Glass-box attribution; federal; real-time |
| **Elliptic Investigator** | Commercial | Enterprise | Cross-chain; DeFi; EU |
| **Dune Analytics** | Free / Pro | Free / $49+ | Custom SQL; quick queries; public data |
| **Nansen** | Commercial | $100+/mo | Smart money; wallet labels; alerts |
| **Arkham Intelligence** | Freemium | Free / $50+ | Entity labels; whale alerts; free tier |
| **Etherscan** | Free / Pro | Free / $49+ | Basic transaction inspection |
| **Blockscout** | Free | Free | Multi-chain explorer |
| **Neo4j + custom** | Open source | Free | Custom graph analysis; GNN |
| **Gephi** | Open source | Free | Network visualization | 