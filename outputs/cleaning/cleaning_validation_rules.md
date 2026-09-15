# PlacementLens — Post-Cleaning Validation Rules & Constraints (`v1.0 Clean`)

**Target Processed Artifact:** `data/processed/placementlens_students_clean.csv`  
**Clean Row Count Target:** Exactly 1,500 unique student records  
**Schema Compliance:** PostgreSQL DDL `v1.0` Schema

---

## 1. Structural & Population Constraints

| Rule ID | Target Field | Validation Rule Statement | Failure Threshold | Cleaning Action Reference |
|---|---|---|---|---|
| **VAL-01** | `student_id` | Exactly 1,500 unique student IDs matching regex `^S[0-9]{4}$`. | Any duplicate or non-compliant format. | Deduplicate keeping first valid row |
| **VAL-02** | Total Dataset | Exactly 1,500 physical rows in processed CSV. | Physical rows $\neq 1,500$. | Deduplication of 5 extra tail rows |
| **VAL-03** | `branch` | 100% values ∈ {`CSE`, `IT`, `ECE`, `EEE`, `ME`, `CE`}. | Any lowercase or unapproved string. | `str.strip()` + `str.upper()` |
| **VAL-04** | `gender` | 100% values ∈ {`Female`, `Male`, `Non-binary`, `Prefer not to say`}. | Any whitespace padding or unapproved category. | `str.strip()` |
| **VAL-05** | `company_type` | 100% values ∈ {`Product`, `Service`, `Startup`, `Other`} for `placed=1`; `NULL` for `placed=0`. | Any lowercase/padded string or `placed=0` non-null. | `str.strip()` + `str.title()` |
| **VAL-06** | `python_skill` | 100% values ∈ {`0`, `1`} (Binary integer). | Any string `"Yes"`, `"No"`, `"True"`, `"False"`. | Binary mapping: `"Yes"`/`"True"` $\rightarrow 1$, `"No"`/`"False"` $\rightarrow 0$ |
| **VAL-07** | `communication_score` | 100% non-null numeric floats in range [0.00, 100.00]. | Any missing value or out-of-bounds score. | Impute missing values via branch-level cohort median |
| **VAL-08** | `package_lpa` | 100% non-null floats in (0.00, 50.00] for `placed=1`; 100% `NULL` for `placed=0`. | Any `placed=0` non-null/zero package or `placed=1` null package. | Preserve strict placement linkage rule |

---

## 2. Integrity & Target Leakage Rules

1. **Target Leakage Prohibition:** `placed`, `package_lpa`, and `company_type` MUST NEVER be used as predictors or sources to impute academic/score features (`communication_score`, `cgpa`, `coding_score`, `aptitude_score`).
2. **Meaningful NULL Rule:** `package_lpa` and `company_type` MUST remain `NULL` for unplaced students (`placed = 0`). Converting `NULL` to `0.00` or `"None"` is strictly prohibited.
3. **Audit Trail Rule:** Every imputation operation MUST be logged in `outputs/cleaning/imputation_log.csv` recording `student_id`, `original_value`, `branch`, `imputation_method`, and `imputed_value`.
