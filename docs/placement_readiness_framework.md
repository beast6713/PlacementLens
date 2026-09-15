# PlacementLens — Placement Readiness Index (PRI) Specification Framework

> **Document Status:** FROZEN & APPROVED FOR P4-P5 IMPLEMENTATION  
> **Phase:** Phase 4 — Insights & Placement Readiness  
> **Part:** P4-P4 — Placement Readiness Framework  
> **Author:** Analytics Architect & Data Science Lead  

---

## 1. Purpose & Analytical Context

This document defines the mathematical, conceptual, governance, and validation specification for the **Placement Readiness Index (PRI)** in the **PlacementLens** analytics project.

The primary objective of the Placement Readiness Index is to synthesize a student's observed, pre-placement preparation profile into a single, standardized, $0 - 100$ composite index. By consolidating technical competencies, academic performance, cognitive aptitude, practical project execution, industry internship experience, and professional communication skills, the PRI provides a transparent, explainable foundation for student-level readiness assessment and institutional intervention planning.

---

## 2. Scope & Target Audience

This specification covers:
- The mathematical definition of all six component scores and normalization rules.
- The weight allocation rationale and weight sum integrity assertions.
- Missing-value policies, NULL semantics, and numerical rounding rules.
- Readiness category thresholds, boundary definitions, and classification logic.
- Target leakage controls, demographic exclusions, and fairness policies.
- Monotonicity, determinism, reproducibility, and sensitivity guidelines.
- The P4-P5 implementation contract and automated test specifications.

**Target Audience:** Analytics engineers, data scientists, Power BI dashboard designers, academic advisors, and interview auditors evaluating the PlacementLens analytical methodology.

---

## 3. PRI Definition & Conceptual Scope

The **Placement Readiness Index (PRI)** is a **PROJECT-DESIGNED ANALYTICAL FRAMEWORK**.

### 3.1 What the PRI Is:
- A transparent, multi-dimensional score summarizing student preparation effort across six observable dimensions.
- A deterministic, reproducible weighted composite index bounded between $0.00$ and $100.00$.
- A tool for institutional benchmarking, identifying cohort skill gaps, and prioritizing career guidance resources.

### 3.2 What the PRI Is NOT:
- **NOT** an industry-certified credential, hiring score, or recruitment decision engine.
- **NOT** a guaranteed predictor or statistical probability of job placement.
- **NOT** a causal model (it does not claim that increasing PRI by $X$ points *causes* placement).
- **NOT** a machine-learning prediction or black-box statistical score.
- **NOT** an employer assessment or third-party rating.

---

## 4. Component Architecture & Variable Mapping

The PRI is composed of six distinct pre-placement preparation dimensions:

```
                                  ┌─────────────────────────────────────────┐
                                  │    PLACEMENT READINESS INDEX (0-100)    │
                                  └────────────────────┬────────────────────┘
                                                       │
   ┌──────────────┬──────────────┬─────────────────────┼─────────────────────┬──────────────┐
   ▼              ▼              ▼                     ▼                     ▼              ▼
Technical Skills Aptitude Score CGPA (Academic) Practical Projects Industry Internships Communication
  Weight: 25%    Weight: 20%    Weight: 15%           Weight: 15%           Weight: 15%    Weight: 10%
```

| Component ID | Component Name | Source Variable(s) | Raw Scale | Normalized Scale ($S_k$) | Weight ($w_k$) | Max Points |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| `PRI-C01` | Technical Skills | `python_skill`, `sql_skill`, `excel_skill`, `power_bi_skill`, `dsa_skill`, `cloud_skill`, `cybersecurity_skill` | $0 - 7$ | $0 - 100$ | **25%** ($0.25$) | $25.0$ |
| `PRI-C02` | Aptitude Score | `aptitude_score` | $0 - 100$ | $0 - 100$ | **20%** ($0.20$) | $20.0$ |
| `PRI-C03` | CGPA (Academics) | `cgpa` | $0.0 - 10.0$ | $0 - 100$ | **15%** ($0.15$) | $15.0$ |
| `PRI-C04` | Practical Projects | `projects` | $0 - N$ | $0 - 100$ | **15%** ($0.15$) | $15.0$ |
| `PRI-C05` | Industry Internships | `internships` | $0 - N$ | $0 - 100$ | **15%** ($0.15$) | $15.0$ |
| `PRI-C06` | Communication Skills| `communication_score` | $0 - 100$ | $0 - 100$ | **10%** ($0.10$) | $10.0$ |
| **TOTAL** | | | | | **100%** (**1.00**) | **100.0** |

