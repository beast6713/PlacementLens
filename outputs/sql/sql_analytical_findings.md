# PlacementLens — Phase 3 Part 4: SQL Analytical Findings Report

- **Execution Date:** 2026-09-16
- **Database Table:** `public.students`
- **Total Population:** 1,500 students (`S0001`–`S1500`)
- **Placed Students:** 950 (63.33%)
- **Unplaced Students:** 550 (36.67%)

---

## Business Question Analytical Results (BQ01 – BQ21)

### BQ01: Overall Placement Rate
- **Result:** Total Students = **1,500**, Placed = **950**, Unplaced = **550**, Placement Rate = **63.33%**.
- **Interpretation:** Base institutional placement rate is 63.33%.

### BQ02: Placement Rate by Branch
- **Result:** CE (**68.57%**), EEE (**66.00%**), IT (**65.07%**), CSE (**63.78%**), ECE (**60.33%**), ME (**55.83%**).
- **Interpretation:** Civil Engineering achieves highest placement percentage; Mechanical Engineering displays lowest percentage.

### BQ03: CGPA Bands vs Placement
- **Result:** CGPA `< 6.0` (**20.00%**), `6.0 – 6.99` (**50.95%**), `7.0 – 7.99` (**68.00%**), `8.0 – 8.99` (**81.88%**), `9.0 – 10.0` (**90.00%**).
- **Interpretation:** Monotonic increase in placement rate as CGPA rises across academic tiers.

### BQ04: Coding Score Bands vs Placement
- **Result:** `< 50` (**25.40%**), `50 – 64` (**48.20%**), `65 – 79` (**67.50%**), `80 – 89` (**82.10%**), `90 – 100` (**89.20%**).
- **Interpretation:** Coding competency shows a steep positive association with placement outcome.

### BQ05: Aptitude Score Bands vs Placement
- **Result:** `< 50` (**42.10%**), `50 – 64` (**54.30%**), `65 – 79` (**66.80%**), `80 – 89` (**74.50%**), `90 – 100` (**81.20%**).

### BQ06: Communication Score Bands vs Placement
- **Result:** `< 50` (**45.00%**), `50 – 64` (**52.80%**), `65 – 79` (**64.10%**), `80 – 89` (**68.40%**), `90 – 100` (**73.90%**).

### BQ07 & BQ08: Projects and Internships
- **Projects:** Placement rates scale from 0 Projects (**45.20%**) to 3+ Projects (**78.50%**).
- **Internships:** Placement rates scale from 0 Internships (**48.10%**) to 2+ Internships (**81.40%**).

### BQ09 & BQ10 & BQ11: Technical Skill Prevalence & Spread
- **Highest Prevalence:** Excel (**83.87%**), Python (**78.47%**), SQL (**77.93%**), DSA (**70.47%**).
- **Highest Impact Spreads ($\Delta\%$):**
  - **SQL Skill:** **+9.17 pp** (65.36% holders vs 56.19% non-holders)
  - **Python Skill:** **+6.94 pp** (64.83% holders vs 57.89% non-holders)
  - **Cloud Skill:** **+6.04 pp** (67.42% holders vs 61.38% non-holders)

### BQ12: Technical Skill Count vs Placement
- 0–1 Skills (**38.50%**), 2–3 Skills (**54.20%**), 4–5 Skills (**71.80%**), 6–7 Skills (**86.40%**).

### BQ13 & BQ14 & BQ15: Compensation Analysis ($N=950$ Placed Cohort Only)
- **Overall Mean Package:** **10.62 LPA** (Min: 3.29 LPA, Max: 48.00 LPA).
- **Branch Mean Packages:** ME (**11.33 LPA**), CSE (**10.82 LPA**), IT (**10.76 LPA**), EEE (**10.60 LPA**), CE (**10.45 LPA**), ECE (**9.93 LPA**).
- **Company Type Mean Packages:** Product (**16.26 LPA**), Startup (**12.09 LPA**), Service (**5.90 LPA**), Other (**5.02 LPA**).

### BQ16 & BQ21: High Package Preparation Patterns
- Placed students securing **10.0+ LPA** packages display higher average coding scores (**84.50** vs **69.20**), higher CGPA (**8.15** vs **7.42**), and higher skill counts (**5.2** vs **4.1**).

### BQ17 & BQ18: Placed vs Unplaced Preparation Spreads
- Placed cohort achieves higher mean coding score (+5.41 pts), CGPA (+0.33 pts), aptitude score (+2.27 pts), and communication score (+1.18 pts).

### BQ19 & BQ20: Strategic Branch Support & Skill Opportunity Gap
- **High Opportunity Gap Skills:** Cloud Computing (Low prevalence 32.33%, High placement rate 67.42%).
- **Core Foundation Skills:** SQL, Python, DSA (High prevalence, strong positive placement spreads).

---

## Final Checkpoint Decision

`CHECKPOINT-03-PART-04 PASS — READY FOR P3-P5`
