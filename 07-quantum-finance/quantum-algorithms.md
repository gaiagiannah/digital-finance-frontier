# Quantum Algorithms for Finance 

## QAOA (Quantum Approximate Optimization Algorithm)

### How It Works
ENCODE: Map portfolio optimization to Ising model
Each qubit = asset (include/exclude)
Cost Hamiltonian H_C = objective + constraint penalties
Mixer Hamiltonian H_B = sum(X_i) (bit-flip)
ALTERNATE: Apply p layers of:
U_C(γ) = exp(-iγH_C) [cost rotation]
U_B(β) = exp(-iβH_B) [mixer rotation]
MEASURE: Sample from final state
Best sample = approximate optimal portfolio
OPTIMIZE: Classical optimizer adjusts (γ, β) parameters
Repeat for p layers
More layers = better approximation (but more qubits)

### Current Results (2026)

| Benchmark | Result | Source |
|---|---|---|
| 225-asset portfolio | Optimized on Quantinuum Helios | Jul 2026 |
| Speedup vs. classical | **12%** | JPMorgan/AWS |
| Qubits needed (practical) | ~7,500 logical | Goldman Sachs |
| Qubits available (best) | 96 logical (QuEra) | Aug 2026 |
| Gap | **~78x** | — |

### Why Only 12%?

- Current hardware: NISQ (Noisy Intermediate-Scale Quantum)
- Error rates: 10^-2 to 10^-3 per gate
- Logical qubits: 96 (vs. 7,500 needed)
- Classical algorithms are very good (cvxpy, MOSEK)
- QAOA advantage requires fault-tolerant QC (1000+ logical qubits)

### When Will QAOA Be Useful?

| Milestone | Year (est.) |
|---|---|
| 100 logical qubits | 2027 |
| 500 logical qubits | 2028-2029 |
| 1,000 logical qubits | 2029-2030 |
| 7,500 logical qubits | 2032-2035 |
| **QAOA practical advantage** | **2030-2035** |

---

## VQE (Variational Quantum Eigensolver)

### How It Works
ENCODE: Map bond/asset pricing to quantum chemistry problem
Hamiltonian = sum of interaction terms
Each term = Pauli operator (X, Y, Z)
PARAMETERIZE: Ansatz circuit with trainable parameters θ
Hardware-efficient (matches qubit connectivity)
Or: ADAPT-VQE (adaptive)
MEASURE: Expectation value ⟨ψ(θ)|H|ψ(θ)⟩
Each Pauli term measured separately
Classical computer combines results
OPTIMIZE: Classical optimizer minimizes ⟨H⟩
Adam, SPSA, or gradient-based
Repeat until convergence
RESULT: Ground state energy = bond price / portfolio value

### Fidelity FCAT Results (2026)

| Benchmark | Result |
|---|---|
| 30-stock index replication | Feasible on current hardware |
| 50-stock index replication | Feasible (with error mitigation) |
| 100+ stocks | Not yet (needs more qubits) |
| Bond pricing (single) | Feasible; matches classical |
| Bond pricing (portfolio) | Not yet |
| Hardware | Rigetti Aspen-M; IonQ trapped-ion |

### Limitations

- Each Pauli term requires separate circuit execution
- 100+ stocks = 100+ circuits = slow
- Error mitigation adds overhead
- Classical alternatives (Monte Carlo, PDE) are very fast
- VQE advantage: **unclear** for finance (unlike chemistry)

---

## Quantum Amplitude Estimation (Most Promising)

### Why It's the Winner

| Metric | Classical Monte Carlo | Quantum Amplitude Estimation |
|---|---|---|
| Convergence | 1/√N (slow) | **1/N** (quadratic speedup) |
| 99% accuracy | ~10,000 samples | ~100 samples |
| 99.9% accuracy | ~100,000 samples | ~1,000 samples |
| **Speedup** | — | **10x (proven, not theoretical)** |

### Application: Derivatives Pricing
Problem: Price a derivative with payoff f(S_T)

S_T = terminal stock price (log-normal)
f = payoff function (call, put, barrier, etc.)
Classical: Monte Carlo with N paths

