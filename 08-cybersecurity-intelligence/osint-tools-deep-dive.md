# OSINT Tools: Deep Dive

## Maltego

| Dimension | Detail |
|---|---|
| Developer | Maltego (acquired by Exabeam, 2021) |
| Price | Free CE / $999+ (Professional) / $5,000+ (Enterprise) |
| Primary Use | **Link analysis, relationship mapping, entity pivoting** |
| Data Sources | 80+ transforms (plugins): DNS, WHOIS, social media, dark web, blockchain, email, IP, phone, company registries |
| Key Features | Graph-based visualization; transform chains (automated pivoting); entity clustering; export to other tools |
| Dark Web | Integrations with ShadowDragon, Recorded Future, custom dark web transforms |
| Blockchain | Transforms for Etherscan, Bitcoin blockchain, Chainalysis (via API) |
| Best For | Complex investigations requiring multi-source correlation; visualizing relationships |
| Limitations | Expensive; learning curve; transform quality varies; not real-time (batch) |
| Workflow | Seed with indicator (address, domain, email) → run transforms → analyze graph → identify clusters → export evidence |

### Maltego Transforms for Crypto Forensics

| Transform | Input | Output |
|---|---|---|
| Etherscan | Address | Transactions, token transfers, contract calls |
| Bitcoin Block Explorer | Address | Transactions, UTXOs |
| WHOIS | Domain | Registrant, creation date, nameservers |
| DNS | Domain | A, AAAA, MX, TXT, CAA records |
| Shodan | IP/Domain | Open ports, services, banners |
| Censys | Domain | Certificates, services, tech stack |
| Social Media | Username/Email | Profiles across 400+ platforms |
| Dark Web (ShadowDragon) | Keyword/Email | Dark web mentions, leak data |
| Recorded Future | IP/Domain/Hash | Threat intel, actor attribution |
| Custom (Python) | Any | Any (build your own) |

## SpiderFoot

| Dimension | Detail |
|---|---|
| Developer | SpiderFoot (open-source core + HX commercial) |
| Price | Free (OSS) / $500+ (HX) / $2,000+ (Enterprise) |
| Primary Use | **Automated OSINT collection, reconnaissance at scale** |
| Data Sources | **200+ modules**: DNS, WHOIS, social platforms, dark web leaks, APIs (VirusTotal, Censys, Shodan), breach databases, search engines |
| Key Features | Modular (enable/disable sources); automated collection; correlation; API for integration; real-time |
| Dark Web | Dark web plugin; leaked credential monitoring; forum scraping |
| Blockchain | Limited (via API integrations); better for infrastructure recon than on-chain |
| Best For | High-volume automated collection; infrastructure mapping; breach monitoring; initial recon |
| Limitations | Less visual than Maltego; correlation is basic; blockchain analysis not primary focus |
| Workflow | Seed with target (domain, IP, email, username) → enable modules → automated collection → correlate → export |

### SpiderFoot Modules for Crypto Forensics

| Module Category | Examples |
|---|---|
| DNS/Infrastructure | DNS, DNSBrute, DNSBruteTXT, DNSCerts, DNSBlacklist |
| WHOIS | WhoisShodan, WhoisRaw, Riddler |
| Social Media | Facebook, Twitter, Instagram, LinkedIn, GitHub, Reddit |
| Dark Web | DarkWebMonitors, TorOnion, DarkSearch |
| Breach Data | Dehashed, HaveIBeenPwned, LeakIX |
| Search Engines | Google, Bing, DuckDuckGo, Yandex |
| APIs | Shodan, Censys, VirusTotal, AbuseIPDB |
| Blockchain (limited) | Via custom modules or API integration |

## BreadcrumbApp

| Dimension | Detail |
|---|---|
| Developer | Breadcrumb (commercial) |
| Price | $500+/mo (subscription) |
| Primary Use | **Email intelligence, breach monitoring, credential exposure** |
| Data Sources | 14B+ breach records; email → identity resolution; social media; dark web; corporate data |
| Key Features | Email-centric investigation; identity resolution from single email; breach history; social graph; dark web monitoring |
| Dark Web | Real-time dark web monitoring for credential exposure; leak site tracking |
| Best For | Identity resolution from a single email address; breach monitoring; corporate OSINT |
| Limitations | Email-centric (not address-centric); less blockchain focus; less graph visualization than Maltego |
| Workflow | Seed with email → identity resolution → social graph → breach history → dark web exposure → export |

## Comparison

| Feature | Maltego | SpiderFoot | BreadcrumbApp |
|---|---|---|---|
| Primary Strength | Link analysis / pivoting | Automated collection at scale | Email intelligence / breach |
| Dark Web | Via transforms | Native plugin | Real-time monitoring |
| Blockchain | Via transforms | Limited (API) | Limited |
| Social Media | 400+ platforms | 200+ modules | Focused (email → social) |
| Visualization | **Best** (graph) | Moderate (list + basic graph) | Moderate |
| Automation | Transform chains | **Best** (modular) | Moderate |
| API | Yes | **Best** (REST) | Yes |
| Price | $999+ | Free / $500+ | $500+ |
| Best For | Complex multi-source investigations | High-volume automated recon | Identity resolution from email |

## Recommended Stack for Crypto Forensics
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 1: SEED & COLLECT │
│ SpiderFoot (automated) + BreadcrumbApp (email identity) │
├─────────────────────────────────────────────────────────────────┤
│ LAYER 2: PIVOT & CORRELATE │
│ Maltego (link analysis) + Shodan/Censys (infrastructure) │
├─────────────────────────────────────────────────────────────────┤
│ LAYER 3: BLOCKCHAIN │
│ Chainalysis/TRM/Elliptic (on-chain) + Etherscan/Dune (public) │
├─────────────────────────────────────────────────────────────────┤
│ LAYER 4: DARK WEB & SOCIAL │
│ DarkSearch + Flashpoint (dark web) + Telegram/X/Discord (API) │
├─────────────────────────────────────────────────────────────────┤
│ LAYER 5: ANALYZE & ATTRIBUTE │
│ NER models + GNN clustering + cross-platform correlation │
├─────────────────────────────────────────────────────────────────┤
│ LAYER 6: REPORT & EXPORT │
│ Evidence package + chain of custody + regulatory filing │
└─────────────────────────────────────────────────────────────────┘