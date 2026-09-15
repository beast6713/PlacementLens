# Project Architecture

```text
Synthetic Raw CSV (immutable: data/raw/placementlens_students_raw.csv)
        |
        v
Pandas Ingestion, Profiling & Validation Engine
        |
        v
Clean Processed CSV (data/processed/placementlens_students_clean.csv)
        |                                       |
        v                                       v
PostgreSQL Primary Database (placementlens)   SQLite Backup Engine (placementlens.db)
        |                                       |
        v                                       v
SQL Analytics & Query Catalog (AQ-001 to 017) <--- Metric Reconciliation
        |
        v
Findings + Placement Readiness Index Export
        |
        v
Power BI Interactive Dashboard + Portfolio Documentation
```

## Data Authority and Lineage

- **Raw CSV (`data/raw/placementlens_students_raw.csv`):** Evidence of unconstrained synthetic generation (Seed 42, v1.0). Intentionally permits controlled raw defects. Immutable once frozen.
- **Clean CSV (`data/processed/placementlens_students_clean.csv`):** Result of Pandas validation and cleaning routines; analytical source file.
- **PostgreSQL Database (`placementlens.students`):** Primary canonical relational storage engine (`v1.0`). Enforces DDL data types, primary keys, CHECK constraints, and conditional placement rules.
- **SQLite Database (`placementlens.db`):** Secondary lightweight backup database mirroring PostgreSQL schema structure.
- **Downstream Analytics & BI:** Jupyter notebooks, SQL query catalog, Placement Readiness Index exports, and Power BI dashboards consume the clean PostgreSQL/Processed layer. Trace any metric mismatch upstream: Power BI $\rightarrow$ DAX/SQL $\rightarrow$ PostgreSQL $\rightarrow$ Processed CSV $\rightarrow$ Raw CSV.
