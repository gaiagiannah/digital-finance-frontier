# OSINT Data Scraping: Sources & Methodology

## Data Sources

### Dark Web / Deep Web

| Source | Data Type | Access Method | Legal Status |
|---|---|---|---|
| Tor (.onion) | Marketplaces, forums, leak sites | Tor Browser; crawlers | Legal to access; illegal to purchase |
| I2P | Anonymous services | I2P client | Legal to access |
| DarkSearch | Tor-indexed search | JSON API | Legal |
| Flashpoint | Commercial dark web intel | API | Legal (subscription) |
| ZeroFOX | Dark web monitoring | API | Legal (subscription) |
| Recorded Future | Threat intel (includes dark web) | API | Legal (subscription) |

**What to scrape:**
- Ransom notes (new + updated)
- Stolen data listings ("for sale")
- Money laundering service advertisements
- Fraud marketplace listings (phishing kits, fake investments)
- Threat actor forum communications
- Stolen credentials (exchange API keys, wallet seeds)
- Exploit sales (zero-days for blockchain infrastructure)
- Takedown announcements (marketplace closures)

### Telegram

| Data Type | Method | Legal Status |
|---|---|---|
| Public channels | Telegram API (MTProto); Telethon; Pyrogram | Legal (public data) |
| Public groups | Telegram API | Legal (public data) |
| Channel metadata | Telegram API (subscriber count, description) | Legal |
| Message content (public) | Telegram API | Legal (public data) |
| Private groups/channels | **Requires consent or legal process** | **Illegal without authorization** |
| User profiles (public) | Telegram API | Legal |

**What to scrape:**
- Crypto scam channels (impersonation, fake airdrops)
- Ransomware group communications (public channels)
- Market manipulation signals
- Dark web marketplace announcements
- Threat actor recruitment posts
- Stolen data leaks (public channels)
- Exchange announcement monitoring

**Tools:**
- Telethon / Pyrogram (Python Telegram API)
- Telegram Bot API (limited)
- Custom scrapers with rate limiting
- NLP pipelines for classification

### Twitter / X

| Data Type | Method | Legal Status |
|---|---|---|
| Public tweets | Twitter/X API (paid tiers) | Legal (API terms) |
| Public profiles | Twitter/X API | Legal |
| Hashtag monitoring | Twitter/X API | Legal |
| List monitoring | Twitter/X API | Legal |
| Direct messages | **Requires consent or legal process** | **Illegal without authorization** |
| Deleted tweets | Nitter instances; Wayback Machine | Legal (public archive) |
| User metadata | Twitter/X API | Legal |

**What to scrape:**
- Scam impersonation accounts
- Rug pull announcements (pre- and post-)
- Threat actor communications
- Exchange incident reporting
- Regulatory announcement monitoring
- Sentiment analysis (market manipulation detection)
- Sybil detection (coordinated inauthentic behavior)

**Tools:**
- Twitter/X API v2 (paid: Basic $100/mo, Pro $5,000/mo)
- Nitter (self-hosted, no API needed)
- Apify (scraping platform)
- Custom NLP pipelines

### Discord

| Data Type | Method | Legal Status |
|---|---|---|
| Public servers | Discord API (bot) | Legal (server terms) |
| Public channels | Discord API | Legal |
| Server metadata | Discord API | Legal |
| Private channels | **Requires bot invitation or legal process** | **Illegal without authorization** |
| User profiles (public) | Discord API | Legal |
| Voice channel metadata | Discord API | Legal |

**What to scrape:**
- Crypto project communities (pre-rug monitoring)
- Scam group coordination
- Insider information leaks
- Market manipulation coordination
- Threat actor recruitment

**Tools:**
- Discord API (bot with appropriate permissions)
- Disnake / discord.py
- Custom NLP for message classification

### WhatsApp

| Data Type | Method | Legal Status |
|---|---|---|
| Public business profiles | WhatsApp Business API | Legal |
| Group messages | **Requires consent or legal process** | **Illegal without authorization** |
| Individual messages | **Requires consent or legal process** | **Illegal without authorization** |

**Key limitation**: WhatsApp is end-to-end encrypted. No public API for message content. Only metadata (timestamps, participant lists) accessible via legal process.

**What's possible:**
- Business profile monitoring (public)
- Legal process for message content (warrant/subpoena)
- Device forensics (seized phones)
- Undercover operations (agent participation)

### Other Sources

| Source | Data Type | Method |
|---|---|---|
| GitHub / GitLab | Code, infrastructure, leaked keys | Public API + secret scanning |
| Reddit | Forum discussions, scam reports | Reddit API + scraping |
| Forums (Bitcointalk, etc.) | Historical discussions, actor TTPs | Web scraping |
| Certificate Transparency | Domain infrastructure | crt.sh, Censys |
| DNS history | Domain → IP → hosting | SecurityTrails, ViewDNS |
| WHOIS / RDAP | Domain registration | Public |
| Shodan / Censys | Internet-exposed services | API |
| Dehashed | Breach data (14B+ records) | API (subscription) |
| IntelX | Billions of archived records | API (subscription) |
| Social-Links | 500+ platform username search | API (enterprise) |
| Maigret | 2,500+ platform username search | CLI (free) |
| Sherlock | 400+ platform username search | CLI (free) |

## Legal Boundaries (CRITICAL)

| Activity | Legal? | Authority |
|---|---|---|
| Scraping public data (websites, social media) | **Yes** | CFAA (post-Van Buren: public data = authorized access) |
| Accessing data behind login (without credentials) | **No** | CFAA § 1030(a)(2) |
| Accessing private groups/channels (without invitation) | **No** | CFAA; platform ToS |
| Scraping dark web public markets | **Yes** | Public data |
| Purchasing stolen data on dark web | **No** | 18 U.S.C. § 1030; 18 U.S.C. § 1343 |
| Creating fake accounts for social engineering | **No** | 18 U.S.C. § 1343; 18 U.S.C. § 912 |
| Using compromised credentials | **No** | CFAA; 18 U.S.C. § 1028 |
| Monitoring public Telegram channels | **Yes** | Public data |
| Accessing private Telegram groups (without consent) | **No** | CFAA |
| Scraping public Twitter/X posts | **Yes** | Public data (API terms) |
| Accessing WhatsApp messages (without consent) | **No** | CFAA; 18 U.S.C. § 2511 |
| Using Tor to access public .onion sites | **Yes** | First Amendment; public data |
| Undercover operations (as private citizen) | **Gray area** | Consult legal counsel |

**Golden Rule**: Only collect data you can lawfully access. If it requires a login you don't have, a group you're not in, or a message sent to someone else — **stop and get legal process**.   