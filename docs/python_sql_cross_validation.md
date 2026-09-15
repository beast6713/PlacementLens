# PlacementLens — Phase 3 Part 5: Python ↔ SQL Cross-Validation

## 1. Executive Summary & Validation Architecture

This document presents the complete results of **Phase 3 Part 5 (Python ↔ SQL Cross-Validation)** for **PlacementLens**.

The objective of Part 5 is to execute an independent, dual-path quality assurance audit comparing analytical outputs produced by:
1. **Python EDA** from Phase 3 Part 2 ([`outputs/eda/`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda))
2. **PostgreSQL SQL Analytics** from Phase 3 Part 4 ([`outputs/sql/`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/sql))

The automated validation engine [`scripts/cross_validate_results.py`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/scripts/cross_validate_results.py) evaluated 23 metric checks across 21 analytical categories against frozen tolerances, generating 13 audit deliverables in [`outputs/cross_validation/`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation).

```
             FROZEN CLEAN DATASET
                      │
             ┌────────┴────────┐
             ▼                 ▼
         Python              PostgreSQL
          EDA                  SQL
       (P3-P2)               (P3-P4)
             │                 │
             ▼                 ▼
       Python Result      SQL Result
             │                 │
             └────────┬────────┘
                      ▼
               CROSS-VALIDATOR
                  (P3-P5)
                      │
               23/23 PASSED (0 Discrepancies)
```

---

## 2. Approved Metric Tolerances

- **Student & Cohort Counts:** Exact Match ($\Delta = 0$).
- **Placement Rates (%):** Match within $\pm 0.01\%$.
- **Skill Impact Spreads ($\Delta\%$):** Match within $\pm 0.01$ percentage points.
- **Compensation Packages (LPA):** Match within $\pm 0.01$ LPA.
- **Score Averages & Medians:** Match within $\pm 0.01$ points.

---

## 3. Dual-Path Metric Cross-Validation Summary

### 3.1 Population & Placement Baselines

| Analytical Metric | Python EDA Result | PostgreSQL SQL Result | Absolute Difference | Approved Tolerance | Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Total Student Population** | 1,500 | 1,500 | 0 | Exact (0) | **`PASS`** |
| **Placed Student Count** | 950 | 950 | 0 | Exact (0) | **`PASS`** |
| **Unplaced Student Count** | 550 | 550 | 0 | Exact (0) | **`PASS`** |
| **Overall Placement Rate (%)**| 63.33% | 63.33% | 0.00% | $\pm 0.01\%$ | **`PASS`** |

---

### 3.2 Branch Placement Rates & Student Counts

| Academic Branch | Python Count | SQL Count | Python Rate (%) | SQL Rate (%) | Variance | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Civil Engineering (CE)** | 105 | 105 | 68.57% | 68.57% | 0.00% | **`PASS`** |
| **Electrical Engineering (EEE)** | 150 | 150 | 66.00% | 66.00% | 0.00% | **`PASS`** |
| **Information Technology (IT)** | 375 | 375 | 65.07% | 65.07% | 0.00% | **`PASS`** |
| **Computer Science (CSE)** | 450 | 450 | 63.78% | 63.78% | 0.00% | **`PASS`** |
| **Electronics & Comm (ECE)** | 300 | 300 | 60.33% | 60.33% | 0.00% | **`PASS`** |
| **Mechanical Engineering (ME)** | 120 | 120 | 55.83% | 55.83% | 0.00% | **`PASS`** |

---

### 3.3 Technical Skill Prevalence & Impact Spreads ($\Delta\%$)

| Skill Flag Name | Python Holder N | SQL Holder N | Python Spread ($\Delta\%$) | SQL Spread ($\Delta\%$) | Variance | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **sql_skill** | 1,169 | 1,169 | +9.17 pp | +9.17 pp | 0.00 pp | **`PASS`** |
| **python_skill** | 1,177 | 1,177 | +6.94 pp | +6.94 pp | 0.00 pp | **`PASS`** |
| **cloud_skill** | 485 | 485 | +6.04 pp | +6.04 pp | 0.00 pp | **`PASS`** |
| **excel_skill** | 1,258 | 1,258 | +2.59 pp | +2.59 pp | 0.00 pp | **`PASS`** |
| **dsa_skill** | 1,057 | 1,057 | +1.47 pp | +1.47 pp | 0.00 pp | **`PASS`** |
| **power_bi_skill** | 793 | 793 | +1.01 pp | +1.01 pp | 0.00 pp | **`PASS`** |
| **cybersecurity_skill** | 297 | 297 | -2.98 pp | -2.98 pp | 0.00 pp | **`PASS`** |

---

### 3.4 Compensation Metrics (Placed Cohort $N=950$ Only)

| Employer / Category Segment | Python Mean (LPA) | SQL Mean (LPA) | Variance | Approved Tolerance | Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Overall Placed Cohort** | 10.62 LPA | 10.62 LPA | 0.00 LPA | $\pm 0.01$ LPA | **`PASS`** |
| **Product Companies** | 16.26 LPA | 16.26 LPA | 0.00 LPA | $\pm 0.01$ LPA | **`PASS`** |
| **Startup Companies** | 12.09 LPA | 12.09 LPA | 0.00 LPA | $\pm 0.01$ LPA | **`PASS`** |
| **Service Companies** | 5.90 LPA | 5.90 LPA | 0.00 LPA | $\pm 0.01$ LPA | **`PASS`** |
| **Other Companies** | 5.02 LPA | 5.02 LPA | 0.00 LPA | $\pm 0.01$ LPA | **`PASS`** |

---

## 4. Discrepancy & Root Cause Register

- **Total Discrepancies Detected:** **0**
- **Unresolved Warnings:** **0**
- **Root Cause Category:** `ZERO_DISCREPANCY`
- Register published to [`outputs/cross_validation/11_discrepancy_register.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/11_discrepancy_register.csv).

---

## 5. Audit Deliverables Register

All 13 audit deliverables generated in [`outputs/cross_validation/`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation):
1. [`01_metric_cross_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/01_metric_cross_validation.csv)
2. [`02_population_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/02_population_validation.csv)
3. [`03_placement_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/03_placement_validation.csv)
4. [`04_branch_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/04_branch_validation.csv)
5. [`05_skill_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/05_skill_validation.csv)
6. [`06_band_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/06_band_validation.csv)
7. [`07_package_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/07_package_validation.csv)
8. [`08_preparation_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/08_preparation_validation.csv)
9. [`09_null_semantics_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/09_null_semantics_validation.csv)
10. [`10_schema_logic_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/10_schema_logic_validation.csv)
11. [`11_discrepancy_register.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/11_discrepancy_register.csv)
12. [`12_cross_validation_scorecard.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/12_cross_validation_scorecard.csv)
13. [`13_cross_validation_summary.md`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/cross_validation/13_cross_validation_summary.md)

---

## 6. Final Validation Verdict

`CHECKPOINT-03-PART-05 PASS — READY FOR P3-P6`
