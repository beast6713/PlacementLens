# PlacementLens — Phase 3 Part 1: Analytics Strategy & EDA Plan

## 1. Executive Summary & Analytical Objective

**PlacementLens** is a student placement analytics and business intelligence project designed to analyze relationships between student academic performance, technical skills, preparation indicators, practical experience, and placement outcomes.

The primary objective of **Phase 3** is to execute rigorous, reproducible, and cross-validated exploratory data analysis (EDA) and SQL analytics on the frozen clean dataset [`data/processed/placementlens_students_clean.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/data/processed/placementlens_students_clean.csv). 

This strategy document freezes the analytical scope, business questions, metric definitions, statistical rules, target leakage controls, Python EDA output plan, PostgreSQL query mapping, and cross-validation framework for Phase 3 before any analytical execution begins in Part 2.

---

## 2. Stakeholders & Analytical Deliverables

The analysis serves two primary stakeholder groups:
1. **Students:** Seeking evidence-based guidance on which technical skills, score thresholds, projects, and internships are most strongly associated with placement success and package levels.
2. **Placement Cell / College Management:** Seeking operational insights into branch-level performance disparities, skill development gap areas, and targeted intervention strategies to maximize institutional placement rates.

---

## 3. Frozen Business Questions (BQ01 – BQ21)

### Category A: Placement Rate & Drivers
- **BQ01:** What is the overall placement rate across the entire student population?
- **BQ02:** How does the placement rate vary across academic branches (`CSE`, `IT`, `ECE`, `EEE`, `ME`, `CE`)?
- **BQ03:** How does placement rate vary across CGPA levels and bands?
- **BQ04:** How does placement rate vary across coding score levels and performance tiers?
- **BQ05:** How does placement rate vary across aptitude score levels and performance tiers?
- **BQ06:** How does placement rate vary across communication score levels and performance tiers?
- **BQ07:** How does placement rate vary by the number of completed projects (0 to 3+)?
- **BQ08:** How does placement rate vary by the number of completed internships (0 to 3+)?
- **BQ09:** How does placement rate vary based on individual technical skill ownership?

### Category B: Skill Penetration & Impact
- **BQ10:** Which technical skills have the highest and lowest prevalence across the student body?
- **BQ11:** Which technical skills show the largest percentage point difference in placement rate between students who possess vs. do not possess the skill?
- **BQ12:** How does total technical skill ownership (`technical_skill_count`, 0–7) relate to placement rate?

### Category C: Compensation & Package (Conditional on `placed = 1`)
- **BQ13:** What is the overall distribution, mean, median, IQR, and range of salary packages (`package_lpa`) among placed students?
- **BQ14:** How does median package vary across academic branches?
- **BQ15:** How does median package vary across hiring company types (`Product`, `Service`, `Startup`, `Other`)?
- **BQ16:** How do academic and preparation indicators differ across compensation tiers (e.g., lower tier vs. top tier packages)?

### Category D: Preparation Profiles & Comparative Analysis
- **BQ17:** How do placed and unplaced students differ across key continuous preparation metrics (CGPA, coding score, aptitude score, communication score, projects, internships, skill count)?
- **BQ18:** Which preparation indicators show the strongest linear and rank associations with placement outcome?

### Category E: Business & Operational Decision Support
- **BQ19:** Which academic branches demonstrate the highest need for targeted placement preparation support?
- **BQ20:** Which skill domains present the largest institutional improvement opportunities?
- **BQ21:** What distinct preparation profiles characterize students securing high-package roles versus average-package roles?

---

## 4. 8-Layer Exploratory Data Analysis (EDA) Framework

The Python EDA in Phase 3 Part 2 will be structured across 8 sequential analytical layers:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        8-LAYER EDA FRAMEWORK                           │
├────────────────────────────────────────────────────────────────────────┤
│ Layer 1: DATASET OVERVIEW (Rows, Columns, Types, Cardinality, NULLs)   │
│ Layer 2: UNIVARIATE ANALYSIS (Distributions, Spread, Central Tendency) │
│ Layer 3: PLACEMENT ANALYSIS (Overall & Segmented Placement Rates)     │
│ Layer 4: SKILL ANALYSIS (Prevalence, Differential Impact, Skill Count) │
│ Layer 5: ACADEMIC ANALYSIS (CGPA Patterns, Branch Performance)         │
│ Layer 6: PREPARATION ANALYSIS (Scores, Projects, Internships Impact)  │
│ Layer 7: PACKAGE ANALYSIS (Conditional on Placed, Medians, IQR)       │
│ Layer 8: BRANCH ANALYSIS (Cross-sectional Profile by Branch)           │
└────────────────────────────────────────────────────────────────────────┘
```

### Layer 1: Dataset Overview
- Row count validation (1,500 records), column count (20 columns), student ID range (`S0001`–`S1500`).
- Strict verification of NULL semantics (`company_type` = NULL and `package_lpa` = NULL for unplaced students).

### Layer 2: Univariate Analysis
- Continuous variables (`age`, `cgpa`, `internships`, `projects`, `coding_score`, `aptitude_score`, `communication_score`, `package_lpa`): count, mean, std, min, Q1 (25%), median (50%), Q3 (75%), max, IQR, skewness.
- Categorical / Binary variables (`gender`, `branch`, `placed`, `company_type`, 7 skill flags): frequencies and percentages.

### Layer 3: Placement Analysis
- Overall placement rate calculation ($N_{placed} / N_{total} \times 100$).
- Crosstabulation of placement rates against `branch`, `cgpa_band`, `coding_band`, `aptitude_band`, `communication_band`, `projects`, `internships`.

### Layer 4: Skill Analysis
- Individual skill prevalence across 7 technical flags (`python_skill`, `sql_skill`, `excel_skill`, `power_bi_skill`, `dsa_skill`, `cloud_skill`, `cybersecurity_skill`).
- Derived feature creation: `technical_skill_count` = sum of all 7 binary flags (range 0 to 7).
- Differential placement impact: $\text{Placement Rate}_{\text{Skill=1}} - \text{Placement Rate}_{\text{Skill=0}}$.

### Layer 5: Academic Analysis
- CGPA distribution profiling, branch-wise CGPA medians, CGPA tier placement crosstabs.

### Layer 6: Preparation Analysis
- Placed vs. Unplaced cohort comparisons for all performance scores and practical experience indicators.
- Mean/median differences and percentage point spreads.

### Layer 7: Package Analysis (Strictly Conditional on `placed = 1`)
- Population: $N = 950$ placed students (unplaced $N = 550$ with `package_lpa` = NULL are excluded).
- Metrics: Median (primary), Mean, Std, IQR, Min, Max, Quantiles.
- Breakdown by `branch` and `company_type`.

### Layer 8: Branch Analysis
- Cross-sectional profile matrix by branch combining student count, placement rate, median scores, median package, and skill prevalence.

---

## 5. Statistical Methods, Correlation & Leakage Controls

### 5.1 Statistical Metrics & Selection Rationale
- **Central Tendency:** Median is prioritized over Mean for package distributions due to potential right-skewness. Mean and Median are both reported for test scores and CGPA.
- **Dispersion:** Standard Deviation and Interquartile Range (IQR = Q3 - Q1) are calculated for all continuous features.
- **Categorical Association:** Percentage point differences ($\Delta\%$) for binary skill comparisons.
- **Correlation Coefficients:**
  - **Pearson Correlation ($r$):** Evaluates linear associations between continuous performance metrics (e.g., `coding_score` vs. `cgpa`).
  - **Point-Biserial / Pearson Correlation ($r_{pb}$):** Evaluates linear association between continuous metrics and binary placement outcome (`placed`).
  - **Spearman Rank Correlation ($\rho$):** Evaluates monotonic relationships between ordinal/ranked variables (e.g., `technical_skill_count`, `projects`, `internships` vs. `placed`).

### 5.2 Target Leakage Controls
- **CRITICAL RULE:** `package_lpa` and `company_type` MUST NOT be used as predictors, features, or independent variables for placement outcome (`placed`).
- **Rationale:** Package and company type are post-placement outcome attributes generated downstream of placement. Using them to predict placement introduces catastrophic target leakage.
- **Allowed Direction:** `placed` $\rightarrow$ `package_lpa` / `company_type` (conditional post-placement profiling).

### 5.3 Causality & Synthetic Data Limitations
- **Non-Causal Language Policy:** All observations must use associative terminology ("associated with", "shows a higher rate of", "observed cohort difference") rather than causal claims ("causes", "drives", "guarantees").
- **Synthetic Data Context:** The dataset is generated under Seed 42 with known structural patterns. Findings describe synthetic cohort behavior and serve analytical workflow demonstration purposes.

---

## 6. Derived Analytical Variables

Derived variables will be computed dynamically in memory during EDA and exported in analytical summary tables. They will **NEVER** overwrite or mutate the canonical input file.

1. **`technical_skill_count`** (Integer, 0–7):
   $$\text{technical\_skill\_count} = \sum_{i \in \text{skills}} \text{skill}_i$$
2. **`cgpa_band`** (Categorical):
   `< 6.0`, `6.0 – 6.99`, `7.0 – 7.99`, `8.0 – 8.99`, `9.0 – 10.0`
3. **`coding_score_band`** (Categorical):
   `< 50`, `50 – 64`, `65 – 79`, `80 – 89`, `90 – 100`
4. **`aptitude_score_band`** (Categorical):
   `< 50`, `50 – 64`, `65 – 79`, `80 – 89`, `90 – 100`
5. **`communication_score_band`** (Categorical):
   `< 50`, `50 – 64`, `65 – 79`, `80 – 89`, `90 – 100`
6. **`package_band`** (Categorical, placed only):
   `< 4.0 LPA`, `4.0 – 6.0 LPA`, `6.0 – 10.0 LPA`, `10.0+ LPA`

---

## 7. Python EDA Output Strategy & Script Architecture

### 7.1 Directory Layout
All Python EDA outputs generated in Part 2 will be saved to [`outputs/eda/`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda):

```
outputs/eda/
├── 01_dataset_overview.csv
├── 02_numeric_summary.csv
├── 03_categorical_summary.csv
├── 04_null_profile.csv
├── 05_branch_analysis.csv
├── 06_placement_analysis.csv
├── 07_score_analysis.csv
├── 08_skill_prevalence.csv
├── 09_skill_placement_analysis.csv
├── 10_experience_analysis.csv
├── 11_package_analysis.csv
├── 12_correlation_matrix.csv
├── 13_derived_metrics.csv
├── 14_eda_validation.csv
├── 15_eda_run_summary.md
└── plots/
    ├── 01_placement_rate_by_branch.png
    ├── 02_package_distribution_by_company.png
    ├── 03_score_distributions_by_placement.png
    ├── 04_skill_prevalence_and_impact.png
    └── 05_correlation_heatmap.png
```

### 7.2 Python Script Design (`scripts/eda_analysis.py`)
The modular script will execute the following functions:
- `load_clean_dataset()`: Read-only load of processed dataset.
- `validate_clean_input()`: Asserts 1,500 rows, 20 columns, zero missing values in required fields.
- `create_analytical_features()`: Computes `technical_skill_count` and analytical bands.
- `profile_dataset()`: Computes overview, numeric, categorical, and NULL summaries.
- `analyze_placement()`: Calculates overall and segmented placement rates.
- `analyze_skills()`: Profiles skill prevalence and placement rate impact.
- `analyze_scores_and_experience()`: Conducts score/experience comparison between placed and unplaced cohorts.
- `analyze_packages()`: Profiles conditional package distributions.
- `analyze_branches()`: Generates cross-sectional branch profile.
- `calculate_correlations()`: Builds Pearson and Spearman correlation matrices.
- `generate_plots()`: Creates 5 clean visualization figures.
- `save_eda_outputs()`: Exports all CSV tables, plots, and run summary markdown.

---

## 8. SQL Analytics & PostgreSQL Query Mapping

In Phase 3 Parts 3 and 4, the clean dataset will be ingested into a PostgreSQL table `public.students`. The following table maps Business Questions to SQL query structures:

| Business Question | SQL Query Concept / Functions | Expected Analytical Output | Validation Metric |
| :--- | :--- | :--- | :--- |
| **BQ01: Overall Placement Rate** | `SELECT COUNT(*), SUM(placed), ROUND(100.0*AVG(placed), 2)` | Overall placement % | Python vs SQL match ($\pm 0.00\%$) |
| **BQ02: Branch Placement Rate** | `SELECT branch, COUNT(*), SUM(placed), ROUND(100.0*AVG(placed), 2) GROUP BY branch ORDER BY placement_rate DESC` | Placement % by branch (6 rows) | Exact branch count & rate match |
| **BQ03: CGPA vs Placement** | `SELECT CASE WHEN cgpa >= 8.0 ... GROUP BY cgpa_band` | Placement % per CGPA band | Row counts & placement rates |
| **BQ09 & BQ10: Skill Prevalence** | `SELECT SUM(python_skill), SUM(sql_skill)...` | Count & % per skill flag | Prevalence counts match Python |
| **BQ11: Skill Impact Spreads** | CTE with skill crosstabs and percentage point difference | $\Delta\%$ placement rate per skill | Exact impact spread match |
| **BQ12: Skill Count vs Placement** | `SELECT (python_skill + sql_skill + ...) AS skill_cnt, COUNT(*), AVG(placed) GROUP BY skill_cnt` | Placement % by skill count (0–7) | Skill count distribution match |
| **BQ14: Package by Branch** | `SELECT branch, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY package_lpa) WHERE placed = 1 GROUP BY branch` | Median package (LPA) by branch | Median LPA match within 0.01 LPA |
| **BQ15: Package by Company Type** | `SELECT company_type, COUNT(*), PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY package_lpa) WHERE placed = 1 GROUP BY company_type` | Median package (LPA) by company | Median LPA match within 0.01 LPA |
| **BQ17: Placed vs Unplaced Scores** | `SELECT placed, AVG(cgpa), AVG(coding_score), AVG(aptitude_score), AVG(communication_score) GROUP BY placed` | Mean score comparison table | Exact mean score match |

---

## 9. Python ↔ SQL Cross-Validation Plan

In Phase 3 Part 5, key metrics will be independently calculated in Python and SQL and cross-validated:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   PYTHON ↔ SQL CROSS-VALIDATION FRAMEWORK               │
├────────────────────────────────────────────────────────────────────────┤
│ Metric                        │ Python Value │ SQL Value │ Tolerance   │
├───────────────────────────────┼──────────────┼───────────┼─────────────┤
│ Total Student Population      │ 1,500        │ 1,500     │ Exact (0)   │
│ Placed Student Count          │ Must Match   │ Must Match│ Exact (0)   │
│ Unplaced Student Count        │ Must Match   │ Must Match│ Exact (0)   │
│ Overall Placement Rate (%)    │ Must Match   │ Must Match│ ±0.01%      │
│ Branch Student Counts         │ Must Match   │ Must Match│ Exact (0)   │
│ Branch Placement Rates (%)    │ Must Match   │ Must Match│ ±0.01%      │
│ Individual Skill Counts       │ Must Match   │ Must Match│ Exact (0)   │
│ Skill Placement Rates (%)     │ Must Match   │ Must Match│ ±0.01%      │
│ Placed Median Package (LPA)   │ Must Match   │ Must Match│ ±0.01 LPA   │
│ Company Type Placed Counts    │ Must Match   │ Must Match│ Exact (0)   │
└───────────────────────────────┴──────────────┴───────────┴─────────────┘
```

---

## 10. Pre-EDA Validation Rules & Read-Only Enforcement

Before Phase 3 Part 2 execution begins, the input file [`data/processed/placementlens_students_clean.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/data/processed/placementlens_students_clean.csv) must satisfy the following immutable checks:

1. **VAL-EDA-01:** File exists at canonical path and is non-empty.
2. **VAL-EDA-02:** Cryptographic MD5 hash matches frozen Phase 2 baseline (`96023d297eec5a9a47563eaddc157d0d`).
3. **VAL-EDA-03:** Physical row count equals exactly 1,500 rows.
4. **VAL-EDA-04:** Unique student count equals 1,500 (`S0001`–`S1500`).
5. **VAL-EDA-05:** Column count equals exactly 20 DDL columns.
6. **VAL-EDA-06:** Zero missing values in mandatory columns (`student_id`, `age`, `gender`, `branch`, `cgpa`, `internships`, `projects`, `coding_score`, `aptitude_score`, `communication_score`, 7 skills, `placed`).
7. **VAL-EDA-07:** NULL semantics strictly maintained (`company_type` and `package_lpa` NULL for all 550 unplaced students; non-NULL for all 950 placed students).
8. **VAL-EDA-08:** Zero modifications permitted to source CSV file during or after EDA.
