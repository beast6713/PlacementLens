# PlacementLens — Phase 3 Part 2: Python Exploratory Data Analysis & Statistical Profiling

## 1. Executive Summary & Input Dataset Verification

This document presents the complete results of the **Python Exploratory Data Analysis (EDA) & Statistical Profiling** executed under **Phase 3 Part 2** of PlacementLens. 

The analysis was performed using the standalone script [`scripts/eda_analysis.py`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/scripts/eda_analysis.py) operating in read-only mode on the frozen clean dataset [`data/processed/placementlens_students_clean.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/data/processed/placementlens_students_clean.csv).

### Input Dataset Baseline Verification
- **Input File Path:** `data/processed/placementlens_students_clean.csv`
- **Pre-execution MD5 Hash:** `96023d297eec5a9a47563eaddc157d0d` (**`PASS`**)
- **Post-execution MD5 Hash:** `96023d297eec5a9a47563eaddc157d0d` (**`PASS`** — 100% Source Immutability)
- **Raw Dataset MD5 Hash:** `59c04ee15a0112806c510225d8e75779` (**`PASS`** — 100% Immutable)
- **Population:** 1,500 unique student records (`S0001`–`S1500`)
- **Schema:** Exactly 20 DDL canonical columns
- **Placed Cohort:** 950 students (63.33%)
- **Unplaced Cohort:** 550 students (36.67%)

---

## 2. 8-Layer EDA Detailed Findings

### Layer 1: Dataset Overview
- Physical Rows: `1,500`
- Unique Student IDs: `1,500`
- Column Count: `20`
- Total Missing Values: `1,100` (strictly accounted for by `company_type` = 550 NULLs and `package_lpa` = 550 NULLs for unplaced students). Zero unexpected missing values exist across the 18 mandatory non-conditional attributes.

### Layer 2: Univariate Summaries

#### Continuous Variables Summary (All 1,500 Students, except Package)

| Variable | Count | Mean | Std | Min | Q1 (25%) | Median (50%) | Q3 (75%) | Max | IQR |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **age** | 1500 | 21.49 | 1.12 | 20.0 | 20.0 | 21.0 | 22.0 | 23.0 | 2.0 |
| **cgpa** | 1500 | 7.30 | 0.95 | 5.0 | 6.6 | 7.3 | 8.0 | 9.8 | 1.4 |
| **internships** | 1500 | 1.14 | 0.82 | 0.0 | 0.0 | 1.0 | 2.0 | 3.0 | 2.0 |
| **projects** | 1500 | 1.77 | 0.98 | 0.0 | 1.0 | 2.0 | 2.0 | 4.0 | 1.0 |
| **coding_score** | 1500 | 72.84 | 14.88 | 30.0 | 62.0 | 73.0 | 84.0 | 100.0 | 22.0 |
| **aptitude_score** | 1500 | 71.65 | 11.85 | 35.0 | 63.7 | 71.7 | 79.7 | 100.0 | 16.0 |
| **communication_score** | 1500 | 81.42 | 7.21 | 58.0 | 76.5 | 81.4 | 86.3 | 100.0 | 9.8 |
| **technical_skill_count** | 1500 | 4.16 | 1.32 | 0.0 | 3.0 | 4.0 | 5.0 | 7.0 | 2.0 |
| **package_lpa** *(Placed Only)*| 950 | 10.62 | 5.56 | 3.29 | 6.06 | **9.70** | 14.28 | 48.0 | **8.22** |

---

### Layer 3: Placement Analysis

- **Overall Placement Rate:** **63.33%** ($950 / 1,500$).

#### Segmented Placement Rates

```
┌────────────────────────────────────────────────────────────────────────┐
│                     SEGMENTED PLACEMENT RATES                          │
├────────────────────────────────────────────────────────────────────────┤
│ Segment                     │ Total N │ Placed N │ Placement Rate (%)  │
├─────────────────────────────┼─────────┼──────────┼─────────────────────┤
│ Civil Engineering (CE)      │ 105     │ 72       │ 68.57%              │
│ Electrical Engineering (EEE)│ 150     │ 99       │ 66.00%              │
│ Information Tech (IT)       │ 375     │ 244      │ 65.07%              │
│ Computer Science (CSE)      │ 450     │ 287      │ 63.78%              │
│ Electronics (ECE)           │ 300     │ 181      │ 60.33%              │
│ Mechanical Engineering (ME) │ 120     │ 67       │ 55.83%              │
├─────────────────────────────┼─────────┼──────────┼─────────────────────┤
│ CGPA < 6.0                  │ 135     │ 27       │ 20.00%              │
│ CGPA 6.0 – 6.99             │ 420     │ 214      │ 50.95%              │
│ CGPA 7.0 – 7.99             │ 525     │ 357      │ 68.00%              │
│ CGPA 8.0 – 8.99             │ 320     │ 262      │ 81.88%              │
│ CGPA 9.0 – 10.0             │ 100     │ 90       │ 90.00%              │
└─────────────────────────────┴─────────┴──────────┴─────────────────────┘
```

---

### Layer 4: Skill Analysis & Prevalence

| Skill Name | Total Holders | Prevalence (%) | Holder Placed | Holder Rate (%) | Non-Holder Rate (%) | Impact Spread ($\Delta\%$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **sql_skill** | 1169 | 77.93% | 764 | 65.36% | 56.19% | **+9.17 pp** |
| **python_skill** | 1177 | 78.47% | 763 | 64.83% | 57.89% | **+6.94 pp** |
| **cloud_skill** | 485 | 32.33% | 327 | 67.42% | 61.38% | **+6.04 pp** |
| **excel_skill** | 1258 | 83.87% | 802 | 63.75% | 61.16% | **+2.59 pp** |
| **dsa_skill** | 1057 | 70.47% | 674 | 63.77% | 62.30% | **+1.47 pp** |
| **power_bi_skill** | 793 | 52.87% | 506 | 63.81% | 62.80% | **+1.01 pp** |
| **cybersecurity_skill**| 297 | 19.80% | 181 | 60.94% | 63.92% | **-2.98 pp** |

---

### Layer 5 & 6: Preparation Score & Experience Comparison

| Variable | Placed Mean | Unplaced Mean | Mean Spread ($\Delta$) | Placed Median | Unplaced Median | Median Spread |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **coding_score** | 74.82 | 69.41 | **+5.41** | 75.00 | 69.00 | **+6.00** |
| **cgpa** | 7.42 | 7.09 | **+0.33** | 7.40 | 7.10 | **+0.30** |
| **aptitude_score** | 72.48 | 70.21 | **+2.27** | 72.40 | 70.50 | **+1.90** |
| **communication_score** | 81.85 | 80.67 | **+1.18** | 81.70 | 80.80 | **+0.90** |
| **projects** | 1.85 | 1.63 | **+0.22** | 2.00 | 2.00 | **0.00** |
| **internships** | 1.21 | 1.02 | **+0.19** | 1.00 | 1.00 | **0.00** |

---

### Layer 7: Package Analysis (Placed Cohort $N=950$)

- **Overall Placed Median Package:** **9.70 LPA** (Mean: 10.62 LPA, IQR: 8.22 LPA).

#### Package Breakdown by Company Type

| Company Type | Count ($N$) | Mean (LPA) | Median (LPA) | Std (LPA) | Q1 (25%) | Q3 (75%) | IQR (LPA) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Product** | 304 | 16.26 | **15.58** | 4.91 | 13.07 | 18.26 | 5.20 |
| **Startup** | 222 | 12.09 | **11.71** | 2.76 | 10.14 | 13.82 | 3.68 |
| **Service** | 381 | 5.90 | **6.03** | 0.94 | 5.34 | 6.48 | 1.14 |
| **Other** | 43 | 5.02 | **5.03** | 0.81 | 4.52 | 5.60 | 1.09 |

---

### Layer 8: Branch Analytical Matrix

| Branch | Total N | Placed N | Placement Rate (%) | Median CGPA | Median Coding | Median Aptitude | Median Comm | Median Skill Cnt | Median Package (LPA) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **CE** | 105 | 72 | **68.57%** | 7.10 | 67.08 | 70.81 | 81.24 | 4.0 | **7.89** |
| **EEE** | 150 | 99 | **66.00%** | 7.43 | 67.93 | 73.97 | 81.08 | 4.0 | **10.45** |
| **IT** | 375 | 244 | **65.07%** | 7.35 | 76.36 | 71.52 | 82.34 | 4.0 | **9.86** |
| **CSE** | 450 | 287 | **63.78%** | 7.37 | 75.72 | 71.57 | 81.15 | 5.0 | **9.91** |
| **ECE** | 300 | 181 | **60.33%** | 7.24 | 70.47 | 71.88 | 81.68 | 4.0 | **8.74** |
| **ME** | 120 | 67 | **55.83%** | 7.17 | 69.66 | 71.42 | 81.37 | 4.0 | **10.39** |

---

## 3. Statistical Analysis & Correlations

- **Correlation Selection:** Pearson ($r$) for continuous numerical pairs; Point-biserial ($r_{pb}$) for numerical features vs binary placement (`placed`).
- **Highest Observed Placement Correlations:**
  1. `cgpa` vs. `placed`: $r = +0.1650$
  2. `coding_score` vs. `placed`: $r = +0.1702$
  3. `sql_skill` vs. `placed`: $r = +0.0890$
  4. `python_skill` vs. `placed`: $r = +0.0682$
- **Target Leakage Enforcement:** `package_lpa` and `company_type` were strictly excluded from predictive placement correlation models.

---

## 4. Derived Analytical Features

1. `technical_skill_count` (Range 0 to 7, Mean: 4.16, Median: 4.0).
2. `cgpa_band` (5 mutually exclusive tiers).
3. `coding_score_band` (5 performance tiers).
4. `aptitude_score_band` (5 performance tiers).
5. `communication_score_band` (5 performance tiers).
6. `package_band` (4 compensation tiers, placed cohort only).

---

## 5. Generated Artifacts & Visualizations

### CSV Summary Tables (`outputs/eda/`)
1. [`01_dataset_overview.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/01_dataset_overview.csv)
2. [`02_numeric_summary.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/02_numeric_summary.csv)
3. [`03_categorical_summary.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/03_categorical_summary.csv)
4. [`04_null_profile.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/04_null_profile.csv)
5. [`05_branch_analysis.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/05_branch_analysis.csv)
6. [`06_placement_analysis.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/06_placement_analysis.csv)
7. [`07_score_analysis.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/07_score_analysis.csv)
8. [`08_skill_prevalence.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/08_skill_prevalence.csv)
9. [`09_skill_placement_analysis.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/09_skill_placement_analysis.csv)
10. [`10_experience_analysis.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/10_experience_analysis.csv)
11. [`11_package_analysis.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/11_package_analysis.csv)
12. [`12_correlation_matrix.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/12_correlation_matrix.csv)
13. [`13_derived_metrics.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/13_derived_metrics.csv)
14. [`14_eda_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/14_eda_validation.csv)
15. [`15_eda_run_summary.md`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/15_eda_run_summary.md)

### Plots & Figures (`outputs/eda/plots/`)
1. [`01_placement_rate_by_branch.png`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/plots/01_placement_rate_by_branch.png)
2. [`02_package_distribution_by_company.png`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/plots/02_package_distribution_by_company.png)
3. [`03_score_distributions_by_placement.png`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/plots/03_score_distributions_by_placement.png)
4. [`04_skill_prevalence_and_impact.png`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/plots/04_skill_prevalence_and_impact.png)
5. [`05_correlation_heatmap.png`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/plots/05_correlation_heatmap.png)

---

## 6. Analytical Scorecard & Final Decision

All 16 validation checks in [`14_eda_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda/14_eda_validation.csv) PASSED cleanly with zero errors. Source dataset immutability was cryptographically confirmed.

`CHECKPOINT-03-PART-02 PASS — READY FOR P3-P3`
