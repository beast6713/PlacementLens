# PlacementLens — Power BI Data Architecture & Data Model Specification

> **Document Status:** FROZEN & APPROVED FOR POWER BI MODELING  
> **Phase Target:** Phase 5 Part 1 — Power BI Data Architecture & Model  
> **Dependencies:** Phase 0–4 Validated Baselines (`v1.0-clean`, MD5: `96023d297eec5a9a47563eaddc157d0d`)  

---

## 1. Purpose

This document defines the technical **Power BI Data Architecture and Model Specification** for the **PlacementLens** Student Placement Analytics & Business Intelligence platform. It provides the definitive data blueprint, schema mappings, relationship rules, data types, NULL compensation contracts, target leakage controls, and reproducibility standards required for Power BI Desktop ingestion.

---

## 2. Model Objectives

The Power BI data model establishes a simple, defensible, performant, and auditable star/snowflake hybrid model that:
1. Consumes the frozen analytical baseline established in Phase 3 and Phase 4.
2. Preserves exact student grain ($N=1,500$ unique student records, $S0001$–$S1500$).
3. Integrates Placement Readiness Index (PRI) composite scores, readiness tiers, student preparation quadrants, and skill gap profiles.
4. Prevents target leakage by isolating preparation inputs from post-analysis placement outcomes (`placed`, `package_lpa`, `company_type`).
5. Supports all four planned Phase 5 interactive dashboard pages (Command Center, Student Analytics, Company Intelligence, Reports).

---

## 3. Source-of-Truth Hierarchy

When resolving analytical or data model conflicts, Power BI MUST adhere strictly to the following precedence hierarchy:

```
LEVEL 1 — Phase 4 Validated Outputs (PRI, Segments, Skill Gaps, Insights)
LEVEL 2 — Phase 3 Dual-Path Cross-Validated Outputs (Python ↔ SQL 0% Discrepancy)
LEVEL 3 — PostgreSQL Analytical Schema (public.students)
LEVEL 4 — Phase 3 Python EDA Analytical Tables (outputs/eda/)
LEVEL 5 — Validated Clean Dataset (data/processed/placementlens_students_clean.csv)
LEVEL 6 — Raw Dataset (data/raw/placementlens_students_raw.csv ONLY for Audit/Hash Check)
```

> [!IMPORTANT]
> The raw dataset is NOT a Power BI analytical input. Raw data MD5 (`59c04ee15a0112806c510225d8e75779`) and Clean data MD5 (`96023d297eec5a9a47563eaddc157d0d`) are cryptographically frozen.

---

## 4. Source Files

Power BI connects directly to the following validated file paths:

| File Role | Source File Path | Record Count | MD5 Hash / Status |
| :--- | :--- | :---: | :---: |
| **Clean Student Base** | `data/processed/placementlens_students_clean.csv` | 1,500 | `96023d297eec5a9a47563eaddc157d0d` |
| **Student PRI** | `outputs/readiness/01_student_pri.csv` | 1,500 | Validated Phase 4 Output |
| **PRI Component Scores** | `outputs/readiness/02_pri_component_scores.csv` | 9,000 | Validated Phase 4 Output |
| **Readiness Tier Summary**| `outputs/readiness/03_pri_category_summary.csv` | 4 | Validated Phase 4 Output |
| **Branch Readiness** | `outputs/readiness/04_pri_by_branch.csv` | 6 | Validated Phase 4 Output |
| **Segment Summary** | `outputs/segmentation/03_segment_summary.csv` | 4 | Validated Phase 4 Output |
| **Skill Gap Profile** | `outputs/skill_gaps/02_student_skill_gaps.csv` | 1,500 | Validated Phase 4 Output |
| **Extracted Insights** | `outputs/insights/02_insight_register.csv` | 15 | Validated Phase 4 Output |

---

## 5. Table Inventory

The Power BI model comprises 6 logical tables exported in `outputs/powerbi/01_powerbi_table_inventory.csv`:

