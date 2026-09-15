# Agent Handoff — PlacementLens

## Exact state at handoff

Phase 0 documentation is complete and CHECKPOINT-00 is PASS. No dataset, code, SQL queries, notebook, database, dashboard, analysis, or model exists. This is intentional. Git is initialized and the blueprint baseline is tagged `checkpoint-00`.

## Required reading order

1. `README.md`
2. `00_project_blueprint/30_phase_0_completion_report.md`
3. `00_project_blueprint/23_phase_checkpoints.md`
4. `00_project_blueprint/25_error_recovery_strategy.md`
5. `00_project_blueprint/10_dataset_specification.md`
6. The blueprint for the active phase.

## First permitted action after approval

Perform Phase 1 only: choose and document a fixed generator seed plus controlled raw-data defect rates, create the synthetic raw CSV specified in the data dictionary, profile it, and seek CHECKPOINT-01. Do not start cleaning, EDA, SQL analytics, PRI, or dashboard work before their prerequisite checkpoints.

## Non-negotiable guardrails

- Synthetic data must remain visibly disclosed.
- Associations are not causal claims.
- PRI is not a placement prediction or hiring tool.
- Trace mismatches upstream; do not manually change downstream values.
- Log all material changes and checkpoint results.
