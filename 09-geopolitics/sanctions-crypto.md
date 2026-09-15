# Sanctions & Crypto

## Current Enforcement

| Action | Detail |
|---|---|
| Tornado Cash (2022) | OFAC sanctioned protocol; developers arrested |
| North Korean exchanges | OFAC sanctions on multiple exchanges |
| Lazarus Group | OFAC sanctions; FBI indictments |
| Russian oligarchs | Crypto asset freezes (post-2022) |
| Iranian VASPs | OFAC enforcement |

## The mBridge Question

Can mBridge transactions be subject to US/EU sanctions?

- **If** mBridge transactions don't touch correspondent banking rails → potentially outside US jurisdiction
- **If** mBridge settles in e-CNY → US cannot freeze RMB-denominated assets
- **If** a sanctioned entity uses mBridge → enforcement challenge
- **ZK Proofs**: Mandala's vision — prove sanctions compliance *without* revealing the underlying transaction

## FATF Travel Rule

- Applies to all VASPs globally
- 2026 update: Allow-listing, freeze/burn functions
- Cross-border: Sender/receiver info must accompany transfer
- DeFi: Unresolved — no central entity to enforce

## ZK Proofs & Sanctions

| Scenario | ZK Solution |
|---|---|
| "I am not sanctioned" | Prove wallet is not on list without revealing identity |
| "This transaction is compliant" | Prove AML/sanctions compliance without revealing amount |
| "My reserves are sufficient" | Prove solvency without revealing balance |
| "This user is over 18" | Prove age without revealing DOB |   