1. **`Students` (Fact Table)**: Core student fact table containing demographic, academic, preparation, skill, PRI composite score, readiness category, segment, and placement outcome fields.
2. **`DimPRIComponents` (Fact Detail Table)**: Unpivoted 6-component scores and weighted contributions ($N=9,000$) for radar charts and component breakdown visual layers.
3. **`DimReadinessCategory` (Reference Dimension)**: Readiness category boundaries, tier student counts, and placement distribution ($N=4$).
4. **`DimBranchSummary` (Reference Dimension)**: Academic branch benchmark summary metrics including student count, placement rate, mean PRI, and median package ($N=6$).
5. **`DimSegmentSummary` (Reference Dimension)**: Student preparation quadrant profiles, rules, student counts, and downstream placement rates ($N=4$).
6. **`DimInsightRegister` (Narrative Dimension)**: Validated Phase 4 analytical insights, categories, metrics, non-causal descriptions, and executive takeaway callouts ($N=15$).

---

## 6. Table Grain

- **`Students`**: 1 row per student ($N=1,500$). Primary Key: `student_id`.
- **`DimPRIComponents`**: 1 row per student per PRI component ($N=9,000$). Primary Key: `student_id` + `component`.
- **`DimReadinessCategory`**: 1 row per readiness tier ($N=4$). Primary Key: `readiness_category`.
- **`DimBranchSummary`**: 1 row per academic branch ($N=6$). Primary Key: `branch`.
- **`DimSegmentSummary`**: 1 row per preparation quadrant ($N=4$). Primary Key: `segment_code`.
- **`DimInsightRegister`**: 1 row per analytical insight ($N=15$). Primary Key: `insight_id`.

---

## 7. Column Inventory & Data Dictionary Summary

Exported in `outputs/powerbi/02_powerbi_field_dictionary.csv`. Key columns in `Students`:

- Identity: `student_id` (Text, Primary Key)
- Demographics: `age` (Whole Number), `gender` (Text)
- Academic: `branch` (Text), `cgpa` (Decimal Number)
- Preparation: `internships` (Whole Number), `projects` (Whole Number), `coding_score` (Decimal Number), `aptitude_score` (Decimal Number), `communication_score` (Decimal Number)
- Skills (0/1): `python_skill`, `sql_skill`, `excel_skill`, `power_bi_skill`, `dsa_skill`, `cloud_skill`, `cybersecurity_skill`
- Derived Skills: `technical_skill_count` (0–7), `skill_gap_count` (0–7), `missing_skills` (Text)
- Readiness: `pri_score` (Decimal Number, 0.00–100.00), `readiness_category` (Text)
- Segmentation: `preparation_segment` (Text)
- Outcomes (Post-Analysis): `placed` (Whole Number 0/1), `company_type` (Text, Nullable), `package_lpa` (Decimal Number, Nullable)

---

## 8. Power BI Data Types

Power Query connection types MUST be mapped as follows:
- `student_id` → `Text`
- `age`, `internships`, `projects`, skill flags, `technical_skill_count`, `skill_gap_count`, `placed` → `Whole Number`
- `cgpa`, `coding_score`, `aptitude_score`, `communication_score`, `pri_score`, `package_lpa`, `contribution`, `normalized_score`, `weight` → `Decimal Number`
- `gender`, `branch`, `missing_skills`, `readiness_category`, `preparation_segment`, `company_type`, `component`, `insight_id`, `title`, `finding`, `priority` → `Text`

---

## 9. Derived Fields

1. **`technical_skill_count`**: Sum of 7 binary skill flags ($0 \le \text{count} \le 7$).
2. **`skill_gap_count`**: Derived as $7 - \text{technical\_skill\_count}$.
3. **Skill Invariant**: $\text{technical\_skill\_count} + \text{skill\_gap\_count} = 7$ holds for 100% of students ($1,500/1,500$).

---

## 10. Data Model Relationships

Exported in `outputs/powerbi/03_powerbi_relationship_inventory.csv`:

