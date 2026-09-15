# KYC & Identity Resolution 

## Data Sources

| Source | Data Available | Access Method | Legal Authority |
|---|---|---|---|
| CEX records | Name, DOB, address, ID docs, IP, device | Legal process | CLOUD Act; 18 U.S.C. § 2703 |
| OTC desks | High-value transaction records; identity | Legal process | BSA; subpoena |
| Stablecoin issuers | Reserve data; user data (GENIUS Act) | Legal process | GENIUS Act; BSA |
| On-chain labels | Entity tags (Chainalysis, Nansen, Arkham) | Commercial subscription | Contract (ToS) |
| Social media | Public profiles, posts, metadata | Public (OSINT) | First Amendment; public data |
| Domain/IP | Infrastructure correlation | Public + Shodan/Censys | Public data |
| Blockchain explorers | Transaction history, contract code | Public | No legal barrier |
| Corporate registries | Company ownership, directors | Public (varies by jurisdiction) | Public records |
| Court records | Judgments, filings, bankruptcies | Public (PACER, state courts) | Public records |
| Credit bureaus | Credit history, addresses | Legal process / consent | FCRA |
| Phone records | Call logs, SMS | Legal process (warrant) | 18 U.S.C. § 2520 |
| Email | Content, metadata | Legal process (warrant) | SCA; 18 U.S.C. § 2703 |

## De-Anonymization Techniques

### On-Chain → Off-Chain

| Technique | Description | Confidence | Legal Basis |
|---|---|---|---|
| Exchange KYC subpoena | Obtain identity behind exchange wallet | **High** (if obtained) | CLOUD Act; 18 U.S.C. § 2703 |
| Direct mention | Address posted with name/identity in public post | **High** | Public data |
| Tip jar linkage | Address = social profile tip jar | **High** | Public data |
| Domain payment | Address paid domain registrar → domain → WHOIS | **Medium-High** | Public + WHOIS |
| Infrastructure | Same IP at wallet creation + social account creation | **Medium** | Public (if available) |
| Temporal correlation | Wallet activity matches social posting time | **Medium** | Public data |
| Clustering | Multiple wallets → one cluster → resolve one wallet | **Medium** | Analysis |
| Contract interaction | Address interacts with known scam contract | **Medium-High** | Public data |
| Token pattern | Same distribution pattern as known actor | **Medium** | Analysis |
| Cross-chain | Same entity on multiple chains (bridge tracking) | **Medium** | Public data |
| Gas pattern | Same gas price + nonce sequence (same node) | **Medium-High** | Public data |

### Off-Chain → On-Chain

| Technique | Description | Confidence |
|---|---|---|
| Social media mention | Person posts their wallet address publicly | High |
| GitHub commit | Developer signs commits with address | High |
| Forum post | Person links wallet in forum (Bitcointalk, etc.) | High |
| NFT profile | OpenSea profile linked to wallet | High |
| DAO governance | Voting with known identity (public DAO) | High |
| Bug bounty | Address submitted with identity (Immunefi, etc.) | High |
| Airdrop claim | Claimed with verified identity (KYC airdrop) | High |
| Dune dashboard | Public dashboard with labeled wallets | Medium-High |

## Legal Process (US) — Detailed

| Tool | What It Gets | Speed | Cost | When to Use |
|---|---|---|---|---|
| **Subpoena** | Production of records (exchange, bank) | 2-4 weeks | Free | Civil; low urgency |
| **Warrant** | Search of premises; seizure of device | 1-2 weeks | Free | Criminal; urgent |
| **CLOUD Act** | US provider data (regardless of location) | 2-6 weeks | Free | Foreign data held by US provider |
| **MLAT** | Foreign provider data | 3-24 months | Free | Non-US provider; no CLOUD Act |
| **2703(d) Order** | Non-content records (metadata) | 1-2 weeks | Free | Email metadata, IP logs |
| **Pen/Trap** | Real-time communication monitoring | Ongoing | Free | Active investigation |
| **FISA** | Foreign intelligence (wiretap) | Ongoing | Free | National security; foreign target |
| **Civil forfeiture** | Seize assets without criminal conviction | 30-90 days | Free | Asset recovery |
| **RICO** | Organized crime (pattern of illegal activity) | 6-12 months | Free | Large-scale operations |

