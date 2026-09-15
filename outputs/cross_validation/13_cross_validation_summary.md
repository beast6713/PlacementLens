# PlacementLens — Phase 3 Part 5: Python <-> SQL Cross-Validation Summary

- **Execution Date:** 2026-09-16
- **Clean Dataset Baseline:** [`data/processed/placementlens_students_clean.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/data/processed/placementlens_students_clean.csv)
- **Clean Dataset MD5 Hash:** `96023d297eec5a9a47563eaddc157d0d` (`PASS` — 100% Immutable)
- **Raw Dataset MD5 Hash:** `59c04ee15a0112806c510225d8e75779` (`PASS` — 100% Immutable)
- **Python Source:** [`outputs/eda/`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/eda)
- **SQL Source:** [`outputs/sql/`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/outputs/sql)
- **Total Cross-Validation Checks:** 23
- **Passed Checks:** 23
- **Failed Checks:** 0
- **Warnings / Discrepancies:** 0

---

## Metric Cross-Validation Summary

### 1. Population & Placement Baselines
- **Total Population:** Python = **1,500**, SQL = **1,500** (\Delta = 0, `PASS`).
- **Placed Count:** Python = **950**, SQL = **950** (\Delta = 0, `PASS`).
- **Unplaced Count:** Python = **550**, SQL = **550** (\Delta = 0, `PASS`).
- **Overall Placement Rate:** Python = **63.33%**, SQL = **63.33%** (\Delta = 0.00%), `PASS`).

### 2. Branch Placement Rates & Student Counts
- **Civil Engineering (CE):** Python = **68.57%**, SQL = **68.57%** (\Delta = 0.00%), `PASS`).
- **Electrical Engineering (EEE):** Python = **66.00%**, SQL = **66.00%** (\Delta = 0.00%), `PASS`).
- **Information Tech (IT):** Python = **65.07%**, SQL = **65.07%** (\Delta = 0.00%), `PASS`).
- **Computer Science (CSE):** Python = **63.78%**, SQL = **63.78%** (\Delta = 0.00%), `PASS`).
- **Electronics (ECE):** Python = **60.33%**, SQL = **60.33%** (\Delta = 0.00%), `PASS`).
- **Mechanical Engineering (ME):** Python = **55.83%**, SQL = **55.83%** (\Delta = 0.00%), `PASS`).

### 3. Skill Prevalence & Impact Spreads (\Delta%)
- **SQL Skill Spread:** Python = **+9.17 pp**, SQL = **+9.17 pp** (\Delta = 0.00 pp), `PASS`).
- **Python Skill Spread:** Python = **+6.94 pp**, SQL = **+6.94 pp** (\Delta = 0.00 pp), `PASS`).
- **Cloud Skill Spread:** Python = **+6.04 pp**, SQL = **+6.04 pp** (\Delta = 0.00 pp), `PASS`).

### 4. Placed Compensation Metrics ($N=950$ Placed Cohort)
- **Overall Placed Mean Package:** Python = **10.62 LPA**, SQL = **10.62 LPA** (\Delta = 0.00 LPA), `PASS`).
- **Product Companies Mean:** Python = **16.26 LPA**, SQL = **16.26 LPA** (\Delta = 0.00 LPA), `PASS`).
- **Startup Companies Mean:** Python = **12.09 LPA**, SQL = **12.09 LPA** (\Delta = 0.00 LPA), `PASS`).
- **Service Companies Mean:** Python = **5.90 LPA**, SQL = **5.90 LPA** (\Delta = 0.00 LPA), `PASS`).

---

## Final Validation Verdict

`CHECKPOINT-03-PART-05 PASS — READY FOR P3-P6`
