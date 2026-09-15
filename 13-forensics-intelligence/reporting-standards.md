# Reporting Standards

## Regulatory Reporting

### US

| Report | Filing With | Trigger | Deadline | Penalty (Late) |
|---|---|---|---|---|
| **SAR** (Suspicious Activity Report) | FinCEN | Suspicious activity >$5,000 | 30 days (60 max) | Civil/criminal |
| **CTR** (Currency Transaction Report) | FinCEN | Transaction >$10,000 | 15 days | Civil |
| **1099-DA** (Digital Asset) | IRS / Payer | >$600 in sales | Feb/Mar (tax year) | Civil |
| **Form 8962** | IRS | Crypto gains/losses | With tax return | Civil |
| **SEC 8-K** | SEC | Material event (listed company) | 4 business days | Civil/criminal |
| **SEC 10-K/10-Q** | SEC | Quarterly/annual | 40/90 days | Civil |
| **OFAC Report** | OFAC | Sanctions-related transaction | 10 days | Civil/criminal |
| **DORA Incident** | (EU only) | Operational incident | 72 hours | Civil |

### EU

| Report | Filing With | Trigger | Deadline |
|---|---|---|---|
| **SAR** | FIU (national) | Suspicious activity | Without undue delay |
| **CTR** | FIU | >€15,000 | 3 business days |
| **MiCA Report** | National regulator | VASP obligations | Per MiCA schedule |
| **DORA Incident** | National regulator | Operational incident | 72 hours |
| **AMLD6 Report** | FIU | AML/CFT | Without undue delay |

### UK

| Report | Filing With | Trigger | Deadline |
|---|---|---|---|
| **SAR** | NCA (National Crime Agency) | Suspicious activity | Without undue delay |
| **CTR** | HMRC | >£10,000 | 15 days |
| **FCA Report** | FCA | Financial crime | Per FCA rules |

## SAR Filing (Crypto-Specific)

### When to File

| Scenario | File SAR? | Notes |
|---|---|---|
| Customer deposits $50K, immediately withdraws to new wallet | **Yes** | Structuring; possible laundering |
| Customer sends $10K to OFAC-listed address | **Yes** (24 hrs) | Sanctions evasion |
| Customer trades $1M in 1 hour (normal: $10K/day) | **Yes** | Velocity anomaly |
| Customer uses Tornado Cash | **Yes** | Anonymization intent |
| Customer deposits from 50 different addresses in 1 day | **Yes** | Layering |
| Customer sends round numbers ($10K, $50K) repeatedly | **Yes** | Structuring |
| Customer's IP changes to sanctioned country | **Yes** | Sanctions evasion |
| Customer's device changes frequently | **Yes** | Possible compromise |
| Normal trading activity | No | No trigger |

### SAR Content (Crypto)

| Field | Example |
|---|---|
| SAR Type | 111 (Money Laundering), 120 (Fraud), 130 (Sanctions) |
| Suspected Activity | "Customer moved $2.3M through 12 wallets in 4 hours, consistent with layering" |
| Narrative | Full description with timestamps, addresses, amounts |
| On-chain Evidence | Transaction hashes, addresses, block numbers |
| Off-chain Evidence | IP, device, KYC data (if available) |
| Amount Involved | $2,300,000 |
| Customer Info | Name, DOB, address, account number |
| Recommended Action | "Freeze account; preserve evidence; refer to FBI" |

### Tipping Off

- **DO NOT** tell the customer you filed a SAR
- **DO NOT** discuss the investigation with the customer
- **DO NOT** share SAR details with anyone outside the institution (except legal process)
- Penalty: Criminal (up to 5 years) + civil

## Incident Reporting (Internal)

| Audience | Content | Format | Deadline |
|---|---|---|---|
| CISO / Security Team | Full technical detail | Incident report | Immediate |
| Legal / Compliance | Material facts, legal exposure | Legal memo | <4 hours |
| CIO / CTO | System impact, remediation | Technical report | <24 hours |
| CEO / Board | Business impact, financial loss | Executive summary | <48 hours |
| Regulator | Per regulatory requirements | Regulatory filing | Per deadline |
| Law Enforcement | Evidence, chain of custody | LE report | Per legal process |
| Customers | What happened, what was lost, what's being done | Customer notification | Per GDPR (72 hrs) / state law |
| Insurers | Full detail for claim | Insurance claim | Per policy |
| Industry (ISAC) | TTPs, IOCs, lessons learned | Intelligence sharing | <72 hours |

## Evidence Standards

### Admissibility Requirements

| Standard | Requirement | How to Meet |
|---|---|---|
| **Authentication** | Prove data is what it claims to be | Hash (SHA-256); metadata; source documentation |
| **Best Evidence Rule** | Original preferred | Preserve original; copies admissible if original unavailable |
| **Daubert** (federal) | Scientific methodology reliable | Peer-reviewed method; known error rate; standards |
| **Frye** (some states) | Generally accepted in scientific community | Established technique (GNN, clustering) |
| **Chain of Custody** | Documented every transfer/access | Log every access; hash at each transfer |
| **Hearsay Exceptions** | Business records (1102); public records (803(8)) | Regular business practice; public data |
| **Expert Testimony** | Qualified expert (702) | Experience + methodology + peer review |

### Chain of Custody Log

| Field | Example |
|---|---|
| Item ID | EVID-2026-0042 |
| Description | "Ethereum wallet 0x1234... transaction history (JSON export)" |
| Source | "Etherscan API; collected 2026-09-14 14:32:00 UTC" |
| Collector | "Analyst: J. Smith; Badge: 4521" |
| Hash (SHA-256) | "a3f2b8c9..." |
| Storage | "WORM: /evidence/2026/0042/" |
| Access Log | "2026-09-14 14:32:00 — J. Smith (collect); 2026-09-15 09:00:00 — A. Jones (review)" |
| Transfer | "2026-09-15 10:00:00 — J. Smith → A. Jones (handoff, witnessed by B. Lee)" |
| Disposition | "Active investigation" |

### Expert Witness (Crypto Forensics)

| Qualification | Why It Matters |
|---|---|
| 5+ years crypto forensics experience | Daubert: experience |
| Published research / peer review | Daubert: peer review |
| Known error rate of methodology | Daubert: error rate |
| Standards in the field | Daubert: standards |
| Testified before (track record) | Credibility |
| Training records | Qualification |
| Tools used (Chainalysis, TRM, etc.) | Methodology |
| Chain of custody documentation | Admissibility |

**Key point**: The methodology must be **reproducible**. Another expert with the same data and tools should get the same result. This is why glass-box tools (TRM Labs) are preferred over black-box (for court).      