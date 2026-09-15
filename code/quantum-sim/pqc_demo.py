#!/usr/bin/env python3
"""
Post-Quantum Cryptography Demo — Digital Finance Frontier
Demonstrates ML-KEM (FIPS 203) and ML-DSA (FIPS 204) operations.

Usage:
    python3 pqc_demo.py                          # Run all demos
    python3 pqc_demo.py --operation kem          # Key encapsulation only
    python3 pqc_demo.py --operation sign         # Digital signature only
    python3 pqc_demo.py --operation blockchain   # Blockchain implications only
    python3 pqc_demo.py --operation all --verbose

Requires:
    pip install pyoqs
    # Alternative: OpenSSL 3.x with PQC support (no pyoqs needed for --operation blockchain)

NIST POST-QUANTUM STANDARDS:
    FIPS 203: ML-KEM (Kyber)     — Key Encapsulation
    FIPS 204: ML-DSA (Dilithium) — Digital Signatures
    FIPS 205: SLH-DSA (SPHINCS+) — Hash-based fallback

HNDL (Harvest Now, Decrypt Later):
    Encrypted data captured TODAY is compromised for long-term confidentiality.
    Financial data with 20+ year requirements is ALREADY at risk.
    See: 07-quantum-finance/threat-model.md
"""

import argparse
import sys
import time


# ─── ML-KEM (FIPS 203) ──────────────────────────────────────────────────────

def demo_kem(verbose: bool = False):
    """Demonstrate ML-KEM-768 key encapsulation (FIPS 203)."""
    print(f"\n{'='*64}")
    print(f"  ML-KEM-768 KEY ENCAPSULATION (FIPS 203)")
    print(f"{'='*64}")

    print(f"""
  Purpose:
    Replace ECDH / RSA-KEM for secure key exchange.
    Two parties derive a shared secret without pre-sharing a key.

  Flow:
    1. Bob:   (pk, sk) = KeyGen()
    2. Alice: (ct, ss1) = Encaps(pk)
    3. Bob:   ss2 = Decaps(sk, ct)
    4. Assert: ss1 == ss2  (shared secret established)

  Parameters (ML-KEM-768):
    Public Key Size:    1,184 bytes
    Ciphertext Size:    1,088 bytes
    Shared Secret Size:    32 bytes
    Security Level:       NIST Level 3 (>= AES-192)

  Comparison (Classical ECDH P-256):
    Public Key Size:      65 bytes
    Shared Secret Size:   32 bytes
    Quantum Security:     BROKEN (Shor's algorithm)

  Financial Use Cases:
    - Secure channel: bank <-> central bank (Project Agora)
    - Key exchange for tokenized deposit settlement
    - Cross-border payment encryption (mBridge)
    - HSM-to-HSM key wrapping (JPMorgan Q-CAN)
""")

    try:
        from pyoqs import PQKEM

        kem = PQKEM("ML-KEM-768")

        # PQKEM.keygen() returns (pk, sk) tuple
        t0 = time.perf_counter()
        pk, sk = kem.keygen()
        t_keygen = time.perf_counter() - t0

        # Encapsulation (Alice)
        t0 = time.perf_counter()
        ct, ss1 = kem.encaps(pk)
        t_encaps = time.perf_counter() - t0

        # Decapsulation (Bob)
        t0 = time.perf_counter()
        ss2 = kem.decaps(sk, ct)
        t_decaps = time.perf_counter() - t0

        # Verify
        assert ss1 == ss2, "FATAL: Shared secrets do not match!"

        print(f"  [PASS] Key encapsulation verified: ss1 == ss2")
        print(f"  [INFO] PK size:      {len(pk):>5} bytes  (expected 1184)")
        print(f"  [INFO] CT size:      {len(ct):>5} bytes  (expected 1088)")
        print(f"  [INFO] SS size:      {len(ss1):>5} bytes  (expected 32)")
        print(f"  [INFO] Security:     NIST Level 3")

        if verbose:
            print(f"\n  [PERF] KeyGen:    {t_keygen*1000:.2f} ms")
            print(f"  [PERF] Encaps:    {t_encaps*1000:.2f} ms")
            print(f"  [PERF] Decaps:    {t_decaps*1000:.2f} ms")
            print(f"  [PERF] Total:     {(t_keygen+t_encaps+t_decaps)*1000:.2f} ms")

    except ImportError:
        print(f"  [SKIP] pyoqs not installed. Install with: pip install pyoqs")
        print(f"  [INFO] Parameter values above are correct for ML-KEM-768.")
    except Exception as e:
        print(f"  [ERROR] {type(e).__name__}: {e}")
        sys.exit(1)


