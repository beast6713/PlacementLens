# Phase 1 Part 3: Dataset Generation Specification & Profiling

**Dataset Version:** `v1.0`  
**Generator Script:** `scripts/generate_dataset.py`  
**Fixed Random Seed:** `SEED = 42`  
**Generation Date:** `2026-09-16`  
**Primary Raw Artifact:** `data/raw/placementlens_students_raw.csv`  
**Raw Alias Artifact:** `data/raw/placement_raw.csv`  
**Defect Manifest Artifact:** `data/raw/raw_defect_manifest.csv`  
**MD5 Hash Signature:** `ed3f94bd8a6e87f3473f32483aece776`

---

## 1. Generation Executive Summary

In Phase 1 Part 3, the canonical synthetic raw dataset for **PlacementLens** was generated using deterministic probabilistic algorithms in Python. The dataset models 1,500 unique student records across 6 engineering branches, capturing academic performance, 7 technical skill flags, assessment scores, internship/project experience, placement outcomes, recruiter company categories, and compensation packages (LPA).

---

## 2. Intended Population vs. Physical Raw CSV Rows

| Metric | Value | Description |
|---|---|---|
| **Intended Unique Students** | **1,500** | Canonical student population (`S0001`–`S1500`) |
| **Physical Raw CSV Rows** | **1,505** | Includes 5 controlled duplicate student rows injected for Phase 2 deduplication testing |
| **Duplicate Count** | **5** | Rows duplicating `S0120`, `S0450`, `S0780`, `S1100`, `S1350` at the file tail |

---

## 3. Variable Generation Logic & Distributions

### 3.1 Demographics & Academics
- **Student ID:** Format `S0001` to `S1500` (1,500 unique keys).
- **Age:** Normal distribution $\sim N(21.5, 1.1)$, clipped to integer range [18, 25].
- **Gender:** Probabilistic choice: `Female` (40.0%), `Male` (55.0%), `Non-binary` (3.0%), `Prefer not to say` (2.0%). Excluded from placement decision logic.
- **Branch:** Exact allocation across 6 departments:
  - `CSE` (Computer Science): 450 (30.0%)
  - `IT` (Information Technology): 375 (25.0%)
  - `ECE` (Electronics & Comm.): 300 (20.0%)
  - `EEE` (Electrical & Electronics): 150 (10.0%)
  - `ME` (Mechanical Eng.): 120 (8.0%)
  - `CE` (Civil Eng.): 105 (7.0%)
- **CGPA:** Normal distribution $\sim N(7.3, 1.1)$, clipped to [4.00, 9.85], rounded to 2 decimal places.

### 3.2 Experience & Assessment Scores
- **Internships:** Discrete distribution (0: 45%, 1: 35%, 2: 14%, 3: 4%, 4: 1.5%, 5: 0.5%).
- **Projects:** Discrete distribution (0: 10%, 1: 25%, 2: 35%, 3: 18%, 4+: 12%).
- **Coding Score:** Function of CGPA and projects plus Gaussian noise $\sim N(0, 10)$, clipped to [25.0, 98.5].
- **Aptitude Score:** Function of CGPA plus Gaussian noise $\sim N(0, 11)$, clipped to [30.0, 97.0].
- **Communication Score:** Independent performance metric $\sim N(55, 14)$ + minor CGPA influence, clipped to [35.0, 96.0].

### 3.3 Technical Skill Flags (0 or 1)
Prevalence rates generated via conditional probability functions based on coding scores and branch:
- `python_skill`: ~54.8% prevalence
- `sql_skill`: ~59.2% prevalence
- `excel_skill`: ~69.5% prevalence
- `power_bi_skill`: ~34.1% prevalence
- `dsa_skill`: ~41.3% prevalence
- `cloud_skill`: ~24.6% prevalence
- `cybersecurity_skill`: ~17.9% prevalence

### 3.4 Placement Outcome & Compensation (`placed`, `company_type`, `package_lpa`)
- **Probabilistic Placement Sampling:** Latent preparation index calculated from weighted combination of CGPA (22%), coding (22%), aptitude (18%), communication (15%), internships (10%), projects (8%), and skill count (5%). Logit sampling with noise generates a **64.07% placement rate** (961 placed, 539 unplaced).
- **Unplaced Policy (`placed = 0`):** `company_type = NULL` and `package_lpa = NULL` (100% compliant, never 0.00).
- **Placed Policy (`placed = 1`):** `company_type` distributed across `Service` (502), `Product` (268), `Startup` (135), `Other` (56). `package_lpa` log-normally generated with median **6.40 LPA** (Range: 3.20 LPA to 44.75 LPA).

---

## 4. Controlled Defect Manifest Summary

A total of **95 controlled raw defects** were injected after clean validation and logged in `data/raw/raw_defect_manifest.csv`:

| Defect Type | Target Field(s) | Count | Purpose / Phase 2 Recovery Action |
|---|---|---|---|
| **Case Inconsistency** | `branch` | 25 rows | Test `str.upper()` normalization (e.g., `"cse"` $\rightarrow$ `"CSE"`). |
| **Case & Space Inconsistency** | `company_type` | 15 rows | Test whitespace stripping & titlecase (e.g., `"service "` $\rightarrow$ `"Service"`). |
| **Whitespace Padding** | `gender` | 20 rows | Test `str.strip()` stripping routines. |
| **String Binary Variant** | `python_skill` | 15 rows | Test boolean mapping (e.g., `"Yes"` $\rightarrow$ `1`, `"No"` $\rightarrow$ `0`). |
| **Missing Non-Critical Value** | `communication_score` | 15 rows | Test median imputation routines in Phase 2. |
| **Duplicate Raw Row** | `student_id` | 5 rows | Test deduplication keeping first valid record. |

---

## 5. Verification & Reproducibility Results

1. **Clean Data Integrity Check:** 100% passed prior to defect injection.
2. **Raw Defect Isolation Check:** All injected defects verified against `raw_defect_manifest.csv`. No unapproved corruption introduced.
3. **Reproducibility Test:** Running `python scripts/generate_dataset.py` twice yields identical byte-for-byte MD5 signatures (`ed3f94bd8a6e87f3473f32483aece776`).
