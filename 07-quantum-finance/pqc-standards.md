# Post-Quantum Cryptography Standards

## NIST Final Standards

| Standard | Algorithm | Type | Status |
|---|---|---|---|
| FIPS 203 | ML-KEM (Kyber) | Key encapsulation | Final (Aug 2024) |
| FIPS 204 | ML-DSA (Dilithium) | Digital signature | Final (Aug 2024) |
| FIPS 205 | SLH-DSA (SPHINCS+) | Hash-based signature | Final (Aug 2024) |
| FIPS 206 | FN-DSA (Falcon) | Compact signature | Draft (2026-2027) |
| HQC | Code-based KEM | Backup KEM | Selected Mar 2025; FIPS 2027 |

## Key Sizes

| Algorithm | Public Key | Signature | Security Level |
|---|---|---|---|
| ML-KEM-512 | 800 B | — (KEM) | NIST L1 |
| ML-KEM-768 | 1184 B | — (KEM) | NIST L3 |
| ML-KEM-1024 | 1568 B | — (KEM) | NIST L5 |
| ML-DSA-44 | 1312 B | 2420 B | NIST L2 |
| ML-DSA-65 | 1952 B | 3320 B | NIST L3 |
| ML-DSA-87 | 2592 B | 4628 B | NIST L5 |

## Migration Timeline

| Date | Milestone |
|---|---|
| Aug 2024 | NIST finalizes FIPS 203/204/205 |
| 2025 | EU: National PQC strategies by end 2026; critical infra by 2030 |
| May 2026 | Microsoft ships ML-DSA in Active Directory |
| 2026 | White House EO: Federal PQC migration mandates |
| Jul 2026 | Federal agencies identify PQC migration lead |
| Sep 2026 | OMB guidance: Agencies submit PQC plans |
| Dec 2030 | Federal HVAs: PQC for key establishment |
| Dec 2031 | Federal HVAs: PQC for digital signatures |
| 2030 | EU: Critical infrastructure PQC complete |
| 2035 | EU: Medium-risk; NSA CNSA 2.0 full compliance |
| 2035 | NIST: Full PQC migration for critical infrastructure |

## Hybrid Cryptography (Transition)

- TLS 1.3 + X25519MLKEM768: Deploying now
- Classical + PQC in parallel during transition period
- "Crypto-agility": Ability to swap algorithms without system redesign   