# Validation Strategy

| Phase | Validation | Pass condition |
|---|---|---|
| 0 | Blueprint review | All 30 documents complete, scope/schema/architecture consistent, recovery and DoD defined. |
| 1 | Dataset/schema test | File exists; 1,500 rows documented; required columns, types, and generator/source note present. |
| 2 | Data-quality tests | All DQ hard rules pass on processed export; reconciliation and outlier investigation recorded. |
| 3 | Analytical reconciliation | SQL executes; key metrics equal Python outputs on same data/version; all AQs addressed. |
| 4 | Insight/readiness review | Every finding has evidence and limitation; PRI bounds/formula reproduce; no causal/predictive claims. |
| 5 | BI/portfolio QA | Dashboard measures and filters reconcile, layout is understandable, documentation supports a clean rerun. |

## Cross-system checks

For totals, placed count, placement rate, branch rates, and placed-package statistics, retain exact raw values from Python and SQL. Compare Power BI values at the same filter context. A mismatch is a defect until a documented rounding difference is proved.

## Evidence location

Store test outputs in `tests/`, phase reports in `docs/`, generated figures/tables in `outputs/`, and reference them from the applicable checkpoint. Never use screenshots as the sole validation evidence.

