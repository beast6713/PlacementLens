# PlacementLens — Phase 2 Part 4 Standardization & Imputation Technical Specification

**Phase:** Phase 2 — Data Cleaning & Validation  
**Part:** Part 4 — Missing Values & Data Standardization  
**Script:** `scripts/clean_standardize.py`  
**Input Intermediate Deliverable:** `data/processed/placementlens_students_structural_clean.csv` (1,500 records)  
**Candidate Processed Output:** `data/processed/placementlens_students_clean.csv` (1,500 records)  
**Checkpoint Status:** `CHECKPOINT-02-PART-04 (PASS)`

---

## 1. Executive Summary & Objective

Phase 2 Part 4 resolves the remaining 65 controlled defects present in the working dataset:
1. 15 company type case/space formatting inconsistencies.
2. 20 gender whitespace padding defects.
3. 15 string binary flag representations in `python_skill`.
4. 15 missing values in `communication_score`.

All operations adhere to the frozen strategy: read-only raw baseline verification (`MD5: 59c04ee15a0112806c510225d8e75779`), zero target leakage, preserved `NULL` compensation linkage for unplaced students, and deterministic audit logging.

---

## 2. Standardization Operations

### 2.1 Company Type Standardization (15 Defects)
- **Transformation:** For placed students (`placed == 1`), strip surrounding whitespace and titlecase labels (`df['company_type'].str.strip().str.title()`).
- **Canonical Allowed Set:** {`Product`, `Service`, `Startup`, `Other`}
- **Unplaced Linkage:** For unplaced students (`placed == 0`), `company_type` MUST be `NULL` (`np.nan`). Preserved 100% `NULL` semantics (never converted to `"None"` or `"Unknown"`).

### 2.2 Gender Whitespace Trimming (20 Defects)
- **Transformation:** `df['gender'] = df['gender'].astype(str).str.strip()`
- **Canonical Allowed Set:** {`Female`, `Male`, `Non-binary`, `Prefer not to say`}

### 2.3 Python Skill Binary Flag Normalization (15 Defects)
- **Transformation:** String representations (`"Yes"`, `"No"`) mapped to canonical integer binary flags (`1` for `"Yes"`/`"True"`, `0` for `"No"`/`"False"`).
- **Data Type:** Integer `int64` $\in \{0, 1\}$.

---

## 3. Communication Score Cohort-Median Imputation

### 3.1 Cohort Definition & Methodology
- **Cohort Dimension:** Academic `branch` (frozen in Phase 2 Part 1 strategy).
- **Leakage Prevention:** Cohort statistics exclude target variables (`placed`, `company_type`, `package_lpa`).
- **Calculation Base:** Cohort medians computed strictly from valid, non-null `communication_score` observations within each branch.

### 3.2 Branch Cohort Statistics & Imputation Log Summary

| Branch Cohort | Total Cohort Size | Valid Score Records | Calculated Cohort Median | Missing NULLs Imputed | Target Imputed Student IDs |
|---|---|---|---|---|---|
| **CE** | 105 | 105 | **81.24** | 0 | — |
| **CSE** | 450 | 447 | **81.15** | 3 | `S0681`, `S0931`, `S1016` |
| **ECE** | 300 | 298 | **81.68** | 2 | `S0216`, `S1241` |
| **EEE** | 150 | 150 | **81.08** | 0 | — |
| **IT** | 375 | 368 | **82.34** | 7 | `S0061`, `S0286`, `S0361`, `S0521`, `S0606`, `S0756`, `S0846` |
| **ME** | 120 | 117 | **81.37** | 3 | `S0131`, `S0436`, `S1126` |
| **Total** | **1,500** | **1,485** | — | **15** | **15 Imputed Records Logged** |

*Audit Trail:* All 15 imputations logged to [`outputs/cleaning/imputation_log.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cleaning/imputation_log.csv).

---

## 4. Post-Standardization Validation Summary

| Check Item | Target Rule | Observed Result | Status |
|---|---|---|---|
| **Input Rows** | `physical_rows == 1500` | 1,500 Rows | **PASS** |
| **Output Rows** | `physical_rows == 1500` | 1,500 Rows | **PASS** |
| **Unique Student IDs** | `student_id.nunique() == 1500` | 1,500 Unique IDs | **PASS** |
| **Company Type** | 100% $\in$ ALLOWED_COMPANY_TYPES (placed); `NULL` (unplaced) | 0 Invalid Placed / 0 Unplaced Non-Null | **PASS** |
| **Gender** | 100% $\in$ ALLOWED_GENDERS | 0 Invalid / 0 Whitespace | **PASS** |
| **Python Skill** | 100% $\in \{0, 1\}$ | 0 String flags / 0 Invalid | **PASS** |
| **Communication Score** | 0 NULLs, Range [0, 100] | 0 NULLs / All in bounds | **PASS** |
| **Target Leakage** | Exclude target predictors | Excluded target variables | **PASS** |
| **NULL Linkage** | `placed == 0` $\rightarrow$ `package == NULL` & `company == NULL` | `Package NULL = True`, `Company NULL = True` | **PASS** |
| **Schema Integrity** | 20 Columns in PostgreSQL DDL order | 20 Columns | **PASS** |
| **Raw Immutability** | Pre/Post MD5 Hash Match | `59c04ee15a0112806c510225d8e75779` | **PASS** |
