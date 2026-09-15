# PlacementLens — Data Foundation Validation Report (Phase 1 Part 5)

**Phase 1 Readiness Decision:** **READY FOR PHASE 2 (DATA CLEANING & VALIDATION)**  
**Validation Date:** `2026-09-16`  
**Validation Script:** `scripts/validate_data_foundation.py`  
**Input Source File:** `data/raw/placementlens_students_raw.csv`  
**Defect Manifest Source:** `data/raw/raw_defect_manifest.csv`  
**Raw Data Integrity:** **100% UNCHANGED / READ-ONLY VERIFIED** (MD5: `59c04ee15a0112806c510225d8e75779`)

---

## 1. Executive Summary & Gate Decision

Phase 1 Part 5 evaluated the raw data foundation against all 15 verification categories and 25 checkpoint criteria locked across Phase 0, Part 1, Part 2, Part 3, and Part 4 specifications.

- **Immutability Check:** **PASS** (0 bytes modified, MD5 matches Part 3 generation hash exactly).
- **Population & Size Check:** **PASS** (1,500 unique students `S0001`–`S1500`, 1,505 physical rows including 5 controlled duplicate rows).
- **Schema & DDL Compliance:** **PASS** (All 20 approved columns present in exact order, 0 missing or unapproved fields).
- **Placement Logic Compliance:** **PASS** (100% compliance with `chk_placement_compensation_logic`: 550 unplaced students have 100% `NULL` packages and company categories).
- **Controlled Defect Reconciliation:** **PASS** (100% match: 95 raw defects detected vs 95 expected in `raw_defect_manifest.csv`).
- **Unexpected Defects Detected:** **0** (Zero unapproved anomalies or corrupted values found).
- **Privacy & PII Check:** **PASS** (Zero student names, addresses, emails, or government IDs present).
- **Final Readiness Decision:** **READY FOR PHASE 2**

---

## 2. Validation Scorecard

| Category | Requirement | Observed Result | Status | Evidence |
|---|---|---|---|---|
| **1. File Integrity** | Raw CSV exists and is readable | File size: 105.16 KB, MD5: `59c04ee15a0112806c510225d8e75779` | **PASS** | File readable, hash verified |
| **2. Immutability** | Raw CSV remains untouched from Part 3 | Current MD5 matches Part 3 generation hash | **PASS** | 0 bytes modified |
| **3. Population Size** | 1,500 unique students, 1,505 physical rows | 1,500 unique student IDs, 1,505 physical rows | **PASS** | 5 duplicate rows expected |
| **4. Student IDs** | Formatted `^S[0-9]{4}$` unique keys | 100% regex format compliance (`S0001`–`S1500`) | **PASS** | Non-null, regex compliant |
| **5. Schema & Order** | 20 approved columns matching Part 2 DDL | 20 columns present in approved sequence | **PASS** | 0 missing/unexpected cols |
| **6. Data Types** | Inferred types align with PostgreSQL DDL | Compatible text, numeric, and flag types | **PASS** | No type corruption |
| **7. Category Sets** | Categories match allowed sets + expected defects | All variants reconciled against manifest | **PASS** | 95 defects match manifest |
| **8. Numerical Ranges** | CGPA [0,10], Scores [0,100], Counts $\ge 0$ | 0 unexpected out-of-bounds values | **PASS** | Min/max within limits |
| **9. Placement Logic** | `chk_placement_compensation_logic` table rule | 100% compliant across all 1,505 rows | **PASS** | Unplaced package = 100% NULL |
| **10. Technical Skills** | 7 binary flags present & profiled | Prevalence 17.9% to 69.5% | **PASS** | 15 string defects expected |
| **11. Controlled Defects** | 95 defects reconciled against manifest | 95 detected == 95 expected | **PASS** | 100% manifest match |
| **12. Unexpected Defects** | 0 unapproved defects present | 0 unexpected defects detected | **PASS** | Zero unapproved anomalies |
| **13. Privacy & Ethics** | Zero student PII exposure | Synthetic keys only, zero names/contact PII | **PASS** | PII check passed |
| **14. Reproducibility** | Seed 42 deterministic generator | Deterministic script tested | **PASS** | MD5 hash match |
| **15. Phase 2 Readiness** | Raw data foundation ready for ETL cleaning | All 14 validation categories PASS | **READY** | Scorecard 100% PASS |

---

## 3. Severity Classification & Risk Assessment

- **CRITICAL FAILURES (Blockers):** **0**
- **HIGH SEVERITY ISSUES:** **0**
- **MEDIUM SEVERITY ISSUES (Controlled raw defects to resolve in Phase 2):** **6 Categories / 95 Defects**
  1. 5 Duplicate physical student rows (`S0120`, `S0450`, `S0780`, `S1100`, `S1350`).
  2. 25 Lowercase branch strings (`"cse"`, `"it"`, `"ece"`, `"eee"`, `"me"`, `"ce"`).
  3. 15 Case & space inconsistency recruiter strings (`"product"`, `"Service "`).
  4. 20 Padded whitespace gender strings (`" Female "`).
  5. 15 String binary flag values in `python_skill` (`"Yes"`, `"No"`).
  6. 15 Missing `communication_score` values.
- **LOW SEVERITY ISSUES:** **0**

---

## 4. Phase 2 ETL Cleaning & Validation Handoff Instructions

Phase 2 is authorized to consume `data/raw/placementlens_students_raw.csv` and execute the following ETL pipeline:

1. **Deduplication:** Remove 5 physical duplicate rows based on `student_id`, retaining the first valid row (returning dataset to 1,500 unique rows).
2. **Branch Standardization:** Apply `str.upper()` to normalize 25 lowercase branch strings (`"cse"` $\rightarrow$ `"CSE"`).
3. **Gender Whitespace Trimming:** Apply `str.strip()` to normalize 20 padded gender strings (`" Female "` $\rightarrow$ `"Female"`).
4. **Recruiter Category Normalization:** Apply `str.strip()` and titlecasing to normalize 15 recruiter category strings (`"service "` $\rightarrow$ `"Service"`).
5. **Boolean Flag Parsing:** Parse 15 string binary values in `python_skill` (`"Yes"` $\rightarrow$ `1`, `"No"` $\rightarrow$ `0`).
6. **Missing Value Imputation:** Impute 15 missing `communication_score` values using cohort median scores.
7. **Clean Export & DB Load:** Export `data/processed/placementlens_students_clean.csv` and load into PostgreSQL schema `v1.0`.
