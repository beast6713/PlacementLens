# PlacementLens — Power BI Metric Contract

> **Document Status:** FROZEN & APPROVED DAX METRIC CONTRACT  
> **Phase Target:** Phase 5 Part 2 — DAX Measures & Metric Contract  
> **Dependencies:** P5-P1 Data Architecture (`v1.0-clean`, MD5: `96023d297eec5a9a47563eaddc157d0d`)  

---

## 1. Purpose & Contract Scope

This document establishes the formal **Metric Contract** between Phase 3/4 analytical definitions and all future Phase 5 Power BI dashboard pages (Command Center, Student Analytics, Company Intelligence, Reports). Every visual in the Power BI platform MUST consume measures defined in this contract. Modifying mathematical definitions, hard-coding values, or creating duplicate page-specific measures is **STRICTLY PROHIBITED**.

---

## 2. Global Metric Contract Summary

| Metric ID | Metric Name | Business Definition | DAX Measure Formula | Display Format | Target Baseline | Leakage Status | Primary Dashboard Page |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **MET-01** | **Total Students** | Total count of unique students in cohort | `DISTINCTCOUNT(Students[student_id])` | `#,##0` | 1,500 | PREPARATION / DEMOGRAPHIC | All Pages |
| **MET-02** | **Placed Students** | Count of placed students | `CALCULATE(COUNTROWS(Students), Students[placed]=1)` | `#,##0` | 950 | PLACEMENT OUTCOME | Command Center / Student Analytics / Reports |
| **MET-03** | **Unplaced Students** | Count of unplaced students | `[Total Students] - [Placed Students]` | `#,##0` | 550 | PLACEMENT OUTCOME | Command Center / Student Analytics / Reports |
| **MET-04** | **Placement Rate (%)** | Percentage of students who are placed | `DIVIDE([Placed Students], [Total Students], 0)` | `0.00%` | 63.33% | PLACEMENT OUTCOME | Command Center / Student Analytics / Reports |
| **MET-05** | **Average CGPA** | Mean Cumulative Grade Point Average | `AVERAGE(Students[cgpa])` | `0.00` | 7.59 | PREPARATION INPUT | Student Analytics |
| **MET-06** | **Average Coding Score**| Mean coding assessment score | `AVERAGE(Students[coding_score])` | `0.00` | 76.38 | PREPARATION INPUT | Student Analytics |
| **MET-07** | **Average Aptitude Score**| Mean aptitude assessment score | `AVERAGE(Students[aptitude_score])` | `0.00` | 73.50 | PREPARATION INPUT | Student Analytics |
| **MET-08** | **Average Communication**| Mean communication assessment score | `AVERAGE(Students[communication_score])` | `0.00` | 81.56 | PREPARATION INPUT | Student Analytics |
| **MET-09** | **Average Skill Count**| Mean technical skills owned out of 7 | `AVERAGE(Students[technical_skill_count])` | `0.00` | 3.71 | PREPARATION INPUT | Command Center / Student Analytics |
| **MET-10** | **Average Skill Gap** | Mean missing skills out of 7 | `AVERAGE(Students[skill_gap_count])` | `0.00` | 3.29 | PREPARATION INPUT | Student Analytics |
| **MET-11** | **Average Package** | Mean salary package (placed only) | `AVERAGE(Students[package_lpa])` | `0.00 "LPA"` | 10.62 LPA | COMPENSATION OUTCOME | Command Center / Company Intelligence / Reports |
| **MET-12** | **Median Package** | Median salary package (placed only) | `MEDIAN(Students[package_lpa])` | `0.00 "LPA"` | 9.70 LPA | COMPENSATION OUTCOME | Command Center / Company Intelligence / Reports |
| **MET-13** | **Average PRI** | Mean Placement Readiness Index score | `AVERAGE(Students[pri_score])` | `0.00` | 65.59 | READINESS CONSTRUCT | Command Center / Student Analytics / Reports |
| **MET-14** | **Median PRI** | Median Placement Readiness Index score | `MEDIAN(Students[pri_score])` | `0.00` | 65.91 | READINESS CONSTRUCT | Command Center / Student Analytics / Reports |

---