---

## 5. Weight Breakdown Table & Rationale

The project-defined baseline weights reflect relative analytical emphasis established in campus placement preparation literature:
- **Technical Skills (25%):** Technical competency is the primary threshold filter in software and analytics hiring.
- **Aptitude Score (20%):** Quantitative and logical aptitude serves as the initial screening gate across campus recruitment drives.
- **CGPA (15%):** Academic grade point average establishes institutional eligibility and shortlisting thresholds.
- **Projects (15%):** Practical project count reflects hands-on application of engineering tools and analytical methods.
- **Internships (15%):** Industry internships validate real-world work experience, teamwork, and corporate exposure.
- **Communication (10%):** Communication score captures interpersonal readiness, articulation, and HR interview suitability.

### Mandatory Weight Validation Assertion:
$$\sum_{k=1}^{6} w_k = 0.25 + 0.20 + 0.15 + 0.15 + 0.15 + 0.10 = 1.000000 \quad (100.0\%)$$

No implementation may proceed if any weight is missing, negative, or if the total weight sum deviates from $1.00$.

---

## 6. Normalization Formulas

To ensure fair combination across disparate measurement scales, each raw variable is transformed into a standardized sub-score $S_k \in [0, 100]$.

---

## 7. Component 1 — Technical Skill Normalization

- **Source Variables:** Seven binary indicators (`python_skill`, `sql_skill`, `excel_skill`, `power_bi_skill`, `dsa_skill`, `cloud_skill`, `cybersecurity_skill`).
- **Raw Metric:** `technical_skill_count` = $\sum_{m=1}^{7} \text{skill}_m \in [0, 7]$.
- **Normalization Formula:**
$$S_{\text{tech}} = \left( \frac{\text{technical\_skill\_count}}{7.0} \right) \times 100.0$$

- **Discrete Mapping:**
  - $0 \text{ skills} = 0.0000$
  - $1 \text{ skill}  = 14.2857$
  - $2 \text{ skills} = 28.5714$
  - $3 \text{ skills} = 42.8571$
  - $4 \text{ skills} = 57.1429$
  - $5 \text{ skills} = 71.4286$
  - $6 \text{ skills} = 85.7143$
  - $7 \text{ skills} = 100.0000$

---

## 8. Component 2 — Aptitude Score Normalization

- **Source Variable:** `aptitude_score`.
- **Raw Metric Range:** $0 - 100$.
- **Normalization Formula:**
$$S_{\text{apt}} = \text{aptitude\_score}$$
Direct identity mapping since raw aptitude scores already exist on a validated $0 - 100$ scale. Any value outside $[0, 100]$ triggers an immediate pipeline validation failure.

---

## 9. Component 3 — CGPA Normalization

- **Source Variable:** `cgpa`.
- **Raw Academic Scale:** $0.0 - 10.0$.
- **Normalization Formula:**
$$S_{\text{cgpa}} = \left( \frac{\text{cgpa}}{10.0} \right) \times 100.0 = \text{cgpa} \times 10.0$$

- **Representative Scale:**
  - $5.0 \text{ CGPA} \rightarrow 50.00$
  - $6.0 \text{ CGPA} \rightarrow 60.00$
  - $7.0 \text{ CGPA} \rightarrow 70.00$
  - $8.0 \text{ CGPA} \rightarrow 80.00$
  - $9.0 \text{ CGPA} \rightarrow 90.00$
  - $10.0 \text{ CGPA} \rightarrow 100.00$

---

## 10. Component 4 — Project Normalization (Cap Rule)

- **Source Variable:** `projects` (integer count).
- **Transformation Strategy:** Linear normalization with a saturation cap at `PROJECT_CAP = 3` projects to prevent extreme outlier count distortion.
- **Normalization Formula:**
$$S_{\text{proj}} = \min\left( \frac{\text{projects}}{3.0}, \, 1.0 \right) \times 100.0$$

