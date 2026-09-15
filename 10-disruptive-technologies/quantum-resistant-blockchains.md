# Quantum-Resistant Blockchains

## Purpose-Built Chains

| Chain | Approach | Status |
|---|---|---|
| QANplatform | Quantum-resistant consensus + PQC | Live; limited adoption |
| Abelian | Quantum-resistant DLT | Live; limited adoption |
| QRL (Quantum Resistant Ledger) | SPHINCS+ signatures | Live; limited adoption |
| IOTA (post-2024) | Rebranding; quantum-safe messaging | Transitioning |

## Migration of Major Chains

| Chain | Current Sig | PQC Plan | Timeline |
|---|---|---|---|
| Ethereum | ECDSA | PQC precompile → migration | 2027-2031 |
| Bitcoin | ECDSA (secp256k1) | No formal roadmap; Taproot enables alt schemes | Undetermined |
| Solana | Ed25519 | No formal roadmap | Undetermined |
| Canton | ECDSA | PQC migration in planning | 2027-2028 |
| mBridge | ECDSA | PQC migration in planning | 2027-2028 |

## MIT RLNC Approach (2026)

Random Linear Network Coding:
- Splits data into coded equations
- Can be mixed and recombined in transit
- **Synthesized in hardware at MIT**
- Can scale to silicon and into blockchain node cores
- Proven quantum-safe at the network layer (not the signature layer)
- Complementary to PQC (not a replacement)

## The "Good Enough" Question

- If PQC migration is complete by 2030, and Q-Day is 2030-2040, is migration sufficient?
- If Q-Day arrives in 2030 (early estimate), is there enough time?
- HNDL means the answer is: **migrate NOW, don't wait**   