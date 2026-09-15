# Phase 1 — Part 1: Dataset Strategy & Source Specification

## 1. Strategy Overview

This document defines the approved dataset strategy and source specification for **PlacementLens** (Phase 1 — Part 1). 

PlacementLens uses a **synthetic dataset** of exactly **1,500 student records** representing a single placement-cycle snapshot across 6 engineering branches. The dataset design provides a privacy-first, reproducible foundation for downstream data cleaning, PostgreSQL analytics, and Power BI visualization without exposing real student PII or relying on unverified external datasets.

---

## 2. Strategic Decisions & Rationale

### 2.1 Dataset Type & Source Decision
- **Decision:** **Synthetic Dataset** (`v1.0`)
- **Rationale:** 
  - Protects student privacy (Zero PII exposure).
  - Eliminates dependencies on private institutional databases or public-data licensing constraints.
  - Allows precise control over variable schema and correlation structures.
  - Enables controlled injection of raw data-quality defects to demonstrate data cleaning and profiling pipelines in Phase 2.
  - Guarantees 100% reproducibility across environments.

### 2.2 Record Count Decision
- **Decision:** **1,500 Records**
- **Rationale:** 
  - Provides adequate statistical sample depth across 6 academic branches (minimum $\ge 100$ records per branch).
  - Balances analytical rigor with lightweight execution speed across Python, PostgreSQL, and Power BI DAX calculations during the 1-week timeline.

---

## 3. Approved Variable Schema & Classifications

The raw concept consists of **20 approved variables** categorized into 8 conceptual classifications:

| # | Column Name | Classification | Data Type | Valid Range / Categories | Description |
|---|---|---|---|---|---|
| 1 | `student_id` | A. Identifier | String | `S0001`–`S1500` | Synthetic unique student identifier |
| 2 | `age` | B. Demographic | Integer | 18–25 | Student age at placement snapshot |
| 3 | `gender` | B. Demographic | Category | `Female`, `Male`, `Non-binary`, `Prefer not to say` | Self-described demographic category |
| 4 | `branch` | C. Academic | Category | `CSE`, `IT`, `ECE`, `EEE`, `ME`, `CE` | Academic engineering department |
| 5 | `cgpa` | C. Academic | Float | 0.00–10.00 | Cumulative Grade Point Average |
| 6 | `coding_score` | E. Assessment | Float | 0.0–100.0 | Coding assessment score |
| 7 | `aptitude_score` | E. Assessment | Float | 0.0–100.0 | General aptitude assessment score |
| 8 | `communication_score` | E. Assessment | Float | 0.0–100.0 | Communication assessment score |
| 9 | `internships` | F. Experience | Integer | 0–5 | Number of completed internships |
| 10 | `projects` | F. Experience | Integer | 0–10 | Number of completed projects |
| 11 | `python_skill` | D. Technical Skill | Binary Int | 0, 1 | Capability flag for Python |
| 12 | `sql_skill` | D. Technical Skill | Binary Int | 0, 1 | Capability flag for SQL |
| 13 | `excel_skill` | D. Technical Skill | Binary Int | 0, 1 | Capability flag for Excel |
| 14 | `power_bi_skill` | D. Technical Skill | Binary Int | 0, 1 | Capability flag for Power BI |
| 15 | `dsa_skill` | D. Technical Skill | Binary Int | 0, 1 | Capability flag for Data Structures & Algorithms |
| 16 | `cloud_skill` | D. Technical Skill | Binary Int | 0, 1 | Capability flag for Cloud Computing |
| 17 | `cybersecurity_skill` | D. Technical Skill | Binary Int | 0, 1 | Capability flag for Cybersecurity |
| 18 | `placed` | G. Placement Outcome | Binary Int | 0, 1 | **Target Variable:** Placement status (1=Placed, 0=Unplaced) |
| 19 | `company_type` | H. Compensation | Category | `Product`, `Service`, `Startup`, `Other`, `NULL` | Recruiter tier for placed students |
| 20 | `package_lpa` | H. Compensation | Float | >0.0–50.0 LPA, `NULL` | Compensation package in Lakhs Per Annum |

---

## 4. Analytical Priority & Business Policies

### 4.1 Priority Ranking
1. **Placement / Package Analysis** (`placed`, `package_lpa`, `company_type`)
2. **Technical Skills** (7 binary skill flags)
3. **Coding / Aptitude / Communication** (Assessment test performance)
4. **CGPA / Academic Performance** (Foundation academic metric)
5. **Projects** (Hands-on experience indicator)
6. **Internships** (Industry exposure indicator)

### 4.2 Target Variable & Package Policy
- **Target Variable (`placed`):** Binary outcome (1 = Placed, 0 = Unplaced). Target placement rate: **60%–70%**.
- **Placed Students (`placed = 1`):** `company_type` is non-null (`Product`, `Service`, `Startup`, `Other`); `package_lpa` is a positive float (>0.0 to 50.0 LPA).
- **Unplaced Students (`placed = 0`):** `company_type` is `NULL`; `package_lpa` is `NULL`. Unplaced students are **never** assigned `package_lpa = 0.0`.

