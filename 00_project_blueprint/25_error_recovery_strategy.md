# Error Recovery Strategy

## Mandatory recovery procedure

1. Stop progression and preserve the failing command, file version, error, and observed impact.
2. Identify the affected phase and the most recent `PASS` checkpoint in `23_phase_checkpoints.md`.
3. Map the defect to lineage: raw data → transformations → processed data → SQLite/notebooks → readiness → DAX/dashboard/docs.
4. Determine the earliest root cause; do not patch a downstream result to conceal it.
5. Correct the root cause in the authorized source artifact and record the change in `29_change_log.md`.
6. Re-run the affected phase validation and every downstream validation.
7. Update or invalidate checkpoints as appropriate, including exact files and results.
8. Resume only after the affected checkpoint is `PASS` again.

## Examples

| Symptom | Investigation path | Correct recovery |
|---|---|---|
| Power BI KPI differs from Python | DAX measure → imported export → processed CSV → cleaning → raw data | Fix earliest mismatch, refresh all downstream artifacts, reconcile. |
| SQL placement rate differs | query grain/join → table load → clean data → Python metric | Fix join/filter/load logic; retain cross-check. |
| Invalid processed values | transform logic → raw-data treatment → data dictionary | Correct transform or documented exclusion; rerun quality tests. |
| Finding lacks support | evidence link → calculation/query → data lineage | Withdraw/rewrite finding; do not search for a convenient chart. |

## Rollback and preservation

Initialize the repository under Git before Phase 1. Then use Git commits/tags at approved checkpoints. Preserve raw data and failed-validation evidence; do not overwrite a last known-good processed export without a versioned replacement. Recovery changes require a change-log entry.
