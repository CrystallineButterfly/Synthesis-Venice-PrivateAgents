# Live readiness

- **Project:** Shadow Treasury Desk
- **Track:** Venice Private Agents
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:21+00:00`

## Trust boundaries

- **Venice** — `rest_json` — Run private reasoning over sensitive inputs.
- **SelfProtocol** — `rest_json` — Gate sensitive actions behind privacy-preserving proofs.
- **Lido** — `contract_call` — Route staking yield through guarded treasury actions.
- **Uniswap** — `rest_json` — Quote swaps and bounded liquidity moves.
- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.
- **Octant** — `rest_json` — Publish scored public-goods signals and DPI artifacts.
- **MetaMask Delegations** — `contract_call` — Enforce delegation scopes, expiries, and intent envelopes.

## Offline-ready partner paths

- **Lido** — prepared_contract_call
- **ENS** — prepared_contract_call
- **MetaMask Delegations** — prepared_contract_call

## Live-only partner blockers

- **Venice**: VENICE_API_KEY, VENICE_CHAT_COMPLETIONS_URL, VENICE_MODEL — https://docs.venice.ai/
- **SelfProtocol**: SELF_PROTOCOL_API_KEY, SELF_VERIFICATION_URL — https://docs.self.xyz/
- **Uniswap**: UNISWAP_API_KEY, UNISWAP_QUOTE_URL — https://developers.uniswap.org/
- **Octant**: OCTANT_SIGNAL_URL — https://octant.app/

## Highest-sensitivity actions

- `venice_private_analysis` — Venice — Use Venice for a bounded action in this repo.
- `selfprotocol_zk_verify` — SelfProtocol — Use SelfProtocol for a bounded action in this repo.
- `metamask_delegations_delegate_scope` — MetaMask Delegations — Use MetaMask Delegations for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for PrivateDecisionRegistry.
- Run python3 scripts/run_agent.py to produce a dry run for venice_private_desk.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
