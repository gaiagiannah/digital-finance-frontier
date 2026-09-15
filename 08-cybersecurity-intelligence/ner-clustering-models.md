# NER Models, Cross-Platform Clustering & Blockchain Cross-Referencing

## Named Entity Recognition (NER) for Crypto Forensics

### What to Extract

| Entity Type | Examples | Source |
|---|---|---|
| Person names | "John Doe", "Satoshi" | Social media, forums, dark web, KYC leaks |
| Organization names | "Binance", "Lazarus Group" | All sources |
| Addresses (crypto) | 0x1234...abcd, bc1q... | On-chain, social, dark web |
| Domains | evil-scams.com | Infrastructure, social, dark web |
| IP addresses | 192.168.1.1, 2001:db8::1 | Infrastructure, Shodan, Censys |
| Email addresses | admin@scam.com | All sources |
| Phone numbers | +1-555-0123 | Social, dark web |
| Amounts (crypto) | 100 BTC, 5000 ETH | On-chain, social, dark web |
| Amounts (fiat) | $1,000,000 | Dark web, social, financial records |
| Dates | "March 15, 2026" | All sources |
| Locations | "Singapore", "Seoul" | Social, forums, KYC |
| TTPs | "bridge exploit", "social engineering" | Forums, reports, dark web |
| Threat actors | "Lazarus", "APT41" | Reports, forums, dark web |
| Protocols/Contracts | 0xContract... (DeFi) | On-chain, social |
| Tokens/Assets | USDC, WBTC, PEPE | On-chain, social |

### Model Architecture
INPUT: Raw text (social media, dark web, forums, reports)
│
▼
┌─────────────────────────────────────────────────────────┐
│ PREPROCESSING │
│ - Tokenization (subword for crypto addresses) │
│ - Normalization (lowercase, remove noise) │
│ - Language detection (multi-lingual: EN, RU, ZH, KO) │
├─────────────────────────────────────────────────────────┤
│ NER MODEL (Fine-tuned) │
│ - Base: BERT / RoBERTa / DeBERTa / LLaMA │
│ - Fine-tuned on: Crypto forensics corpus │
│ - Custom entities: CRYPTO_ADDR, DOMAIN, IP, TTP, │
│ THREAT_ACTOR, AMOUNT_CRYPTO, AMOUNT_FIAT │
│ - Output: Entity spans + confidence scores │
├─────────────────────────────────────────────────────────┤
│ POST-PROCESSING │
│ - Entity normalization (address checksum validation) │
│ - Disambiguation (context-aware) │
│ - Confidence thresholding │
│ - Multi-label assignment │
├─────────────────────────────────────────────────────────┤
│ OUTPUT │
│ - Structured JSON: {entity, type, span, confidence} │
│ - Graph edges: entity → entity relationships │
│ - Alert triggers: high-risk entity detected │
└─────────────────────────────────────────────────────────┘

### Training Data Sources

| Source | Volume | Labeling |
|---|---|---|
| Public blockchain transactions + metadata | 500M+ txs | Auto (address format) |
| Dark web forum posts (public) | 10M+ posts | Semi-auto + human |
| Social media (Twitter/X, Telegram, Discord) | 50M+ posts | Semi-auto |
| Threat intelligence reports (public) | 10K+ reports | Human |
| Law enforcement press releases | 5K+ | Human |
| Academic datasets (CoNLL, OntoNotes) | 1M+ | Pre-labeled |
| Synthetic data (LLM-generated) | 1M+ | Auto |

### Implementation