```
┌────────────────────────┐            ┌────────────────────────┐
│  DimReadinessCategory  │            │    DimBranchSummary    │
│  (readiness_category)  │            │        (branch)        │
└───────────┬────────────┘            └───────────┬────────────┘
            │ 1                                   │ 1
            │                                     │
            │ * (Single)                          │ * (Single)
┌───────────┴─────────────────────────────────────┴────────────┐
│                           Students                           │
│                         (student_id)                         │
└───────────┬─────────────────────────────────────┬────────────┘
            │ 1                                   │ * (Single)
            │                                     │
            │ * (Single)                          │ 1
┌───────────┴────────────┐            ┌───────────┴────────────┐
│   DimPRIComponents     │            │   DimSegmentSummary    │
│ (student_id+component) │            │     (segment_name)     │
└────────────────────────┘            └────────────────────────┘
```

---

## 11. Cardinality

- `DimPRIComponents[student_id]` → `Students[student_id]`: Many-to-One (*:1)
- `Students[readiness_category]` → `DimReadinessCategory[readiness_category]`: Many-to-One (*:1)
- `Students[branch]` → `DimBranchSummary[branch]`: Many-to-One (*:1)
- `Students[preparation_segment]` → `DimSegmentSummary[segment_name]`: Many-to-One (*:1)

---

## 12. Cross-Filter Directions

All relationships use **Single Direction Filtering** filtering from the dimension table to the `Students` fact table (or from `DimPRIComponents` to `Students`). Bi-directional cross-filtering is **PROHIBITED** to eliminate ambiguous filter paths.

---

## 13. NULL Semantics & Compensation Contract

1. **Unplaced Package Compensation:** Unplaced students ($N=550$) have `package_lpa = NULL` and `company_type = NULL`.
2. **Zero Conversion Prohibited:** Power BI MUST NOT convert `NULL` to `0` or `0.00 LPA`. DAX measures like `AVERAGE(Students[package_lpa])` evaluate strictly over placed students ($N=950$).
3. **Binary Skill Flags:** Skill indicators contain explicit `1` (Present) or `0` (Absent). `0` indicates skill absence, NOT missing data.

---

## 14. PRI Integration & Weight Architecture

PRI score calculation is frozen from Phase 4 and imported directly into Power BI:
$$\text{PRI} = 0.25 T + 0.20 A + 0.15 C + 0.15 P + 0.15 I + 0.10 M$$
- $T = (\text{technical\_skill\_count} / 7) \times 100$
- $A = \text{aptitude\_score}$
- $C = (\text{cgpa} / 10) \times 100$
- $P = \min(\text{projects} / 3, 1.0) \times 100$
- $I = \min(\text{internships} / 2, 1.0) \times 100$
- $M = \text{communication\_score}$

> [!NOTE]
> `coding_score` is explicitly EXCLUDED from the baseline PRI formula per P4-P4 frozen rules. Power BI MUST NOT recalculate PRI with custom weights.

---

## 15. Student Segmentation Integration

Student preparation quadrants are imported directly from Phase 4 without retuning:
- `SEG-Q1` (**Comprehensive High Performers**): CGPA $\ge 7.50$, Coding $\ge 75.0$, Skills $\ge 4$ ($N=296$)
- `SEG-Q2` (**Technical Specialists**): CGPA $< 7.50$, Coding $\ge 75.0$, Skills $\ge 4$ ($N=200$)
- `SEG-Q3` (**Academic Generalists**): CGPA $\ge 7.50$, (Coding $< 75.0$ OR Skills $< 4$) ($N=358$)
- `SEG-Q4` (**High Support Priority**): CGPA $< 7.50$, Coding $< 75.0$, Skills $< 4$ ($N=646$)

---

## 16. Skill-Gap Integration

- Profiled across 7 technical skills.
- Top missing skill deficits: Cybersecurity (60.67%), Cloud Computing (58.93%), Power BI (58.33%).
- Invariant $\text{technical\_skill\_count} + \text{skill\_gap\_count} = 7$ verified across all 1,500 records.

