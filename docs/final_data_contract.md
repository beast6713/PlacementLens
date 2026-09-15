# PlacementLens — Final Data Contract (`v1.0-clean`)

**Project Name:** PlacementLens — Student Placement Analytics & Business Intelligence  
**Dataset Version:** `v1.0-clean`  
**Schema Version:** `v1.0 DDL`  
**Dataset Path:** `data/processed/placementlens_students_clean.csv`  
**Clean Dataset Hash (MD5):** `96023d297eec5a9a47563eaddc157d0d`  
**Raw Dataset Path:** `data/raw/placementlens_students_raw.csv`  
**Raw Baseline Hash (MD5):** `59c04ee15a0112806c510225d8e75779`  
**Data-Quality Status:** `100% VALIDATED (0 Defects)`  
**Phase 2 Status:** `FROZEN — READY FOR PHASE 3`

---

## 1. Dataset Overview & Grain

- **Primary Objective:** Provide a portfolio-grade, audit-ready student preparation and placement analytical dataset for Python EDA, PostgreSQL analytics, and Power BI dashboard reporting.
- **Dataset Grain:** 1 record = 1 unique student (`student_id`).
- **Physical Row Count:** Exactly 1,500 rows.
- **Unique Primary Key:** `student_id` (`S0001` through `S1500`). Zero duplicates, zero missing keys.
- **Privacy & Ethics Declaration:** 100% synthetic dataset created with seed 42. Zero real student PII present.

---

## 2. Frozen Schema Specification (20 Columns)

| Ordinal | Column Name | Physical Data Type | Logical Type | Allowed Range / Values | NULL Semantics |
|---|---|---|---|---|---|
| **1** | `student_id` | `str` | String PK | Pattern `^S[0-9]{4}$` (`S0001`..`S1500`) | Strictly Non-Null |
| **2** | `age` | `int64` | Discrete Integer | Range [18, 30] years | Strictly Non-Null |
| **3** | `gender` | `str` | Categorical | {`Female`, `Male`, `Non-binary`, `Prefer not to say`} | Strictly Non-Null |
| **4** | `branch` | `str` | Categorical | {`CSE`, `IT`, `ECE`, `EEE`, `ME`, `CE`} | Strictly Non-Null |
| **5** | `cgpa` | `float64` | Continuous Float | Range [0.00, 10.00] | Strictly Non-Null |
| **6** | `internships` | `int64` | Count Integer | Integer $\ge 0$ | Strictly Non-Null |
| **7** | `projects` | `int64` | Count Integer | Integer $\ge 0$ | Strictly Non-Null |
| **8** | `coding_score` | `float64` | Continuous Float | Range [0.00, 100.00] | Strictly Non-Null |
| **9** | `aptitude_score` | `float64` | Continuous Float | Range [0.00, 100.00] | Strictly Non-Null |
| **10** | `communication_score` | `float64` | Continuous Float | Range [0.00, 100.00] | Strictly Non-Null |
| **11** | `python_skill` | `int64` | Binary Flag | Integer $\in \{0, 1\}$ | Strictly Non-Null |
| **12** | `sql_skill` | `int64` | Binary Flag | Integer $\in \{0, 1\}$ | Strictly Non-Null |
| **13** | `excel_skill` | `int64` | Binary Flag | Integer $\in \{0, 1\}$ | Strictly Non-Null |
| **14** | `power_bi_skill` | `int64` | Binary Flag | Integer $\in \{0, 1\}$ | Strictly Non-Null |
| **15** | `dsa_skill` | `int64` | Binary Flag | Integer $\in \{0, 1\}$ | Strictly Non-Null |
| **16** | `cloud_skill` | `int64` | Binary Flag | Integer $\in \{0, 1\}$ | Strictly Non-Null |
| **17** | `cybersecurity_skill` | `int64` | Binary Flag | Integer $\in \{0, 1\}$ | Strictly Non-Null |
| **18** | `placed` | `int64` | Binary Target | Integer $\in \{0, 1\}$ (0=Unplaced, 1=Placed) | Strictly Non-Null |
| **19** | `company_type` | `str` | Categorical / NULL | {`Product`, `Service`, `Startup`, `Other`} for `placed=1` | **NULL** for `placed=0` |
| **20** | `package_lpa` | `float64` | Continuous / NULL | Range (0.00, 50.00] LPA for `placed=1` | **NULL** for `placed=0` |

---

## 3. NULL Semantics & Linkage Rules

1. **Unplaced Compensation Linkage:** For unplaced students (`placed = 0`), `company_type` MUST be `NULL` (`NaN`) and `package_lpa` MUST be `NULL` (`NaN`). Converting these to `0.00`, `"None"`, or `"Unknown"` is strictly prohibited.
2. **Placed Compensation Linkage:** For placed students (`placed = 1`), `company_type` MUST be populated with a valid category and `package_lpa` MUST be a positive float.
3. **Quantitative Zero Rule:** `0` represents a valid quantitative zero (0 projects, 0 internships, or absent skill flag `0`). Quantitative zero and `NULL` are never interchanged.
4. **Zero String Placeholders:** String representations such as `"NULL"`, `"None"`, `"N/A"` are strictly prohibited in the clean dataset.