```python
# Pseudocode: Crypto NER Pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification
import json

class CryptoNER:
    def __init__(self, model_name="roberta-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForTokenClassification.from_pretrained(
            "fine-tuned/crypto-ner-v1"
        )
        self.entity_types = [
            "CRYPTO_ADDR", "DOMAIN", "IP_ADDR", "EMAIL",
            "PERSON", "ORG", "TTP", "THREAT_ACTOR",
            "AMOUNT_CRYPTO", "AMOUNT_FIAT", "DATE", "LOCATION"
        ]

    def extract(self, text: str) -> list[dict]:
        tokens = self.tokenizer(text, return_tensors="pt")
        predictions = self.model(**tokens)
        entities = self._decode(predictions, text)
        entities = self._normalize(entities)  # checksum, format
        entities = self._disambiguate(entities, text)  # context
        return entities

    def _normalize(self, entities):
        # Validate crypto addresses (Bech32, keccak checksum)
        # Normalize domains (lowercase, remove www)
        # Standardize amounts (BTC/ETH/USD)
        pass

    def _disambiguate(self, entities, context):
        # "Apple" → ORG (tech) vs. fruit
        # "0x..." → CRYPTO_ADDR vs. contract vs. token
        # "Lazarus" → THREAT_ACTOR vs. biblical reference
        pass   


Custom Entity Types (Crypto-Specific)
Entity	Regex/Pattern	Validation
Bitcoin (Bech32)	bc1[ac-hj-np-z02-9]{6,87}	Bech32 checksum
Bitcoin (Legacy)	[13][a-km-zA-HJ-NP-Z1-9]{25,34}	Base58Check
Ethereum	0x[a-fA-F0-9]{40}	Keccak-256 checksum
Solana	[1-9A-HJ-NP-Za-km-z]{32,44}	Base58 + Ed25519
Domain	[a-z0-9.-]+\.[a-z]{2,}	DNS lookup
IPv4	\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}	Range validation
IPv6	[0-9a-fA-F:]+	Format validation
Email	standard RFC 5322	MX record check
TTP	Keyword + context	MITRE ATT&CK mapping
Threat Actor	Known list + context	Confidence scoring


Cross-Platform Clustering
Problem
The same actor appears across multiple platforms with different identifiers:

Twitter: @scam_master
Telegram: t.me/scamchannel
Discord: ScamMaster#1234
Dark web: "DarkLord"
On-chain: 0x1234...abcd
Domain: evil-scams.com
Goal: Cluster all these identifiers into a single entity profile.

Clustering Algorithm
┌─────────────────────────────────────────────────────────────────┐
│  INPUT: Entities from all platforms (NER output)               │
├─────────────────────────────────────────────────────────────────┤
│  STEP 1: FEATURE EXTRACTION                                    │
│  - String similarity (Levenshtein, Jaccard)                    │
│  - Temporal correlation (same time window)                     │
│  - Infrastructure overlap (same IP, domain, hosting)           │
│  - Behavioral similarity (posting patterns, language)          │
│  - Financial linkage (same wallet, same exchange)              │
│  - Content similarity (embedding distance)                     │
├─────────────────────────────────────────────────────────────────┤
│  STEP 2: GRAPH CONSTRUCTION                                    │
│  - Nodes = entities (all types, all platforms)                 │
│  - Edges = similarity scores (weighted)                        │
│  - Edge types: string, temporal, infra, behavioral, financial  │
├─────────────────────────────────────────────────────────────────┤
│  STEP 3: COMMUNITY DETECTION                                   │
│  - Louvain / Leiden algorithm (modularity optimization)        │
│  - OR: GNN-based node classification (PyTorch Geometric)       │
│  - OR: DBSCAN on embedding space (density-based)              │
├─────────────────────────────────────────────────────────────────┤
│  STEP 4: ENTITY RESOLUTION                                     │
│  - Merge clusters with high-confidence links                   │
│  - Assign canonical identifier (most-verified entity)          │
│  - Generate entity profile (all linked identifiers)            │
│  - Confidence score per link                                   │
├─────────────────────────────────────────────────────────────────┤
│  STEP 5: OUTPUT                                                │
│  - Entity cluster: {canonical_id, [linked_entities],           │
│    confidence, first_seen, last_seen, platforms, risk_score}   │
│  - Alert: New cluster matching known threat actor              │
└─────────────────────────────────────────────────────────────────┘   

Feature Engineering
Feature	Type	Weight	Source
String similarity (name/handle)	Cosine (embeddings)	0.2	All platforms
Temporal overlap	Jaccard (active hours)	0.15	All platforms
Infrastructure (IP/domain)	Exact match	0.3	Shodan, Censys, DNS
Financial (wallet/exchange)	Exact match	0.25	On-chain, exchange KYC
Content similarity	Cosine (embeddings)	0.1	NLP
Language / dialect	Classification	0.05	NLP
Posting frequency	Correlation	0.05	Timestamps

GNN Approach (Advanced)
# Pseudocode: GNN Entity Clustering
import torch
import torch_geometric as pyg

class EntityClusterGNN(pyg.nn.MessagePassing):
    def __init__(self, hidden_dim=256, num_layers=3):
        super().__init__(aggr='mean')
        self.lin1 = pyg.nn.GATConv(in_channels, hidden_dim, heads=8)
        self.lin2 = pyg.nn.GATConv(hidden_dim * 8, hidden_dim)
        self.lin3 = pyg.nn.GATConv(hidden_dim, hidden_dim)
        self.classifier = torch.nn.Linear(hidden_dim, 2)  # same / different

    def forward(self, x, edge_index, edge_attr):
        # x: node features (entity embeddings)
        # edge_index: graph structure (potential links)
        # edge_attr: edge features (similarity scores)
        x = torch.relu(self.lin1(x, edge_index))
        x = torch.relu(self.lin2(x, edge_index))
        x = torch.relu(self.lin3(x, edge_index))
        return self.classifier(x)

# Training:
# - Positive pairs: confirmed same entity (from law enforcement, KYC)
# - Negative pairs: confirmed different entities
# - Semi-supervised: few labeled + many unlabeled
# - Loss: Contrastive + cross-entropy   

Blockchain Cross-Referencing
Problem
Connect on-chain activity to off-chain identity:

Wallet 0x1234... → Person "John Doe" (via exchange KYC)
Wallet 0x5678... → Domain evil-scams.com (via payment to registrar)
Wallet 0x9abc... → Telegram t.me/scamchannel (via tip jar)

Cross-Reference Pipeline
┌─────────────────────────────────────────────────────────────────┐
│  ON-CHAIN DATA                                                  │
│  - Transaction history (all chains)                             │
│  - Token transfers                                              │
│  - Contract interactions                                        │
│  - Gas payments                                                 │
│  - Exchange deposits/withdrawals                                │
├─────────────────────────────────────────────────────────────────┤
│  OFF-CHAIN DATA                                                 │
│  - Social media mentions (address posted)                       │
│  - Dark web payments (address in listing)                       │
│  - Domain payments (address → registrar)                        │
│  - Tip jars (address → social profile)                          │
│  - KYC data (legal process)                                     │
│  - Infrastructure (IP → wallet creation)                        │
├─────────────────────────────────────────────────────────────────┤
│  LINKAGE RULES                                                  │
│  1. Direct: Address mentioned in post with identity             │
│  2. Financial: Payment to known entity (domain, service)        │
│  3. Behavioral: Same timing as social activity                  │
│  4. Infrastructure: Same IP at wallet creation                  │
│  5. Exchange: Deposit/withdrawal pattern matches KYC user       │
│  6. Clustering: Group wallets → resolve cluster to entity       │
├─────────────────────────────────────────────────────────────────┤
│  OUTPUT                                                         │
│  - Entity → Wallet mapping (with confidence)                    │
│  - Entity → Infrastructure mapping                              │
│  - Entity → Activity timeline                                   │
│  - Risk score per entity                                        │
└─────────────────────────────────────────────────────────────────┘   

Key Techniques
Technique	Description	Confidence
Direct mention	Address posted with name/identity in public post	High
Tip jar linkage	Address used as tip jar on social profile	High
Domain payment	Address paid domain registrar → domain → WHOIS	Medium-High
Exchange pattern	Deposit → trade → withdrawal matches KYC user	High (with legal process)
Temporal correlation	Wallet activity matches social posting time	Medium
Infrastructure	Same IP at wallet creation + social account creation	Medium
Clustering	Multiple wallets → one cluster → resolve one wallet	Medium
Contract interaction	Address interacts with known scam contract	Medium-High
Token pattern	Same token distribution pattern as known actor	Medium
Cross-chain	Same entity on multiple chains (bridge tracking)	Medium

---

## `08-cybersecurity-intelligence/legal-framework.md`

```markdown
# Legal Framework: Laws, Acts & Regulations

