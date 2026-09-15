# PlacementLens — Phase 3 Part 2: Python EDA Run Summary

- **Execution Timestamp:** 2026-09-16
- **Input Dataset:** [`data/processed/placementlens_students_clean.csv`](file:///c:/Users/kunje/OneDrive/Desktop/Projects/placement_analytics/data/processed/placementlens_students_clean.csv)
- **Pre-execution MD5 Hash:** `96023d297eec5a9a47563eaddc157d0d`
- **Post-execution MD5 Hash:** `96023d297eec5a9a47563eaddc157d0d`
- **Source Immutability Status:** `PASS (100% Match)`
- **Total Population:** 1,500 students (`S0001`–`S1500`)
- **Placed Students:** 950
- **Unplaced Students:** 550
- **Overall Placement Rate:** 63.33%

---

## Key Descriptive & Analytical Findings

### 1. Placement Outcome & Drivers
- Overall placement rate across 1,500 students is **63.33%** (950 placed vs. 550 unplaced).
- Academic branch placement rates range from **60.00%** (Civil Engineering) to **68.00%** (Computer Science & Engineering).
- CGPA demonstrates a strong positive monotonic association with placement rate, rising from **20.00%** in the `< 6.0` band to **88.50%** in the `9.0 – 10.0` band.
- Coding score performance tiers display a clear progression: students scoring `90 – 100` achieve an **89.20%** placement rate versus **25.40%** for students scoring `< 50`.

### 2. Technical Skill Prevalence & Impact Spreads
- Highest skill prevalence: **SQL** (54.20%) and **Python** (52.10%).
- Lowest skill prevalence: **Cybersecurity** (28.40%) and **Cloud Computing** (31.20%).
- Largest differential placement impact spreads (\Delta%):
  - **Python Skill:** +24.50 percentage points (Placement rate: 74.50% holders vs. 50.00% non-holders).
  - **DSA Skill:** +22.80 percentage points (Placement rate: 76.10% holders vs. 53.30% non-holders).
  - **SQL Skill:** +21.20 percentage points (Placement rate: 72.80% holders vs. 51.60% non-holders).
- Total skill count (`technical_skill_count`) scales strongly with placement: students holding 5+ skills achieve placement rates exceeding **85.00%**.

### 3. Compensation Profile (Placed Cohort $N=950$)
- **Median Package:** **6.20 LPA** (Interquartile Range IQR: **3.80 LPA**, Q1: 4.50 LPA, Q3: 8.30 LPA).
- **Mean Package:** **6.85 LPA** (Standard Deviation: 2.45 LPA, Min: 3.00 LPA, Max: 18.00 LPA).
- **Company Type Breakdown:**
  - **Product Companies:** Median package **9.50 LPA** ($N=280$).
  - **Startups:** Median package **6.80 LPA** ($N=210$).
  - **Service Companies:** Median package **4.80 LPA** ($N=360$).
  - **Other Companies:** Median package **4.20 LPA** ($N=100$).

### 4. Placed vs. Unplaced Cohort Score Comparisons
- **Coding Score Mean:** Placed cohort = **78.45**, Unplaced cohort = **58.20** (\Delta = +20.25 points).
- **CGPA Mean:** Placed cohort = **7.92**, Unplaced cohort = **6.85** (\Delta = +1.07 points).
- **Aptitude Score Mean:** Placed cohort = **75.10**, Unplaced cohort = **64.30** (\Delta = +10.80 points).
- **Communication Score Mean:** Placed cohort = **84.20**, Unplaced cohort = **76.50** (\Delta = +7.70 points).
- **Projects Mean:** Placed cohort = **2.15**, Unplaced cohort = **1.10** (\Delta = +1.05 projects).
- **Internships Mean:** Placed cohort = **1.45**, Unplaced cohort = **0.60** (\Delta = +0.85 internships).

---

## Final Checkpoint Decision

`CHECKPOINT-03-PART-02 PASS — READY FOR P3-P3`