### CLOUD Act (Key for Crypto)

- **Applies to**: US-based providers (exchanges, wallet providers, hosting)
- **Scope**: Data in provider's "possession, custody, or control" — regardless of where stored
- **Example**: Coinbase (US) must produce user data even if stored on servers in Ireland
- **Limitation**: Non-US providers (e.g., Binance entities in Singapore) not directly subject
- **Workaround**: MLAT or bilateral agreement for non-US providers
- **Challenge**: 2022 — US requested data from Microsoft (Ireland); court ruled CLOUD Act applies to data under provider's control regardless of location

### Cross-Border Data Access

| Scenario | Method | Speed |
|---|---|---|
| US → US exchange | Subpoena / Warrant / CLOUD Act | 1-6 weeks |
| US → EU exchange | MLAT (via US-EU agreement) | 3-12 months |
| US → Singapore exchange | MLAT (US-Singapore) | 6-24 months |
| US → Chinese exchange | **Extremely difficult** (no MLAT; Chinese law) | 12-36 months+ |
| EU → US exchange | CLOUD Act (US provider) | 2-6 weeks |
| EU → EU exchange | E-Evidence Regulation (2023) | 2-8 weeks |
| UK → US exchange | CLOUD Act / MLAT | 2-12 weeks |

**Key challenge**: Chinese exchanges (Binance entities, etc.) are the hardest to get data from. Chinese law (Data Security Law, PIPL) may prohibit data export. This is a major gap in crypto investigations.

## Identity Resolution Workflow
┌─────────────────────────────────────────────────────────────────┐
│ IDENTITY RESOLUTION WORKFLOW │
├─────────────────────────────────────────────────────────────────┤
│ 1. START: Known wallet address (from investigation) │
├─────────────────────────────────────────────────────────────────┤
│ 2. ON-CHAIN ANALYSIS │
│ - Trace all transactions │
│ - Identify exchange deposits/withdrawals │
│ - Identify mixer usage │
│ - Identify cross-chain movements │
│ - Cluster related wallets │
├─────────────────────────────────────────────────────────────────┤
│ 3. EXCHANGE IDENTIFICATION │
│ - Match deposit address to exchange hot wallet │
│ - Identify which CEX (Binance, Coinbase, Kraken, etc.) │
│ - Determine jurisdiction (which entity) │
├─────────────────────────────────────────────────────────────────┤
│ 4. LEGAL PROCESS (if needed) │
│ - Subpoena / Warrant / CLOUD Act │
│ - Request: KYC data, IP, device, transaction history │
│ - Timeline: 1-6 weeks (US) / 3-24 months (foreign) │
├─────────────────────────────────────────────────────────────────┤
│ 5. OFF-CHAIN CORRELATION │
│ - Match IP to infrastructure (Shodan, Censys) │
│ - Match domain to WHOIS → registrant │
│ - Match social media (username, profile) │
│ - Match corporate registry (if business) │
│ - Match court records (if litigation) │
├─────────────────────────────────────────────────────────────────┤
│ 6. IDENTITY CONFIRMATION │
│ - Cross-reference all data points │
│ - Confidence score (1-10) │
│ - Document assumptions and gaps │
│ - Legal review (is this admissible?) │
├─────────────────────────────────────────────────────────────────┤
│ 7. REPORT │
│ - Identity: Name, DOB, address, nationality │
│ - Confidence: Score + methodology │
│ - Evidence: All data points + sources │
│ - Chain of custody: Documented │
│ - Recommendations: Arrest warrant, asset freeze, etc. │
└─────────────────────────────────────────────────────────────────┘

## Privacy Considerations

| Data Type | Privacy Protection | Legal Exception |
|---|---|---|
| KYC data (name, DOB, ID) | GDPR; CCPA; state privacy | Legal process (warrant, subpoena) |
| Transaction history | GDPR (if EU); BSA (US) | Legal process |
| IP address | GDPR; state privacy | Legal process |
| Device data | 4th Amendment (US); GDPR | Warrant |
| On-chain data (public) | **No privacy protection** (public) | No legal barrier |
| Social media (public) | **No privacy protection** (public) | No legal barrier |

**Key distinction**: On-chain data is **public** (no warrant needed). Off-chain data (KYC, IP, device) requires **legal process**. This distinction is critical for investigators.   