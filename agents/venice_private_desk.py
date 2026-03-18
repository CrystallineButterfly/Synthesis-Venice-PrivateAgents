"""Project-specific context for Shadow Treasury Desk."""

        from __future__ import annotations

        PROJECT_CONTEXT = {
    "project_name": "Shadow Treasury Desk",
    "track": "Venice Private Agents",
    "pitch": "A private reasoning desk that keeps sensitive treasury, governance, and grant analysis off public rails while still producing verifiable downstream actions.",
    "overlap_targets": [
        "SelfProtocol",
        "Lido stETH Treasury",
        "Uniswap Agentic Finance",
        "ENS",
        "Octant",
        "MetaMask Delegations"
    ],
    "goals": [
        "discover a bounded opportunity",
        "plan a dry-run-first action",
        "verify receipts and proofs"
    ]
}


        def seed_targets() -> list[str]:
            """Return the first batch of overlap targets for planning."""
            return list(PROJECT_CONTEXT['overlap_targets'])
