# Dark Web Monitoring

## What to Monitor

### Categories

| Category | Indicators | Priority |
|---|---|---|
| **Ransom notes** | New demands, deadline extensions, victim names | Critical |
| **Stolen data** | "For sale" listings, data types, volumes | Critical |
| **Money laundering** | Mixer services, "cleaning" services, rates | High |
| **Fraud marketplaces** | Phishing kits, fake investments, scam tools | High |
| **Threat actor forums** | TTP sharing, recruitment, brag posts | High |
| **Stolen credentials** | Exchange API keys, wallet seeds, admin panels | Critical |
| **Exploit sales** | Zero-days for blockchain infrastructure | High |
| **Takedown announcements** | Marketplace closures, law enforcement ops | Medium |
| **Sanctions evasion** | OFAC-listed entity services, "sanctions-free" | Critical |
| **Insider threats** | "I work at [exchange]", job postings for "operators" | High |

### Specific Indicators (IOC)

| Type | Example | Source |
|---|---|---|
| Ransom note | "We have 500GB of your data. Pay 100 BTC in 72 hours" | Leak site |
| Data listing | "Binance user database — 200M records — $50K" | Dark market |
| Service ad | "Bitcoin mixing service — 5% fee — no questions" | Forum |
| Credential dump | "Coinbase admin panel: admin@coinbase.com / ***" | Leak site |
| Recruitment | "Experienced DeFi developer needed. Pay: 5 ETH/month." | Forum |
| Brag post | "Just drained $2M from [protocol]. WAGMI." | Forum/social |
| TTP share | "How to bypass [exchange] 2FA — step by step" | Forum |
| Sanctions | "We can move your BTC without OFAC. Contact us." | Dark market |

## Tools (Detailed)

| Tool | Type | Cost | Dark Web Capability |
|---|---|---|---|
| **Tor Browser** | Access | Free | Basic browsing |
| **I2P** | Access | Free | Alternative network |
| **DarkSearch** | Search | Free / $50/mo | Tor-indexed search; API |
| **Flashpoint** | Commercial intel | $50K+/yr | Full dark web monitoring; NLP; alerts |
| **ZeroFOX** | Monitoring | $30K+/yr | Real-time alerts; breach monitoring |
| **Recorded Future** | Threat intel | $100K+/yr | Dark web + OSINT + SIGINT |
| **Inca Digital** | Multi-source | Custom | Dark web + social + blockchain + HUMINT |
| **Maltego (ShadowDragon)** | Link analysis | $999+/yr | Dark web transforms |
| **Custom NLP pipeline** | Automated | Dev cost | Real-time classification; entity extraction |

