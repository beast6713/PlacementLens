# PlacementLens — Initial Data Profiling Summary Report

**Execution Date:** `2026-09-16`  
**Input Source:** `data/raw/placementlens_students_raw.csv`  
**Data Integrity:** **READ-ONLY VERIFIED** (0 rows modified)

---

## Executive Profile Summary

- **Physical Raw Rows:** 1,505 rows
- **Unique Student Population:** 1,500 students (`S0001` to `S1500`)
- **Extra Duplicate Rows:** 5 physical rows
- **Total Columns:** 20 columns
- **Overall Placement Rate:** 63.33% (950 Placed, 550 Unplaced)
- **Placed Salary Package:** Median = 9.70 LPA (Range: 3.29 LPA to 48.00 LPA)
- **Unplaced Salary Package:** 100% NULL (0 non-null values for unplaced)

---

## Controlled Defect Manifest Reconciliation

| Defect Type | Column | Detected Count | Reconciliation Status |
|---|---|---|---|
| Case Inconsistency | `branch` | 25 | **MATCH** |
| Case & Space Inconsistency | `company_type` | 15 | **MATCH** |
| Whitespace Padding | `gender` | 20 | **MATCH** |
| String Binary Variant | `python_skill` | 15 | **MATCH** |
| Missing Non-Critical Value | `communication_score` | 15 | **MATCH** |
| Duplicate Physical Row | `student_id` | 5 | **MATCH** |

---

## Exported Profiling CSV Artifacts Summary

1. `column_profile.csv` — Comprehensive 20-column field types, counts, nulls, unique values, mins, maxes.
2. `missing_values.csv` — Full null analysis across all 20 columns.
3. `duplicate_profile.csv` — Duplicate ID and physical row breakdown.
4. `branch_profile.csv` — Department distribution and lowercase defect counts.
5. `placement_profile.csv` — Placed vs unplaced counts and percentages.
6. `package_profile.csv` — Compensation LPA min, max, mean, median, std, percentiles for placed cohort.
7. `score_profile.csv` — Continuous distributions for CGPA, coding, aptitude, communication, projects, internships.
8. `skill_profile.csv` — Technical skill prevalence percentages and string binary defect counts.
9. `preparation_vs_placement.csv` — Descriptive comparisons of placed vs unplaced cohorts.
10. `profiled_quality_issues.csv` — Catalog of all 6 observed raw anomaly categories.
11. `defect_reconciliation.csv` — Manifest reconciliation matching 95 injected raw defects.
