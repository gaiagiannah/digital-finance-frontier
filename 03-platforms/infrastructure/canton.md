# Canton Network

## 2026 Contributions

| Item | Detail |
|---|---|
| Architecture | Privacy-preserving institutional DLT; split validation/ordering |
| Participants | JPMorgan, HSBC, Lloyds, Citi, UBS, BNY + 100s of institutions |
| Status | Live; top fee-generating institutional chain Q1 2026 |
| Visa Integration | One of 9 chains for stablecoin settlement |
| SWIFT Ledger | Built on Hyperledger Besu (separate from Canton) |

## Positioning

The de facto standard for **institutional tokenized deposits** in the G7 corridor. Privacy by default; permissioned; split validation enables regulatory compliance across jurisdictions.   

## Company Profile

| Dimension | Detail |
|---|---|
| Founded | 2021 (London) |
| Founders | Tom Enright (ex-Ripple), ex-DLT developers |
| Backers | Digital Asset Development Fund (UK), JPMorgan, HSBC, Lloyds, Citi, UBS, BNY |
| Architecture | Permissioned; split validation/ordering; privacy by default |
| Technology | Daml smart contract language; Cosmos SDK-based |

## Architecture
┌─────────────────────────────────────────────────────────────────┐
│ CANTON NETWORK ARCHITECTURE │
├─────────────────────────────────────────────────────────────────┤
│ SPLIT VALIDATION / ORDERING │
│ - Validators: Verify transactions (correctness) │
│ - Orderers: Sequence transactions (liveness) │
│ - Separation enables: │
│ • Different validators per jurisdiction │
│ • Privacy: Validators see only their jurisdiction's data │
│ • Regulatory compliance: Each jurisdiction's rules enforced │
│ │
│ PRIVACY BY DEFAULT │
│ - Data is encrypted at rest │
│ - Access controlled via "data access policies" │
│ - Counterparties see only what they need to see │
│ - Regulators can be granted access (compliance) │
│ - ZK proofs for selective disclosure │
│ │
│ DAML SMART CONTRACTS │
│ - Functional programming language (Haskell-based) │
│ - Formal verification possible │
│ - Template-based (type-safe) │
│ - Multi-party authorization built-in │
└─────────────────────────────────────────────────────────────────┘

## Participants (2026)

| Institution | Role |
|---|---|
| JPMorgan | Tokenized deposits; Kinexys integration |
| HSBC | Tokenized deposits; cross-border payments |
| Lloyds | Tokenized deposits |
| Citi | Tokenized deposits; SWIFT integration |
| UBS | Tokenized deposits |
| BNY | Custody; tokenized assets |
| BNP Paribas | Tokenized deposits (EU) |
| Standard Chartered | Tokenized deposits; APAC |
| + 100s more | Various (asset managers, corporates, regulators) |

## Key Use Cases (2026)

| Use Case | Status | Participants |
|---|---|---|
| Tokenized deposits | **Live** | 17+ banks |
| Cross-border payments | Live (pilot) | JPMorgan, HSBC, Citi |
| Tokenized assets (bonds, equities) | Pilot | BNY, UBS, Citi |
| Trade finance | Pilot | Standard Chartered, HSBC |
| Repo / Collateral | Live | JPMorgan (Onyx integration) |
| Agorá settlement | RVT complete | 8 central banks + 28 institutions |

## Visa Integration

- Canton is one of **9 chains** for Visa stablecoin settlement
- Visa VSP (launched Jul 2026) supports Canton as a settlement chain
- Institutional stablecoin transfers via Canton + CCIP

## Key Differentiator

The **privacy-preserving institutional standard**. Unlike public blockchains (Ethereum, Base) where all data is visible, Canton provides:
- **Privacy by default**: Counterparties see only what they need
- **Regulatory compliance**: Each jurisdiction's rules enforced at the protocol level
- **Split validation**: Different validators per jurisdiction (multi-sovereign)
- **Formal verification**: Daml enables provable correctness of smart contracts
- **Institutional trust**: Backed by the world's largest banks

## Limitations

- Permissioned (not open)
- Daml is less flexible than Solidity (fewer developers)
- Not suitable for retail / open DeFi
- G7-centric (not used in China/Gulf corridor)
- Smaller ecosystem than Ethereum/Base   