- **Behavior:**
  - $0 \text{ projects} = 0.00$
  - $1 \text{ project}  = 33.3333$
  - $2 \text{ projects} = 66.6667$
  - $3+ \text{ projects} = 100.00$

---

## 11. Component 5 — Internship Normalization (Cap Rule)

- **Source Variable:** `internships` (integer count).
- **Transformation Strategy:** Linear normalization with a saturation cap at `INTERNSHIP_CAP = 2` internships.
- **Normalization Formula:**
$$S_{\text{intern}} = \min\left( \frac{\text{internships}}{2.0}, \, 1.0 \right) \times 100.0$$

- **Behavior:**
  - $0 \text{ internships} = 0.00$
  - $1 \text{ internship}  = 50.00$
  - $2+ \text{ internships} = 100.00$

---

## 12. Component 6 — Communication Score Normalization

- **Source Variable:** `communication_score`.
- **Raw Metric Range:** $0 - 100$.
- **Normalization Formula:**
$$S_{\text{comm}} = \text{communication\_score}$$
Direct identity mapping on $0 - 100$ scale.

---

## 13. Missing-Value Policy & Imputation Prohibition

- **Null Semantics:** `NULL` is NOT automatically $0$, `FALSE`, or "No skill".
- **Strict Validation Policy:** If any required input attribute for PRI calculation is unexpectedly `NULL` in `placementlens_students_clean.csv`, the calculation engine MUST **FAIL VALIDATION** and halt.
- **No Ad-Hoc Imputation:** No silent imputation (e.g. replacing `NULL` with mean, median, or zero) is permitted during P4-P4 or P4-P5. The input dataset was fully validated in Phase 2; missing required inputs indicate dataset corruption.

---

## 14. Detailed NULL Semantics Matrix

| Input Variable | Expected NULL Count | Operational Treatment if Unexpected NULL Encountered |
| :--- | :---: | :--- |
| `student_id` | 0 | **FAIL VALIDATION.** Primary Key Integrity Violation. |
| `cgpa` | 0 | **FAIL VALIDATION.** Mandatory Academic Input Missing. |
| `aptitude_score` | 0 | **FAIL VALIDATION.** Mandatory Screening Input Missing. |
| `communication_score` | 0 | **FAIL VALIDATION.** Mandatory Soft Skill Input Missing. |
| `projects` | 0 | **FAIL VALIDATION.** Mandatory Project Count Missing. |
| `internships` | 0 | **FAIL VALIDATION.** Mandatory Internship Count Missing. |
| Skill Variables (`python_skill`, etc.) | 0 | **FAIL VALIDATION.** Mandatory Skill Indicator Missing. |
| `placed` | 0 | Excluded from PRI formula. Used in P4-P5 outcome evaluation. |
| `package_lpa` | 550 (Unplaced) | Preserved as `NULL` for unplaced. Excluded from PRI formula. |
| `company_type` | 550 (Unplaced) | Preserved as `NULL` for unplaced. Excluded from PRI formula. |

---

## 15. Rounding & Precision Policy

- **Internal Calculation Precision:** Full 64-bit floating-point precision (`float64`) MUST be retained across all component normalization steps and weighted summation. No premature rounding of sub-scores is permitted.
- **Display & Export Precision:** Final composite PRI scores and sub-scores exported to CSV or displayed in Power BI reports are rounded to exactly **two decimal places** ($0.01$ precision) using half-up round rules.
- **Example:** $72.846291 \rightarrow 72.85$.

---

## 16. Composite PRI Mathematical Formula & Proof

### 16.1 Mathematical Formula
For student $i$:
$$\text{PRI}_i = 0.25 \, S_{\text{tech}, i} + 0.20 \, S_{\text{apt}, i} + 0.15 \, S_{\text{cgpa}, i} + 0.15 \, S_{\text{proj}, i} + 0.15 \, S_{\text{intern}, i} + 0.10 \, S_{\text{comm}, i}$$

