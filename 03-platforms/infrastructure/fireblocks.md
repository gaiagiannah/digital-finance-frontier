# Fireblocks

## Company Profile

| Dimension | Detail |
|---|---|
| Founded | 2018 (New York) |
| CEO | Itai Tiran |
| Funding | $150M+ (Series D, 2023); valued at $2.5B+ |
| Customers | 1,000+ institutions (banks, exchanges, asset managers, custodians) |
| Assets Under Custody | $500B+ (est. 2026) |

## Products

| Product | Function | 2026 Status |
|---|---|---|
| **Institutional Custody** | MPC-based multi-sig custody; no single point of key failure | Production; 1,000+ institutions |
| **Stablecoin Compliance** | GENIUS Act compliance tooling; reserve monitoring | Production |
| **Payment Orchestration** | Multi-chain payment execution; smart approvals | Production |
| **Risk & Compliance** | Real-time transaction monitoring; policy engine | Production |
| **PQC Migration** | Evaluating PQC for custody keys | Research (2026) |

## MPC Architecture
┌─────────────────────────────────────────────────────────┐
│ INSTITUTIONAL CUSTODY (MPC) │
├─────────────────────────────────────────────────────────┤
│ Key Share 1: Institution (HSM) │
│ Key Share 2: Fireblocks (HSM) │
│ Key Share 3: Third party (institution's choice) │
│ Key Share 4: Quorum (2-of-4 or 3-of-4 policy) │
├─────────────────────────────────────────────────────────┤
│ No single party holds the full key │
│ No single point of failure │
│ Policy engine: multi-approval workflows │
│ Audit trail: Every action logged + signed │
└─────────────────────────────────────────────────────────┘

## GENIUS Act Compliance (continued)

| Requirement | Fireblocks Solution |
|---|---|
| 1:1 reserve backing | Real-time reserve monitoring via Proof of Reserve |
| Custody requirements | MPC custody; SOC 1/2 certified |
| AML/CFT | Integrated Chainalysis/TRM screening |
| Reporting | Automated regulatory reports |
| Redemption at par | Instant redemption workflow; smart contract execution |
| Transparency | On-chain reserve proofs; auditor access |

## Key Partnerships (2026)

| Partner | Integration |
|---|---|
| Circle | USDC custody + compliance for GENIUS Act |
| Coinbase | Institutional custody for Base L2 |
| JPMorgan | Kinexys custody integration |
| Citi | Tokenized deposit custody |
| BlackRock | BUIDL custody |
| Ondo Finance | OUSG custody + compliance |
| Mastercard | Crypto Partner Program member |
| DTCC | Tokenized securities custody (Oct 2026 launch) |

## PQC Migration

| Phase | Action | Timeline |
|---|---|---|
| 1 | Inventory all ECDSA keys in custody | 2026 |
| 2 | Deploy hybrid (ECDSA + ML-DSA) key pairs | 2027 |
| 3 | Migrate to ML-DSA-only for new accounts | 2028 |
| 4 | Full migration; deprecate ECDSA | 2030 |

**Key challenge**: 500B+ in assets under custody. Key migration must be zero-downtime. MPC + PQC intersection is unsolved (can ML-DSA be split into MPC shares?). Fireblocks is actively researching.

## Key Differentiator

The **trust layer** for institutional crypto. No other provider combines:
- MPC custody (no single point of failure)
- GENIUS Act compliance (turnkey)
- Multi-chain (25+ chains)
- Policy engine (multi-approval workflows)
- Real-time risk monitoring
- SOC 1/2 + ISO 27001 certified   