# ─── ML-DSA (FIPS 204) ──────────────────────────────────────────────────────

def demo_sign(verbose: bool = False):
    """Demonstrate ML-DSA-65 digital signature (FIPS 204)."""
    print(f"\n{'='*64}")
    print(f"  ML-DSA-65 DIGITAL SIGNATURE (FIPS 204)")
    print(f"{'='*64}")

    print(f"""
  Purpose:
    Replace ECDSA / RSA-PSS for digital signatures.
    Prove authenticity and integrity without revealing the signing key.

  Flow:
    1. Alice: sk = KeyGen()
    2. Alice: pk = PK_from_SK(sk)
    3. Alice: sig = Sign(sk, message)
    4. Bob:   valid = Verify(pk, message, sig)

  Parameters (ML-DSA-65):
    Public Key Size:    1,952 bytes
    Secret Key Size:    4,896 bytes
    Signature Size:     3,320 bytes
    Security Level:       NIST Level 3

  Comparison (Classical ECDSA secp256k1):
    Public Key Size:      65 bytes
    Secret Key Size:      32 bytes
    Signature Size:        64 bytes
    Quantum Security:     BROKEN (Shor's algorithm)

  Blockchain Implication:
    - 3,320-byte sig vs. 64-byte ECDSA = 52x larger
    - Transaction size increase: ~50x
    - Ethereum: PQC precompile needed (roadmap 2027-2031)
    - Bitcoin: No formal PQC roadmap yet
    - Canton / mBridge: PQC migration in planning
""")

    try:
        from pyoqs import PQSignature

        sig_alg = PQSignature("ML-DSA-65")

        # PQSignature.keygen() returns ONLY sk (not a tuple)
        t0 = time.perf_counter()
        sk = sig_alg.keygen()
        pk = sig_alg.pk_from_sk(sk)
        t_keygen = time.perf_counter() - t0

        # Sign
        message = b"Digital Finance Frontier - PQC Demo - 2026-09-15"
        t0 = time.perf_counter()
        signature = sig_alg.sign(sk, message)
        t_sign = time.perf_counter() - t0

        # Verify (valid)
        t0 = time.perf_counter()
        valid = sig_alg.verify(pk, message, signature)
        t_verify = time.perf_counter() - t0
        assert valid, "FATAL: Valid signature failed verification!"

        # Verify (tampered)
        tampered = message + b" "
        t0 = time.perf_counter()
        invalid = sig_alg.verify(pk, tampered, signature)
        t_verify_bad = time.perf_counter() - t0
        assert not invalid, "FATAL: Tampered message passed verification!"

        print(f"  [PASS] Signature verified: valid=True")
        print(f"  [PASS] Tamper detection:   valid=False (correct)")
        print(f"  [INFO] PK size:        {len(pk):>5} bytes  (expected 1952)")
        print(f"  [INFO] SK size:        {len(sk):>5} bytes  (expected 4896)")
        print(f"  [INFO] Signature size: {len(signature):>5} bytes  (expected 3320)")
        print(f"  [INFO] Message:        {message.decode()}")
        print(f"  [INFO] Security:       NIST Level 3")

        if verbose:
            print(f"\n  [PERF] KeyGen:   {t_keygen*1000:.2f} ms")
            print(f"  [PERF] Sign:     {t_sign*1000:.2f} ms")
            print(f"  [PERF] Verify:   {t_verify*1000:.2f} ms")
            print(f"  [PERF] Verify(bad): {t_verify_bad*1000:.2f} ms")

    except ImportError:
        print(f"  [SKIP] pyoqs not installed. Install with: pip install pyoqs")
        print(f"  [INFO] Parameter values above are correct for ML-DSA-65.")
    except Exception as e:
        print(f"  [ERROR] {type(e).__name__}: {e}")
        sys.exit(1)


# ─── BLOCKCHAIN IMPLICATIONS ────────────────────────────────────────────────

