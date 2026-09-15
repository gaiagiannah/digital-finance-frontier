# Quantum-Safe Blockchain Migration

## Approaches

| Approach | Description | Status |
|---|---|---|
| PQC on-chain | Replace ECDSA with ML-DSA in transaction signatures | Ethereum roadmap; FIPS 204 (2,420-byte sigs) |
| Quantum-resistant chains | QANplatform, Abelian, QRL | Early; limited adoption |
| RLNC (MIT) | Random Linear Network Coding: quantum-safe data encoding | MIT hardware synthesis complete (2026) |
| Hybrid cryptography | Classical + PQC in parallel | Deploying now |
| QKD | Physics-based key exchange | Limited by distance/cost |

## MIT Contribution (2026)

Random Linear Network Coding (RLNC) — developed over two decades at MIT's Network Coding and Reliable Communications Group:
- Splits data into coded equations that can be mixed and recombined in transit
- **Synthesized in hardware at MIT**
- Can scale to silicon and into blockchain node cores
- Proven quantum-safe alternative at the network layer

## Ethereum PQC Roadmap

| Phase | Change | Timeline |
|---|---|---|
| 1 | Introduce PQC precompile | 2027-2028 |
| 2 | Enable PQC signatures in transactions | 2028-2029 |
| 3 | Migrate PoS validator signatures | 2029-2030 |
| 4 | Deprecate ECDSA | 2031+ |

## Bitcoin PQC Roadmap

- No formal roadmap yet
- Taproot already enables alternative signature schemes (Schnorr)
- PQC would require soft fork
- Address reuse is the most immediate vulnerability (Google whitepaper, Mar 2026)

## Key Risk: "On-Spend" Attack

A quantum adversary watches the mempool, intercepts a transaction, and derives the private key before it's confirmed. This is the **most immediate threat** (before full Q-Day). Mitigation:
- Use fresh addresses (no reuse)
- PQC signatures in mempool
- Fast confirmation (reduce mempool window)   