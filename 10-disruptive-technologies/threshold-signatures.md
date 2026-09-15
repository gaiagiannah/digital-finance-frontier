# Threshold Signatures & MPC

## Concept

Distribute a cryptographic key across N parties. Any K parties (K ≤ N) can jointly produce a valid signature without any single party holding the full key.

## Applications

| Application | Description | Status |
|---|---|---|
| Institutional custody | Fireblocks, Safe, Ledger — no single point of key failure | Production |
| Exchange security | Multi-sig for exchange hot wallets | Production |
| CBDC key management | Central bank + commercial bank joint keys | Research (Mandala) |
| Smart contract signing | Multi-party approval for on-chain actions | Production |
| PQC transition | MPC + PQC for quantum-safe key management | Research |

## Key Schemes

| Scheme | Type | Status |
|---|---|---|
| ECDSA TSS | Threshold ECDSA | Production (Fireblocks, Safe) |
| EdDSA TSS | Threshold EdDSA | Production |
| ML-DSA TSS | Threshold PQC signature | Research (2026) |
| BLS TSS | Threshold BLS (Ethereum validators) | Production (Lido) |

## PQC + MPC

The intersection of threshold signatures and post-quantum cryptography is an active research area:
- Can ML-DSA be split into shares? (Open problem)
- Hybrid: Classical TSS + PQC key wrapping
- JPMorgan Q-CAN: Crypto-agile network supporting both   