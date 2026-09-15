# P5-P1 Audit — Power BI Data Architecture & Model

## 1. Status: COMPLETE
- **Data Source:** Verified against `placementlens_students_clean.csv` (MD5: `96023d297eec5a9a47563eaddc157d0d`).
- **Student Granularity:** 1 row = 1 student (1,500 unique `student_id` values).
- **Schema Validation:** 20 canonical columns present (`student_id`, `age`, `gender`, `branch`, `cgpa`, `internships`, `projects`, `coding_score`, `aptitude_score`, `communication_score`, `python_skill`, `sql_skill`, `excel_skill`, `power_bi_skill`, `dsa_skill`, `cloud_skill`, `cybersecurity_skill`, `placed`, `company_type`, `package_lpa`).
- **NULL Semantics:** 550 unplaced students maintain NULL `package_lpa` and NULL `company_type` (never converted to 0 or "Unknown").
- **Unsupported Fields:** Zero fake fields (`academic_year`, `company_name`, `recruitment_date`, `offer_count`).

## 2. Summary Table
| Metric | Baseline Expected | Actual Verified | Status |
|---|---|---|---|
| Total Students | 1,500 | 1,500 | PASS |
| Placed Students | 950 | 950 | PASS |
| Unplaced Students | 550 | 550 | PASS |
| Placement Rate | 63.33% | 63.33% | PASS |
