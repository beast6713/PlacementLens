import os
import sys
import hashlib
import pandas as pd

def compute_md5(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def main():
    print("=== STARTING P4-P4 PLACEMENT READINESS FRAMEWORK DESIGN & FREEZE ===")
    
    clean_csv = "data/processed/placementlens_students_clean.csv"
    raw_csv = "data/raw/placementlens_students_raw.csv"
    
    expected_clean_hash = "96023d297eec5a9a47563eaddc157d0d"
    expected_raw_hash = "59c04ee15a0112806c510225d8e75779"
    
    clean_hash = compute_md5(clean_csv)
    raw_hash = compute_md5(raw_csv)
    
    print(f"Clean CSV MD5: {clean_hash} (Expected: {expected_clean_hash})")
    print(f"Raw CSV MD5:   {raw_hash} (Expected: {expected_raw_hash})")
    
    assert clean_hash == expected_clean_hash, "Clean dataset MD5 hash mismatch!"
    assert raw_hash == expected_raw_hash, "Raw dataset MD5 hash mismatch!"
    print("[PASS] Dataset MD5 Verification Successful.")

    os.makedirs("outputs/phase4_strategy", exist_ok=True)
    os.makedirs("docs", exist_ok=True)
    os.makedirs("00_project_blueprint", exist_ok=True)

    # ---------------------------------------------------------
    # 1. GENERATE outputs/phase4_strategy/pri_component_matrix.csv
    # ---------------------------------------------------------
    component_matrix_data = [
        {
            "component": "Technical Skills",
            "source_variables": "python_skill, sql_skill, excel_skill, power_bi_skill, dsa_skill, cloud_skill, cybersecurity_skill",
            "raw_range": "0-7 (Count of binary indicators)",
            "normalized_range": "0-100",
            "formula": "(technical_skill_count / 7.0) * 100.0",
            "weight": "25%",
            "maximum_contribution": "25.0 PRI points",
            "missing_policy": "Explicit binary (1/0). Unexpected NULL triggers validation failure.",
            "validation_rule": "Range [0, 100], discrete steps of ~14.2857%",
            "leakage_status": "NO LEAKAGE (Pre-placement skill indicator)",
            "interpretation": "Breadth of core technical, data, cloud, and security skill coverage"
        },
        {
            "component": "Aptitude Score",
            "source_variables": "aptitude_score",
            "raw_range": "0-100",
            "normalized_range": "0-100",
            "formula": "aptitude_score",
            "weight": "20%",
            "maximum_contribution": "20.0 PRI points",
            "missing_policy": "Complete cases required. Unexpected NULL triggers validation failure.",
            "validation_rule": "Range [0, 100]. Out of bounds triggers validation error.",
            "leakage_status": "NO LEAKAGE (Pre-placement cognitive test score)",
            "interpretation": "Quantitative, analytical, and logical reasoning aptitude"
        },
        {
            "component": "CGPA",
            "source_variables": "cgpa",
            "raw_range": "0.0-10.0",
            "normalized_range": "0-100",
            "formula": "(cgpa / 10.0) * 100.0",
            "weight": "15%",
            "maximum_contribution": "15.0 PRI points",
            "missing_policy": "Complete cases required. Unexpected NULL triggers validation failure.",
            "validation_rule": "Range [0.0, 10.0] raw -> [0, 100] normalized.",
            "leakage_status": "NO LEAKAGE (Cumulative academic grade point average)",
            "interpretation": "Academic consistency and foundational domain performance"
        },
        {
            "component": "Projects",
            "source_variables": "projects",
            "raw_range": "0-N (Integer count)",
            "normalized_range": "0-100",
            "formula": "MIN(projects / 3.0, 1.0) * 100.0",
            "weight": "15%",
            "maximum_contribution": "15.0 PRI points",
            "missing_policy": "Complete cases required. Unexpected NULL triggers validation failure.",
            "validation_rule": "Bounded cap at 3 projects (PROJECT_CAP=3). Saturation above 3.",
            "leakage_status": "NO LEAKAGE (Pre-placement practical project count)",
            "interpretation": "Practical application of engineering/analytics tools"
        },
        {
            "component": "Internships",
            "source_variables": "internships",
            "raw_range": "0-N (Integer count)",
            "normalized_range": "0-100",
            "formula": "MIN(internships / 2.0, 1.0) * 100.0",
            "weight": "15%",
            "maximum_contribution": "15.0 PRI points",
            "missing_policy": "Complete cases required. Unexpected NULL triggers validation failure.",
            "validation_rule": "Bounded cap at 2 internships (INTERNSHIP_CAP=2). Saturation above 2.",
            "leakage_status": "NO LEAKAGE (Pre-placement industry internship count)",
            "interpretation": "Direct industry experience and work environment exposure"
        },
        {
            "component": "Communication",
            "source_variables": "communication_score",
            "raw_range": "0-100",
            "normalized_range": "0-100",
            "formula": "communication_score",
            "weight": "10%",
            "maximum_contribution": "10.0 PRI points",
            "missing_policy": "Complete cases required. Unexpected NULL triggers validation failure.",
            "validation_rule": "Range [0, 100]. Out of bounds triggers validation error.",
            "leakage_status": "NO LEAKAGE (Pre-placement interpersonal/interview assessment)",
            "interpretation": "Soft skills, verbal expression, and professional presentation readiness"
        }
    ]
    df_component_matrix = pd.DataFrame(component_matrix_data)
    df_component_matrix.to_csv("outputs/phase4_strategy/pri_component_matrix.csv", index=False, encoding="utf-8")
    print("[CREATED] outputs/phase4_strategy/pri_component_matrix.csv")

    # ---------------------------------------------------------
    # 2. GENERATE outputs/phase4_strategy/pri_weight_matrix.csv
    # ---------------------------------------------------------
    weight_matrix_data = [
        {
            "component": "Technical Skills",
            "weight_percent": 25.0,
            "weight_decimal": 0.25,
            "maximum_points": 25.0,
            "rationale": "Highest single predictor dimension in technical campus placement baseline.",
            "placement_used_for_weight_selection": False
        },
        {
            "component": "Aptitude Score",
            "weight_percent": 20.0,
            "weight_decimal": 0.20,
            "maximum_points": 20.0,
            "rationale": "Core screening filter across campus placement written rounds.",
            "placement_used_for_weight_selection": False
        },
        {
            "component": "CGPA",
            "weight_percent": 15.0,
            "weight_decimal": 0.15,
            "maximum_points": 15.0,
            "rationale": "Academic eligibility criterion for initial company shortlisting.",
            "placement_used_for_weight_selection": False
        },
        {
            "component": "Projects",
            "weight_percent": 15.0,
            "weight_decimal": 0.15,
            "maximum_points": 15.0,
            "rationale": "Demonstration of practical coding, analytical, and problem-solving execution.",
            "placement_used_for_weight_selection": False
        },
        {
            "component": "Internships",
            "weight_percent": 15.0,
            "weight_decimal": 0.15,
            "maximum_points": 15.0,
            "rationale": "Industry exposure, professional teamwork, and corporate readiness.",
            "placement_used_for_weight_selection": False
        },
        {
            "component": "Communication",
            "weight_percent": 10.0,
            "weight_decimal": 0.10,
            "maximum_points": 10.0,
            "rationale": "HR interview performance and interpersonal collaboration capacity.",
            "placement_used_for_weight_selection": False
        }
    ]
    df_weight_matrix = pd.DataFrame(weight_matrix_data)
    df_weight_matrix.to_csv("outputs/phase4_strategy/pri_weight_matrix.csv", index=False, encoding="utf-8")
    print("[CREATED] outputs/phase4_strategy/pri_weight_matrix.csv")

    # Verify weight sum
    total_pct = df_weight_matrix["weight_percent"].sum()
    total_dec = df_weight_matrix["weight_decimal"].sum()
    assert total_pct == 100.0, f"Weight percentage sum mismatch: {total_pct}"
    assert abs(total_dec - 1.00) < 1e-7, f"Weight decimal sum mismatch: {total_dec}"
    print(f"[PASS] Weight sum mathematically verified: {total_pct}% = {total_dec}")

    # ---------------------------------------------------------
    # 3. GENERATE outputs/phase4_strategy/pri_category_matrix.csv
    # ---------------------------------------------------------
    category_matrix_data = [
        {
            "category": "High Readiness",
            "minimum_pri": 80.00,
            "maximum_pri": 100.00,
            "inclusive_lower": True,
            "inclusive_upper": True,
            "description": "Comprehensive multi-dimensional preparation profile. Suitable for premium/tier-1 drives.",
            "validation_status": "VALIDATED_CONTINUOUS_BOUND"
        },
        {
            "category": "Moderate Readiness",
            "minimum_pri": 60.00,
            "maximum_pri": 79.99,
            "inclusive_lower": True,
            "inclusive_upper": True,
            "description": "Solid foundational profile with targeted technical or aptitude growth opportunities.",
            "validation_status": "VALIDATED_CONTINUOUS_BOUND"
        },
        {
            "category": "Needs Improvement",
            "minimum_pri": 40.00,
            "maximum_pri": 59.99,
            "inclusive_lower": True,
            "inclusive_upper": True,
            "description": "Moderate preparation deficits across multiple core dimensions requiring structured intervention.",
            "validation_status": "VALIDATED_CONTINUOUS_BOUND"
        },
        {
            "category": "High Improvement Priority",
            "minimum_pri": 0.00,
            "maximum_pri": 39.99,
            "inclusive_lower": True,
            "inclusive_upper": True,
            "description": "Substantial gaps across technical, academic, or aptitude dimensions requiring priority remediation.",
            "validation_status": "VALIDATED_CONTINUOUS_BOUND"
        }
    ]
    df_category_matrix = pd.DataFrame(category_matrix_data)
    df_category_matrix.to_csv("outputs/phase4_strategy/pri_category_matrix.csv", index=False, encoding="utf-8")
    print("[CREATED] outputs/phase4_strategy/pri_category_matrix.csv")

    # ---------------------------------------------------------
    # 4. GENERATE outputs/phase4_strategy/pri_leakage_matrix.csv
    # ---------------------------------------------------------
    leakage_matrix_data = [
        {"variable": "student_id", "used_in_pri": False, "reason": "Unique Identifier", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "age", "used_in_pri": False, "reason": "Demographic Variable - Excluded to prevent bias", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "gender", "used_in_pri": False, "reason": "Demographic Variable - Excluded to prevent bias", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "branch", "used_in_pri": False, "reason": "Academic Demographics - Excluded to maintain uniform scoring", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "cgpa", "used_in_pri": True, "reason": "Pre-placement preparation indicator (Academic component)", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "internships", "used_in_pri": True, "reason": "Pre-placement preparation indicator (Internship component)", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "projects", "used_in_pri": True, "reason": "Pre-placement preparation indicator (Project component)", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "coding_score", "used_in_pri": False, "reason": "EXCLUDED from baseline PRI per frozen P4-P1 formula to adhere to 6-component specification", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "aptitude_score", "used_in_pri": True, "reason": "Pre-placement preparation indicator (Aptitude component)", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "communication_score", "used_in_pri": True, "reason": "Pre-placement preparation indicator (Communication component)", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "python_skill", "used_in_pri": True, "reason": "Pre-placement binary skill indicator (Technical component)", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "sql_skill", "used_in_pri": True, "reason": "Pre-placement binary skill indicator (Technical component)", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "excel_skill", "used_in_pri": True, "reason": "Pre-placement binary skill indicator (Technical component)", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "power_bi_skill", "used_in_pri": True, "reason": "Pre-placement binary skill indicator (Technical component)", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "dsa_skill", "used_in_pri": True, "reason": "Pre-placement binary skill indicator (Technical component)", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "cloud_skill", "used_in_pri": True, "reason": "Pre-placement binary skill indicator (Technical component)", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "cybersecurity_skill", "used_in_pri": True, "reason": "Pre-placement binary skill indicator (Technical component)", "allowed_for_post_pri_evaluation": True, "leakage_risk": "NONE"},
        {"variable": "placed", "used_in_pri": False, "reason": "TARGET VARIABLE — Post-placement outcome. Strictly prohibited from PRI formula.", "allowed_for_post_pri_evaluation": True, "leakage_risk": "CRITICAL IF USED (PREVENTED)"},
        {"variable": "company_type", "used_in_pri": False, "reason": "TARGET VARIABLE — Post-placement outcome. Strictly prohibited from PRI formula.", "allowed_for_post_pri_evaluation": True, "leakage_risk": "CRITICAL IF USED (PREVENTED)"},
        {"variable": "package_lpa", "used_in_pri": False, "reason": "TARGET VARIABLE — Post-placement outcome. Strictly prohibited from PRI formula.", "allowed_for_post_pri_evaluation": True, "leakage_risk": "CRITICAL IF USED (PREVENTED)"}
    ]
    df_leakage_matrix = pd.DataFrame(leakage_matrix_data)
    df_leakage_matrix.to_csv("outputs/phase4_strategy/pri_leakage_matrix.csv", index=False, encoding="utf-8")
    print("[CREATED] outputs/phase4_strategy/pri_leakage_matrix.csv")

    # ---------------------------------------------------------
    # 5. GENERATE outputs/phase4_strategy/pri_test_case_specification.csv
    # ---------------------------------------------------------
    test_case_data = [
        {
            "test_case_id": "TC01",
            "test_name": "Minimum Theoretical PRI",
            "input_description": "All skill indicators = 0, aptitude = 0, cgpa = 0.0, projects = 0, internships = 0, communication = 0",
            "expected_normalized_scores": "S_tech=0, S_apt=0, S_cgpa=0, S_proj=0, S_intern=0, S_comm=0",
            "expected_pri": 0.00,
            "expected_category": "High Improvement Priority",
            "verification_type": "Formula & Bounds"
        },
        {
            "test_case_id": "TC02",
            "test_name": "Maximum Theoretical PRI",
            "input_description": "All 7 skills = 1, aptitude = 100, cgpa = 10.0, projects = 3+, internships = 2+, communication = 100",
            "expected_normalized_scores": "S_tech=100, S_apt=100, S_cgpa=100, S_proj=100, S_intern=100, S_comm=100",
            "expected_pri": 100.00,
            "expected_category": "High Readiness",
            "verification_type": "Formula & Bounds"
        },
        {
            "test_case_id": "TC03",
            "test_name": "Mid-Range Benchmark Profile",
            "input_description": "4 skills (Python, SQL, Excel, PowerBI -> 4/7=57.1429), aptitude=60, cgpa=7.0 (70), projects=1 (33.3333), internships=1 (50), communication=60",
            "expected_normalized_scores": "S_tech=57.1429, S_apt=60.0, S_cgpa=70.0, S_proj=33.3333, S_intern=50.0, S_comm=60.0",
            "expected_pri": 55.29,
            "expected_category": "Needs Improvement",
            "verification_type": "Formula Precision"
        },
        {
            "test_case_id": "TC04",
            "test_name": "Lower Boundary (40.00)",
            "input_description": "Sub-scores constructed to sum exactly to 40.00 PRI points",
            "expected_normalized_scores": "S_tech=40, S_apt=40, S_cgpa=40, S_proj=40, S_intern=40, S_comm=40",
            "expected_pri": 40.00,
            "expected_category": "Needs Improvement",
            "verification_type": "Category Boundary"
        },
        {
            "test_case_id": "TC05",
            "test_name": "Moderate Boundary (60.00)",
            "input_description": "Sub-scores constructed to sum exactly to 60.00 PRI points",
            "expected_normalized_scores": "S_tech=60, S_apt=60, S_cgpa=60, S_proj=60, S_intern=60, S_comm=60",
            "expected_pri": 60.00,
            "expected_category": "Moderate Readiness",
            "verification_type": "Category Boundary"
        },
        {
            "test_case_id": "TC06",
            "test_name": "High Boundary (80.00)",
            "input_description": "Sub-scores constructed to sum exactly to 80.00 PRI points",
            "expected_normalized_scores": "S_tech=80, S_apt=80, S_cgpa=80, S_proj=80, S_intern=80, S_comm=80",
            "expected_pri": 80.00,
            "expected_category": "High Readiness",
            "verification_type": "Category Boundary"
        },
        {
            "test_case_id": "TC07",
            "test_name": "Just Below 40 Boundary (39.99)",
            "input_description": "Calculated score yielding 39.99 PRI points",
            "expected_normalized_scores": "Calculated combination summing to 39.99",
            "expected_pri": 39.99,
            "expected_category": "High Improvement Priority",
            "verification_type": "Boundary Precision"
        },
        {
            "test_case_id": "TC08",
            "test_name": "Just Below 60 Boundary (59.99)",
            "input_description": "Calculated score yielding 59.99 PRI points",
            "expected_normalized_scores": "Calculated combination summing to 59.99",
            "expected_pri": 59.99,
            "expected_category": "Needs Improvement",
            "verification_type": "Boundary Precision"
        },
        {
            "test_case_id": "TC09",
            "test_name": "Just Below 80 Boundary (79.99)",
            "input_description": "Calculated score yielding 79.99 PRI points",
            "expected_normalized_scores": "Calculated combination summing to 79.99",
            "expected_pri": 79.99,
            "expected_category": "Moderate Readiness",
            "verification_type": "Boundary Precision"
        },
        {
            "test_case_id": "TC10",
            "test_name": "Unexpected NULL Input Violation",
            "input_description": "One required PRI input (e.g. aptitude_score) is unexpectedly NULL",
            "expected_normalized_scores": "N/A - Execution Interrupted",
            "expected_pri": None,
            "expected_category": None,
            "verification_type": "Missing Value Exception Handling"
        },
        {
            "test_case_id": "TC11",
            "test_name": "Weight Sum Assertion",
            "input_description": "Verify sum of component weights w1 + w2 + w3 + w4 + w5 + w6 == 1.00",
            "expected_normalized_scores": "w_tech=0.25, w_apt=0.20, w_cgpa=0.15, w_proj=0.15, w_intern=0.15, w_comm=0.10",
            "expected_pri": 1.00,
            "expected_category": "PASS",
            "verification_type": "Weight Constraint"
        },
        {
            "test_case_id": "TC12",
            "test_name": "Zero Target Leakage Audit",
            "input_description": "Check column names in PRI formula definition for outcome variables (placed, package_lpa, company_type)",
            "expected_normalized_scores": "Zero occurrence in calculation logic",
            "expected_pri": 0.00,
            "expected_category": "PASS",
            "verification_type": "Leakage Governance"
        },
        {
            "test_case_id": "TC13",
            "test_name": "Monotonicity Verification",
            "input_description": "Increment any single preparation input while holding all others constant",
            "expected_normalized_scores": "Delta S_k >= 0.0",
            "expected_pri": "Delta PRI >= 0.0 (Strictly non-decreasing)",
            "expected_category": "Same or Higher Category",
            "verification_type": "Monotonicity Constraint"
        },
        {
            "test_case_id": "TC14",
            "test_name": "Deterministic Reproducibility",
            "input_description": "Run PRI calculation pipeline twice on identical input dataset",
            "expected_normalized_scores": "Identical sub-scores across runs",
            "expected_pri": "Exact 0.0 difference (Delta = 0.000000)",
            "expected_category": "100% Identical categories",
            "verification_type": "Determinism Audit"
        },
        {
            "test_case_id": "TC15",
            "test_name": "Manual Calculation Cross-Check",
            "input_description": "Student profile: 5 skills (71.4286), Aptitude 75, CGPA 8.2 (82.0), 2 Projects (66.6667), 1 Internship (50.0), Comm 80",
            "expected_normalized_scores": "Tech=71.4286, Apt=75, CGPA=82, Proj=66.6667, Intern=50, Comm=80",
            "expected_pri": 70.66,
            "expected_category": "Moderate Readiness",
            "verification_type": "Manual Arithmetic Cross-Check"
        }
    ]
    df_test_case = pd.DataFrame(test_case_data)
    df_test_case.to_csv("outputs/phase4_strategy/pri_test_case_specification.csv", index=False, encoding="utf-8")
    print("[CREATED] outputs/phase4_strategy/pri_test_case_specification.csv")

    # ---------------------------------------------------------
    # 6. WRITE docs/placement_readiness_framework.md (28 SECTIONS)
    # ---------------------------------------------------------
    framework_doc_content = r"""# PlacementLens — Placement Readiness Index (PRI) Specification Framework

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
"""
    with open("docs/placement_readiness_framework.md", "w", encoding="utf-8") as f:
        f.write(framework_doc_content.strip() + "\n")
    print("[UPDATED] docs/placement_readiness_framework.md (28 Sections)")

    # ---------------------------------------------------------
    # 7. UPDATE docs/phase4_validation_strategy.md (14 SPECIFICATIONS)
    # ---------------------------------------------------------
    val_doc_content = r"""# PlacementLens — Phase 4 Validation & Governance Strategy

> **Document Status:** FROZEN & APPROVED FOR P4-P5 IMPLEMENTATION  
> **Phase:** Phase 4 — Insights & Placement Readiness  
> **Part:** P4-P4 — Placement Readiness Framework  

---

## 1. Executive Summary & Purpose

This document specifies the **Validation & Governance Strategy** for Phase 4 of **PlacementLens**. It defines automated verification assertions, data integrity checks, target leakage controls, and mathematical audits required to certify Phase 4 outputs.

---

## 2. Comprehensive 14-Layer Validation Architecture

Phase 4 validation operates across fourteen automated assertions (`VAL-P4-01` through `VAL-P4-14`). The P4-P5 calculation pipeline MUST pass 100% of these validation layers before certifying the final Placement Readiness Index outputs.

```
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                           PHASE 4 VALIDATION ARCHITECTURE                                 │
├───────────────────────────────────────────────────────────────────────────────────────────┤
│ VAL-P4-01: Baseline Population Check (N=1,500 exact, unique IDs S0001-S1500)              │
│ VAL-P4-02: Identity Linkage Check (1:1 student mapping, 0 orphan records)                 │
│ VAL-P4-03: Formula Mathematical Integrity (Weighted component sum = PRI)                 │
│ VAL-P4-04: Weight Sum Constraint (Weights sum to exactly 1.000000 / 100.0%)              │
│ VAL-P4-05: Score Scale Bounds Check (PRI strictly in 0.00 - 100.00)                        │
│ VAL-P4-06: NULL Semantics & Missing Value Enforcement (Unexpected NULL = Failure)         │
│ VAL-P4-07: Boundary Precision Check (TC04-TC09 exact threshold mapping)                   │
│ VAL-P4-08: Category Allocation Check (100% records map to exactly 1 category)             │
│ VAL-P4-09: Zero Target Leakage Audit (Zero outcome variables in PRI formula)              │
│ VAL-P4-10: Monotonicity Constraint Verification (Increasing input does not decrease PRI)  │
│ VAL-P4-11: Component Contribution Audit (Sum of point contributions = PRI)               │
│ VAL-P4-12: Nondeterminism & Randomness Elimination (2 runs = 100% identical outputs)      │
│ VAL-P4-13: Reproducibility Protocol (Clean dataset + script = identical artifact hashes)  │
│ VAL-P4-14: Weight Sensitivity & Robustness Protocol (Baseline weights remain un-altered)│
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Detailed Validation Specification Rules

| Validation ID | Target Layer | Assertion Rule & Verification Logic | Failure Action |
| :---: | :--- | :--- | :--- |
| `VAL-P4-01` | Baseline Population | Count physical rows in clean input dataset = 1,500; verify MD5 hash = `96023d297eec5a9a47563eaddc157d0d`. | **STOP.** Halt Phase 4 execution. |
| `VAL-P4-02` | Identity Linkage | Unique `student_id` count = 1,500; sequence = `S0001` to `S1500`; zero missing or orphan IDs. | **STOP.** Flag primary key defect. |
| `VAL-P4-03` | Formula Math Integrity | Verify $\text{PRI}_i - \sum (w_k S_{k, i}) = 0.0$ (within floating point precision tolerance $10^{-6}$). | **STOP.** Calculation drift error. |
| `VAL-P4-04` | Weight Sum Rule | Sum of 6 component weights $w_1 + w_2 + w_3 + w_4 + w_5 + w_6 = 1.000000$ (exact). | **STOP.** Invalid weight configuration. |
| `VAL-P4-05` | PRI Score Bounds | Min composite PRI score $\ge 0.00$ AND Max composite PRI score $\le 100.00$; zero `NaN` or `Inf` values. | **STOP.** Out-of-bounds score error. |
| `VAL-P4-06` | NULL Semantics | Verify zero unexpected `NULL` values in required PRI input columns. | **STOP.** Missing value violation. |
| `VAL-P4-07` | Boundary Precision | Test boundary values ($39.99, 40.00, 59.99, 60.00, 79.99, 80.00$) against category assignment. | **STOP.** Category threshold misclassification. |
| `VAL-P4-08` | Category Allocation | 100% of students mapped to exactly 1 category (`High`, `Moderate`, `Needs Imp`, `High Imp Priority`). | **STOP.** Categorization gap error. |
| `VAL-P4-09` | Zero Target Leakage | Verify `placed`, `package_lpa`, `company_type` are NOT present in PRI formula or feature set. | **STOP.** Critical target leakage defect. |
| `VAL-P4-10` | Monotonicity Check | Verify partial derivative $\frac{\partial \text{PRI}}{\partial \text{Input}} \ge 0$ across all 6 dimensions. | **STOP.** Non-monotonic scoring logic. |
| `VAL-P4-11` | Contribution Audit | Verify $\sum_{k=1}^6 \text{Contribution}_{k, i} = \text{PRI}_i$ for all 1,500 students. | **STOP.** Contribution accounting error. |
| `VAL-P4-12` | Determinism Audit | Re-run calculation pipeline; verify 100% identity match ($\Delta = 0.0$) against previous execution output. | **STOP.** Non-deterministic calculation. |
| `VAL-P4-13` | Reproducibility Protocol | Full dataset execution runs reproducibly across environments without seed dependence. | **STOP.** Reproducibility failure. |
| `VAL-P4-14` | Sensitivity Policy | Sensitivity scenarios executed independently without altering baseline weight table. | **STOP.** Baseline modification error. |

---

## 4. Verification Audit Trail Protocol

All validation checks MUST export structured CSV artifacts into `outputs/readiness/07_pri_validation.csv` during P4-P5. Every validation run MUST record:
1. `check_id`
2. `check_name`
3. `expected_condition`
4. `actual_condition`
5. `status` (`PASS` / `FAIL` / `WARNING`)

---
"""
    with open("docs/phase4_validation_strategy.md", "w", encoding="utf-8") as f:
        f.write(val_doc_content.strip() + "\n")
    print("[UPDATED] docs/phase4_validation_strategy.md (14 Assertions)")

    # ---------------------------------------------------------
    # 8. GENERATE 00_project_blueprint/52_phase_4_part_4_completion_report.md
    # ---------------------------------------------------------
    completion_report_content = r"""# Phase 4 — Part 4 Completion Report: Placement Readiness Framework Design & Freeze

## 1. Part Overview
- **Project Name:** PlacementLens
- **Phase:** Phase 4 — Insights & Placement Readiness
- **Part:** P4-P4 — Placement Readiness Framework
- **Status:** COMPLETED & FROZEN
- **Checkpoint:** CHECKPOINT-04-PART-04 (PASS)

---

## 2. Executive Summary & Objective
Phase 4 — Part 4 has successfully designed, specified, mathematically validated, and frozen the exact **Placement Readiness Framework** for the PlacementLens project.

The Placement Readiness Index (PRI) is a project-designed analytical framework that synthesizes student preparation indicators across six core dimensions into a bounded $0.00 - 100.00$ composite score.

Strict governance controls have been enforced:
- Zero outcome variable target leakage (`placed`, `package_lpa`, `company_type` strictly excluded).
- Zero outcome-based weight tuning or cap optimization.
- Non-causal and non-predictive framework disclaimers established.
- 100% deterministic, reproducible, and explainable mathematical specification.
- Zero student-level scoring executed (scoring is strictly reserved for P4-P5).

---

## 3. Inputs Consumed & MD5 Verification
- Primary Clean Dataset: `data/processed/placementlens_students_clean.csv` (MD5: `96023d297eec5a9a47563eaddc157d0d` — VERIFIED)
- Primary Raw Dataset: `data/raw/placementlens_students_raw.csv` (MD5: `59c04ee15a0112806c510225d8e75779` — VERIFIED)
- Strategy & Baseline Frameworks: `docs/insight_framework.md`, `docs/phase4_analytical_rules.md`, `docs/skill_gap_framework.md`, `docs/student_segmentation_framework.md`

---

## 4. PRI Definition & Component Architecture
The baseline PRI is mathematically defined as a weighted linear combination of six normalized sub-scores ($S_k \in [0, 100]$):

$$\text{PRI}_i = 0.25 \, S_{\text{tech}, i} + 0.20 \, S_{\text{apt}, i} + 0.15 \, S_{\text{cgpa}, i} + 0.15 \, S_{\text{proj}, i} + 0.15 \, S_{\text{intern}, i} + 0.10 \, S_{\text{comm}, i}$$

### Weight Table & Rationale
| Component | Source Variable | Weight (%) | Weight ($w_k$) | Max Points | Normalization Rule |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Technical Skills** | 7 Binary Indicators | 25.0% | 0.25 | 25.0 | $( \text{count} / 7.0 ) \times 100.0$ |
| **Aptitude Score** | `aptitude_score` | 20.0% | 0.20 | 20.0 | Direct identity ($0 - 100$) |
| **CGPA** | `cgpa` | 15.0% | 0.15 | 15.0 | $( \text{cgpa} / 10.0 ) \times 100.0$ |
| **Projects** | `projects` | 15.0% | 0.15 | 15.0 | $\min( \text{projects} / 3.0, 1.0 ) \times 100.0$ (Cap = 3) |
| **Internships** | `internships` | 15.0% | 0.15 | 15.0 | $\min( \text{internships} / 2.0, 1.0 ) \times 100.0$ (Cap = 2) |
| **Communication** | `communication_score` | 10.0% | 0.10 | 10.0 | Direct identity ($0 - 100$) |
| **TOTAL** | | **100.0%** | **1.00** | **100.0** | $\sum w_k = 1.000000$ (PASS) |

---

## 5. Explicit Decision on Coding Score
- `coding_score` is explicitly **EXCLUDED** from the baseline PRI formula to maintain exact compliance with the frozen 6-component framework and frozen weights.
- It remains available as a separate pre-placement analytical variable for post-PRI comparison in P4-P5.

---

## 6. Readiness Categories & Boundary Rules
- **High Readiness:** $80.00 \le \text{PRI} \le 100.00$
- **Moderate Readiness:** $60.00 \le \text{PRI} < 80.00$
- **Needs Improvement:** $40.00 \le \text{PRI} < 60.00$
- **High Improvement Priority:** $0.00 \le \text{PRI} < 40.00$

All boundary test cases (TC04 - TC09: $39.99, 40.00, 59.99, 60.00, 79.99, 80.00$) map unambiguously to exactly one readiness category.

---

## 7. Target Leakage Audit
- Outcomes (`placed`, `package_lpa`, `company_type`) are 100% excluded from PRI calculation.
- Demographic attributes (`gender`, `age`, `branch`) are excluded from scoring formulas to prevent bias.

---

## 8. Strategy Matrices & Files Created/Updated
1. `outputs/phase4_strategy/pri_component_matrix.csv` (CREATED)
2. `outputs/phase4_strategy/pri_weight_matrix.csv` (CREATED)
3. `outputs/phase4_strategy/pri_category_matrix.csv` (CREATED)
4. `outputs/phase4_strategy/pri_leakage_matrix.csv` (CREATED)
5. `outputs/phase4_strategy/pri_test_case_specification.csv` (CREATED — TC01 to TC15)
6. `docs/placement_readiness_framework.md` (UPDATED — 28 Sections Complete)
7. `docs/phase4_validation_strategy.md` (UPDATED — 14 Assertions Complete)
8. `00_project_blueprint/52_phase_4_part_4_completion_report.md` (CREATED)

---

## 9. Final Checkpoint Declaration
- **Checkpoint:** CHECKPOINT-04-PART-04
- **Status:** PASS
- **Next Part:** P4-P5 — PRI Calculation & Validation
"""
    with open("00_project_blueprint/52_phase_4_part_4_completion_report.md", "w", encoding="utf-8") as f:
        f.write(completion_report_content.strip() + "\n")
    print("[CREATED] 00_project_blueprint/52_phase_4_part_4_completion_report.md")

    print("\n=== P4-P4 DESIGN & FREEZE EXECUTION COMPLETED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
