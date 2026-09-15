# Data Dictionary & Canonical PostgreSQL Schema (`v1.0`)

## Overview

This Data Dictionary defines the canonical PostgreSQL data model (`v1.0`) for **PlacementLens**. It specifies the exact SQL data types, nullability, default values, key constraints, CHECK rules, business meanings, example values, and validation rules for `public.students`.

---

## Technical PostgreSQL DDL Schema Specification

| Column Name | Class | PostgreSQL Type | Nullable | Default | Constraints | Business Meaning | Example | Validation Rule |
|---|---|---|---|---|---|---|---|---|
| `student_id` | A. Identifier | `VARCHAR(10)` | No | None | `PRIMARY KEY`, `CHECK (student_id ~ '^S[0-9]{4}$')` | Synthetic student identifier | `S0001` | Unique, non-null, regex `^S[0-9]{4}$` |
| `age` | B. Demographic | `SMALLINT` | No | None | `CHECK (age BETWEEN 18 AND 25)` | Student age at snapshot | `21` | Integer in range [18, 25] |
| `gender` | B. Demographic | `VARCHAR(20)` | No | None | `CHECK (gender IN ('Female', 'Male', 'Non-binary', 'Prefer not to say'))` | Demographic grouping | `Female` | Allowed categorical set |
| `branch` | C. Academic | `VARCHAR(10)` | No | None | `CHECK (branch IN ('CSE', 'IT', 'ECE', 'EEE', 'ME', 'CE'))` | Academic department | `CSE` | Allowed categorical set |
| `cgpa` | C. Academic | `NUMERIC(4,2)` | No | None | `CHECK (cgpa >= 0.00 AND cgpa <= 10.00)` | Cumulative Grade Point Average | `8.25` | Numeric float in range [0.00, 10.00] |
| `coding_score` | E. Assessment | `NUMERIC(5,2)` | No | None | `CHECK (coding_score >= 0.00 AND coding_score <= 100.00)` | Coding test score | `76.50` | Numeric float in range [0.00, 100.00] |
| `aptitude_score` | E. Assessment | `NUMERIC(5,2)` | No | None | `CHECK (aptitude_score >= 0.00 AND aptitude_score <= 100.00)` | Aptitude test score | `68.00` | Numeric float in range [0.00, 100.00] |
| `communication_score` | E. Assessment | `NUMERIC(5,2)` | No | None | `CHECK (communication_score >= 0.00 AND communication_score <= 100.00)` | Communication test score | `72.00` | Numeric float in range [0.00, 100.00] |
| `internships` | F. Experience | `SMALLINT` | No | `0` | `CHECK (internships >= 0 AND internships <= 5)` | Internship count | `1` | Non-negative integer ≤ 5 |
| `projects` | F. Experience | `SMALLINT` | No | `0` | `CHECK (projects >= 0 AND projects <= 10)` | Project count | `3` | Non-negative integer ≤ 10 |
| `python_skill` | D. Technical Skill | `SMALLINT` | No | `0` | `CHECK (python_skill IN (0, 1))` | Python capability flag | `1` | Binary integer ∈ {0, 1} |
| `sql_skill` | D. Technical Skill | `SMALLINT` | No | `0` | `CHECK (sql_skill IN (0, 1))` | SQL capability flag | `1` | Binary integer ∈ {0, 1} |
| `excel_skill` | D. Technical Skill | `SMALLINT` | No | `0` | `CHECK (excel_skill IN (0, 1))` | Excel capability flag | `1` | Binary integer ∈ {0, 1} |
| `power_bi_skill` | D. Technical Skill | `SMALLINT` | No | `0` | `CHECK (power_bi_skill IN (0, 1))` | Power BI capability flag | `0` | Binary integer ∈ {0, 1} |
| `dsa_skill` | D. Technical Skill | `SMALLINT` | No | `0` | `CHECK (dsa_skill IN (0, 1))` | DSA capability flag | `1` | Binary integer ∈ {0, 1} |
| `cloud_skill` | D. Technical Skill | `SMALLINT` | No | `0` | `CHECK (cloud_skill IN (0, 1))` | Cloud capability flag | `0` | Binary integer ∈ {0, 1} |
| `cybersecurity_skill` | D. Technical Skill | `SMALLINT` | No | `0` | `CHECK (cybersecurity_skill IN (0, 1))` | Cybersecurity capability flag | `0` | Binary integer ∈ {0, 1} |
| `placed` | G. Outcome | `SMALLINT` | No | None | `CHECK (placed IN (0, 1))` | **Target Variable:** Placement outcome | `1` | Binary integer ∈ {0, 1} |
| `company_type` | H. Compensation | `VARCHAR(20)` | Conditionally | `NULL` | `CHECK (company_type IS NULL OR company_type IN ('Product', 'Service', 'Startup', 'Other'))` | Recruiter company tier | `Product` | Required iff `placed=1`; `NULL` iff `placed=0` |
| `package_lpa` | H. Compensation | `NUMERIC(4,2)` | Conditionally | `NULL` | `CHECK (package_lpa IS NULL OR (package_lpa > 0.00 AND package_lpa <= 50.00))` | Compensation package (LPA) | `8.50` | Required iff `placed=1` (>0.00 and ≤50.00); `NULL` iff `placed=0` |

---

## Multi-Column Table Check Constraint

The table enforces logical consistency between placement outcome and compensation fields:

```sql
CONSTRAINT chk_placement_compensation_logic CHECK (
    (placed = 0 AND company_type IS NULL AND package_lpa IS NULL)
    OR
    (placed = 1 AND company_type IS NOT NULL AND package_lpa IS NOT NULL)
)
```

---

## Integrity & NULL Policy Notes

1. **Unplaced Student Rule:** `placed = 0` requires `company_type = NULL` and `package_lpa = NULL`. Unplaced students are never assigned `package_lpa = 0.00`.
2. **Placed Student Rule:** `placed = 1` requires non-null `company_type` from allowed set and positive `package_lpa` in (0.00, 50.00].
3. **Data Privacy Notice:** `student_id` is synthetic (`S0001`–`S1500`) with zero real student PII. `package_lpa` is synthetic illustrative compensation data.
