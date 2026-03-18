# Shadow Treasury Desk

- **Repo:** `Synthesis-Venice-PrivateAgents`
- **Primary track:** Venice Private Agents
- **Category:** privacy
- **Submission status:** implementation ready, waiting for credentials and TxIDs.

A private reasoning desk that keeps sensitive treasury, governance, and grant analysis off public rails while still producing verifiable downstream actions.

## Selected concept

Sensitive inputs are routed through a private-analysis module, while only redacted decisions, hashes, and consequence proofs reach public logs. A policy contract binds each private recommendation to a permitted action envelope so the repo stays privacy-first and auditable.

## Idea shortlist

1. Confidential Treasury Copilot
2. Private Risk Desk
3. Private Octant Grant Scorer

## Partners covered

Venice, SelfProtocol, Lido, Uniswap, ENS, Octant, MetaMask Delegations

## Architecture

```mermaid
flowchart TD
    Signals[Discover signals]
    Planner[Agent runtime]
    DryRun[Dry-run artifact]
    Contract[PrivateDecisionRegistry policy contract]
    Verify[Verify and render submission]
    Signals --> Planner --> DryRun --> Contract --> Verify
    Contract --> venice[Venice]
    Contract --> selfprotocol[SelfProtocol]
    Contract --> lido[Lido]
    Contract --> uniswap[Uniswap]
    Contract --> ens[ENS]
    Contract --> octant[Octant]
```

## Repository layout

- `src/`: shared policy contracts plus the repo-specific wrapper contract.
- `script/`: Foundry deployment entrypoint.
- `agents/`: Python runtime, partner adapters, and project metadata.
- `scripts/`: CLI utilities for running the loop and rendering submissions.
- `docs/`: architecture, credentials, demo script, and security notes.
- `submissions/`: generated `synthesis.md` snippet for this repo.

## Action catalog

| Action | Partner | Purpose | Max USD | Sensitivity |
| --- | --- | --- | --- | --- |
| `venice_private_analysis` | Venice | Use Venice for a bounded action in this repo. | $5 | high |
| `selfprotocol_zk_verify` | SelfProtocol | Use SelfProtocol for a bounded action in this repo. | $3 | high |
| `lido_yield_route` | Lido | Use Lido for a bounded action in this repo. | $200 | medium |
| `uniswap_quote_route` | Uniswap | Use Uniswap for a bounded action in this repo. | $220 | medium |
| `ens_ens_publish` | ENS | Use ENS for a bounded action in this repo. | $5 | low |
| `octant_signal_publish` | Octant | Use Octant for a bounded action in this repo. | $25 | medium |
| `metamask_delegations_delegate_scope` | MetaMask Delegations | Use MetaMask Delegations for a bounded action in this repo. | $2 | high |

## Commands

```bash
python3 -m unittest discover -s tests
forge test
python3 scripts/run_agent.py
python3 scripts/plan_live_demo.py
python3 scripts/render_submission.py
```

## Credentials

| Partner | Variables | Docs |
| --- | --- | --- |
| Venice | VENICE_API_KEY, VENICE_CHAT_COMPLETIONS_URL, VENICE_MODEL | https://docs.venice.ai/ |
| SelfProtocol | SELF_PROTOCOL_API_KEY, SELF_VERIFICATION_URL | https://docs.self.xyz/ |
| Lido | RPC_URL | https://docs.lido.fi/ |
| Uniswap | UNISWAP_API_KEY, UNISWAP_QUOTE_URL | https://developers.uniswap.org/ |
| ENS | ENS_NAME | https://docs.ens.domains/ |
| Octant | OCTANT_SIGNAL_URL | https://octant.app/ |
| MetaMask Delegations | RPC_URL | https://docs.metamask.io/delegation-toolkit/ |

## Live demo plan

1. Copy .env.example to .env and fill the required keys.
2. Deploy the contract with forge script script/Deploy.s.sol --broadcast for PrivateDecisionRegistry.
3. Run python3 scripts/run_agent.py to produce a dry run for venice_private_desk.
4. Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
5. Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