### 4.3 Branch Distribution Strategy
Target allocation across 6 branches:
- `CSE` (Computer Science): ~30% (~450)
- `IT` (Information Technology): ~25% (~375)
- `ECE` (Electronics & Comm.): ~20% (~300)
- `EEE` (Electrical & Electronics): ~10% (~150)
- `ME` (Mechanical Eng.): ~8% (~120)
- `CE` (Civil Eng.): ~7% (~105)

### 4.4 Demographic Policy (Age & Gender)
- **Age:** Synthetic values between 18 and 25 (mean ~21.5).
- **Gender:** Synthetic distribution: `Female` (~40%), `Male` (~55%), `Non-binary` (~3%), `Prefer not to say` (~2%). Included strictly for aggregate exploratory visualization; excluded from placement scoring algorithms and screening rules.

---

## 5. Synthetic Generation Principles

1. **Realism:** Generate plausible continuous and discrete distributions (e.g. CGPA ~ Normal(7.2, 1.1) clipped to [0, 10]).
2. **Probabilistic Outcomes:** Outcome `placed` is generated probabilistically via a logistic function of CGPA, skills, assessment scores, and experience plus random noise ($\sigma$). No single threshold (e.g., CGPA > 8.0) deterministically guarantees placement.
3. **No Data Leakage:** No synthetic feature is created that directly reveals `placed`.
4. **No Pre-determined Conclusions:** Analytical findings must emerge naturally from probabilistic generation rules rather than hard-coded rules.

---

## 6. Controlled Raw Data Quality Defect Strategy

To validate Phase 2 data cleaning pipelines, controlled defects will be injected into `data/raw/placementlens_students_raw.csv`:

| Defect Type | Target Fields | Defect Rate | Handling / Recovery Plan |
|---|---|---|---|
| Case Inconsistency | `branch`, `company_type` | ~2.0% | Test `str.upper()` / `str.title()` standardization. |
| Whitespace Padding | `branch`, `gender`, `company_type` | ~1.5% | Test `str.strip()` stripping routines. |
| String-Binary Representation | `python_skill`, `placed` | ~1.0% | Test boolean mapping to integer `0`/`1`. |
| Missing Non-Critical Value | `communication_score`, `projects` | ~1.0% | Test documented median/mode imputation routines. |
| Duplicate Raw Rows | `student_id` | ~0.5% (5–8 rows) | Test deduplication logic retaining first valid row. |

---

## 7. Reproducibility & Versioning

- **Random Seed:** `SEED = 42` (Python `numpy` & `random`)
- **Dataset Version:** `v1.0`
- **Raw Artifact Path:** `data/raw/placementlens_students_raw.csv`
- **Clean Artifact Path:** `data/processed/placementlens_students_clean.csv` (Phase 2 output)

---

## 8. Decision Log Table

| Decision Area | Selected Decision | Primary Rationale |
|---|---|---|
| **Dataset Type** | Synthetic Dataset | Student data privacy protection (Zero PII), no licensing risks, full control over schema & defects. |
| **Dataset Size** | 1,500 Student Records | Provides adequate statistical sample per branch while maintaining fast query and DAX performance. |
| **Database System** | PostgreSQL | Strong SQL interview portfolio demonstration (CTEs, Window Functions, Schema management). |
| **Target Variable** | `placed` (Binary 0/1) | Primary placement outcome for binary classification and rate analysis. |
| **Package Policy** | `NULL` when unplaced | Preserves distinction between "unplaced" (`NULL`) and "zero package". |
| **Company Categories** | Product, Service, Startup, Other | Standardized recruiter categories covering major hiring segments. |
| **Branch Scope** | 6 Branches (CSE, IT, ECE, EEE, ME, CE) | Covers tech and core engineering departments with realistic proportion weights. |
| **Demographics** | Retain Age & Gender (Aggregates only) | Explores aggregate trends without influencing placement scoring or readiness index logic. |
| **Defect Strategy** | Controlled, documented raw defects | Demonstrates data-quality validation and ETL cleaning pipelines in Phase 2. |
| **Reproducibility** | Fixed Seed (`42`), Version `v1.0` | Enables reproducible generation across all developer environments. |

---

## 9. Part 1 Validation Checklist

- [x] Dataset type finalized (Synthetic)
- [x] Dataset size finalized (1,500 records)
- [x] Variable list finalized (20 approved fields)
- [x] Variable classifications finalized (8 classifications A–H)
- [x] Target variable finalized (`placed` binary 0/1)
- [x] Package policy finalized (`placed=1` ↔ package > 0 & company non-null; `placed=0` ↔ both `NULL`)
- [x] Branch strategy finalized (6 branches with documented distribution)
- [x] Skill representation finalized (7 binary skill flags)
- [x] Synthetic-data principles documented (Realism, Variation, Imperfect relationships, No leakage)
- [x] Reproducibility strategy documented (`SEED = 42`, `v1.0`)
- [x] Controlled defect strategy documented (Case, whitespace, string binary, missing non-critical, duplicate rows)
- [x] Privacy strategy documented (Synthetic disclosure, zero PII, non-discriminatory gender policy)
- [x] Distribution checks documented (Branch, class balance, package skew, score bounds)
- [x] Data dictionary updated (`00_project_blueprint/11_data_dictionary.md`)
- [x] Dataset specification updated (`00_project_blueprint/10_dataset_specification.md`)
- [x] No unresolved critical design conflicts
- [x] Phase 0 scope has not been violated
