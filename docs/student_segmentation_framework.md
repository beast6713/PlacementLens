# PlacementLens — Student Segmentation & Profile Framework

## 1. Executive Summary & Purpose

This document defines the official **Student Segmentation Framework** for Phase 4 of **PlacementLens**. Student segmentation groups students with similar academic, technical, and aptitude profiles to enable targeted institutional counseling and placement readiness interventions.

To maintain complete auditability and prevent methodological bias, all student segmentations in PlacementLens MUST be rule-based, transparent, and deterministic.

---

## 2. Allowed vs Forbidden Segmentation Inputs

```
                   ┌─────────────────────────────────────────┐
                   │    STUDENT SEGMENTATION INPUT BOUNDS    │
                   └────────────────────┬────────────────────┘
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             ▼                                                     ▼
   ALLOWED PREPARATION DIMENSIONS                      FORBIDDEN OUTCOME DIMENSIONS
   - CGPA (`cgpa`)                                      - Placement Status (`placed`)
   - Coding Score (`coding_score`)                      - Package LPA (`package_lpa`)
   - Aptitude Score (`aptitude_score`)                  - Company Type (`company_type`)
   - Communication Score (`communication_score`)        *(Excluded to prevent Target Leakage)*
   - Project Count (`projects_count`)
   - Internship Count (`internships_count`)
   - Technical Skill Count (`technical_skill_count`)
```

---

## 3. Preparation Segment vs Readiness Category

A fundamental distinction MUST be preserved between a student's **Preparation Segment** and their **Readiness Category**.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       PREPARATION SEGMENT                               │
│ Multi-dimensional rule-based categorization describing a student's      │
│ specific pattern of strengths and weaknesses across distinct domains.   │
│ Example: "High Technical / Low Communication Profile"                   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     │ (Input to PRI Scoring Model)
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        READINESS CATEGORY                               │
│ Single aggregate 0–100 index tier derived from the weighted Placement   │
│ Readiness Index (PRI).                                                  │
│ Example: "Moderate Readiness (Score: 68.4)"                             │
└─────────────────────────────────────────────────────────────────────────┘
```

These two constructs serve complementary purposes:
- **Preparation Segments** provide granular, domain-specific diagnostics (e.g., identifying students who need communication coaching vs coding bootcamps).
- **Readiness Categories** provide executive-level summary tiering of overall preparation.

---

## 4. Fundamental Segmentation Principles

All segmentation models in PlacementLens MUST adhere to the following five principles:

1. **Deterministic:** Given identical student input features, the segmentation model MUST assign identical segment labels 100% of the time.
2. **Reproducible:** Segmentation logic must be expressed as pure code or SQL logic without random seeding or stochastic initialization.
3. **Explainable:** Every student's segment assignment must be traceable to explicit boundary rules (e.g., "CGPA $\ge 8.0$ AND Coding Score $< 60$").
4. **Mutually Exclusive & Exhaustive:** Every student $i \in \{1, \dots, 1500\}$ must be mapped to exactly ONE preparation segment.
5. **Rule-Based (NO Unsupervised ML):** Algorithms such as K-Means clustering, DBSCAN, Gaussian Mixture Models, or Agglomerative Clustering are **STRICTLY FORBIDDEN**.

---

## 5. Frozen Segmentation Matrix Architecture

Phase 4 defines a 2-tier segmentation hierarchy based on academic performance and technical/analytical skill breadth.

### 5.1 Primary Profile Matrix (4 Core Preparation Quadrants)

Students are mapped into four primary preparation quadrants based on academic standing (CGPA) and composite technical capability (Coding Score + Technical Skill Count).

| Quadrant Code | Quadrant Name | Rule Criteria (CGPA & Technical Profile) | Operational Description |
| :--- | :--- | :--- | :--- |
| **`SEG-Q1`** | **Comprehensive High Performers** | $\text{CGPA} \ge 7.50$ **AND** $\text{coding\_score} \ge 75.0$ **AND** $\text{skill\_count} \ge 4$ | Strong academic standing combined with above-average technical skills. |
| **`SEG-Q2`** | **Technical Specialists** | $\text{CGPA} < 7.50$ **AND** $\text{coding\_score} \ge 75.0$ **AND** $\text{skill\_count} \ge 4$ | High technical proficiency despite moderate academic standing. |
| **`SEG-Q3`** | **Academic Generalists** | $\text{CGPA} \ge 7.50$ **AND** ($\text{coding\_score} < 75.0$ **OR** $\text{skill\_count} < 4$) | High academic standing with opportunities for technical skill growth. |
| **`SEG-Q4`** | **High Support Priority** | $\text{CGPA} < 7.50$ **AND** $\text{coding\_score} < 75.0$ **AND** $\text{skill\_count} < 4$ | Below-median academic and technical scores requiring targeted support. |

---

## 6. Execution Rules for Phase 4

1. **P4-P1 Strategy Freeze:** P4-P1 defines and freezes these rules, logic, and prohibited inputs.
2. **P4-P3 Execution:** Actual row-by-row segment assignments across all 1,500 students will be computed in **P4-P3**.
3. **Zero Target Leakage Audit:** Post-segmentation validation in P4-P3 will confirm zero dependence on `placed`, `package_lpa`, or `company_type`.