## CRITICAL: This project operates within legal boundaries.
## Only collect data you can lawfully access. When in doubt, consult legal counsel.

---

## United States

### Federal Laws

| Law | Citation | Relevance |
|---|---|---|
| **Computer Fraud and Abuse Act (CFAA)** | 18 U.S.C. § 1030 | **Most critical.** Prohibits unauthorized access to computer systems. Post-*Van Buren v. United States* (2021): "gates-up-or-down" test — accessing data you're authorized to view (even if you violate a policy) is NOT a CFAA violation. Accessing data you're NOT authorized to view IS. |
| **Wiretap Act** | 18 U.S.C. § 2511 | Prohibits intercepting communications. One-party consent (US) / all-party consent (some states). |
| **Stored Communications Act (SCA)** | 18 U.S.C. § 2701 | Prohibits accessing stored communications (email, messages) without consent or legal process. |
| **Electronic Communications Privacy Act (ECPA)** | 18 U.S.C. § 2510 | Umbrella for Wiretap + SCA. |
| **Bank Secrecy Act (BSA)** | 31 U.S.C. § 5311 | Requires financial institutions to file SARs/CTRs. |
| **Patriot Act (Title III)** | 18 U.S.C. § 980 | Expanded law enforcement powers; FISA. |
| **CLOUD Act** | 18 U.S.C. § 2713 | US providers must produce data in their possession, regardless of location. |
| **RICO** | 18 U.S.C. § 1961 | Racketeer Influenced and Corrupt Organizations — used for organized crypto crime. |
| **Money Laundering Control Act** | 18 U.S.C. § 1956 | Prohibits laundering proceeds of specified unlawful activities. |
| **Travel Rule** | 31 C.F.R. § 1010.100 | VASPs must share sender/receiver info for transfers >$3,000. |
| **FATF Recommendations** | (International) | 40 recommendations; US implements via BSA/AML. |
| **OFAC Sanctions** | IEEPA; 31 C.F.R. Part 500 | Prohibits transactions with sanctioned entities; crypto included. |
| **SEC Registration** | Securities Act of 1933; Exchange Act of 1934 | Tokenized securities; market manipulation. |
| **CFTC** | CEA; CFTC Act | Digital commodities; derivatives. |
| **GDPR (if EU data)** | EU 2016/679 | If processing EU personal data, GDPR applies regardless of location. |

