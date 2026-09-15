# PlacementLens — Page 02 Student & Placement Analytics Specification Document

> **Document Version:** 1.0.0  
> **Phase Assignment:** Phase 5 — Part 5 (P5-P5)  
> **Target Page:** Page 02 — Student & Placement Analytics  
> **Status:** FROZEN & VALIDATED (100% QA PASS)  

---

## 1. Page Identity & Purpose

### 1.1 Identity
- **Page Name:** `PAGE 02 STUDENT & PLACEMENT ANALYTICS`
- **Recommended Page Title:** `Student & Placement Analytics`
- **Recommended Subtitle:** `Preparation profiles, technical skills and observed placement outcomes`
- **Navigation Position:** Page 02 in Global Sidebar (Active Highlight: `02 Student & Placement`)

### 1.2 Purpose & Core Analytical Questions
Page 01 (Command Center) answers: *"What is happening across the overall placement population?"*  
Page 02 (Student & Placement Analytics) answers: *"What does student preparation look like across academic, skill, and segment dimensions, and how does it relate to downstream observed placement outcomes?"*

Stakeholders use Page 02 to examine:
1. Academic preparation (CGPA distributions across branches and placement outcomes).
2. Cognitive & communication scores (Coding Score, Aptitude Score, Communication Score).
3. Practical exposure (Projects, Internships).
4. Technical skill coverage across the canonical 7 technical skills (Python, SQL, Excel, Power BI, DSA, Cloud, Cybersecurity).
5. Skill gap distributions ($0$ to $7$ gaps, where $\text{skill\_gap\_count} = 7 - \text{technical\_skill\_count}$).
6. Phase 4 validated preparation segments (`SEG-Q1` through `SEG-Q4`).
7. Observed placement rate differences across preparation profiles and skill holder groups.

---

## 2. Analytical Boundaries & Observational Language

### 2.1 Descriptive & Observational Mandate
Page 02 is strictly **descriptive and observational**. It documents empirical associations present in the cross-validated dataset without claiming predictive guarantees or causal mechanisms.

### 2.2 Prohibited vs Approved Wording
- **Prohibited Causal Claims:**
  - ❌ *"SQL causes placement."*
  - ❌ *"Students with 8.0 CGPA will get placed."*
  - ❌ *"This segment has a 90% probability of placement."*
  - ❌ *"Coding score drives placement success."*
- **Approved Observational Phrasing:**
  - ✅ *"Students in this group show a higher observed placement rate."*
  - ✅ *"The selected skill-holder group exhibits a higher observed placement rate than the comparison group."*
  - ✅ *"Observed placement rate across preparation segments."*
  - ✅ *"Prevalence of technical skills among placed vs unplaced cohorts."*

---

## 3. Data Grain & Source-of-Truth Hierarchy

### 3.1 Data Grain
- **Underlying Grain:** 1 row = 1 student ($1,500$ rows preserved).
- **Aggregation Levels:** Branch, Gender, Placement Status, Technical Skill, Skill Gap Count, Preparation Segment, Readiness Category.

### 3.2 Source-of-Truth Hierarchy
1. Phase 4 validated outputs (`01_student_pri.csv`, `01_preparation_segments.csv`).
2. Phase 3 cross-validated analytical baselines (`01_analytical_baseline.csv`).
3. P5-P1 Power BI Data Architecture (`Students`, `DimBranchSummary`, `DimReadinessCategory`).
4. P5-P2 DAX Metric Contract (61 centralized measures).
5. P5-P3 UI Design System & Visual Tokens.
6. P5-P4 Command Center implementation standards.

---

## 4. Page Architecture & Grid Layout

The layout uses the 12-column responsive grid established in P5-P3:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ PAGE HEADER & CONTEXT BAR                                                    │
│ Student & Placement Analytics | Branch: All | Gender: All | Segment: All    │
├──────────────────────────────────────────────────────────────────────────────┤
│ ANALYTICAL SLICER BAR                                                        │
│ [Branch Dropdown] [Gender Dropdown] [Placed Status] [Segment] [PRI Category] │
├──────────────────────────────────────────────────────────────────────────────┤
│ KPI 01            KPI 02            KPI 03            KPI 04                 │
│ AVERAGE CGPA      AVG CODING SCORE  AVG APTITUDE      AVG TECH SKILLS        │
│ 7.32              72.87             71.78             4.16                   │
├───────────────────────────────┬──────────────────────────────────────────────┤
│ PREPARATION SCORE PROFILE     │ ACADEMIC & CGPA DISTRIBUTION                 │
│ Placed vs Unplaced Metrics    │ Population Density by CGPA Bands             │
├───────────────────────────────┼──────────────────────────────────────────────┤
│ TECHNICAL SKILL COVERAGE      │ SKILL GAP DISTRIBUTION                       │
│ 7 Canonical Technical Skills  │ Student Population by Gap Count (0-7)        │
├───────────────────────────────┴──────────────────────────────────────────────┤
│ PREPARATION SEGMENT ANALYSIS & OBSERVED PLACEMENT EVALUATION                 │
│ SEG-Q1 (296) | SEG-Q3 (358) | SEG-Q2 (200) | SEG-Q4 (646)                  │
├──────────────────────────────────────────────────────────────────────────────┤
│ STUDENT EXPLORATORY PREPARATION DATA MATRIX                                  │
│ Limited student-level preparation metrics grid (No package/company leakage)  │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Page 02 Visual Inventory

