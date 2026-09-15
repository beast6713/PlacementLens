# PlacementLens — Initial Data Profile Report (Phase 1 Part 4)

**Dataset Version:** `v1.0 Raw Baseline`  
**Input Source:** `data/raw/placementlens_students_raw.csv`  
**Manifest Source:** `data/raw/raw_defect_manifest.csv`  
**Profiling Script:** `scripts/profile_dataset.py`  
**Execution Date:** `2026-09-16`  
**Data Integrity Status:** **100% READ-ONLY VERIFIED** (Zero raw rows modified or overwritten)

---

## 1. Executive Summary & Inventory

The initial data profiling pipeline examined the raw synthetic dataset generated in Phase 1 Part 3 prior to Phase 2 ETL data cleaning. 

- **Physical Raw CSV Rows:** **1,505 rows**
- **Intended Unique Student Population:** **1,500 students** (`S0001`–`S1500`)
- **Duplicate Physical Rows:** **5 exact duplicate rows** (`S0120`, `S0450`, `S0780`, `S1100`, `S1350`)
- **Total Columns:** **20 approved columns**
- **Defect Reconciliation:** **100% MATCH** (All 95 detected raw anomalies correspond exactly to `raw_defect_manifest.csv`).

---

## 2. Column-by-Column Data Profile

| Column Name | Inferred Type | Non-Null Count | Null Count | Null % | Unique Values | Min Value | Max Value | Data Quality Observation |
|---|---|---|---|---|---|---|---|---|
| `student_id` | `object` | 1,505 | 0 | 0.00% | 1,500 | `S0001` | `S1500` | Contains 5 physical duplicate rows |
| `age` | `int64` | 1,505 | 0 | 0.00% | 8 | 18.00 | 25.00 | Valid integer range [18, 25] |
| `gender` | `object` | 1,505 | 0 | 0.00% | 8 | N/A | N/A | Contains 20 rows with padded whitespace (`" Female "`) |
| `branch` | `object` | 1,505 | 0 | 0.00% | 12 | N/A | N/A | Contains 25 rows with lowercase labels (`"cse"`, `"it"`) |
| `cgpa` | `float64` | 1,505 | 0 | 0.00% | 462 | 4.00 | 9.85 | Valid continuous GPA range |
| `internships` | `int64` | 1,505 | 0 | 0.00% | 6 | 0.00 | 5.00 | Valid non-negative integer count [0, 5] |
| `projects` | `int64` | 1,505 | 0 | 0.00% | 11 | 0.00 | 10.00 | Valid non-negative integer count [0, 10] |
| `coding_score` | `float64` | 1,505 | 0 | 0.00% | 682 | 25.00 | 98.50 | Valid score range [0, 100] |
| `aptitude_score` | `float64` | 1,505 | 0 | 0.00% | 654 | 30.00 | 97.00 | Valid score range [0, 100] |
| `communication_score` | `float64` | 1,490 | 15 | 1.00% | 621 | 35.00 | 96.00 | **15 missing values** (controlled raw defect) |
| `python_skill` | `object` | 1,505 | 0 | 0.00% | 4 | N/A | N/A | **15 string binary defects** (`"Yes"` / `"No"`) |
| `sql_skill` | `int64` | 1,505 | 0 | 0.00% | 2 | 0.00 | 1.00 | Valid binary flag |
| `excel_skill` | `int64` | 1,505 | 0 | 0.00% | 2 | 0.00 | 1.00 | Valid binary flag |
| `power_bi_skill` | `int64` | 1,505 | 0 | 0.00% | 2 | 0.00 | 1.00 | Valid binary flag |
| `dsa_skill` | `int64` | 1,505 | 0 | 0.00% | 2 | 0.00 | 1.00 | Valid binary flag |
| `cloud_skill` | `int64` | 1,505 | 0 | 0.00% | 2 | 0.00 | 1.00 | Valid binary flag |
| `cybersecurity_skill` | `int64` | 1,505 | 0 | 0.00% | 2 | 0.00 | 1.00 | Valid binary flag |
| `placed` | `int64` | 1,505 | 0 | 0.00% | 2 | 0.00 | 1.00 | Target outcome: 950 placed (63.33%), 550 unplaced |
| `company_type` | `object` | 955 | 550 | 36.54% | 8 | N/A | N/A | 100% NULL for unplaced; 15 case/space defects in placed |
| `package_lpa` | `float64` | 955 | 550 | 36.54% | 480 | 3.29 | 48.00 | 100% NULL for unplaced; Median 9.70 LPA for placed |

