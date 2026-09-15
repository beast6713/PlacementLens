# PlacementLens

PlacementLens is a portfolio-grade student placement analytics and business-intelligence project. It will analyze **associations** between student preparation indicators and placement outcomes; it is not a causal study, automated hiring system, or placement prediction product.

## Current status

- Current phase: **Phase 0 — Project Blueprint and Initialization**
- Latest valid checkpoint: **CHECKPOINT-00 (PASS — Phase 0 validated)**
- Implementation status: **not started by design**
- Resume here: [`00_project_blueprint/30_phase_0_completion_report.md`](00_project_blueprint/30_phase_0_completion_report.md)

## Recovery-first handoff

Any new contributor must read these files, in order, before changing the project:

1. `00_project_blueprint/30_phase_0_completion_report.md`
2. `00_project_blueprint/23_phase_checkpoints.md`
3. `00_project_blueprint/29_change_log.md`
4. `00_project_blueprint/25_error_recovery_strategy.md`
5. The blueprint document for the phase they will execute.

Begin Phase 1 only from CHECKPOINT-00 and only with the Day 1 work defined in the blueprint. Record every significant scope or requirement change in the change log, then update the affected checkpoint.

## Planned structure

```text
PlacementLens/
├── 00_project_blueprint/  # Approved source of truth
├── data/raw/              # Immutable acquired/generated source data
├── data/processed/        # Validated analysis-ready data
├── notebooks/             # Ordered, reproducible notebooks
├── sql/                   # Schema, loading, and analytical queries
├── dashboard/             # Power BI source and dashboard documentation
├── docs/                  # Findings, handoff, portfolio documentation
├── tests/                 # Reproducible validation checks
└── outputs/               # Generated, non-authoritative artifacts
```

## Guardrails

- No real personal data or automated hiring decisions.
- Synthetic data, if used, must be disclosed everywhere it is presented.
- Do not report causal conclusions, fabricated results, or unvalidated readiness predictions.
- Validate upstream data before altering downstream outputs.
