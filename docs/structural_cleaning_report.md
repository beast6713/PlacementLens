# PlacementLens — Phase 2 Part 3 Structural & Duplicate Cleaning Report

**Phase:** Phase 2 — Data Cleaning & Validation  
**Part:** Part 3 — Duplicate & Structural Cleaning  
**Script:** `scripts/clean_structural.py`  
**Input Dataset:** `data/raw/placementlens_students_raw.csv` (MD5: `59c04ee15a0112806c510225d8e75779`)  
**Intermediate Processed Output:** `data/processed/placementlens_students_structural_clean.csv`  
**Checkpoint Status:** `CHECKPOINT-02-PART-03 (PASS)`

---

## 1. Objective & Scope

Phase 2 Part 3 focuses exclusively on resolving duplicate physical records and executing structural category normalization assigned to Part 3.

The scope is strictly bound to:
1. Auditing and removing the 5 tail duplicate physical student rows (`S0120`, `S0450`, `S0780`, `S1100`, `S1350`).
2. Deduplicating physical CSV rows from **1,505 to 1,500 unique student records** using the `keep='first'` policy.
3. Normalizing 25 lowercase branch values (`cse`, `it`, `ece`, `eee`, `me`, `ce`) using `str.strip().str.upper()`.
4. Validating structural integrity, student ID population coverage (`S0001`–`S1500`), and raw dataset immutability.
5. Exporting `data/processed/placementlens_students_structural_clean.csv` without applying Part 4 transformations (missing score imputations, skill binary flag parsing, company type normalization).

---

## 2. Duplicate Audit & Deduplication Accounting

### Audit Methodology
- **Primary Identity Key:** `student_id`
- **Policy:** `KEEP FIRST OCCURRENCE` (`keep='first'`). Remove subsequent physical occurrences.
- **Audit File:** [`outputs/cleaning/duplicate_audit.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cleaning/duplicate_audit.csv)

### Duplicate Record Reconciliation

| Student ID | Occurrence 1 Line | Action 1 | Retained | Occurrence 2 Line | Action 2 | Retained | Reason |
|---|---|---|---|---|---|---|---|
| **S0120** | Line 121 | KEEP | TRUE | Line 1502 | REMOVE | FALSE | Duplicate student_id |
| **S0450** | Line 451 | KEEP | TRUE | Line 1503 | REMOVE | FALSE | Duplicate student_id |
| **S0780** | Line 781 | KEEP | TRUE | Line 1504 | REMOVE | FALSE | Duplicate student_id |
| **S1100** | Line 1101 | KEEP | TRUE | Line 1505 | REMOVE | FALSE | Duplicate student_id |
| **S1350** | Line 1351 | KEEP | TRUE | Line 1506 | REMOVE | FALSE | Duplicate student_id |

- **Physical Raw Rows Input:** 1,505
- **Physical Duplicate Rows Removed:** 5
- **Physical Clean Rows Output:** 1,500
- **Unique Student Count:** 1,500 (`S0001` → `S1500`)

---

## 3. Branch Structural Normalization

- **Inconsistent Raw Inputs:** 25 records containing lowercase branch values (`cse`, `it`, `ece`, `eee`, `me`, `ce`).
- **Transformation:** `df['branch'] = df['branch'].astype(str).str.strip().str.upper()`
- **Canonical Allowed Set:** {`CSE`, `IT`, `ECE`, `EEE`, `ME`, `CE`}
- **Post-Transformation Status:** 0 lowercase or unapproved branch categories remain. 100% compliance verified.

---

## 4. Structural Integrity & Validation Results

| Rule ID | Rule Statement | Expected | Actual Result | Status |
|---|---|---|---|---|
| **ST-01** | `student_id` Existence & Non-Null | 100% Non-Null | 1,500/1,500 Non-Null | **PASS** |
| **ST-02** | `student_id` Regex Format | `^S[0-9]{4}$` | 100% Matching | **PASS** |
| **ST-03** | `student_id` Uniqueness | 1,500 Unique IDs | 1,500 Unique IDs | **PASS** |
| **ST-04** | ID Population Coverage | `S0001` to `S1500` | 0 Missing / 0 Unexpected | **PASS** |
| **ST-05** | Physical Row Count | 1,500 Rows | 1,500 Rows | **PASS** |
| **ST-06** | Column Count & DDL Schema | 20 Columns | 20 Columns | **PASS** |
| **ST-07** | Branch Category Integrity | 100% $\in$ Allowed Set | 0 Invalid / 0 Unused | **PASS** |
| **ST-08** | Remaining Duplicate Keys | 0 Duplicates | 0 Duplicates | **PASS** |

---

## 5. Deliverables & Immutability Verification

1. **Intermediate Clean CSV:** `data/processed/placementlens_students_structural_clean.csv` (1,500 records).
2. **Duplicate Audit CSV:** `outputs/cleaning/duplicate_audit.csv` (10 records audited).
3. **Structural Summary CSV:** `outputs/cleaning/structural_cleaning_summary.csv`.
4. **Structural Validation CSV:** `outputs/cleaning/structural_cleaning_validation.csv`.
5. **Run Log Markdown:** `outputs/cleaning/structural_cleaning_run_log.md`.
6. **Raw Immutability Check:** Pre-MD5 `59c04ee15a0112806c510225d8e75779` == Post-MD5 `59c04ee15a0112806c510225d8e75779` (**PASSED**).