---

## 17. Target Leakage Controls

- `placed`, `package_lpa`, and `company_type` are 100% EXCLUDED from PRI calculation, component weights, and segmentation rules.
- Demographics (`age`, `gender`, `branch`) are 100% EXCLUDED from formula scoring.
- Outcome variables are used strictly downstream for observed placement rate evaluation.

---

## 18. Model Validation Scorecard Summary

Exported in `outputs/powerbi/04_powerbi_model_validation.csv`. Passed **25/25** checks:
- CHECK-01 to CHECK-04: Student row count 1,500, PK uniqueness, 0 null IDs (PASS)
- CHECK-05 to CHECK-09: Branch normalization, binary skills, skill counts 0–7, sum invariant = 7 (PASS)
- CHECK-10 to CHECK-13: Outcome flags, NULL package/company for unplaced (550 NULLs), 0 unexpected input NULLs (PASS)
- CHECK-14 to CHECK-18: PRI range 31.48–91.90, 4 readiness tiers, 100% ID key alignment across outputs (PASS)
- CHECK-19 to CHECK-21: Unique PKs across dimensions, single filter direction, 0 target leakage (PASS)
- CHECK-22 to CHECK-25: Zero fabricated fields, zero fake date dimensions, raw/clean MD5 immutability (PASS)

---

## 19. Unsupported Design Concepts (Gap Register)

Exported in `outputs/powerbi/05_powerbi_model_gap_register.csv`. The current static synthetic dataset does NOT support:
1. `academic_year` / `batch` (`NOT SUPPORTED BY CURRENT DATA`)
2. `eligibility` criteria (`NOT SUPPORTED BY CURRENT DATA`)
3. `company_name` / Individual company leaderboards (`PARTIALLY SUPPORTED` via `company_type`)
4. `offer_count` (`PARTIALLY SUPPORTED` via binary `placed` flag)
5. `recruitment_date` / Date Calendar (`NOT SUPPORTED BY CURRENT DATA`)
6. `active_company_count` / `new_company_count` (`NOT SUPPORTED BY CURRENT DATA`)

---

## 20. Reproducibility Instructions

To reproduce the Power BI data model:
1. Execute `python scripts/build_powerbi_model.py` to regenerate CSV inventories and run validation checks.
2. In Power BI Desktop, load `data/processed/placementlens_students_clean.csv` and merge with `outputs/readiness/01_student_pri.csv` on `student_id`.
3. Set Power Query data types according to Section 8.
4. Establish Many-to-One relationships as specified in Section 10 with Single filter direction.

---

## 21. Known Limitations

- Static single snapshot placement cohort ($N=1,500$); no multi-year historical time-series analytics.
- Company analysis restricted to 4 major categories (`Service`, `Product`, `Startup`, `MNC`).

---

## 22. Phase 5 Part 2 Handoff Contract

The Power BI Data Architecture & Model is **CERTIFIED AND FROZEN**. Phase 5 Part 2 (DAX Measures & Metric Contract) is authorized to consume this foundation:

- **DATA MODEL READY:** YES
- **SOURCE VALIDATION:** PASS
- **STUDENT GRAIN:** PASS (1 row per student, $N=1,500$)
- **PRI INTEGRATION:** PASS
- **SEGMENTATION INTEGRATION:** PASS
- **SKILL-GAP INTEGRATION:** PASS
- **LEAKAGE AUDIT:** PASS (0 leakage variables in formula)
- **NULL SEMANTICS:** PASS (550 unplaced package NULLs preserved)
- **RELATIONSHIP VALIDATION:** PASS (4 active 1:Many single-direction relationships)
- **DASHBOARD SUPPORT:** PASS (Supports Command Center, Student Analytics, Company Intelligence, Reports)
- **DOCUMENTATION:** PASS
- **CHECKPOINT-05-PART-01:** PASS
