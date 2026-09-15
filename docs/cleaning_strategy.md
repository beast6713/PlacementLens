# PlacementLens — Phase 2 Cleaning Strategy & Rules Specification

**Phase:** Phase 2 — Data Cleaning & Validation  
**Part:** Part 1 — Cleaning Strategy & Rules Freeze  
**Strategy Version:** `v1.0 Frozen Strategy`  
**Phase 1 Raw Baseline:** `data/raw/placementlens_students_raw.csv` (MD5: `59c04ee15a0112806c510225d8e75779`)  
**Target Processed Deliverable:** `data/processed/placementlens_students_clean.csv`

---

## 1. Executive Summary & Phase 2 Roadmap

Phase 2 transforms the intentionally raw synthetic dataset generated in Phase 1 into an audit-ready, validated clean analytical dataset (`v1.0 Clean`). 

The phase operates across six structured parts:
- **Part 1 (Current):** **Cleaning Strategy & Rules Freeze** — Define exact transformation rules, defect resolution matrices, and validation bounds. Zero raw data modification occurs in Part 1.
- **Part 2:** **Data Ingestion & Cleaning Pipeline** — Build `scripts/clean_dataset.py` ETL architecture.
- **Part 3:** **Duplicate & Structural Cleaning** — Implement `student_id` deduplication (1,505 $\rightarrow$ 1,500 rows).
- **Part 4:** **Missing Values & Data Standardization** — Implement branch/gender/company string normalization, binary skill parsing, and branch-level cohort median imputation for communication scores.
- **Part 5:** **Post-Cleaning Validation & Quality Audit** — Execute `scripts/validate_clean_dataset.py` to audit clean dataset against DDL constraints.
- **Part 6:** **Phase 2 Final Completion & Handoff** — Freeze `data/processed/placementlens_students_clean.csv` and authorize Phase 3 (Python EDA + SQL Analytics).

---

## 2. Raw Dataset Immutability & Data Lineage

- **Raw Baseline Protection:** `data/raw/placementlens_students_raw.csv` is the immutable source of truth (Seed 42, MD5 `59c04ee15a0112806c510225d8e75779`). It will **NEVER** be overwritten, cleaned in place, or modified.
- **Data Lineage Flow:**
  $$\text{data/raw/placementlens\_students\_raw.csv} \xrightarrow{\text{scripts/clean\_dataset.py}} \text{data/processed/placementlens\_students\_clean.csv}$$

---

## 3. Defect-by-Defect Cleaning Strategy & Rules

The Phase 1 baseline contains **95 controlled raw defects** logged in `data/raw/raw_defect_manifest.csv`. Each defect will be resolved using explicit deterministic transformations:

### Defect 1: Duplicate Physical Student Rows (5 Rows)
- **Raw State:** 1,505 physical rows containing 5 tail duplicate rows for student IDs `S0120`, `S0450`, `S0780`, `S1100`, `S1350`.
- **Cleaning Method:** Deduplicate dataframe on key `student_id` keeping the first valid occurrence (`df.drop_duplicates(subset=['student_id'], keep='first')`).
- **Expected Outcome:** Physical rows reduced from 1,505 to exactly 1,500 unique student records.

### Defect 2: Branch Case Inconsistency (25 Rows)
- **Raw State:** 25 rows containing lowercase branch labels (`"cse"`, `"it"`, `"ece"`, `"eee"`, `"me"`, `"ce"`).
- **Cleaning Method:** Apply string trimming and uppercase conversion (`df['branch'].astype(str).str.strip().str.upper()`).
- **Validation:** All branch values must strictly belong to {`CSE`, `IT`, `ECE`, `EEE`, `ME`, `CE`}.

### Defect 3: Company Type Case & Space Inconsistency (15 Placed Rows)
- **Raw State:** 15 placed student rows containing lowercase or space-padded recruiter labels (`"product"`, `"Service "`).
- **Cleaning Method:** Apply string trimming and titlecasing (`df['company_type'].astype(str).str.strip().str.title()`). Preserve `NULL` for unplaced students.
- **Validation:** Placed company types must strictly belong to {`Product`, `Service`, `Startup`, `Other`}.

### Defect 4: Gender Whitespace Padding (20 Rows)
- **Raw State:** 20 rows containing padded whitespace (`" Female "`).
- **Cleaning Method:** Apply string trimming (`df['gender'].astype(str).str.strip()`).
- **Validation:** All gender values must strictly belong to {`Female`, `Male`, `Non-binary`, `Prefer not to say`}.