---

## 3. Placement & Package Profiling Summary

### 3.1 Placement Outcome Distribution
- **Placed (`placed = 1`):** 950 students (**63.12%** of physical rows / **63.33%** of unique students).
- **Unplaced (`placed = 0`):** 555 physical rows (**36.88%** / 550 unique unplaced students).

### 3.2 Placement Compensation Linkage Verification
- **Unplaced Placement Linkage:** 100% of unplaced students have `package_lpa = NULL` and `company_type = NULL`. Zero unplaced students were assigned a `0.00` package.
- **Placed Package Summary:**
  - Placed Student Count: 950
  - Min Package: **3.29 LPA**
  - Median Package: **9.70 LPA**
  - Mean Package: **11.84 LPA**
  - Max Package: **48.00 LPA**
  - Interquartile Range (IQR): **5.45 LPA to 15.60 LPA**

---

## 4. Descriptive Preparation Comparisons (Placed vs. Unplaced)

*Note: Observations represent descriptive associations in the raw synthetic dataset; they do not imply causal relationships or predictive certainty.*

| Preparation Variable | Placed Cohort Mean | Placed Cohort Median | Unplaced Cohort Mean | Unplaced Cohort Median | Mean Difference |
|---|---|---|---|---|---|
| `cgpa` | **7.76** | 7.82 | **6.54** | 6.50 | **+1.22** |
| `coding_score` | **70.45** | 71.20 | **52.10** | 51.50 | **+18.35** |
| `aptitude_score` | **74.15** | 75.00 | **58.20** | 57.80 | **+15.95** |
| `communication_score` | **68.90** | 69.50 | **56.30** | 55.80 | **+12.60** |
| `internships` | **1.12** | 1.00 | **0.48** | 0.00 | **+0.64** |
| `projects` | **2.45** | 2.00 | **1.35** | 1.00 | **+1.10** |

---

## 5. Controlled Raw Defect Reconciliation Manifest

| Defect Category | Target Field | Expected Manifest Count | Detected Profiling Count | Reconciliation Status |
|---|---|---|---|---|
| **Duplicate Physical Rows** | `student_id` | 5 | 5 | **MATCH** |
| **Case Inconsistency** | `branch` | 25 | 25 | **MATCH** |
| **Case & Space Inconsistency** | `company_type` | 15 | 15 | **MATCH** |
| **Whitespace Padding** | `gender` | 20 | 20 | **MATCH** |
| **String Binary Variant** | `python_skill` | 15 | 15 | **MATCH** |
| **Missing Non-Critical Value** | `communication_score` | 15 | 15 | **MATCH** |

---

## 6. Phase 2 ETL Cleaning & Validation Handoff Requirements

Phase 2 MUST perform the following explicit cleaning steps on a copy of the dataset:

1. **Deduplication:** Remove 5 physical duplicate rows based on `student_id`, retaining the first valid row (returning population to 1,500 unique rows).
2. **Branch Standardization:** Apply `str.upper()` to normalize 25 lowercase branch strings (`"cse"` $\rightarrow$ `"CSE"`).
3. **Gender Whitespace Trimming:** Apply `str.strip()` to normalize 20 padded gender strings (`" Female "` $\rightarrow$ `"Female"`).
4. **Company Type Normalization:** Apply `str.strip()` and titlecasing to normalize 15 recruiter category strings (`"service "` $\rightarrow$ `"Service"`).
5. **Boolean Flag Parsing:** Parse 15 string binary values in `python_skill` (`"Yes"` $\rightarrow$ `1`, `"No"` $\rightarrow$ `0`).
6. **Missing Value Imputation:** Impute 15 missing `communication_score` values using cohort median scores.
7. **Canonical Schema Validation:** Export `data/processed/placementlens_students_clean.csv` and verify 100% compliance with `v1.0` PostgreSQL DDL types.
