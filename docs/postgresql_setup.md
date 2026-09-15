# PlacementLens — Phase 3 Part 3: PostgreSQL Database Setup & Data Loading

## 1. Executive Summary & Infrastructure Setup

This document specifies the database setup, schema architecture, performance indexing, data loading pipeline, security controls, and source-to-database validation for **Phase 3 Part 3** of **PlacementLens**.

The database layer serves as the primary analytical engine for SQL queries, CTEs, window functions, and cross-validation against Python EDA results in subsequent parts (P3-P4 and P3-P5).

---

## 2. PostgreSQL Schema Architecture

The database table [`public.students`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/sql/01_create_schema.sql) was instantiated with the following 20 canonical attributes, primary key, and domain CHECK constraints:

```sql
CREATE TABLE IF NOT EXISTS public.students (
    student_id          VARCHAR(5)   NOT NULL PRIMARY KEY,
    age                 INTEGER      NOT NULL CHECK (age >= 18 AND age <= 30),
    gender              VARCHAR(20)  NOT NULL CHECK (gender IN ('Female', 'Male', 'Non-binary', 'Prefer not to say')),
    branch              VARCHAR(10)  NOT NULL CHECK (branch IN ('CSE', 'IT', 'ECE', 'EEE', 'ME', 'CE')),
    cgpa                NUMERIC(4,2) NOT NULL CHECK (cgpa >= 0.00 AND cgpa <= 10.00),
    internships         INTEGER      NOT NULL CHECK (internships >= 0),
    projects            INTEGER      NOT NULL CHECK (projects >= 0),
    coding_score        NUMERIC(5,2) NOT NULL CHECK (coding_score >= 0.00 AND coding_score <= 100.00),
    aptitude_score      NUMERIC(5,2) NOT NULL CHECK (aptitude_score >= 0.00 AND aptitude_score <= 100.00),
    communication_score NUMERIC(5,2) NOT NULL CHECK (communication_score >= 0.00 AND communication_score <= 100.00),
    python_skill        INTEGER      NOT NULL CHECK (python_skill IN (0, 1)),
    sql_skill           INTEGER      NOT NULL CHECK (sql_skill IN (0, 1)),
    excel_skill         INTEGER      NOT NULL CHECK (excel_skill IN (0, 1)),
    power_bi_skill      INTEGER      NOT NULL CHECK (power_bi_skill IN (0, 1)),
    dsa_skill           INTEGER      NOT NULL CHECK (dsa_skill IN (0, 1)),
    cloud_skill         INTEGER      NOT NULL CHECK (cloud_skill IN (0, 1)),
    cybersecurity_skill INTEGER      NOT NULL CHECK (cybersecurity_skill IN (0, 1)),
    placed              BOOLEAN      NOT NULL,
    company_type        VARCHAR(20)  NULL CHECK (company_type IN ('Product', 'Service', 'Startup', 'Other') OR company_type IS NULL),
    package_lpa         NUMERIC(6,2) NULL CHECK (package_lpa >= 0.00 OR package_lpa IS NULL),

    CONSTRAINT chk_placed_null_semantics CHECK (
        (placed = TRUE  AND company_type IS NOT NULL AND package_lpa IS NOT NULL) OR
        (placed = FALSE AND company_type IS NULL     AND package_lpa IS NULL)
    )
);
```

---

## 3. Performance Indexing Strategy

Four performance indexes were created via [`sql/02_create_indexes.sql`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/sql/02_create_indexes.sql) to optimize downstream analytical queries:

1. `idx_students_branch`: B-Tree index on `branch` for branch-wise aggregation queries.
2. `idx_students_placed`: B-Tree index on `placed` status for cohort filtering.
3. `idx_students_placed_company`: Composite B-Tree index on `(placed, company_type)` for compensation breakdowns.
4. `idx_students_branch_placed`: Composite B-Tree index on `(branch, placed)` for branch placement rate CTEs.

---

## 4. Reproducible Data Loading Pipeline

The data ingestion script [`scripts/load_postgres.py`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/scripts/load_postgres.py) executes a deterministic 8-step pipeline:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   REPRODUCIBLE DATA LOADING PIPELINE                    │
├────────────────────────────────────────────────────────────────────────┤
│ Step 1: Pre-load Clean & Raw Dataset MD5 Hash Check Verification       │
│ Step 2: PostgreSQL Connection / Architecture Engine Driver Handshake   │
│ Step 3: Atomic Table DDL Execution & Index Setup                       │
│ Step 4: Idempotent Table Truncation (Prevent Duplicate Appends)        │
│ Step 5: Bulk Ingestion of 1,500 Frozen Clean Records                   │
│ Step 6: Transaction Commit (Atomic Transaction)                        │
│ Step 7: Source-to-Database Data Quality Audit & Metric Verification    │
│ Step 8: Post-load Clean & Raw Dataset MD5 Hash Immutability Verification│
└────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Source-to-Database Audit Metrics

| Metric Category | Source CSV Baseline | Loaded Database Table | Variance | Status |
| :--- | :---: | :---: | :---: | :---: |
| **Total Physical Rows** | 1,500 | 1,500 | 0 | **`PASS`** |
| **Unique Student IDs** | 1,500 (`S0001`–`S1500`) | 1,500 (`S0001`–`S1500`) | 0 | **`PASS`** |
| **Total DDL Columns** | 20 | 20 | 0 | **`PASS`** |
| **Placed Students** | 950 | 950 | 0 | **`PASS`** |
| **Unplaced Students** | 550 | 550 | 0 | **`PASS`** |
| **Placement Rate (%)** | 63.33% | 63.33% | 0.00% | **`PASS`** |
| **Unplaced Package NULL Count** | 550 | 550 | 0 | **`PASS`** |
| **Placed Package Non-Null Count** | 950 | 950 | 0 | **`PASS`** |
| **Binary Skill Flags (0 or 1)** | 100% | 100% | 0 | **`PASS`** |

---

## 6. Security & Credential Protection

- **Environment Variable Abstraction:** Connection parameters use `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, `PGDATABASE`.
- **Zero Secrets Logging:** No passwords, connection strings, or environment secrets are exposed in logs or audit CSVs.
- **Git Safety:** Database files and environment configurations are excluded from raw version control exposure.

---

## 7. Audit Deliverables Register

All 11 audit deliverables generated in [`outputs/postgresql/`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/postgresql):
1. [`01_database_connection_check.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/postgresql/01_database_connection_check.csv)
2. [`02_source_database_comparison.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/postgresql/02_source_database_comparison.csv)
3. [`03_postgresql_schema_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/postgresql/03_postgresql_schema_validation.csv)
4. [`04_postgresql_data_quality_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/postgresql/04_postgresql_data_quality_validation.csv)
5. [`05_postgresql_null_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/postgresql/05_postgresql_null_validation.csv)
6. [`06_postgresql_category_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/postgresql/06_postgresql_category_validation.csv)
7. [`07_postgresql_numeric_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/postgresql/07_postgresql_numeric_validation.csv)
8. [`08_postgresql_placement_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/postgresql/08_postgresql_placement_validation.csv)
9. [`09_postgresql_skill_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/postgresql/09_postgresql_skill_validation.csv)
10. [`10_postgresql_load_summary.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/postgresql/10_postgresql_load_summary.csv)
11. [`11_postgresql_run_log.md`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/postgresql/11_postgresql_run_log.md)

---

## 8. Final Checkpoint Decision

`CHECKPOINT-03-PART-03 PASS — READY FOR P3-P4`
