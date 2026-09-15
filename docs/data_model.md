# PlacementLens — Final Data Model & Schema Specification

**Schema Version:** `v1.0`  
**Database System:** PostgreSQL (Primary Analytical Storage) / SQLite (Backup Compatibility)  
**Data Grain:** ONE ROW = ONE STUDENT (`student_id` PK)

---

## 1. Executive Summary & Analytical Scope

This document specifies the implementation-ready data model and PostgreSQL database schema for **PlacementLens**. 

The schema is designed to store, manage, and query 1,500 synthetic student records to answer 17 core Analytical Questions (AQ-001 to AQ-017) spanning academic performance, technical skills, assessment test scores, practical experience, placement outcomes, and compensation packages.

---

## 2. Data Grain & Entity Normalization Evaluation

### 2.1 Primary Data Grain
- **Grain Definition:** One row per student at a single placement-cycle snapshot.
- **Canonical Identifier:** `student_id` (Format: `S0001`–`S1500`), guaranteed unique and non-null.

### 2.2 Normalization Evaluation: Option A vs. Option B

During Phase 1 Part 2, two candidate data model architectures were evaluated:

* **Option A: Single Canonical Analytical Table (`students`)**  
  All 20 attributes (demographics, academics, 7 skill flags, scores, counts, placement outcome, and package) are stored in a single wide table at the student grain (`student_id` PK).
* **Option B: Normalized 4-Table Relational Model**  
  Splitting the schema into four tables: `students` (demographics/academics), `student_skills` (skills), `student_experience` (counts), and `student_placement` (placement outcome/package), linked via 1:1 Foreign Keys on `student_id`.

#### Decision: **Option A (Single Canonical Analytical Table) is Selected.**

#### Rationale & Trade-off Analysis:
1. **Strict 1:1 Grain:** Every student has exactly one record at the placement snapshot—one CGPA, one branch, one set of assessment scores, one set of skill flags, one placement status, and one package. There are no 1:N array attributes (e.g. historical attempts or multiple job offers) in the current project scope.
2. **Elimination of Join Overhead:** Option B would split a lightweight 20-column record across 4 tables with identical 1:1 primary keys. Querying basic student profiles or calculating multi-variable aggregations in SQL would require 3 mandatory `JOIN`s per query, adding unnecessary complexity to a 1-week BI project.
3. **Power BI & DAX Optimization:** Power BI tabular models perform with maximum efficiency when consuming flat analytical fact tables or clean star-schema models. Option A avoids complex multi-directional 1:1 relationship modeling in DAX.
4. **Data Ingestion & Reproducibility:** Option A simplifies Python pandas ingestion, PostgreSQL bulk loading (`COPY`), and validation checks while preserving 100% data integrity.

*Note for BI Extensibility:* While `students` serves as the primary analytical table, PostgreSQL views or Power BI DAX dimension references (`dim_branch`, `dim_company_type`) can be constructed dynamically without altering the underlying physical storage layer.

---

## 3. PostgreSQL Database Schema Specification

### 3.1 Environment Target
- **Database Name:** `placementlens`
- **Schema Name:** `public`
- **Primary Table:** `public.students`
- **DDL Artifact Path:** `sql/01_schema_ddl.sql`

### 3.2 Field-by-Field Technical Data Dictionary (`v1.0`)