| Visual ID | Visual Name | Visual Type | Dimension | DAX Measure / Field | Interaction |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **P2-HEADER** | Global Page Header | Banner | N/A | Static Title & Subtitle | Static |
| **P2-SIDEBAR**| Navigation Sidebar | Menu | Page Name | Active Highlight: `02 Student & Placement` | Page Switch |
| **P2-FILTERS**| Analytical Slicer Bar | Slicer Panel | `branch`, `gender`, `placed`, `preparation_segment`, `readiness_category` | N/A | Global Slicing |
| **P2-FILTER-CONTEXT** | Active Context Bar | Dynamic Text | Slicer Context | `[Active Filter Context]` | Dynamic |
| **P2-KPI-01** | Average CGPA | Card | N/A | `[Average CGPA]` | Slicer Responsive |
| **P2-KPI-02** | Average Coding Score | Card | N/A | `[Average Coding Score]` | Slicer Responsive |
| **P2-KPI-03** | Average Aptitude Score | Card | N/A | `[Average Aptitude Score]` | Slicer Responsive |
| **P2-KPI-04** | Average Tech Skills | Card | N/A | `[Average Technical Skill Count]` | Slicer Responsive |
| **P2-PREP-01** | Preparation Profile Comparison | Clustered Bar | Placement Status | `[Average CGPA]`, `[Average Coding Score]`, `[Average Aptitude Score]`, `[Average Projects]`, `[Average Internships]` | Cross-Highlight |
| **P2-PREP-02** | CGPA Band Distribution | Stacked Bar | `cgpa_band`, `placed` | `[Total Students]`, `[Placement Rate]` | Cross-Filter |
| **P2-SKILL-01**| Technical Skill Coverage | Horizontal Bar | 7 Canonical Skills | `[<Skill> Skill Prevalence]`, `[<Skill> Skill Holders]` | Cross-Highlight |
| **P2-SKILL-02**| Observed Skill Placement Spread| Diverging Bar | 7 Canonical Skills | `[<Skill> Skill Placement Rate]`, `[<Skill> Skill Placement Spread]` | Cross-Highlight |
| **P2-GAP-01**  | Skill Gap Distribution | Column Chart | `skill_gap_count` (0-7) | `[Total Students]`, `[Placement Rate]` | Cross-Filter |
| **P2-SEGMENT-01**| Preparation Segment Matrix | Stacked Bar / Matrix | `preparation_segment` | `[Total Students]`, `[Placement Rate]`, Segment Counts | Cross-Filter |
| **P2-PLACEMENT-01**| Exploratory Student Grid | Data Table | `student_id`, `branch`, `cgpa`, `coding_score`, `aptitude_score`, `communication_score`, `projects`, `internships`, `technical_skill_count`, `skill_gap_count`, `preparation_segment`, `pri_score` | N/A | Row Selection |

---

## 6. Measure Mapping & Baseline Reconciliation

All numbers on Page 02 originate dynamically from P5-P2 DAX measures:

| Metric Name | DAX Expression | Unfiltered Baseline Value | QA Reconciliation |
| :--- | :--- | :---: | :---: |
| **Average CGPA** | `AVERAGE(Students[cgpa])` | **7.32** | Verified |
| **Average Coding Score** | `AVERAGE(Students[coding_score])` | **72.87** | Verified |
| **Average Aptitude Score** | `AVERAGE(Students[aptitude_score])` | **71.78** | Verified |
| **Average Technical Skill Count**| `AVERAGE(Students[technical_skill_count])` | **4.16** | Verified |
| **Coding Score Difference** | `CALCULATE([Average Coding Score], placed=1) - CALCULATE([Average Coding Score], placed=0)` | **+4.13 points** | Verified (74.38 vs 70.25) |
| **Aptitude Score Difference** | `CALCULATE([Average Aptitude Score], placed=1) - CALCULATE([Average Aptitude Score], placed=0)` | **+3.35 points** | Verified (73.00 vs 69.65) |
| **CGPA Difference** | `CALCULATE([Average CGPA], placed=1) - CALCULATE([Average CGPA], placed=0)` | **+0.28 points** | Verified (7.42 vs 7.14) |
| **Average Skill Gap Count** | `AVERAGE(Students[skill_gap_count])` | **2.84 gaps** | Verified ($7 - 4.16 = 2.84$) |
| **Comprehensive High Performers**| `CALCULATE(COUNTROWS(Students), preparation_segment="Comprehensive High Performers")` | **296 (19.73%)** | Verified (Placement: 73.31%) |
| **Academic Generalists** | `CALCULATE(COUNTROWS(Students), preparation_segment="Academic Generalists")` | **358 (23.87%)** | Verified (Placement: 65.08%) |
| **Technical Specialists** | `CALCULATE(COUNTROWS(Students), preparation_segment="Technical Specialists")` | **200 (13.33%)** | Verified (Placement: 65.00%) |
| **High Support Priority** | `CALCULATE(COUNTROWS(Students), preparation_segment="High Support Priority")` | **646 (43.07%)** | Verified (Placement: 57.28%) |

