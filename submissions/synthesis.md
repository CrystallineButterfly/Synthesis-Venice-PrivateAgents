# Shadow Treasury Desk

- **Repo:** https://github.com/CrystallineButterfly/Synthesis-Venice-PrivateAgents
- **Primary track:** Venice Private Agents
- **Overlap targets:** SelfProtocol, Lido stETH Treasury, Uniswap Agentic Finance, ENS, Octant, MetaMask Delegations
- **Primary contract:** PrivateDecisionRegistry
- **Primary operator module:** venice_private_desk
- **Live TxIDs:** PENDING
- **ERC-8004 registrations:** PENDING
- **Demo link:** docs/demo_video_script.md

A private reasoning desk that keeps sensitive treasury, governance, and grant analysis off public rails while still producing verifiable downstream actions.

## Track evidence

- `artifacts/onchain_intents/lido_yield_route.json`
- `artifacts/onchain_intents/ens_ens_publish.json`
- `artifacts/onchain_intents/metamask_delegations_delegate_scope.json`

## Latest verification

```json
{
  "status": "verified",
  "project_name": "Shadow Treasury Desk",
  "track": "Venice Private Agents",
  "plan_id": "0x5f3973530e4c38ed4577915d4d16466d2aecc8b73985323d7cd18bbbd8c434ba",
  "simulation_hash": "0xfdd1cac854a06cb1c13acbf22af9d243ea53e5d69577f7e3acac81e5c9893dc1",
  "execution_status": "offline_prepared",
  "tx_ids": [],
  "artifact_paths": [
    "artifacts/onchain_intents/lido_yield_route.json",
    "artifacts/onchain_intents/ens_ens_publish.json",
    "artifacts/onchain_intents/metamask_delegations_delegate_scope.json"
  ],
  "partner_statuses": {
    "Venice": "awaiting_credentials",
    "SelfProtocol": "awaiting_credentials",
    "Lido": "prepared_contract_call",
    "Uniswap": "awaiting_credentials",
    "ENS": "prepared_contract_call",
    "Octant": "awaiting_credentials",
    "MetaMask Delegations": "prepared_contract_call"
  },
  "created_at": "2026-03-19T03:52:21+00:00"
}
```