### Key CFAA Interpretations (Post-2021)

| Scenario | CFAA Violation? | Authority |
|---|---|---|
| Scraping public website data | **No** | *hiQ v. LinkedIn* (9th Cir. 2022); *Van Buren* (2021) |
| Accessing data behind login (with valid credentials, violating ToS) | **No** (post-Van Buren) | *Van Buren v. United States*, 593 U.S. 365 (2021) |
| Accessing data behind login (without credentials) | **Yes** | CFAA § 1030(a)(2) |
| Accessing private social media group (not a member) | **Yes** | CFAA § 1030(a)(2) |
| Using compromised credentials | **Yes** | CFAA; 18 U.S.C. § 1028 |
| Scraping dark web public market | **No** | Public data; *hiQ* |
| Purchasing stolen data | **Yes** | 18 U.S.C. § 1030; § 1343 |
| Creating fake social media account for social engineering | **Gray area** | Consult counsel; potentially § 1343 (wire fraud) |
| Monitoring public Telegram channel | **No** | Public data |
| Accessing private Telegram group (not a member) | **Yes** | CFAA |

### State Laws (Most Relevant)

| State | Law | Relevance |
|---|---|---|
| California | CCPA/CPRA | Personal data privacy (if handling user data) |
| New York | SHIELD Act | Data breach notification; security requirements |
| Texas | Texas Identity Theft Enforcement Act | Identity theft; financial fraud |
| Florida | Florida Information Protection Act | Data security; breach notification |

---

## European Union

| Law | Relevance |
|---|---|
| **GDPR** (EU 2016/679) | Personal data processing; applies if processing EU data subjects' data |
| **MiCA** (EU 2023/1114) | Crypto-asset regulation; VASP licensing; AML |
| **AMLD6** (EU 2024/1624) | Anti-money laundering; crypto-asset service providers |
| **DORA** (EU 2022/2554) | Digital operational resilience for financial entities |
| **ePrivacy Directive** (2002/58/EC) | Electronic communications privacy |
| **NIS2 Directive** (EU 2022/2555) | Network and information security |

---

## United Kingdom

| Law | Relevance |
|---|---|
| **UK GDPR + DPA 2018** | Personal data (post-Brexit equivalent) |
| **Computer Misuse Act 1990** | UK equivalent of CFAA; unauthorized access |
| **Proceeds of Crime Act 2002 (POCA)** | Money laundering; asset freeze |
| **Terrorism Act 2000** | Terrorist financing |
| **FCA Handbook** | Financial services regulation; crypto |

