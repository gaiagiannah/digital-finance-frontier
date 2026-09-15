# Zero-Knowledge Machine Learning

## Concept

Prove that a ML model was run correctly on specific data, without revealing the data or the model weights.

## Applications

| Application | Description | Status |
|---|---|---|
| Private credit scoring | Prove creditworthiness without revealing financial data | Research |
| Confidential AML | Prove AML compliance without revealing transaction details | Research (Mandala) |
| IP protection | Prove model ran without revealing proprietary weights | Research |
| Regulated AI | Prove AI decision was fair/compliant without revealing training data | Theoretical |

## Technical Approaches

| Approach | Description | Limitation |
|---|---|---|
| ZK + FHE | Homomorphic encryption inside ZK circuit | Extremely slow |
| ZK + MPC | Multi-party computation inside ZK | Communication overhead |
| ZK + TEE | Trusted Execution Environment + ZK attestation | Trust in hardware |
| ZK + Confidential Computing | SGX/SEV + ZK proof of computation | Emerging |

## Research Status

- MIT: ZK-ML circuit compilation (2025-2026)
- Stanford: ZK proofs for neural network inference
- No production system yet
- Estimated: 2028-2030 for first production use in finance   