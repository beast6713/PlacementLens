# Data Quality Rules

## Hard rules: fail validation

| ID | Rule | Resolution |
|---|---|---|
| DQ-01 | `student_id` is unique, non-null, and matches the approved format. | Quarantine duplicate/invalid raw rows; resolve before clean export. |
| DQ-02 | Required non-conditional fields are non-null. | Apply documented imputation only where justified; otherwise exclude and log. |
| DQ-03 | Numeric fields meet dictionary ranges and integer constraints. | Correct traceable formatting errors or null/exclude; never silently clip. |
| DQ-04 | Categories are in their allowed standardized set. | Normalize documented variants; reject unknowns. |
| DQ-05 | Skill and placement flags are binary. | Normalize known representations; reject others. |
| DQ-06 | `placed=1` requires company type and positive package; `placed=0` requires both null. | Correct only from reliable raw evidence; otherwise quarantine. |

## Soft rules: investigate and document

- Outliers in package, scores, CGPA, project count, and internships using distribution plots and IQR/z-score screening.
- Unexpected branch/gender proportions, implausible combinations, and abrupt distributions.
- Exact duplicate rows, inconsistent capitalization/spacing, and imputation rate.

## Validation report

Phase 2 must produce a row-count reconciliation: raw rows, duplicate rows, corrected fields, imputed fields, quarantined/excluded rows, and final clean rows. Tests must prevent export if a hard rule fails.