## 3. Skill Metric Family Contract

For each of the 7 canonical technical skills ($X \in \{\text{Python, SQL, Excel, Power BI, DSA, Cloud, Cybersecurity}\}$):

1. **`[<X> Skill Holders]`**: `CALCULATE([Total Students], Students[<x>_skill] = 1)`
2. **`[<X> Skill Prevalence]`**: `DIVIDE([<X> Skill Holders], [Total Students], 0)` (Format: `0.00%`)
3. **`[<X> Skill Placement Rate]`**: `DIVIDE(CALCULATE([Placed Students], Students[<x>_skill] = 1), [<X> Skill Holders], 0)` (Format: `0.00%`)
4. **`[<X> Skill Placement Spread]`**: `[<X> Skill Placement Rate] - DIVIDE(CALCULATE([Placed Students], Students[<x>_skill] = 0), CALCULATE([Total Students], Students[<x>_skill] = 0), 0)` (Format: `+0.00%`)

---

## 4. Readiness Tier & Segmentation Metric Contract

- **`[High Readiness Count]`**: `CALCULATE([Total Students], Students[readiness_category] = "High Readiness")` ($N=82$)
- **`[Moderate Readiness Count]`**: `CALCULATE([Total Students], Students[readiness_category] = "Moderate Readiness")` ($N=862$)
- **`[Needs Improvement Count]`**: `CALCULATE([Total Students], Students[readiness_category] = "Needs Improvement")` ($N=540$)
- **`[High Improvement Priority Count]`**: `CALCULATE([Total Students], Students[readiness_category] = "High Improvement Priority")` ($N=16$)
- **`[Comprehensive High Performers Count]`**: `CALCULATE([Total Students], Students[preparation_segment] = "Comprehensive High Performers")` ($N=296$)
- **`[Technical Specialists Count]`**: `CALCULATE([Total Students], Students[preparation_segment] = "Technical Specialists")` ($N=200$)
- **`[Academic Generalists Count]`**: `CALCULATE([Total Students], Students[preparation_segment] = "Academic Generalists")` ($N=358$)
- **`[High Support Priority Count]`**: `CALCULATE([Total Students], Students[preparation_segment] = "High Support Priority")` ($N=646$)

---

## 5. Dashboard Page Mapping Matrix

```
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                               POWER BI METRIC CONSUMPTION MAP                             │
├───────────────────────────────────────────────────────────────────────────────────────────┤
│ PAGE 01: Command Center                                                                   │
│   → [Total Students], [Placed Students], [Placement Rate], [Average Package],            │
│     [Median Package], [Average PRI], [Median PRI], [Branch Placement Rates],             │
│     [Skill Prevalences], [Readiness Tier Counts]                                          │
├───────────────────────────────────────────────────────────────────────────────────────────┤
│ PAGE 02: Student & Placement Analytics                                                    │
│   → [Average CGPA], [Average Coding Score], [Average Aptitude Score],                     │
│     [Average Communication Score], [Average Skill Count], [Skill Placement Spreads],     │
│     [Segment Counts], [Segment Placement Rates], [Score Differences]                      │
├───────────────────────────────────────────────────────────────────────────────────────────┤
│ PAGE 03: Company & Package Intelligence                                                   │
│   → [Average Package], [Median Package], [Min Package], [Max Package],                    │
│     [Placed Students by Company Type], [Package by Branch], [Package by PRI Tier]         │
├───────────────────────────────────────────────────────────────────────────────────────────┤
│ PAGE 04: Reports & Intelligence                                                           │
│   → Student detail table drill-through using base measures & unpivoted PRI components.    │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Target Leakage & NULL Semantics Rules

1. **Formula Isolation:** Outcome variables (`placed`, `package_lpa`, `company_type`) are NEVER referenced inside PRI calculation or preparation segment DAX formulas.
2. **NULL Compensation:** `package_lpa` for 550 unplaced students is strictly `NULL`. DAX `AVERAGE` and `MEDIAN` evaluate exclusively over placed students ($N=950$).
3. **No Hard-Coding:** All metrics are calculated dynamically from data model tables. Hard-coded numeric constants in production measures are prohibited.
