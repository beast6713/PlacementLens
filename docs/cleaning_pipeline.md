# PlacementLens — Data Cleaning & Ingestion Pipeline Technical Architecture (`v1.0 Clean`)

**Phase:** Phase 2 — Data Cleaning & Validation  
**Part:** Part 2 — Data Ingestion & Cleaning Pipeline  
**Pipeline Script:** `scripts/clean_dataset.py`  
**Input Dataset:** `data/raw/placementlens_students_raw.csv` (MD5: `59c04ee15a0112806c510225d8e75779`)  
**Output Dataset:** `data/processed/placementlens_students_clean.csv`  
**Status:** `CHECKPOINT-02-PART-02 (PASS)`

---

## 1. Executive Summary & Pipeline Objective

The PlacementLens Data Cleaning & Ingestion Pipeline (`scripts/clean_dataset.py`) converts the frozen, raw Phase 1 synthetic dataset (1,505 physical rows, 95 controlled defects) into a validated clean analytical dataset (`v1.0 Clean`) of exactly 1,500 unique student records.

The pipeline is designed to be **reproducible**, **auditable**, **deterministic**, and **non-destructive**. The raw dataset remains strictly read-only and immutable throughout.

---

## 2. Pipeline Architecture & Execution Flow

```text
               ┌─────────────────────────────────────────┐
               │ data/raw/placementlens_students_raw.csv │
               └────────────────────┬────────────────────┘
                                    │ (Read-Only & Hash Verify)
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        scripts/clean_dataset.py                         │
├─────────────────────────────────────────────────────────────────────────┤
│ 1. Verify Raw Input MD5 Checksum (59c04ee15a0112806c510225d8e75779)     │
│ 2. Load Raw DataFrame & Create In-Memory Working Copy                   │
│ 3. Apply String Whitespace & Case Trimming (gender, branch, company)    │
│ 4. Parse String Binary Flags (python_skill -> 1/0 int64)                │
│ 5. Remove Physical Duplicate Records (student_id deduplication)         │
│ 6. Impute Missing Communication Scores (Branch Cohort Median)           │
│ 7. Enforce PostgreSQL v1.0 DDL Data Types & NULL Semantics              │
│ 8. Audit Clean DataFrame against Post-Cleaning Rules (VAL-01..VAL-08)   │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
┌──────────────┐          ┌───────────────────┐       ┌────────────────────┐
│  Processed   │          │    Audit Logs     │       │ Raw Immutability   │
│  Clean CSV   │          │  & Summary CSVs   │       │ Post-Check MD5     │
└──────────────┘          └───────────────────┘       └────────────────────┘
```

---

## 3. Transformation Sequence & Defect Resolution Summary

| Step | Target Field | Defect Category | Expected Count | Clean Transformation Logic | Verification Result |
|---|---|---|---|---|---|
| **1. Whitespace** | `gender` | Whitespace Padding | 20 | `df['gender'].str.strip()` | 100% Trimmed $\in$ ALLOWED_GENDERS |
| **2. Case Norm.** | `branch` | Case Inconsistency | 25 | `df['branch'].str.strip().str.upper()` | 100% Uppercase $\in$ ALLOWED_BRANCHES |
| **3. Format Norm.** | `company_type` | Case & Space Variants | 15 | `df['company_type'].str.strip().str.title()` | 100% Titlecase $\in$ ALLOWED_COMPANY_TYPES |
| **4. Binary Parse** | `python_skill` | String Binary Flags | 15 | Parse `"Yes"`/`"True"` $\rightarrow 1$, `"No"`/`"False"` $\rightarrow 0$ | 100% Binary Integer $\in \{0, 1\}$ |
| **5. Deduplicate** | `student_id` | Physical Tail Duplicates | 5 | `df.drop_duplicates(subset=['student_id'], keep='first')` | Rows reduced from 1,505 to 1,500 |
| **6. Imputation** | `communication_score` | Missing Nulls | 15 | Branch-level cohort median calculated on valid observations | 0 Nulls remain; score $\in [0, 100]$ |
| **Total** | **Dataset Wide** | **All Controlled Defects** | **95** | **Deterministic ETL Execution** | **100% Defect Resolution (95/95)** |

---

## 4. Branch Cohort Median Imputation Breakdown

The 15 missing `communication_score` values were imputed using valid observations grouped by academic branch:

| Branch Cohort | Valid Observations | Calculated Cohort Median | Missing Records Imputed | Imputed Student IDs |
|---|---|---|---|---|
| **CE** | 163 | 81.24 | 0 | — |
| **CSE** | 338 | 81.15 | 3 | `S0681`, `S0931`, `S1016` |
| **ECE** | 250 | 81.68 | 2 | `S0216`, `S1241` |
| **EEE** | 148 | 81.08 | 0 | — |
| **IT** | 322 | 82.34 | 7 | `S0061`, `S0286`, `S0361`, `S0521`, `S0606`, `S0756`, `S0846` |
| **ME** | 264 | 81.37 | 3 | `S0131`, `S0436`, `S1126` |
| **Total** | **1,485** | — | **15** | **15 Imputed Records Logged** |

*Note: Target leakage protection strictly maintained — placement status, company type, and compensation were excluded from imputation logic.*

---

## 5. Generated Artifacts & Lineage Deliverables

1. **Clean Processed Dataset:** `data/processed/placementlens_students_clean.csv` (1,500 physical rows, 1,500 unique student IDs).
2. **Cleaning Audit Log:** `outputs/cleaning/cleaning_audit_log.csv` (95 individual defect audit records).
3. **Imputation Log:** `outputs/cleaning/imputation_log.csv` (15 detailed imputation records).
4. **Summary Report CSV:** `outputs/cleaning/cleaning_summary.csv` (Summary table across all 6 defect categories).
5. **Cleaning Run Log:** `outputs/cleaning/cleaning_run_log.md` (Markdown execution audit trail).

---

## 6. Raw Data Immutability & Reproducibility Verification

- **Baseline Raw Hash:** `59c04ee15a0112806c510225d8e75779`
- **Post-Execution Raw Hash:** `59c04ee15a0112806c510225d8e75779`
- **Immutability Result:** `PASSED (100% Byte-for-byte identical)`
- **Reproducibility Test:** Executing `python scripts/clean_dataset.py` sequentially produces byte-identical processed clean CSVs and audit logs.