---

## International

| Framework | Relevance |
|---|---|
| **FATF Recommendations** | 40 recommendations; Travel Rule; VASP regulation |
| **UNODC** | Cybercrime Convention (Budapest Convention) |
| **INTERPOL** | Cross-border law enforcement cooperation |
| **MLATs** | Mutual Legal Assistance Treaties (bilateral) |
| **CLOUD Act** | US extraterritorial data access |

---

## Operational Legal Rules (For This Project)

### DO

| Action | Legal Basis |
|---|---|
| Scrape public websites, social media, forums | *hiQ*; *Van Buren*; First Amendment |
| Access public blockchain data | Public information; no legal barrier |
| Use Tor to access public .onion sites | First Amendment; public data |
| Monitor public Telegram/Twitter/Discord channels | Public data |
| Use commercial OSINT tools (Maltego, SpiderFoot, BreadcrumbApp) | Terms of Service compliance |
| Use blockchain analytics platforms (Chainalysis, TRM, Elliptic) | Commercial subscription; ToS |
| Correlate publicly available data | No legal barrier |
| Build NER models on public data | No legal barrier |
| Publish research on public data | First Amendment; academic freedom |
| Respond to lawful legal process (if you're a provider) | CLOUD Act; BSA |

### DO NOT

| Action | Legal Risk |
|---|---|
| Access data behind login without valid credentials | CFAA § 1030(a)(2); up to 10 years |
| Access private groups/channels without invitation/consent | CFAA; platform ToS |
| Use compromised/stolen credentials | CFAA; 18 U.S.C. § 1028; up to 15 years |
| Purchase stolen data on dark web | 18 U.S.C. § 1030; § 1343; up to 20 years |
| Create fake accounts for social engineering | 18 U.S.C. § 1343 (wire fraud); § 912 (impersonation) |
| Intercept communications (Wiretap/SCA) | 18 U.S.C. § 2511; up to 5 years |
| Access WhatsApp/private messages without consent | CFAA; 18 U.S.C. § 2511 |
| Exfiltrate data from systems you don't own | CFAA; 18 U.S.C. § 1030 |
| Bypass technical access controls (without authorization) | CFAA; 18 U.S.C. § 1030(a)(5) |
| Violate platform Terms of Service in ways that constitute "unauthorized access" | CFAA (post-Van Buren: ToS alone insufficient, but ToS + technical barrier = unauthorized) |

### GRAY AREA (Consult Legal Counsel)

| Action | Risk |
|---|---|
| Undercover operations (private citizen) | Varies by jurisdiction; consult counsel |
| Scraping data at high volume (DoS risk) | CFAA; computer misuse; ToS |
| Using AI to generate synthetic identity for research | 18 U.S.C. § 1028; state identity theft laws |
| Cross-border data access (US person, foreign data) | GDPR; local laws; CLOUD Act |
| Publishing identified individuals (doxxing) | Defamation; state privacy laws; GDPR |
| Using dark web data to identify real persons | GDPR; state privacy; First Amendment balance |

---

## Evidence Admissibility

| Standard | Requirement |
|---|---|
| **Authentication** | Prove the data is what it claims to be (hash, metadata, chain of custody) |
| **Best Evidence Rule** | Original data preferred; copies admissible if original unavailable |
| **Daubert/Frye** | Scientific methodology must be reliable (for expert testimony) |
| **Chain of Custody** | Documented every transfer/access from collection to presentation |
| **Hearsay Exceptions** | Business records (1102); public records (803(8)); statements against interest |
| **Frye (some states)** | Generally accepted in scientific community |
| **Daubert (federal)** | Testable, peer-reviewed, known error rate, standards |

## Data Retention & Privacy

| Requirement | Source |
|---|---|
| Minimize data collection | GDPR Art. 5(1)(c); CCPA |
| Purpose limitation | GDPR Art. 5(1)(b) |
| Data subject rights | GDPR Arts. 15-22; CCPA |
| Breach notification | GDPR Art. 33; state laws (60 days); NY SHIELD |
| Cross-border transfer | GDPR Ch. V; SCCs; adequacy decisions |
| Retention limits | BSA (5 years); GDPR (as long as necessary); state laws |   
