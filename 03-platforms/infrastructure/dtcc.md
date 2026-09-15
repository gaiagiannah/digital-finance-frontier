# DTCC (Depository Trust & Clearing Corporation)

## 2026 Contributions

| Item | Detail |
|---|---|
| Production Testing | July 2026: Tokenized Russell 1000 equities, ETFs, US Treasuries |
| Service Launch | **October 2026** |
| Participants | 50+ firms |
| BlackRock | BUIDL pilot participant |
| Goldman Sachs | Tokenized fund pilot |

## Company Profile

| Dimension | Detail |
|---|---|
| Founded | 1978 (New York) |
| Type | Private, member-owned (not publicly traded) |
| Members | 1,200+ (broker-dealers, banks, asset managers, custodians) |
| Assets Under Custody | **$75T+** (US securities) |
| Role | Systemically important financial infrastructure (SIFI-adjacent) |
| Regulation | SEC oversight; critical infrastructure |

## Why DTCC Matters

DTCC is the **central counterparty and custodian** for US securities. Every stock trade, bond settlement, and ETF transaction in the US flows through DTCC. Its tokenization pilot is the single most important event for institutional tokenization in 2026.

## Tokenized Securities Pilot

### Timeline

| Date | Milestone |
|---|---|
| 2024 | Pilot concept developed |
| 2025 | Participant selection; technical architecture |
| **July 2026** | **Production testing**: Tokenized Russell 1000 equities, ETFs, US Treasuries |
| **October 2026** | **Service launch** (production) |

### What's Being Tokenized

| Asset | Detail |
|---|---|
| Russell 1000 equities | 1,000 largest US stocks |
| ETFs | Major index ETFs (SPY, QQQ, VOO) |
| US Treasuries | On-chain T-bills, T-notes |

### Participants (50+ firms)

| Category | Firms |
|---|---|
| Asset Managers | BlackRock (BUIDL), Goldman Sachs, Fidelity |
| Banks | JPMorgan, Citi, BNY, BofA |
| Brokers | Schwab, Morgan Stanley, Merrill |
| Infrastructure | Chainlink (CCIP), Fireblocks (custody), Canton (settlement) |
| Exchanges | NYSE (blockchain platform), Nasdaq (Kraken xStocks) |
| Custodians | BNY, State Street, JPMorgan |

### Architecture
┌─────────────────────────────────────────────────────────────────┐
│ DTCC TOKENIZED SECURITIES ARCHITECTURE │
├─────────────────────────────────────────────────────────────────┤
│ ISSUANCE │
│ - DTCC issues tokenized representation of DTC-held securities │
│ - 1:1 backing (each token = one share/bond) │
│ - Smart contract enforces: transfer, vote, dividend │
├─────────────────────────────────────────────────────────────────┤
│ SETTLEMENT │
│ - T+0 settlement in stablecoins (USDC) │
│ - 24/7 availability (vs. current T+1, market hours only) │
│ - Atomic: trade + payment settle simultaneously │
│ - Chains: Ethereum, Base, Canton (via CCIP) │
├─────────────────────────────────────────────────────────────────┤
│ CUSTODY │
│ - Fireblocks / BNY / JPMorgan (institutional MPC custody) │
│ - Token = proof of ownership (on-chain) │
│ - DTC remains legal record (token is derivative) │
├─────────────────────────────────────────────────────────────────┤
│ CORPORATE ACTIONS │
│ - Dividends: Auto-distributed on-chain │
│ - Votes: On-chain proxy voting (Kraken xStocks integration) │
│ - Splits: Token rebase (smart contract) │
│ - Mergers/Acquisitions: Token swap (smart contract) │
├─────────────────────────────────────────────────────────────────┤
│ REGULATORY │
│ - SEC oversight (tokenized securities = securities) │
│ - MiFID II equivalent (in EU) │
│ - BSA/AML: KYC at issuance + transfer │
│ - Travel Rule: Sender/receiver info on transfer │
└─────────────────────────────────────────────────────────────────┘

### Integration Points

| System | Integration |
|---|---|
| NYSE Blockchain Platform | 24/7 trading; T+0 stablecoin-funded settlement (May 2026 approval) |
| Kraken xStocks | Nasdaq integration; corporate actions; proxy voting |
| Chainlink CCIP | Cross-chain settlement (Ethereum ↔ Base ↔ Canton) |
| Fireblocks | Institutional custody |
| Visa / Mastercard | Stablecoin settlement for tokenized securities |
| Fidelity | NYSE participant; tokenized fund products |
| BlackRock | BUIDL on Base; DTCC pilot |

### What Changes on October 2026 Launch

| Before | After |
|---|---|
| T+1 settlement (next business day) | **T+0** (immediate, 24/7) |
| Market hours only (9:30-4:00 ET) | **24/7/365** |
| DTC book-entry (opaque) | **On-chain** (transparent, auditable) |
| SWIFT for cross-border | **CCIP + stablecoins** (faster, cheaper) |
| Corporate actions: 5-10 days | **Instant** (smart contract) |
| Voting: Mail/email proxy | **On-chain** (immediate, verifiable) |
| Dividends: 3-5 days | **Instant** (auto-distributed) |

### Systemic Implications

- **DTCC becomes the tokenization authority** for US securities
- **Stablecoins become the settlement currency** for equities
- **24/7 trading** becomes standard (not just crypto)
- **Cross-border** tokenized equity trading becomes feasible
- **The "tokenized vs. traditional" debate is over** — they're the same asset, different representation

## Key Risks

| Risk | Mitigation |
|---|---|
| Smart contract bug in issuance | Formal verification; Daml; multiple audits |
| Chain outage (Ethereum/Base) | Multi-chain (Canton backup); DTTC remains legal record |
| Regulatory (SEC) | DTCC is under SEC oversight; tokenized = securities |
| Adoption (do brokers migrate?) | Schwab, Morgan Stanley, Merrill are participants |
| Key management | MPC (Fireblocks); HSM; institutional custody |   