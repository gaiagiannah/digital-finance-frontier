# Encryption Standards: Current + PQC Migration

## Current Standards (Being Replaced)

| Standard | Algorithm | Use | Vulnerability |
|---|---|---|---|
| RSA-2048 | RSA | Key exchange, signatures | Shor's algorithm (quantum) |
| ECDSA (secp256k1) | ECC | Blockchain signatures | Shor's algorithm (quantum) |
| ECDH (P-256) | ECC | Key exchange | Shor's algorithm (quantum) |
| AES-256 | Symmetric | Data encryption | Grover (quadratic → effective 128-bit; still secure) |
| SHA-256 | Hash | Integrity, PoW | Grover (quadratic → effective 128-bit; still secure) |

## PQC Replacement Mapping

| Current | PQC Replacement | Standard |
|---|---|---|
| ECDH | ML-KEM-768 | FIPS 203 |
| ECDSA | ML-DSA-65 | FIPS 204 |
| RSA-PSS | ML-DSA-65 or SLH-DSA | FIPS 204/205 |
| AES-256 | AES-256 (unchanged) | — |
| SHA-256 | SHA-256 (unchanged) or SHA-3 | — |

## Blockchain-Specific Considerations

| Chain | Current Sig | PQC Plan |
|---|---|---|
| Bitcoin | ECDSA (secp256k1) | No formal roadmap; Taproot enables alt schemes |
| Ethereum | ECDSA (secp256k1) | Roadmap: PQC precompile → migration (2027-2031) |
| Solana | Ed25519 | No formal roadmap |
| Canton | ECDSA | PQC migration in planning |
| mBridge | ECDSA | PQC migration in planning |

## The HNDL Problem

| Data Type | Confidentiality Need | PQC Urgency |
|---|---|---|
| Customer PII | 7-10 years | Medium |
| Trade strategies | 5-10 years | Medium |
| Central bank data | 20+ years | **Critical — NOW** |
| Customer deposits | 20+ years | **Critical — NOW** |
| National security | 20+ years | **Critical — NOW** |
| Blockchain keys | Indefinite (as long as chain exists) | **Critical — NOW** |   