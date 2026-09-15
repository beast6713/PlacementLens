# Dataset Specification

## 1. Executive Summary & Strategy Decision

Phase 1 establishes a **synthetic dataset** of exactly **1,500 de-identified student records** for PlacementLens (Version `v1.0`). 

- **Source Type:** Synthetic internally generated data.
- **Record Count:** Exactly 1,500 student records at a single placement-cycle snapshot.
- **Primary Objective:** Provide a realistic, multi-branch student preparation and placement outcome dataset without exposing real student Personally Identifiable Information (PII) or institutional data.
- **Key Advantage:** Guarantees student privacy, eliminates public-data licensing issues, enables deterministic reproducibility via a fixed random seed (`SEED = 42`), and allows controlled raw-data defect injection to validate data quality engineering pipelines in subsequent phases.

---

## 2. Grain, Deliverables & Versioning

- **Grain:** One row per synthetic student record at a single placement-cycle snapshot.
- **Dataset Version:** `v1.0 Baseline`
- **Raw File Path:** `data/raw/placementlens_students_raw.csv` (Untouched raw dataset baseline)
- **Clean File Path:** `data/processed/placementlens_students_clean.csv` (To be produced in Phase 2)
- **Random Seed:** `42` (Python `numpy.random` & `random` modules)
- **Generation Date:** `2026-09-16`

---

## 3. Approved Fields & Variable Classifications

The dataset consists of **20 approved fields** categorized into 8 functional variable classifications:

| Variable Name | Data Type | Classification | Business Description | Allowed Values / Range |
|---|---|---|---|---|
| `student_id` | String | A. Identifier | Synthetic unique student identifier | `S0001`–`S1500` |
| `age` | Integer | B. Demographic | Student age at snapshot | 18–25 |
| `gender` | Category | B. Demographic | Self-described demographic grouping | `Female`, `Male`, `Non-binary`, `Prefer not to say` |
| `branch` | Category | C. Academic | Academic branch | `CSE`, `IT`, `ECE`, `EEE`, `ME`, `CE` |
| `cgpa` | Float | C. Academic | Cumulative Grade Point Average | 0.00–10.00 (Continuous) |
| `internships` | Integer | F. Experience | Number of completed internships | 0–5 |
| `projects` | Integer | F. Experience | Number of completed projects | 0–10 |
| `coding_score` | Float | E. Assessment | Assessment score in coding | 0.0–100.0 |
| `aptitude_score` | Float | E. Assessment | Assessment score in general aptitude | 0.0–100.0 |
| `communication_score` | Float | E. Assessment | Assessment score in communication | 0.0–100.0 |
| `python_skill` | Binary/Int | D. Technical Skill | Capability indicator for Python | 0 or 1 |
| `sql_skill` | Binary/Int | D. Technical Skill | Capability indicator for SQL | 0 or 1 |
| `excel_skill` | Binary/Int | D. Technical Skill | Capability indicator for Excel | 0 or 1 |
| `power_bi_skill` | Binary/Int | D. Technical Skill | Capability indicator for Power BI | 0 or 1 |
| `dsa_skill` | Binary/Int | D. Technical Skill | Capability indicator for Data Structures | 0 or 1 |
| `cloud_skill` | Binary/Int | D. Technical Skill | Capability indicator for Cloud Computing | 0 or 1 |
| `cybersecurity_skill` | Binary/Int | D. Technical Skill | Capability indicator for Cybersecurity | 0 or 1 |
| `placed` | Binary/Int | G. Placement Outcome | **Target Variable:** Placement status | 1 (Placed) or 0 (Unplaced) |
| `company_type` | Category | H. Compensation | Recruiter company tier/category | `Product`, `Service`, `Startup`, `Other`, or `NULL` |
| `package_lpa` | Float | H. Compensation | Annual CTC compensation in Lakhs Per Annum | >0.0–50.0 LPA, or `NULL` |

---

## 4. Analytical Focus & Priority Ranking

The generation logic and subsequent analytics strictly align with the approved priority order:

1. **Placement / Package Analysis** (Primary target: `placed`, `package_lpa`, `company_type`)
2. **Technical Skills** (7 binary skill flags: Python, SQL, Excel, Power BI, DSA, Cloud, Cybersecurity)
3. **Coding / Aptitude / Communication** (Assessment test metrics evaluating core capabilities)
4. **CGPA / Academic Performance** (Academic eligibility and foundational performance)
5. **Projects** (Hands-on practical execution indicator)
6. **Internships** (Industry exposure indicator)

---

## 5. Specific Business Rules & Policies

### 5.1 Target Variable (`placed`) Policy
- `placed` is the primary binary outcome variable (1 = Placed, 0 = Unplaced).
- Expected placement rate target: **60%–70% placed**, **30%–40% unplaced** across the overall population.

### 5.2 Compensation & Company Type Policy
- **When `placed = 1`**: `company_type` MUST be non-null (`Product`, `Service`, `Startup`, or `Other`) and `package_lpa` MUST be a positive float (>0.0 LPA up to 50.0 LPA).
- **When `placed = 0`**: `company_type` MUST be `NULL` and `package_lpa` MUST be `NULL`.
- *Strict Rule:* Unplaced students are NEVER assigned `package_lpa = 0.0`. The distinction between "no package because unplaced" (`NULL`) and a "zero package" is strictly preserved.

### 5.3 Branch Strategy
Target distribution across the 6 approved branches ensures robust sample sizes per cohort:
- `CSE` (Computer Science): ~30% (~450 records)
- `IT` (Information Technology): ~25% (~375 records)
- `ECE` (Electronics & Comm.): ~20% (~300 records)
- `EEE` (Electrical & Electronics): ~10% (~150 records)
- `ME` (Mechanical Eng.): ~8% (~120 records)
- `CE` (Civil Eng.): ~7% (~105 records)

### 5.4 Demographic Policy (Age & Gender)
- **Age:** Synthetic values range between 18 and 25 (mean ~21.5). Age is treated as a secondary background field and does not drive placement outcomes.
- **Gender:** Synthetic distribution: `Female` (~40%), `Male` (~55%), `Non-binary` (~3%), `Prefer not to say` (~2%). Gender is evaluated exclusively for aggregate exploratory visualization; it is strictly excluded from placement scoring formulas, readiness calculations, or screening rules.

---

## 6. Synthetic Generation Design Principles

1. **Realism:** Values mimic real-world student engineering cohorts with plausible means, standard deviations, and skill co-occurrence.
2. **Variation & Imperfect Relationships:** Placement outcomes are probabilistic (modeled via multi-factor logistic probability functions with gaussian noise). No single variable (e.g. CGPA > 8.0) deterministically guarantees placement.
3. **No Data Leakage:** No synthetic variable (e.g. `placement_score`) is created that directly mirrors `placed`.
4. **No Fabricated Findings:** Data generation will not enforce artificial conclusions (e.g. forcing "Python guarantees a Product job"). Analytical findings must emerge naturally from probabilistic rules.

---

## 7. Controlled Raw Data Quality Defect Strategy

To demonstrate data quality engineering and validation pipelines in Phase 2, the raw generator will introduce controlled, documented benign quality defects into `data/raw/placementlens_students_raw.csv`:

- **Case Inconsistencies (~2.0%):** e.g., `"cse"`, `"it"`, `"service "` instead of standard capitalization.
- **Whitespace Defects (~1.5%):** Leading/trailing spaces in branch or company type string fields.
- **Type/String Variations (~1.0%):** Binary flags represented as `"Yes"`/`"No"` or `"True"`/`"False"` instead of `1`/`0`.
- **Missing Non-Critical Values (~1.0%):** Occasional `NULL` in `communication_score` or `projects` for raw data cleaning practice.
- **Duplicate Records (~0.5%):** 5-8 duplicate student ID rows introduced in raw file only.

*Integrity Constraint:* Structural linkages between `placed`, `company_type`, and `package_lpa` remain logically consistent in underlying generation. All injected raw defects will be fully documented and recoverable in Phase 2.