### Defect 5: String Binary Flag Representation (15 Rows)
- **Raw State:** 15 rows in `python_skill` containing string representations (`"Yes"`, `"No"`).
- **Cleaning Method:** Parse string binary flags to canonical integers (`1` if string $\in$ `['Yes', 'True', '1']` else `0`).
- **Validation:** `python_skill` values must be binary integers $\in \{0, 1\}$.

### Defect 6: Missing Communication Scores (15 Rows)
- **Raw State:** 15 rows containing missing/empty `communication_score` values.
- **Cleaning Method:** Branch-level cohort median imputation. For each record with missing `communication_score`, calculate the median `communication_score` of valid records within the same `branch` and replace the missing value with that branch median.
- **Target Leakage Prevention:** Imputation uses **only** academic branch grouping and valid communication scores. It **NEVER** uses `placed`, `package_lpa`, or `company_type`.

---

## 4. Expected Before vs. After Count Reconciliation

| Data Quality Issue | Target Field | Raw Before Count | Clean Target Count | Resolved Count | Validation Test |
|---|---|---|---|---|---|
| Physical CSV Rows | File Length | 1,505 | 1,500 | 5 | Total rows == 1,500 |
| Duplicate Student IDs | `student_id` | 5 | 0 | 5 | `student_id.nunique() == 1500` |
| Branch Case Defects | `branch` | 25 | 0 | 25 | 100% uppercase in allowed set |
| Company Type Formatting Defects | `company_type` | 15 | 0 | 15 | 100% titlecase in allowed set |
| Gender Whitespace Defects | `gender` | 20 | 0 | 20 | 100% trimmed in allowed set |
| Python Skill String Binary Defects | `python_skill` | 15 | 0 | 15 | 100% binary integer ∈ {0, 1} |
| Missing Communication Scores | `communication_score` | 15 | 0 | 15 | 0 missing values; score ∈ [0, 100] |
| **Total Controlled Defects** | **Dataset Wide** | **95** | **0** | **95** | **100% Defect Resolution Match** |

---

## 5. NULL Semantics & Compensation Linkage Protection

- **Unplaced Compensation Rule:** `package_lpa` and `company_type` MUST be `NULL` for unplaced students (`placed = 0`). Converting `NULL` to `0.00` or `"None"` is strictly prohibited.
- **Placed Compensation Rule:** `package_lpa` MUST be a positive float (>0.00 to 50.00 LPA) and `company_type` MUST be non-null for placed students (`placed = 1`).
- **Quantitative Zero Rule:** `0` represents a valid quantitative zero (0 internships, 0 projects, or absent skill flag). `0` and `NULL` are never used interchangeably.

---

## 6. Transformation Execution Order

The Python ETL cleaning script (`scripts/clean_dataset.py`) will execute transformations in the following strict order:

```text
1. Read data/raw/placementlens_students_raw.csv (Verify MD5 hash)
2. Copy raw DataFrame to in-memory clean working DataFrame
3. Perform Whitespace Trimming (gender, branch, company_type, python_skill)
4. Perform Categorical Case Normalization (branch -> str.upper, company_type -> str.title)
5. Parse String Binary Flags (python_skill -> 1/0 integer)
6. Deduplicate Student Records (subset=['student_id'], keep='first')
7. Impute Missing Communication Scores (Branch-level cohort median)
8. Enforce Data Types & Schema Format (int64, float64, str)
9. Validate Clean DataFrame against Post-Cleaning Rules (VAL-01 to VAL-08)
10. Export data/processed/placementlens_students_clean.csv
11. Export outputs/cleaning/imputation_log.csv
12. Export outputs/cleaning/cleaning_summary_report.md
```

---

## 7. Audit Trail & Pipeline Error Handling

- **Imputation Audit Trail:** Every imputed value is logged to `outputs/cleaning/imputation_log.csv` recording `student_id`, `field`, `original_value`, `branch_cohort`, `cohort_median_value`, and `cleaned_value`.
- **Pipeline Recovery:** If an unexpected unapproved defect is encountered during ETL execution, the pipeline halts immediately, logs the anomaly to `outputs/cleaning/unexpected_defects.log`, and leaves the raw dataset untouched.