### 16.2 Proof of Upper and Lower Bounds
- **Maximum Theoretical Bound:**
$$\text{PRI}_{\max} = 0.25(100) + 0.20(100) + 0.15(100) + 0.15(100) + 0.15(100) + 0.10(100) = 25 + 20 + 15 + 15 + 15 + 10 = 100.00$$

- **Minimum Theoretical Bound:**
$$\text{PRI}_{\min} = 0.25(0) + 0.20(0) + 0.15(0) + 0.15(0) + 0.15(0) + 0.10(0) = 0.00$$

- **Conclusion:** $0.00 \le \text{PRI}_i \le 100.00$ for all valid student profiles.

---

## 17. Component Contribution Breakdown

To ensure transparency and explainability, every student score can be decomposed into exact point contributions:

$$\text{Contribution}_k = w_k \times S_k$$

- Technical Contribution: $\le 25.0 \text{ points}$
- Aptitude Contribution: $\le 20.0 \text{ points}$
- CGPA Contribution: $\le 15.0 \text{ points}$
- Project Contribution: $\le 15.0 \text{ points}$
- Internship Contribution: $\le 15.0 \text{ points}$
- Communication Contribution: $\le 10.0 \text{ points}$

**Sum of Contributions:** $\sum_{k=1}^6 \text{Contribution}_k = \text{PRI}$.

---

## 18. Readiness Categories & Operational Definitions

Students are categorized into four project-defined Readiness Tiers:

| Readiness Category | Score Range ($\text{PRI}$) | Category Description & Intervention Strategy |
| :--- | :---: | :--- |
| **High Readiness** | $80.00 - 100.00$ | Excellent multi-dimensional preparation. Recommended for tier-1 campus drives and peer mentoring roles. |
| **Moderate Readiness** | $60.00 - 79.99$ | Solid foundational profile. Recommended for targeted technical skill workshops and mock interviews. |
| **Needs Improvement** | $40.00 - 59.99$ | Moderate preparation deficits across core dimensions. Intensive bootcamp and academic tutoring required. |
| **High Improvement Priority** | $0.00 - 39.99$ | Substantial gaps across technical, academic, or aptitude areas. Immediate priority remediation required. |

---

## 19. Boundary Rules & Edge-Case Evaluation

Category boundaries are continuous, mutually exclusive, and exhaustive:
- $\text{PRI} \ge 80.00 \rightarrow$ **High Readiness**
- $60.00 \le \text{PRI} < 80.00 \rightarrow$ **Moderate Readiness**
- $40.00 \le \text{PRI} < 60.00 \rightarrow$ **Needs Improvement**
- $\text{PRI} < 40.00 \rightarrow$ **High Improvement Priority**

### Explicit Boundary Test Cases:
- $39.99 \rightarrow$ High Improvement Priority
- $40.00 \rightarrow$ Needs Improvement
- $59.99 \rightarrow$ Needs Improvement
- $60.00 \rightarrow$ Moderate Readiness
- $79.99 \rightarrow$ Moderate Readiness
- $80.00 \rightarrow$ High Readiness
- $100.00 \rightarrow$ High Readiness
- $0.00 \rightarrow$ High Improvement Priority

---

## 20. Target Leakage Matrix & Audit Controls

Target leakage occurs when post-placement outcome information influences pre-placement readiness scores.

### Target Leakage Control Rules:
1. `placed`, `package_lpa`, and `company_type` are **STRICTLY PROHIBITED** from the PRI formula, normalization functions, and weighting decisions.
2. PRI weights were established *a priori* based on structural framework rules, NOT by optimizing correlation with placement outcomes.
3. Outcome variables are reserved exclusively for post-calculation validation and descriptive evaluation in P4-P5.

---

## 21. Demographic Exclusions & Bias Controls

- **Excluded Variables:** `gender`, `age`, `branch`.
- **Governance Rationale:** Demographics do not represent student preparation effort. Including them would introduce structural bias into the readiness index.
- **Subgroup Analysis:** Demographic attributes may be used downstream in P4-P5 to conduct fairness reviews and branch-level descriptive summaries, but they MUST NOT alter individual student scores or category assignments.

---

## 22. Branch Handling Strategy

