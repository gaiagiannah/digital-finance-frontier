# Quantum Threat Model

## Shor's Algorithm

Can break RSA and ECC — the foundation of virtually all current financial encryption.

| Parameter | Value |
|---|---|
| Qubits to break RSA-2048 | ~4,000 error-corrected logical qubits |
| Largest demonstrated logical qubit count (Aug 2026) | 96 (QuEra) |
| Quantinuum Helios | 48 logical qubits, 99.97% two-qubit fidelity |
| Projected Q-Day | 2030–2040 |
| **HNDL (Harvest Now, Decrypt Later)** | **Already occurring** |

## The Critical Insight

You don't need a quantum computer *today* to be compromised. If an adversary captures encrypted data *now* and stores it, they decrypt it *later*. For financial data with 20+ year confidentiality requirements, **the data is already compromised**.

## Google Quantum AI Whitepaper (March 2026)

"Securing Elliptic Curve Cryptocurrencies against Quantum Attacks" (with Ethereum Foundation + Stanford):

- Live Bitcoin transaction: private key derivable in **~9 minutes** by fault-tolerant QC
- Address reuse (Binance, Robinhood, Bitfinex) dramatically increases exposure
- "Abandoned" assets (dormant wallets) permanently at risk
- Calls for on-chain PQC migration before "on-spend" attack window opens

## Attack Vectors

| Attack | Target | Timeline |
|---|---|---|
| HNDL | Encrypted financial data (20+ year confidentiality) | **Now** |
| On-spend | Live blockchain transactions (mempool) | Q-Day |
| Key recovery | Dormant/abandoned wallets | Q-Day |
| Smart contract break | All ECDSA-based contracts | Q-Day |
| PoS consensus break | Validator key derivation | Q-Day |   