| Column Name | PostgreSQL Type | Nullable | Default | Constraints | Description | Analytical Purpose |
|---|---|---|---|---|---|---|
| `student_id` | `VARCHAR(10)` | `NOT NULL` | None | `PRIMARY KEY`, `CHECK (student_id ~ '^S[0-9]{4}$')` | Synthetic student identifier | Primary key / student grain identifier |
| `age` | `SMALLINT` | `NOT NULL` | None | `CHECK (age BETWEEN 18 AND 25)` | Student age at snapshot | Secondary demographic exploration |
| `gender` | `VARCHAR(20)` | `NOT NULL` | None | `CHECK (gender IN ('Female', 'Male', 'Non-binary', 'Prefer not to say'))` | Demographic category | Aggregate exploratory visualization (non-screening) |
| `branch` | `VARCHAR(10)` | `NOT NULL` | None | `CHECK (branch IN ('CSE', 'IT', 'ECE', 'EEE', 'ME', 'CE'))` | Academic department | Branch-level cohort comparison & slicing |
| `cgpa` | `NUMERIC(4,2)` | `NOT NULL` | None | `CHECK (cgpa >= 0.00 AND cgpa <= 10.00)` | Cumulative GPA | Academic baseline performance analysis |
| `coding_score` | `NUMERIC(5,2)` | `NOT NULL` | None | `CHECK (coding_score >= 0.00 AND coding_score <= 100.00)` | Coding test score | Technical assessment capability analysis |
| `aptitude_score` | `NUMERIC(5,2)` | `NOT NULL` | None | `CHECK (aptitude_score >= 0.00 AND aptitude_score <= 100.00)` | Aptitude test score | Quantitative reasoning capability analysis |
| `communication_score` | `NUMERIC(5,2)` | `NOT NULL` | None | `CHECK (communication_score >= 0.00 AND communication_score <= 100.00)` | Communication test score | Soft skill capability analysis |
| `internships` | `SMALLINT` | `NOT NULL` | `0` | `CHECK (internships >= 0 AND internships <= 5)` | Internship count | Industry exposure analysis |
| `projects` | `SMALLINT` | `NOT NULL` | `0` | `CHECK (projects >= 0 AND projects <= 10)` | Project count | Practical application analysis |
| `python_skill` | `SMALLINT` | `NOT NULL` | `0` | `CHECK (python_skill IN (0, 1))` | Python capability flag | Technical skill prevalence & readiness |
| `sql_skill` | `SMALLINT` | `NOT NULL` | `0` | `CHECK (sql_skill IN (0, 1))` | SQL capability flag | Technical skill prevalence & readiness |
| `excel_skill` | `SMALLINT` | `NOT NULL` | `0` | `CHECK (excel_skill IN (0, 1))` | Excel capability flag | Technical skill prevalence & readiness |
| `power_bi_skill` | `SMALLINT` | `NOT NULL` | `0` | `CHECK (power_bi_skill IN (0, 1))` | Power BI capability flag | Technical skill prevalence & readiness |
| `dsa_skill` | `SMALLINT` | `NOT NULL` | `0` | `CHECK (dsa_skill IN (0, 1))` | DSA capability flag | Technical skill prevalence & readiness |
| `cloud_skill` | `SMALLINT` | `NOT NULL` | `0` | `CHECK (cloud_skill IN (0, 1))` | Cloud capability flag | Technical skill prevalence & readiness |
| `cybersecurity_skill` | `SMALLINT` | `NOT NULL` | `0` | `CHECK (cybersecurity_skill IN (0, 1))` | Cybersecurity capability flag | Technical skill prevalence & readiness |
| `placed` | `SMALLINT` | `NOT NULL` | None | `CHECK (placed IN (0, 1))` | **Target Variable:** Placement status | Primary placement outcome classification |
| `company_type` | `VARCHAR(20)` | `NULLABLE` | `NULL` | `CHECK (company_type IS NULL OR company_type IN ('Product', 'Service', 'Startup', 'Other'))` | Recruiter company tier | Employer segment distribution analysis |
| `package_lpa` | `NUMERIC(4,2)` | `NULLABLE` | `NULL` | `CHECK (package_lpa IS NULL OR (package_lpa > 0.00 AND package_lpa <= 50.00))` | Annual CTC compensation | Placement compensation & salary analysis |

---

## 4. Integrity Constraints & NULL Policy

### 4.1 Conditional Placement & Compensation Rule
To prevent logical contradictions (e.g. unplaced students having packages, or placed students missing recruiter data), the PostgreSQL table enforces a multi-column table check constraint:

```sql
CONSTRAINT chk_placement_compensation_logic CHECK (
    (placed = 0 AND company_type IS NULL AND package_lpa IS NULL)
    OR
    (placed = 1 AND company_type IS NOT NULL AND package_lpa IS NOT NULL)
)
```

### 4.2 Explicit NULL Semantics
- `NULL`: Represents **Non-Applicability**. Specifically, `package_lpa` and `company_type` MUST be `NULL` for unplaced students (`placed = 0`).
- `0`: Represents a **Valid Quantitative Zero** (e.g., `internships = 0` means zero internships; `python_skill = 0` means Python skill is absent).
- **Prohibition:** Unplaced students are **never** assigned `package_lpa = 0.00`.

---

## 5. Raw Data vs. Canonical Database Coexistence

PlacementLens maintains strict separation between unconstrained raw data ingestion and canonical database storage:

1. **Raw CSV Layer (`data/raw/placementlens_students_raw.csv`):** Unconstrained text format. Intentionally permits controlled raw defects (whitespace, lowercase branch names like `"cse"`, string representation of binary flags like `"Yes"`) to test Phase 2 cleaning pipelines.
2. **Canonical PostgreSQL Database (`placementlens.students`):** Strictly typed, clean, validated schema with enforced CHECK constraints and primary key uniqueness. Populated only after Phase 2 Pandas cleaning.

---

## 6. Compatibility Evaluations

### 6.1 Analytical Questions Support (AQ-001 to AQ-017)
The `students` schema directly supports all 17 Analytical Questions in SQL:
- **AQ-001 & AQ-002 (Placement Rates):** `AVG(placed::numeric) * 100 GROUP BY branch`.
- **AQ-003 & AQ-004 (CGPA Analysis):** `WIDTH_BUCKET(cgpa, 0, 10, 5)` and score aggregations by `placed`.
- **AQ-007 & AQ-008 (Skill Analysis):** Aggregations across the 7 binary skill flags (`SUM(python_skill)`, `AVG(placed) WHERE sql_skill = 1`).
- **AQ-012 & AQ-013 (Package Distribution):** `PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY package_lpa)` grouped by `branch` and `company_type`.

### 6.2 Power BI Compatibility
- The flat tabular structure maps cleanly into Power BI Desktop.
- Binary flags (`0`/`1`) work seamlessly with DAX measures (e.g. `DIVIDE(CALCULATE(COUNTROWS(students), students[placed] = 1), COUNTROWS(students))`).
- DAX logical dimensions (`Branch`, `Company Type`) can be used directly as visual slicers.

### 6.3 SQLite Backup Compatibility
An equivalent SQLite DDL schema is provided in `sql/01_sqlite_schema_ddl.sql` using SQLite-compatible types (`INTEGER` for flags/scores, `REAL` for CGPA/package), ensuring fallback compatibility without compromising the primary PostgreSQL architecture.

---

## 7. Schema Review Answers (20 Mandatory Verification Questions)

1. **What is the grain of the data?** One row per synthetic student record at a single placement snapshot.
2. **What uniquely identifies a student?** `student_id` (`S0001`–`S1500`).
3. **Which table represents the core student entity?** `public.students`.
4. **How are technical skills represented?** 7 binary integer flags (`0` = absent, `1` = present) stored directly in `students`.
5. **How are internships and projects represented?** Integer count fields (`internships` ∈ [0, 5], `projects` ∈ [0, 10]).
6. **How is placement represented?** Binary integer flag `placed` (`1` = Placed, `0` = Unplaced).
7. **How is package represented?** Numeric float `package_lpa` in Lakhs Per Annum (e.g. `8.50`).
8. **How is "not placed" represented?** `placed = 0`, with `company_type = NULL` and `package_lpa = NULL`.
9. **What does NULL mean?** Attribute not applicable (specifically compensation fields for unplaced students).
10. **What does 0 mean?** Valid numeric zero (0 internships, 0 projects, or absent skill flag `0`).
11. **What does FALSE mean?** Absent skill flag or unplaced outcome (represented numerically as `0`).
12. **What constraints prevent impossible data?** Primary key uniqueness, numerical range CHECK constraints, categorical allowed-set checks, and table-level conditional check `chk_placement_compensation_logic`.
13. **How will controlled raw defects coexist with the canonical schema?** Defects exist only in `data/raw/ placementlens_students_raw.csv`. The PostgreSQL schema accepts only clean data post-Phase 2 validation.
14. **Can the schema answer every analytical question?** Yes, directly supports AQ-001 through AQ-017.
15. **Can Power BI consume it cleanly?** Yes, flat tabular structure allows direct DAX aggregations and slicer filters.
16. **Can PostgreSQL support the required SQL analysis?** Yes, full support for window functions, CTEs, GROUP BY, and percentiles.
17. **Can Python generate 1,500 records against it?** Yes, perfectly aligned with Pandas DataFrame generation.
18. **Is any table unnecessary?** Splitting into 4 separate 1:1 tables was evaluated and rejected as unnecessary complexity.
19. **Is any field unnecessary?** No, all 20 fields directly map to approved business requirements and analytical priorities.
20. **Does the schema introduce data leakage?** No, no target-derived score or predictor variable is present.
