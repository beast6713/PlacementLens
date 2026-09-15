# PlacementLens — Phase 2 Part 4 Run Log

- **Execution Date:** 2026-09-16
- **Input File:** `data/processed/placementlens_students_structural_clean.csv`
- **Candidate Clean Output:** `data/processed/placementlens_students_clean.csv`
- **Raw MD5 Before:** `59c04ee15a0112806c510225d8e75779`
- **Raw MD5 After:** `59c04ee15a0112806c510225d8e75779`
- **Raw Immutability:** `PASS (100% Match)`
- **Input Physical Rows:** 1,500
- **Output Physical Rows:** 1,500
- **Company Type Transformations:** 15
- **Gender Transformations:** 20
- **Python Skill Binary Transformations:** 15
- **Communication Score NULLs Imputed:** 15 (Branch Cohort Median)
- **Target Leakage Protection:** `PASS (Target variables excluded)`
- **NULL Semantics Preservation:** `PASS (Unplaced package/company NULL)`
- **Validation Audit:** `PASS (100%)`
- **Checkpoint:** `CHECKPOINT-02-PART-04 (PASS)`

## Summary Table

| Metric | Before | After | Expected | Status |
|---|---|---|---|---|
| physical_rows | 1500 | 1500 | 1500 | PASS |
| unique_student_ids | 1500 | 1500 | 1500 | PASS |
| duplicate_student_ids | 0 | 0 | 0 | PASS |
| company_type_inconsistencies | 15 | 0 | 15 | PASS |
| gender_whitespace_defects | 20 | 0 | 20 | PASS |
| python_skill_string_defects | 15 | 0 | 15 | PASS |
| communication_score_nulls | 15 | 0 | 0 | PASS |
| communication_score_imputations | 0 | 15 | 15 | PASS |
| invalid_company_types | 15 | 0 | 0 | PASS |
| invalid_gender_values | 20 | 0 | 0 | PASS |
| invalid_python_skill_values | 15 | 0 | 0 | PASS |
| invalid_communication_scores | 15 | 0 | 0 | PASS |
| unexpected_nulls | 15 | 0 | 0 | PASS |
| raw_immutability | 1 | 1 | 1 | PASS |
