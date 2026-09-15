# DFINT Investigation Methodology

## Framework
┌─────────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: DETECTION │
│ On-chain Alerts · OSINT Triggers · Dark Web Monitoring · AI Anomaly │
├─────────────────────────────────────────────────────────────────────────────┤
│ PHASE 2: COLLECTION │
│ On-chain · Off-chain · Network · Preservation (hash, WORM) │
├─────────────────────────────────────────────────────────────────────────────┤
│ PHASE 3: ANALYSIS │
│ Chain Tracing · Graph Analysis · Clustering · Temporal Patterns │
├─────────────────────────────────────────────────────────────────────────────┤
│ PHASE 4: ATTRIBUTION │
│ TTP Mapping · OSINT Correlation · KYC Linking · Actor Profiling │
├─────────────────────────────────────────────────────────────────────────────┤
│ PHASE 5: RESPONSE & REPORTING │
│ Asset Freezing · Regulatory Reporting · Law Enforcement · Intelligence │
└─────────────────────────────────────────────────────────────────────────────┘

## Chain of Custody

1. **Discovery**: Document initial detection (timestamp, source, operator)
2. **Collection**: Acquire data with hash verification (SHA-256)
3. **Preservation**: Store in WORM (Write Once, Read Many) storage
4. **Analysis**: Work on copies only; document all steps
5. **Reporting**: Generate admissible evidence package
6. **Retention**: Maintain per jurisdictional requirements

## Legal Considerations

- Jurisdiction determines legal process (warrant, subpoena, MLAT)
- Cross-border data access: CLOUD Act (US), GDPR (EU), local laws
- Exchange cooperation: KYC data available via legal process
- Chain analysis: Public data (no warrant needed for on-chain)
- Off-chain data: Requires legal process   