Price ≈ (1/N) * sum(f(S_T^i))
Error ∝ 1/√N
10,000 paths for 1% accuracy
Quantum: Amplitude Estimation

Encode probability distribution in quantum state
Estimate amplitude (probability) with 1/N convergence
100 paths for 1% accuracy
100x fewer evaluations

### Goldman Sachs Benchmark

| Parameter | Value |
|---|---|
| Logical qubits needed | ~7,500 |
| Circuit depth | ~10,000 gates |
| Current best | 96 logical qubits (QuEra) |
| Gap | ~78x |
| Estimated timeline | 2030-2032 |

### Why Amplitude Estimation > QAOA for Finance

| Factor | QAOA | Amplitude Estimation |
|---|---|---|
| Speedup type | Theoretical (unproven) | **Proven (quadratic)** |
| Qubits needed | 7,500 | 7,500 |
| Circuit depth | p layers (shallow) | ~10,000 gates (deep) |
| Error sensitivity | High (shallow = less error) | High (deep = more error) |
| Classical baseline | Very good (cvxpy) | Good (Monte Carlo) |
| **Advantage magnitude** | Small (12% current) | **Large (10x potential)** |
| **First to production** | Later | **First (most likely)** |

---

## HHL (Harrow-Hassidim-Lloyd)

### Application: Risk Modeling
Problem: Solve Ax = b for large matrix A (risk covariance)

A = covariance matrix (n×n)
b = return vector
x = optimal portfolio weights
Classical: O(n²) or O(n³)
Quantum (HHL): O(log n) — exponential speedup (theoretical)

JPMorgan: Hybrid HHL++ on Quantinuum H-series (2024)

"Hybrid" = classical + quantum (not pure quantum)
Practical for n < 100 (current hardware)
Advantage for n > 1000 (future hardware)

### Limitations

- Requires fault-tolerant QC (error correction)
- Matrix must be sparse (covariance matrices often aren't)
- State preparation is expensive
- Readout is probabilistic (need multiple runs)
- **Not practical until 2030+**

---

## Quantum Machine Learning (QML)

### Current State (2026)

- **No production QML in finance**
- Theoretical speedups unproven at financial scale
- Hybrid quantum-classical workflows in research only

### Applications (Theoretical)

| Application | Algorithm | Potential Speedup | Status |
|---|---|---|---|
| Fraud detection | QSVT, QAOA | 2-10x (if it works) | Proof-of-concept |
| Portfolio classification | Quantum kernel | 2-5x | Research |
| AML (graph) | Quantum GNN | Unknown | Theoretical |
| NLP (OSINT) | Quantum NLP | Unknown | Theoretical |
| Anomaly detection | Quantum autoencoder | 2-5x | Research |

### Key Challenges

1. **QRAM**: Loading classical data into quantum state (unsolved at scale)
2. **Circuit depth**: QML circuits are deep (error-prone on NISQ)
3. **Feature engineering**: New discipline (quantum feature maps)
4. **Classical baseline**: Classical ML is very good (GNNs, transformers)
5. **Data volume**: Financial datasets are large (millions of transactions)

### Most Likely First Production Use

**Quantum-enhanced fraud detection** at JPMorgan or Fidelity, **2029-2030**, if hardware cooperates. Even then, likely a 2-5x improvement over classical (not 100x).

---

## Grover's Algorithm (Search)

### Financial Application

| Application | Classical | Quantum (Grover) |
|---|---|---|
| Brute-force key recovery (AES-256) | 2^256 | **2^128** (quadratic) |
| Database search (n records) | O(n) | **O(√n)** |
| Sanctions list screening (1M entries) | 1M checks | **1,000 checks** |

### Key Insight

- Grover gives **quadratic** speedup (not exponential)
- AES-256 → effective 128-bit (still secure)
- SHA-256 → effective 128-bit (still secure)
- **Symmetric crypto is NOT broken by quantum** (only asymmetric: RSA, ECC)
- Financial impact: Minimal for data encryption; significant for key recovery   