---

## 7. Canonical 7 Technical Skills Analysis

The page strictly evaluates the canonical 7 technical skills:

| Technical Skill | Holder Count | Prevalence % | Holder Placement Rate | Non-Holder Placement Rate | Observed Spread (pp) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Excel** | 1,258 | **83.87%** | 63.75% | 61.16% | **+2.59 pp** |
| **Python** | 1,177 | **78.47%** | 64.83% | 57.89% | **+6.93 pp** |
| **SQL** | 1,169 | **77.93%** | 65.36% | 56.19% | **+9.16 pp** |
| **DSA** | 1,057 | **70.47%** | 63.77% | 62.30% | **+1.46 pp** |
| **Power BI** | 793 | **52.87%** | 63.81% | 62.80% | **+1.01 pp** |
| **Cloud** | 485 | **32.33%** | 67.42% | 61.38% | **+6.04 pp** |
| **Cybersecurity** | 297 | **19.80%** | 60.94% | 63.92% | **-2.98 pp** |

---

## 8. Skill Gap Distribution

Skill gap counts range strictly from $0$ to $7$:

| Skill Gap Count | Student Count | Cohort % | Observed Placement Rate |
| :---: | :---: | :---: | :---: |
| **0 Gaps** | 33 | 2.20% | 69.70% |
| **1 Gap** | 181 | 12.07% | 65.19% |
| **2 Gaps** | 420 | 28.00% | 66.43% |
| **3 Gaps** | 419 | 27.93% | 62.53% |
| **4 Gaps** | 288 | 19.20% | 60.07% |
| **5 Gaps** | 122 | 8.13% | 61.48% |
| **6 Gaps** | 35 | 2.33% | 57.14% |
| **7 Gaps** | 2 | 0.13% | 50.00% |

---

## 9. Preparation Segments & Outcome Evaluation

Page 02 consumes the Phase 4 validated preparation segments:

1. **Comprehensive High Performers (`SEG-Q1`):** High Academic & High Technical Preparation ($296$ students, $19.73\%$ cohort, $73.31\%$ observed placement rate).
2. **Academic Generalists (`SEG-Q3`):** High Academic & Low Technical Preparation ($358$ students, $23.87\%$ cohort, $65.08\%$ observed placement rate).
3. **Technical Specialists (`SEG-Q2`):** Low Academic & High Technical Preparation ($200$ students, $13.33\%$ cohort, $65.00\%$ observed placement rate).
4. **High Support Priority (`SEG-Q4`):** Low Academic & Low Technical Preparation ($646$ students, $43.07\%$ cohort, $57.28\%$ observed placement rate).

---

## 10. Target Leakage & Safety Audit

- **Strict Separation:** `placed`, `package_lpa`, and `company_type` are strictly excluded from preparation features, skill gap counts, and segment definitions.
- **Post-Profile Evaluation:** Outcome variables are evaluated only post-profiling to observe rate differences.
- **Exploratory Table Scope:** Student-level grid contains preparation variables only. Sensitive compensation (`package_lpa`) and hiring company (`company_type`) are omitted to avoid converting the table into a candidate ranking list.

---

## 11. QA Scorecard Summary

- **Total QA Checks:** 25 Validation Checks
- **Pass Rate:** 100% (25/25)
- **Script Executor:** `scripts/build_student_analytics.py`
- **Output Validation CSV:** `outputs/powerbi/24_student_placement_validation.csv`
- **Summary Report:** `outputs/powerbi/25_student_placement_qa_summary.md`

---

## 12. Certification & Next Steps

Page 02 — Student & Placement Analytics is **FROZEN**, **VALIDATED**, and ready for production consumption.

```
PAGE 02 STATUS: PASS 100%
HANDOFF TARGET: PHASE 5 PART 6 — COMPANY & PACKAGE INTELLIGENCE (PAGE 03)
```
