# PlacementLens — Phase 3 Part 4: SQL Analytics & Business Question Execution

## 1. Executive Summary & Database Architecture

This document specifies the implementation, execution, and analytical outputs of **Phase 3 Part 4 (SQL Analytics & Business Questions)** for **PlacementLens**.

All 21 frozen business questions (BQ01 to BQ21) were evaluated using PostgreSQL / SQL against table [`public.students`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/sql/01_create_schema.sql) containing 1,500 student records (`S0001`–`S1500`).

The analytical SQL script [`sql/03_business_analytics.sql`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/sql/03_business_analytics.sql) and execution runner [`scripts/execute_sql_analytics.py`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/scripts/execute_sql_analytics.py) generated 24 output deliverables in [`outputs/sql/`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/sql).

---

## 2. Advanced SQL Analytical Techniques Applied

| SQL Technique | Application in BQ Queries | Example Business Question |
| :--- | :--- | :--- |
| **CTEs (Common Table Expressions)** | Intermediate segment aggregation & denominator isolation | BQ02, BQ03, BQ09, BQ11, Q16, Q18 |
| **Window Functions (`DENSE_RANK()`)** | Dense ranking of branches and skill impact spreads | BQ02 (Branch Rank), BQ11 (Spread Rank) |
| **Conditional Aggregation** | `SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END)` | BQ01–BQ12, BQ16, BQ19 |
| **Non-Zero Division Guard** | `NULLIF(denominator, 0)` for percentage protection | BQ01–BQ12, BQ19, BQ20 |
| **SQL-Derived Features** | In-query sum of 7 binary skill flags (`technical_skill_count`) | BQ12, BQ16, BQ17, BQ19, BQ21 |
| **Union All Aggregation** | Pivoting 7 binary skill columns for prevalence & impact spreads | BQ09, BQ10, BQ11, BQ20 |
| **Conditional Filtering** | Restricting compensation queries to `placed = TRUE AND package_lpa IS NOT NULL` | BQ13, BQ14, BQ15, BQ16, BQ21 |

---

## 3. Business Question Analytical Results Summary (BQ01 – BQ21)

### BQ01: Overall Placement Rate
- **SQL Result:** Total = **1,500**, Placed = **950**, Unplaced = **550**, Placement Rate = **63.33%**.

### BQ02: Branch Placement Rate & Rank
1. **Civil Engineering (CE):** 68.57% (72 placed / 105 total) — **Rank 1**
2. **Electrical Engineering (EEE):** 66.00% (99 placed / 150 total) — **Rank 2**
3. **Information Technology (IT):** 65.07% (244 placed / 375 total) — **Rank 3**
4. **Computer Science (CSE):** 63.78% (287 placed / 450 total) — **Rank 4**
5. **Electronics & Comm (ECE):** 60.33% (181 placed / 300 total) — **Rank 5**
6. **Mechanical Engineering (ME):** 55.83% (67 placed / 120 total) — **Rank 6**

### BQ03 – BQ06: Academic & Performance Tiers
- **CGPA Tiers:** `< 6.0` (**20.00%**), `6.0 – 6.99` (**50.95%**), `7.0 – 7.99` (**68.00%**), `8.0 – 8.99` (**81.88%**), `9.0 – 10.0` (**90.00%**).
- **Coding Score Tiers:** `< 50` (**25.40%**), `50 – 64` (**48.20%**), `65 – 79` (**67.50%**), `80 – 89` (**82.10%**), `90 – 100` (**89.20%**).

### BQ09 – BQ11: Technical Skill Impact Spreads ($\Delta\%$)
- **SQL Skill:** Prevalence **77.93%**, Placement rate 65.36% holders vs 56.19% non-holders (**+9.17 pp spread**) — **Rank 1**
- **Python Skill:** Prevalence **78.47%**, Placement rate 64.83% holders vs 57.89% non-holders (**+6.94 pp spread**) — **Rank 2**
- **Cloud Skill:** Prevalence **32.33%**, Placement rate 67.42% holders vs 61.38% non-holders (**+6.04 pp spread**) — **Rank 3**

### BQ13 – BQ15: Compensation Analysis (Placed Cohort $N=950$ Only)
- **Overall Mean Package:** **10.62 LPA** (Min: 3.29 LPA, Max: 48.00 LPA).
- **Branch Mean Packages:** ME (**11.33 LPA**), CSE (**10.82 LPA**), IT (**10.76 LPA**), EEE (**10.60 LPA**), CE (**10.45 LPA**), ECE (**9.93 LPA**).
- **Company Type Mean Packages:** Product (**16.26 LPA**), Startup (**12.09 LPA**), Service (**5.90 LPA**), Other (**5.02 LPA**).

### BQ17 & BQ18: Placed vs Unplaced Preparation Spreads
- Placed cohort achieves higher mean coding score (+5.41 pts), CGPA (+0.33 pts), aptitude score (+2.27 pts), and communication score (+1.18 pts).

### BQ20: Strategic Skill Opportunity Gap Matrix
- **High Opportunity Gap:** Cloud Computing (Low prevalence 32.33%, High placement rate 67.42%).
- **Core Foundation Skills:** SQL, Python, DSA (High prevalence, strong positive placement spreads).

---

## 4. Target Leakage & Null Safety Controls

1. **Post-Placement Attributes Guard:** `package_lpa` and `company_type` were strictly filtered using `WHERE placed IN (TRUE, 1)` and never used as placement predictors.
2. **Zero Null Conversion:** Unplaced student NULL package values were strictly maintained as NULL without converting to 0.

---

## 5. Output Deliverables Register

All 24 output deliverables in [`outputs/sql/`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/sql):
- `01_bq01_overall_placement.csv` to `21_bq21_high_package_patterns.csv` (21 BQ outputs).
- [`sql_query_register.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/sql/sql_query_register.csv) (Formal query register).
- [`sql_metric_validation.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/sql/sql_metric_validation.csv) (Metric baseline validation).
- [`sql_analytical_findings.md`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/sql/sql_analytical_findings.md) (Analytical findings markdown).

---

## 6. Final Checkpoint Decision

`CHECKPOINT-03-PART-04 PASS — READY FOR P3-P5`
