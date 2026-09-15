# Threat Actor Attribution (Expanded)

## Attribution Framework

### Five Intelligence Disciplines (INTEL)

| Discipline | Data Source | Crypto Application |
|---|---|---|
| **SIGINT** | Signals intelligence | Network traffic; API calls; blockchain mempool |
| **OSINT** | Open source | Social media, forums, dark web, public data |
| **HUMINT** | Human intelligence | Informants, arrests, undercover |
| **FININT** | Financial intelligence | Transaction patterns, exchange KYC, bank records |
| **IMINT** | Image intelligence | Screenshots, video, dark web imagery |

### Confidence Scoring

| Level | Score | Meaning | Action |
|---|---|---|---|
| Almost Certain | 9-10 | Multiple independent sources confirm | Full response; prosecution |
| High | 7-8 | Two+ sources; strong TTP match | Active response; legal process |
| Moderate | 5-6 | Single source; partial TTP match | Enhanced monitoring |
| Low | 3-4 | Weak correlation; single indicator | Monitor only |
| Negligible | 1-2 | Coincidence; no corroboration | No action |

### TTP Mapping (MITRE ATT&CK Crypto)

| Tactic | Technique | Example |
|---|---|---|
| Initial Access | T1566: Phishing | Fake airdrop email |
| Initial Access | T1195: Supply Chain | Compromised DeFi protocol |
| Execution | T1059: Command Script | Malicious smart contract |
| Persistence | T1543: Create Account | New wallet for fund movement |
| Defense Evasion | T1564: Mix/Tumble | Tornado Cash, CoinJoin |
| Defense Evasion | T1070: Cross-Chain | Bridge to different chain |
| Collection | T1560: Archive | Screenshot of wallet balance |
| C2 | T1105: Transfer | Wallet-to-wallet (staging) |
| Exfiltration | T1567: Exchange Withdrawal | CEX cash-out |
| Impact | T1529: Fund Movement | Move to cold storage |
| Impact | T1486: Ransomware | Encrypt + demand BTC |

## Known Crypto Threat Actors (Detailed)

### Lazarus Group (North Korea)

| Dimension | Detail |
|---|---|
| Aliases | Hidden Cobra, Zinc, Blue noroff, APT38, APT38, Labyrinth Chollima |
| First Active | 2009 |
| Primary Targets | Exchanges, DeFi protocols, blockchain infrastructure |
| TTPs | Social engineering (insider), bridge exploits, API key theft, fake tokens |
| Known Incidents | Mt. Gox (2014, $460M), Binance (2022, $600M), Ronin (2022, $625M), Harmony (2022, $100M) |
| Total Stolen | **$3B+** (largest crypto thief in history) |
| Funding | North Korean government (cyber warfare division) |
| Attribution Confidence | 9/10 (multiple incidents, consistent TTPs, North Korean nationals arrested) |
| On-chain Signature | Specific wallet patterns; time-zone activity (KST); exchange preferences |
| Dark Web | No known dark web presence (state actor) |

### APT41 (China)

| Dimension | Detail |
|---|---|
| Aliases | Voodoo Bear, Double Dragon, Honeybee, Comment Crew |
| First Active | 2012 |
| Primary Targets | Exchanges, blockchain infrastructure, supply chain |
| TTPs | Supply chain compromise, insider access, watering hole, spear phishing |
| Known Incidents | Multiple exchange intrusions (unattributed publicly) |
| Funding | PLA Unit 61398 (Chinese military cyber) |
| Attribution Confidence | 7/10 (TTP match; fewer public incidents) |
| On-chain Signature | Different from Lazarus; more patient; longer dwell time |

### Charming Kitten / APT35 (Iran)

| Dimension | Detail |
|---|---|
| Aliases | Elfin, Ramsay, Phosphorus |
| First Active | 2009 |
| Primary Targets | Exchanges, DeFi, financial institutions |
| TTPs | Phishing, insider, ransomware, social engineering |
| Known Incidents | Multiple (often attributed jointly with other groups) |
| Funding | IRGC (Islamic Revolutionary Guard Corps) |
| Attribution Confidence | 6/10 (TTP match; less public data) |

### LockBit (Ransomware)

| Dimension | Detail |
|---|---|
| Type | Ransomware-as-a-Service (RaaS) |
| First Active | 2019 |
| Primary Targets | Enterprises, healthcare, financial services |
| TTPs | Initial access brokers, phishing, RDP exploitation, double extortion |
| Ransom Currency | BTC, ETH, USDT (Monero abandoned 2022) |
| Total Ransom | $4B+ demanded; ~$1B paid |
| Takedown | 2024: FBI + international law enforcement (DDoS on infrastructure) |
| Attribution | Russian-speaking; affiliates in 50+ countries |
| On-chain Signature | Mixers (Tornado Cash); exchange cash-out within 24-48 hrs |

### BlackCat / ALPHV (Ransomware)

| Dimension | Detail |
|---|---|
| Type | RaaS |
| First Active | 2021 |
| Primary Targets | Enterprises, critical infrastructure |
| TTPs | Similar to LockBit; RaaS model |
| Ransom Currency | BTC, ETH, USDT |
| Attribution | Russian-speaking; overlap with LockBit affiliates |

## Attribution Methodology (Step-by-Step)
STEP 1: INDICATOR COLLECTION

On-chain: Wallet addresses, transaction patterns, timing
Off-chain: IP, domain, social media, dark web
Financial: Exchange deposits/withdrawals, OTC desks
Network: API calls, RPC endpoints, infrastructure
STEP 2: PATTERN ANALYSIS

Time-zone analysis (activity peaks → geographic location)
Exchange preferences (which CEXs used → jurisdiction)
Transaction patterns (round numbers, velocity, structure)
Token preferences (BTC vs. ETH vs. USDT)
Mixer usage (Tornado Cash, CoinJoin, Wasabi)
Cross-chain behavior (which bridges, which chains)
STEP 3: TTP MAPPING

Map observed behavior to MITRE ATT&CK
Compare against known actor TTPs
Score similarity (0-10) per actor
STEP 4: CORROBORATION

Cross-reference with public reports (Chainalysis, FBI, Europol)
Check against OFAC sanctions list
Compare with law enforcement press releases
Check dark web forums (actor claims)
Social media (brag posts, recruitment)
STEP 5: CONFIDENCE SCORING

Weight each evidence type
Calculate overall confidence (1-10)
Identify gaps (what would increase confidence?)
Document assumptions
STEP 6: REPORTING

Attribution report (classified per sensitivity)
Confidence level + caveats
Recommended actions
Legal process needed (if any)

## On-Chain "Fingerprinting"

| Feature | What It Reveals | Reliability |
|---|---|---|
| Time-zone of activity | Geographic location | Medium (VPN, bots) |
| Exchange used | Jurisdiction preference | Medium |
| Transaction size patterns | Individual vs. institutional | High |
| Round-number usage | Individual (less sophisticated) | Medium |
| Mixer usage | Intent to anonymize | High |
| Cross-chain behavior | Technical sophistication | Medium |
| Gas price sensitivity | Cost consciousness (individual) | Low |
| Token diversification | Portfolio strategy | Low |
| Address reuse | Individual (sloppy) vs. institutional | High |
| Wallet age | New (disposable) vs. old (established) | Medium |   