The exact same PRI formula, component weights, caps, and category thresholds apply uniformly across all academic branches (`CSE`, `ECE`, `EEE`, `ME`, `CE`, `IT`). Branch-specific weighting is strictly prohibited to maintain standardized cross-institutional comparability.

---

## 23. Relationship to P4-P3 Student Segmentation

P4-P3 preparation segments (e.g. *Full-Stack Analytical Ready*, *Academic Specialist*, *Aptitude-Dominant*, *High Need*) represent unsupervised, multi-attribute clustering profiles.
- PRI calculation is **INDEPENDENT** of segment membership.
- Segment labels are NOT inputs to PRI.
- In P4-P5, cross-tabulations between PRI readiness categories and P4-P3 preparation segments will be generated for descriptive comparison.

---

## 24. Explicit Coding Score Decision

- **Decision:** `coding_score` is **EXCLUDED** from the baseline PRI formula.
- **Rationale:** The frozen P4-P1 six-component framework specifies `technical_skill_count` (25%), `aptitude_score` (20%), `cgpa` (15%), `projects` (15%), `internships` (15%), and `communication_score` (10%). Modifying this formula to include `coding_score` would alter frozen project weights.
- **Analytical Role:** `coding_score` remains available in the clean dataset for standalone bivariate evaluation against PRI and placement outcomes in P4-P5.

---

## 25. Weight Sensitivity & Robustness Policy

- **Purpose:** Sensitivity analysis tests whether minor, reasonable weight adjustments materially alter student tier classifications.
- **Policy:**
  - Sensitivity checks will be executed in P4-P5 using alternative weight scenarios (e.g. Equal Weights: 16.67% each; Tech-Heavy: 35% Tech, 15% others).
  - Sensitivity checks MUST NOT alter the baseline frozen PRI weights.
  - Rank correlation (Spearman's $\rho$) and category classification overlap (%) will be reported.

---

## 26. Validation Requirements & Assertion Specifications

P4-P5 implementation must pass 14 automated validation checks (`VAL-P4-01` through `VAL-P4-14`):
1. **Formula Validation:** Sub-scores and PRI match symbolic formulas.
2. **Weight Validation:** $\sum w_k = 1.000000$.
3. **Range Validation:** $0.00 \le \text{PRI}_i \le 100.00$.
4. **Null Validation:** Zero unexpected NULLs.
5. **Boundary Validation:** Test cases TC04-TC09 pass exactly.
6. **Category Validation:** 100% of records mapped to exactly one category.
7. **Leakage Validation:** Zero outcome variables in feature set.
8. **Monotonicity Validation:** $\frac{\partial \text{PRI}}{\partial \text{Input}} \ge 0$.
9. **Contribution Validation:** $\sum \text{Contribution}_k = \text{PRI}$.
10. **Determinism Validation:** Run 1 outcome == Run 2 outcome.
11. **Reproducibility Validation:** Pipeline runs cleanly from script + dataset.
12. **Sensitivity Validation:** Sensitivity scenarios evaluated without altering baseline.
13. **Cross-Check Validation:** Manual calculations match machine output within $\pm 0.01$.
14. **Documentation Validation:** Code comments reference P4-P4 specification.

---

## 27. Change Control Protocol

Any proposed modification to the frozen PRI specification (weights, caps, formulas, thresholds) after P4-P4 freeze requires:
1. Formal Change Request documenting: `Change ID`, `Prior Rule`, `Proposed Rule`, `Technical Justification`, `Impact Analysis`.
2. Re-execution of full P4 validation suite.
3. Explicit change log logging in `00_project_blueprint/29_change_log.md`.

---

## 28. P4-P5 Implementation Contract & Power BI Readiness

The P4-P5 execution engine will produce student-level CSV outputs containing raw variables, normalized sub-scores, point contributions, composite PRI score, and readiness category.

### Power BI Data Model Integration:
- **Primary Key:** `student_id` (1:1 relationship with `placementlens_students_clean.csv`).
- **Dashboard Measures:** Average PRI, Median PRI, Category Distribution (%), Component Contribution Stacked Bar, Observed Placement Rate by PRI Category.

---
