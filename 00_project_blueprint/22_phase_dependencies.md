# Phase Dependencies

| Phase | Depends on | Required output before next phase |
|---|---|---|
| 0 — Blueprint | None | Approved requirements, scope, schema, architecture, validation, recovery plan (CHECKPOINT-00). |
| 1 — Data Foundation | CHECKPOINT-00 | Frozen raw synthetic CSV, source/generator note, schema/profile report (CHECKPOINT-01). |
| 2 — Cleaning & Validation | CHECKPOINT-01 | Validated processed CSV, quality report, test results (CHECKPOINT-02). |
| 3 — Python EDA & SQL | CHECKPOINT-02 | EDA/statistical outputs, SQLite database, query catalog and reconciliation (CHECKPOINT-03). |
| 4 — Insights & Readiness | CHECKPOINT-03 | Evidence-backed findings, PRI and gap outputs, limitations/recommendations (CHECKPOINT-04). |
| 5 — Dashboard & Portfolio | CHECKPOINT-04 | Validated three-page dashboard, documentation, reproducibility evidence (CHECKPOINT-05). |

No phase may consume a predecessor output that has not passed its checkpoint. A material upstream change invalidates downstream checkpoints until revalidated.

