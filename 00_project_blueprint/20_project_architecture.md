# Project Architecture

```text
Synthetic raw CSV (immutable)
        |
        v
Schema/profile + validation logs
        |
        v
Clean processed CSV -----------------> SQLite normalized tables
        |                                      |
        v                                      v
Python EDA + statistics <-------- metric reconciliation
        |
        v
Findings + Placement Readiness Index
        |
        v
Power BI dashboard + portfolio documentation
```

## Data authority and lineage

- Raw CSV is evidence of the generated source, never edited in place after freezing at CHECKPOINT-01.
- Transformation code and validation report create the processed CSV, the analytical source of truth.
- SQLite, notebooks, readiness export, and Power BI are downstream consumers; they must be regenerated when processed data changes.
- Dashboard numbers are never manually adjusted. Trace a mismatch upstream through DAX, derived exports, processed data, transformations, then raw data.

