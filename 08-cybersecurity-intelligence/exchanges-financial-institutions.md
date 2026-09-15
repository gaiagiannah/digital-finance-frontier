# Crypto Exchanges & Financial Institutions: Internal Forensics

## How Exchanges Handle Forensics

### Coinbase

| Dimension | Detail |
|---|---|
| Internal Team | Trust & Safety; Crypto Crimes Unit |
| Data Sources | Full KYC data (all users), transaction logs, IP/device metadata, on-chain data, internal risk models |
| Investigations Performed | Fraud, AML, sanctions, insider threats, API abuse, wash trading |
| What They Do with Data | Account freezes, SAR filings, law enforcement cooperation (subpoenas/warrants), takedown requests, internal discipline |
| Legal Process Response | CLOUD Act compliant; responds to subpoenas, warrants, court orders; 2,000+ legal requests annually (est.) |
| Key Capability | **Full KYC = full de-anonymization** for all users on the platform |

### Kraken (Payward)

| Dimension | Detail |
|---|---|
| Internal Team | Trust, Risk & Compliance; Investigations |
| Data Sources | KYC data, transaction logs, on-chain data, risk models |
| Investigations Performed | AML, sanctions, fraud, market manipulation |
| What They Do with Data | SAR filings, account freezes, law enforcement cooperation, regulatory reporting |
| Key Capability | EU + US dual compliance; Travel Rule enforcement |

### Binance

| Dimension | Detail |
|---|---|
| Internal Team | Trust & Safety; Regional compliance teams |
| Data Sources | KYC data (where required), transaction logs, on-chain data, risk models |
| Investigations Performed | AML, sanctions, fraud, market manipulation, insider threats |
| What They Do with Data | Account freezes, SAR filings (where required), law enforcement cooperation |
| Key Risk | 2022 hack ($600M, Lazarus); address reuse pattern flagged in Google quantum whitepaper |
| Limitations | Jurisdictional complexity (multiple entities); KYC not universal |

### Banks (JPMorgan, Citi, etc.)

| Dimension | Detail |
|---|---|
| Internal Team | Financial Crime; BSA/AML; Cyber; Investigations |
| Data Sources | SWIFT messages, wire transfers, KYC/CIP, on-chain data (for tokenized deposits), internal risk models |
| Investigations Performed | Money laundering, sanctions evasion, fraud, insider threats, cyber intrusions |
| What They Do with Data | SAR/CTR filings, account freezes, law enforcement referrals, internal discipline, regulatory reporting |
| Key Capability | **BSA/AML infrastructure** — the most mature compliance systems in finance |
| Crypto-Specific | Tokenized deposit monitoring (Canton, TCH); stablecoin reserve monitoring; GENIUS Act compliance |

## How Financial Institutions Get Data

| Source | Method | Authority |
|---|---|---|
| Own platform data | Internal (full access) | Terms of Service; BSA |
| On-chain (public) | Public API / RPC | No legal barrier |
| Other exchanges | Legal process (subpoena, warrant) | BSA; 18 U.S.C. § 2703 |
| Blockchain analytics vendors | Commercial subscription | Contract |
| FinCEN | SAR/CTR analysis | BSA |
| OFAC | Sanctions screening | IEEPA; OFAC regulations |
| International | MLAT / CLOUD Act | 28 U.S.C. § 1782 |

## What Financial Institutions Do with Data

1. **Regulatory compliance**: SAR/CTR filings, Travel Rule, AML/CFT
2. **Risk management**: Counterparty risk, credit risk, operational risk
3. **Fraud prevention**: Real-time transaction monitoring, anomaly detection
4. **Law enforcement cooperation**: Responding to legal process, voluntary disclosure
5. **Internal investigations**: Insider threats, compliance violations
6. **Litigation support**: Expert testimony, document production
7. **Regulatory reporting**: MiCA, GENIUS Act, FATF, local regulations   