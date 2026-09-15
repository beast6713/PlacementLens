# PlacementLens — Phase 3 Analytics Validation Rules

## 1. Overview

This document specifies the exact data quality, structural integrity, and analytical execution rules required before and during Phase 3 analytics execution. All validation rules must pass cleanly before results are accepted into Phase 3 completion reports.

---

## 2. Pre-EDA Input Validation Rules (VAL-EDA-01 to VAL-EDA-08)

| Rule ID | Rule Category | Validation Requirement | Threshold / Expected Value | Failure Action |
| :--- | :--- | :--- | :--- | :--- |
| **VAL-EDA-01** | File Existence | Clean dataset exists at `data/processed/placementlens_students_clean.csv`. | File present, size > 0 | STOP — File missing |
| **VAL-EDA-02** | Cryptographic Hash | Pre-execution MD5 hash matches frozen Phase 2 baseline. | `96023d297eec5a9a47563eaddc157d0d` | STOP — Baseline corrupted |
| **VAL-EDA-03** | Row Count | Physical row count of clean dataset equals expected population. | Exactly 1,500 rows | STOP — Row count mismatch |
| **VAL-EDA-04** | Primary Key Unique | `student_id` is unique with zero duplicates in ID range `S0001`–`S1500`. | 1,500 unique IDs, 0 duplicates | STOP — Duplicate IDs detected |
| **VAL-EDA-05** | DDL Schema | Column count and schema names match exact 20 DDL specification. | 20 exact columns | STOP — Column schema error |
| **VAL-EDA-06** | Mandatory Completeness | Zero missing values across 18 non-conditional features. | 0 NULLs in non-conditional cols | STOP — Unexpected missing values |
| **VAL-EDA-07** | NULL Semantics | `company_type` and `package_lpa` NULL if and only if `placed = 0`. | 550 unplaced NULLs, 950 placed non-NULLs | STOP — NULL linkage violation |
| **VAL-EDA-08** | Source Immutability | Source CSV file `placementlens_students_clean.csv` remains 100% untouched. | MD5 hash unchanged after EDA | STOP — Source file mutated |

---

## 3. Target Leakage Prevention Rules (VAL-LEAK-01 to VAL-LEAK-03)

| Rule ID | Rule Category | Target Leakage Constraint | Enforced Behavior |
| :--- | :--- | :--- | :--- |
| **VAL-LEAK-01** | Feature Selection | `package_lpa` MUST NOT be included as an independent predictor for placement. | Disallow `package_lpa` in placement regression/classification |
| **VAL-LEAK-02** | Feature Selection | `company_type` MUST NOT be included as an independent predictor for placement. | Disallow `company_type` in placement modeling/crosstabs |
| **VAL-LEAK-03** | Directionality | Analysis direction must strictly follow `placed` $\rightarrow$ `package_lpa` / `company_type`. | Restrict package analysis to `placed = 1` population only |

---

## 4. Derived Metric Rules (VAL-DERIV-01 to VAL-DERIV-03)

| Rule ID | Rule Category | Derived Feature Requirement | Implementation Rule |
| :--- | :--- | :--- | :--- |
| **VAL-DERIV-01** | In-Memory Computation | Derived features (e.g. `technical_skill_count`, score bands) must be computed in memory. | Do NOT write derived features back into canonical CSV |
| **VAL-DERIV-02** | Skill Count Range | `technical_skill_count` must be integer bounded strictly between 0 and 7. | Range $0 \le \text{skill\_count} \le 7$ |
| **VAL-DERIV-03** | Band Completeness | All score and CGPA bands must cover 100% of non-null student values without gaps or overlaps. | 1,500 students mapped to valid bands |

---

## 5. Python ↔ SQL Cross-Validation Tolerances (VAL-XVAL-01 to VAL-XVAL-05)

| Rule ID | Metric Name | Allowed Numerical Tolerance | Failure Action |
| :--- | :--- | :--- | :--- |
| **VAL-XVAL-01** | Total & Placed Counts | Exact match ($0$ difference) | Investigate SQL filter or grouping |
| **VAL-XVAL-02** | Placement Rates (%) | $\pm 0.01\%$ | Re-examine rounding logic |
| **VAL-XVAL-03** | Skill Prevalence Counts | Exact match ($0$ difference) | Audit binary flag aggregation |
| **VAL-XVAL-04** | Median Package (LPA) | $\pm 0.01$ LPA | Re-examine percentile method (e.g., continuous vs discrete) |
| **VAL-XVAL-05** | Score Averages | $\pm 0.01$ points | Audit floating-point division |