## Pipeline Architecture
┌─────────────────────────────────────────────────────────────────┐
│ DARK WEB MONITORING PIPELINE │
├─────────────────────────────────────────────────────────────────┤
│ 1. ACCESS │
│ Tor daemon (rotating identity every 10 min) │
│ I2P (secondary network) │
│ Rate limiting: 1 req/sec per source │
│ Error handling: Sites go down frequently │
├─────────────────────────────────────────────────────────────────┤
│ 2. CRAWL │
│ Scheduled: Every 15-60 min (per source) │
│ Depth: 2-3 levels (don't go too deep) │
│ Filter: Skip known illegal content pages │
│ Store: Raw HTML + metadata (WORM) │
├─────────────────────────────────────────────────────────────────┤
│ 3. EXTRACT │
│ BeautifulSoup / lxml → text │
│ NER model → entities (addresses, domains, names, amounts) │
│ Classification → category (ransom, data, service, forum) │
│ Language detection → EN, RU, ZH, KO, AR │
├─────────────────────────────────────────────────────────────────┤
│ 4. CORRELATE │
│ Match against known indicators (IOCs) │
│ Cross-reference with on-chain data │
│ Match against known threat actors │
│ Temporal correlation with active incidents │
├─────────────────────────────────────────────────────────────────┤
│ 5. ALERT │
│ Critical: Ransom note with known victim → immediate │
│ High: New data listing with client data → 1 hour │
│ Medium: New service/actor → daily digest │
│ Low: Forum chatter → weekly report │
│ Channels: Slack, email, API, dashboard │
├─────────────────────────────────────────────────────────────────┤
│ 6. ARCHIVE │
│ WORM storage (legal evidence) │
│ Hash: SHA-256 of every page │
│ Timestamp: NTP-synced │
│ Retention: 7 years (BSA) / indefinite (evidence) │
└─────────────────────────────────────────────────────────────────┘

## Legal Boundaries (CRITICAL)

| Action | Legal? | Authority |
|---|---|---|
| Browse public .onion sites | **Yes** | First Amendment; public data |
| Read public forum posts | **Yes** | Public data |
| Read public marketplace listings | **Yes** | Public data |
| Screenshot + hash for evidence | **Yes** | Legal (documenting public info) |
| Purchase stolen data | **NO** | 18 U.S.C. § 1030; § 1343 |
| Order services (mixing, hacking) | **NO** | 18 U.S.C. § 1030; § 1343 |
| Message vendors/actors | **GRAY** | Consult counsel; may be entrapment |
| Create fake account to investigate | **GRAY** | Consult counsel; 18 U.S.C. § 912 |
| Download illegal content (child exploitation, etc.) | **NO** | 18 U.S.C. § 2252 |
| Access private/hidden pages (password-protected) | **NO** | CFAA |
| Use Tor (access) | **Yes** | First Amendment; *Tor Project v. Molotov* (9th Cir. 2025) |
| Use I2P (access) | **Yes** | First Amendment; public data |
| Run Tor node (relay) | **Yes** | First Amendment; *Tor Project v. Molotov* |
| Scrape at high volume (DoS risk) | **GRAY** | Be respectful; rate limit; consult counsel |
| Publish identified individuals (doxxing) | **NO** | Defamation; state privacy; GDPR |

## Monitoring Schedule

| Source Type | Frequency | Method |
|---|---|---|
| Ransom note sites (leak sites) | Every 15 min | Automated crawl + NLP |
| Dark marketplaces (public) | Every 30 min | Automated crawl |
| Threat actor forums | Every 15 min | Automated crawl + NLP |
| Social media (public crypto) | Real-time | API (Telegram, X, Discord) |
| Breach forums | Every 30 min | Automated crawl |
| Exploit sales | Every 1 hour | Automated crawl + NLP |
| Sanctions evasion services | Every 1 hour | Keyword monitoring |

## Alert Escalation

| Level | Trigger | Response Time | Action |
|---|---|---|---|
| **CRITICAL** | Ransom note naming client; stolen client data listed; active exploit sale | **Immediate** (<5 min) | Page IR team; legal; CISO; Board |
| **HIGH** | New actor targeting client's industry; credential dump with client domain; active money laundering service | **<1 hour** | Alert security team; investigate; document |
| **MEDIUM** | New marketplace; new service; forum chatter about client sector | **<4 hours** | Log; analyze; add to threat intel |
| **LOW** | General forum activity; new actor registration; market changes | **<24 hours** | Weekly digest; trend analysis |

## Evidence Collection (Dark Web)

| Step | Action | Purpose |
|---|---|---|
| 1 | Screenshot (full page, with URL visible) | Visual evidence |
| 2 | Save raw HTML | Preserves metadata, links, scripts |
| 3 | Hash (SHA-256) of HTML + screenshot | Integrity verification |
| 4 | Timestamp (NTP-synced) | Proves when observed |
| 5 | Record .onion URL + Tor circuit | Reproducibility |
| 6 | Store in WORM | Legal preservation |
| 7 | Log analyst + action | Chain of custody |

**Admissibility**: Dark web screenshots + hashes are admissible in US federal court as business records (FRE 803(6)) or public records (FRE 803(8)) when collected by law enforcement. For private investigators, admissibility depends on chain of custody documentation.

## Known Dark Web Infrastructure (2026)

| Category | Examples | Status |
|---|---|---|
| Marketplaces | (various; high turnover) | Takedowns frequent; new ones emerge |
| Ransom leak sites | (varies per group) | Active |
| Forums | (various; Russian, English) | Active |
| Mixers (dark web) | Tornado Cash (mainnet), Wasabi (BTC) | Active |
| Data breach forums | (various) | Active |
| Exploit marketplaces | (various) | Active; low volume |
| Sanctions evasion | (various; often Russian) | Active; OFAC enforcement |

**Note**: Specific .onion URLs are intentionally omitted from this document. They change frequently and publishing them creates legal/safety issues. Maintain a separate, access-controlled IOC database.   