# PlacementLens — Phase 3 Final Analytical Baseline

## 1. Phase 3 Objective & Architecture
Phase 3 of **PlacementLens** produced rigorous, reproducible, and cross-validated analytical evidence from the frozen Phase 2 clean dataset (`data/processed/placementlens_students_clean.csv`) using a dual-path engine architecture (Python EDA + PostgreSQL SQL Analytics).

```
                 FROZEN CLEAN DATASET
            (MD5: 96023d297eec5a9a47563eaddc157d0d)
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
                   CROSS-VALIDATION
                       (P3-P5)
                          │
                  23/23 PASSED (0 Discrepancies)
                          │
                          ▼
                 FINAL EVIDENCE BASELINE
                       (P3-P6)
```

---

## 2. Frozen Data Baseline
- **Clean Dataset Path:** `data/processed/placementlens_students_clean.csv`
- **Clean Dataset MD5:** `96023d297eec5a9a47563eaddc157d0d` (`PASS` — 100% Immutable)
- **Raw Dataset Path:** `data/raw/placementlens_students_raw.csv`
- **Raw Dataset MD5:** `59c04ee15a0112806c510225d8e75779` (`PASS` — 100% Immutable)
- **Population:** 1,500 physical records (`S0001`–`S1500`)
- **Schema:** 20 normalized columns

---

## 3. Verified Core Analytical Baseline

### 3.1 Population & Placement Baseline
- **Total Population:** 1,500 students
- **Placed Cohort:** 950 students (63.33%)
- **Unplaced Cohort:** 550 students (36.67%)

### 3.2 Branch Placement Hierarchy
1. **Civil Engineering (CE):** 68.57% placement rate (72 placed / 105 total)
2. **Electrical Engineering (EEE):** 66.00% placement rate (99 placed / 150 total)
3. **Information Technology (IT):** 65.07% placement rate (244 placed / 375 total)
4. **Computer Science (CSE):** 63.78% placement rate (287 placed / 450 total)
5. **Electronics & Comm (ECE):** 60.33% placement rate (181 placed / 300 total)
6. **Mechanical Engineering (ME):** 55.83% placement rate (67 placed / 120 total)

### 3.3 Skill Prevalence & Observed Placement Spreads ($\Delta\%$)
1. **SQL Skill:** Prevalence = 77.93% (1,169 holders) | Placement Spread = **+9.17 pp** (65.36% vs 56.19%)
2. **Python Skill:** Prevalence = 78.47% (1,177 holders) | Placement Spread = **+6.94 pp** (64.83% vs 57.89%)
3. **Cloud Skill:** Prevalence = 32.33% (485 holders) | Placement Spread = **+6.04 pp** (67.42% vs 61.38%)
4. **Excel Skill:** Prevalence = 83.87% (1,258 holders) | Placement Spread = **+2.59 pp** (63.75% vs 61.16%)
5. **DSA Skill:** Prevalence = 70.47% (1,057 holders) | Placement Spread = **+1.47 pp** (63.77% vs 62.30%)
6. **Power BI Skill:** Prevalence = 52.87% (793 holders) | Placement Spread = **+1.01 pp** (63.81% vs 62.80%)
7. **Cybersecurity Skill:** Prevalence = 19.80% (297 holders) | Placement Spread = **-2.98 pp** (60.94% vs 63.92%)

### 3.4 Placed Cohort Compensation Metrics ($N=950$)
- **Overall Placed Package:** Mean = **10.62 LPA** | Median = **9.70 LPA** | IQR = **8.22 LPA**
- **Product Companies:** Mean = **16.26 LPA** | Median = **16.03 LPA** ($N=162$)
- **Startup Companies:** Mean = **12.09 LPA** | Median = **12.16 LPA** ($N=142$)
- **Service Companies:** Mean = **5.90 LPA** | Median = **5.91 LPA** ($N=482$)
- **Other Companies:** Mean = **5.02 LPA** | Median = **4.97 LPA** ($N=164$)

### 3.5 Placed vs Unplaced Preparation Differences
- **Coding Score:** Placed Mean = **78.36** | Unplaced Mean = **72.95** (Spread = **+5.41 pts**)
- **CGPA:** Placed Mean = **7.81** | Unplaced Mean = **7.22** (Spread = **+0.59 pts**)
- **Aptitude Score:** Placed Mean = **75.40** | Unplaced Mean = **70.21** (Spread = **+5.19 pts**)
- **Communication Score:** Placed Mean = **81.56** | Unplaced Mean = **81.35** (Spread = **+0.21 pts**)
- **Technical Skill Count:** Placed Median = **4.0** | Unplaced Median = **3.0** (Spread = **+1.0 skill**)

---

## 4. Key Validated Analytical Findings
1. **Strongest Predictors of Placement:** Higher technical skill counts, coding score performance, and CGPA demonstrate strong positive association with student placement success.
2. **Employer Salary Tiers:** Compensation is heavily stratified by employer company type, with Product firms offering a ~2.75x salary premium over Service firms.
3. **Core Technical Skill Premiums:** SQL, Python, and Cloud technologies exhibit the highest placement rate spreads among skill holders.
4. **Target Leakage Control:** Compensation attributes (`package_lpa` and `company_type`) are strictly verified to be conditional downstream properties of placed students only.

---

## 5. Synthetic Data Limitations & Observational Scope
- **Synthetic Data Notice:** The dataset is synthetically generated for analytical demonstration. Results reflect the statistical rules of the generator.
- **Non-Causal Policy:** All observed relationships are associative. No causal claims ("causes", "guarantees", "predicts") are made.

---

## 6. Phase 4 Handoff Status
Phase 3 is 100% COMPLETE. The verified metric baseline in `outputs/phase3/` is formally frozen and ready for consumption in Phase 4 (Insights & Placement Readiness Framework).