def demo_blockchain():
    """Explain PQC implications for blockchain and financial infrastructure."""
    print(f"\n{'='*64}")
    print(f"  PQC IMPACT ON BLOCKCHAIN & FINANCIAL INFRASTRUCTURE")
    print(f"{'='*64}")

    print(f"""
  1. TRANSACTION SIZE INCREASE
     ECDSA signature:      64 bytes
     ML-DSA signature:   3,320 bytes  (52x larger)
     Impact: Block size, bandwidth, storage, gas fees

  2. KEY SIZE INCREASE
     ECDSA private key:    32 bytes
     ML-DSA private key: 4,896 bytes  (153x larger)
     Impact: Key storage, HSM capacity, backup, MPC shares

  3. MIGRATION ROADMAP
     Ethereum:  PQC precompile -> soft fork (2027-2031)
     Bitcoin:   No formal roadmap; Taproot enables alt schemes
     Solana:    No formal roadmap
     Canton:    PQC migration in planning (2027-2028)
     mBridge:   PQC migration in planning
     SWIFT:     ISO 20022 + PQC (2027+)

  4. HNDL THREAT (ALREADY ACTIVE)
     - Encrypted financial data captured today by adversaries
     - Decrypted after Q-Day (est. 2030-2040)
     - 20+ year confidentiality data: ALREADY compromised
     - Mitigation: PQC migration NOW (not at Q-Day)
     - JPMorgan Q-CAN: First production deployment (2026)
     - Microsoft ML-DSA in Active Directory (May 2026)

  5. ON-SPEND ATTACK (MOST IMMEDIATE)
     - Quantum adversary monitors mempool
     - Intercepts transaction, derives private key in ~9 min
     - Before transaction is confirmed
     - Source: Google Quantum AI + Ethereum Foundation + Stanford (Mar 2026)
     - Mitigation:
       * Use fresh addresses (no reuse)
       * PQC signatures in mempool
       * Fast confirmation (reduce mempool window)
       * Address reuse at Binance/Robinhood/Bitfinex = high risk

  6. MITIGATION STRATEGY
     - Hybrid cryptography (classical + PQC in parallel)
     - Crypto-agility (swap algorithms without system redesign)
     - TLS 1.3 + X25519MLKEM768: Deploying now
     - NIST deadline: Full migration by 2035
     - White House EO: Federal migration by Dec 2030-2031
     - EU: Critical infrastructure by 2030; medium-risk by 2035

  7. DECISION FRAMEWORK (BY DATA CLASS)

     Data Class              | Confidentiality | PQC Urgency
     ------------------------|-----------------|------------
     Customer PII            | 7-10 years      | Medium
     Trade strategies        | 5-10 years      | Medium
     Central bank reserves   | 20+ years       | CRITICAL (NOW)
     Customer deposits       | 20+ years       | CRITICAL (NOW)
     National security       | 20+ years       | CRITICAL (NOW)
     Blockchain keys         | Indefinite      | CRITICAL (NOW)
     Public blockchain data  | N/A (public)    | Low
""")


# ─── MAIN ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="PQC Demo - Digital Finance Frontier",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 pqc_demo.py
  python3 pqc_demo.py --operation kem
  python3 pqc_demo.py --operation sign --verbose
  python3 pqc_demo.py --operation blockchain
        """
    )
    parser.add_argument(
        "--operation",
        default="all",
        choices=["all", "kem", "sign", "blockchain"],
        help="Which demo to run (default: all)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show performance timings"
    )
    args = parser.parse_args()

    print(f"""
================================================================
  POST-QUANTUM CRYPTOGRAPHY DEMO
  Digital Finance Frontier v1.0 | 2026-09-15

  Standards: NIST FIPS 203 (ML-KEM) / FIPS 204 (ML-DSA)
  Threat:    HNDL - Harvest Now, Decrypt Later
================================================================
    """)

    if args.operation in ("all", "kem"):
        demo_kem(args.verbose)

    if args.operation in ("all", "sign"):
        demo_sign(args.verbose)

    if args.operation in ("all", "blockchain"):
        demo_blockchain()

    print(f"\n{'='*64}")
    print(f"  References:")
    print(f"    - NIST FIPS 203 (ML-KEM): csrc.nist.gov/pqc")
    print(f"    - NIST FIPS 204 (ML-DSA): csrc.nist.gov/pqc")
    print(f"    - Google Quantum AI whitepaper (Mar 2026)")
    print(f"    - 07-quantum-finance/pqc-standards.md")
    print(f"    - 07-quantum-finance/blockchain-migration.md")
    print(f"{'='*64}\n")


if __name__ == "__main__":
    main()   