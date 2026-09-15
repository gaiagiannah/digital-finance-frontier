# SaaS Blockchain Analytics Providers

## Market Overview

- **Market size**: $2.5B (2025) → projected $9.9B (2030)
- **Dominant players**: Chainalysis, TRM Labs, Elliptic
- **Emerging**: Crystal Intelligence, Scorechain, CipherTrace (Mastercard), Allium

## Chainalysis

| Dimension | Detail |
|---|---|
| Founded | 2014 (New York) |
| Revenue | ~$100M+ (2025 est.) |
| Customers | 6,500+ VASPs; 100+ law enforcement agencies; 50+ regulators |
| Chain Coverage | 27+ blockchains; 150+ DeFi protocols |
| Labeled Addresses | **1B+ addresses, 15M+ clusters** |
| VASP Coverage | 6,500+ via Kryptos |
| Data Sources | Public blockchain data, exchange partnerships (Kryptos), law enforcement intelligence, proprietary clustering algorithms, ML models, dark web monitoring |
| Products | Reactor (investigation), KYT (monitoring), Kryptos (VASP data), Atlas (market intelligence), Sanctions Screening |
| Investigation Methodology | Heuristic clustering (common input, sequential funding) + ML entity resolution + expert-verified labels + cross-chain tracing |
| What They Do with Data | Risk scoring, entity attribution, transaction tracing, SAR support, court evidence, market reports (Crypto Crime Report) |
| Evidentiary Standard | "Court-trusted intelligence" — used in 100+ legal cases; glass-box scoring with confidence levels |
| Key Differentiator | Largest law enforcement client base; established court record; Kryptos data moat |
| Limitations | Historically weaker on DeFi (improving); vendor-hosted (limited on-prem); less transparent methodology than TRM |

## TRM Labs

| Dimension | Detail |
|---|---|
| Founded | 2018 (New York) |
| Customers | Federal agencies (FedRAMP High), 1,000+ financial institutions |
| Chain Coverage | **77+ blockchains**; 350+ DeFi protocols |
| Data Sources | Public blockchain data, 160+ new services added to attribution DB weekly, KYV (Know Your VASP) with 80+ risk indicators, behavioral analysis |
| Products | Screening, Investigation, Sanctions, Travel Rule, Incident Response |
| Investigation Methodology | **Glass-box attribution**: Every label includes confidence level + explicit reasoning + source methodology. Rule-based + ML hybrid. Transfer Labels detect specific fraud patterns. |
| What They Do with Data | Real-time risk triage, AI-powered threat detection, government agency workflows, FedRAMP-compliant operations |
| Evidentiary Standard | Transparent, explainable — designed for audit defense and regulatory examinations |
| Key Differentiator | FedRAMP High (only one); glass-box transparency; fastest real-time triage; strong federal/government focus |
| Notable | Head of Global Investigations: Chris Janczewski (former IRS-CI, 10+ years crypto investigations, led Lazarus disruption) |
| Limitations | Less visual than Chainalysis Reactor; smaller VASP database than Kryptos |

## Elliptic

| Dimension | Detail |
|---|---|
| Founded | 2014 (London) |
| Customers | 1,000+ VASPs via Discovery; strong EU/FCA presence |
| Chain Coverage | **50+ blockchains, 250+ bridges**; 400+ DeFi protocols |
| Labeled Addresses | **2B+ addresses** |
| Data Sources | Public blockchain data, 100B+ data points, VASP profiles via Discovery, expert threat intelligence, cross-chain analytics |
| Products | Lens (screening), Investigator (tracing), Discovery (VASP data), Holistic Screening (cross-chain) |
| Investigation Methodology | ML + expert threat intelligence; **Holistic Screening** merges data across all assets/blockchains into single risk assessment; superior cross-chain tracing (99% market coverage) |
| What They Do with Data | Cross-chain compliance, EU market focus, FCA regulatory engagement, DeFi protocol analysis |
| Evidentiary Standard | Documented evidence per label; ISO 27001 certified |
| Key Differentiator | Best cross-chain visibility; strongest EU/FCA relationship; deepest DeFi protocol coverage; 2M+ monthly screenings |
| Limitations | Less law enforcement focus than Chainalysis; limited on-prem; UK-centric (though expanding) |

## Crystal Intelligence

| Dimension | Detail |
|---|---|
| Focus | OFAC sanctions compliance; Eastern European exchange attribution |
| Labeled Entities | 110,000+ attributed entities |
| VASP Coverage | 2,500+ service providers |
| Key Differentiator | Explainable risk scoring; on-premise available; data not available in other three platforms |
| Best For | Sanctions compliance, Eastern European attribution |

## CipherTrace (Mastercard)

| Dimension | Detail |
|---|---|
| Acquired | By Mastercard (2021) |
| Focus | Legacy compliance, Travel Rule, Bitcoin/Ethereum + major chains |
| Products | Threat monitoring, risk scoring, intelligence feeds, de-anonymization, ransomware detection |
| Key Differentiator | Mastercard integration; Travel Rule compliance; individual victim support |
| Limitations | Reduced standalone development post-acquisition; limited chain coverage vs. competitors |

## Allium

| Dimension | Detail |
|---|---|
| Focus | Data infrastructure for compliance, screening, custom models |
| Chain Coverage | 150+ chains |
| Deployment | Snowflake, Databricks, BigQuery datashares; APIs; streams |
| Key Differentiator | SOC 1 & SOC 2 data; queryable, reproducible source data; on-prem/air-gapped; your own secure compute |
| Best For | Organizations wanting raw data + custom ML models |

## Comparison Matrix

| Feature | Chainalysis | TRM Labs | Elliptic | Crystal |
|---|---|---|---|---|
| Chains | 27+ | 77+ | 50+ | Major |
| DeFi Protocols | 150+ | 350+ | 400+ | ~50 |
| Labeled Addresses | 1B+ | Not disclosed | 2B+ | 110K entities |
| VASPs | 6,500+ | Thousands (KYV) | 1,000+ (Discovery) | 2,500+ |
| FedRAMP | No | **High** | No | No |
| On-Prem | Limited | Via FedRAMP cloud | Limited | **Yes** |
| Glass-Box | Partial | **Full** | Documented | Explainable |
| Cross-Chain | Good | Strong | **Best (99%)** | Moderate |
| Law Enforcement | **Best** | Strong (federal) | Moderate | Niche |
| EU/FCA | Moderate | Moderate | **Best** | Moderate |
| DeFi Coverage | Improving | Strong | **Best** | Limited |
| Dark Web | Yes | Yes | Yes | Yes |   