# AI Agent Architecture in Finance

## Coinbase AgentKit & x402

- **AgentKit**: SDK for building AI agents that can transact on-chain
- **x402 Protocol**: HTTP 402 Payment Required — enables AI agents to pay for services on-chain
- **Smart Wallet**: Coinbase wallet designed for agent-driven transactions
- **Base L2**: Native support for agent commerce

## Agent Types

| Type | Function | Example |
|---|---|---|
| Trading Agent | Autonomous portfolio management | 68% of new protocols |
| Market Maker | 24/7 liquidity provision | DEX AMMs with AI |
| Compliance Agent | AML, sanctions, reporting | Mandala Phase 2 vision |
| Governance Agent | DAO voting, policy enforcement | APOLLO (2026) |
| Prediction Agent | Market prediction, arbitrage | Polymarket, Kalshi (18%) |
| Treasury Agent | Cash management, rebalancing | Emerging |

## Safety Architecture

- **Bounded LLM Orchestration** (Arcifa et al., 2026): Smart contract safety gates around LLM actions
- **Circuit Breakers**: Hard limits on agent actions (max position, max velocity)
- **Auditability**: All agent actions logged on-chain (Phiri, 2025: "Eight Auditability Axioms")
- **Human-in-the-Loop**: Approval required for actions above threshold   