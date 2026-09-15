# Incident Response: Crypto Asset DFIR Playbook

## Phase 1: Detection & Triage (0-1 hour)

1. Confirm the incident (false positive check)
2. Classify: Exploit, Insider, Ransomware, Phishing, Bridge Fail
3. Activate incident response team
4. Begin logging (preserve all evidence)
5. Notify: Legal, Compliance, CISO, Board (per policy)

## Phase 2: Containment (1-4 hours)

1. Isolate affected systems
2. Freeze affected wallets/addresses (if possible)
3. Notify exchanges (for freezing if legal process allows)
4. Preserve memory, disk, network captures
5. Document chain of custody

## Phase 3: Investigation (4-72 hours)

1. On-chain tracing (follow the money)
2. Off-chain OSINT (attacker infrastructure, social media)
3. Dark web monitoring (ransom notes, stolen data)
4. KYC data requests (legal process)
5. Attribution (TTP mapping, actor profiling)

## Phase 4: Eradication & Recovery

1. Patch vulnerability / rotate keys
2. Restore from clean backups
3. Monitor for re-exploitation
4. Recover assets (if possible)

## Phase 5: Reporting & Lessons Learned

1. Regulatory reporting (FinCEN SAR, SEC 8-K, EU equivalents)
2. Law enforcement handoff (FBI, SEC, Europol)
3. Customer notification (per GDPR/CCPA if PII affected)
4. Post-incident review
5. Update playbooks and controls

## Crypto-Specific Considerations

| Consideration | Detail |
|---|---|
| Irreversibility | Transactions cannot be reversed; speed is critical |
| Jurisdiction | Assets may move across borders in minutes |
| Legal process | KYC data requires warrant/subpoena/MLAT |
| Public data | On-chain data is public; no warrant needed for tracing |
| Mixers | Tornado Cash, CoinJoin complicate tracing |
| Cross-chain | Assets may bridge to other chains during investigation |
| Timing | "Golden hour" — first 60 minutes determine recoverability |   