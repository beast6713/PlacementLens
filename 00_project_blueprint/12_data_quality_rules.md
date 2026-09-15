# Data Quality & Distribution Validation Strategy

## 1. Quality Targets (Pass Criteria)

Before Phase 1 strategy validation is complete, the following baseline quality targets are established for dataset `v1.0`:

- **Record Count:** Exactly 1,500 synthetic student records generated.
- **Completeness:** 100% non-null values for all non-conditional fields in the clean deliverable.
- **Identifier Uniqueness:** `student_id` strictly unique (`S0001` to `S1500`) after clean deduplication.
- **Range Validity:** 100% of numerical values fall within defined dictionary bounds (`cgpa` ∈ [0,10], scores ∈ [0,100], `age` ∈ [18,25], `package_lpa` ∈ (0,50]).
- **Categorical Integrity:** All categorical strings match standard allowed sets after normalization.
- **Logical Consistency:** `placed = 1` ↔ valid `company_type` and positive `package_lpa`; `placed = 0` ↔ `company_type = NULL` and `package_lpa = NULL`.

---

## 2. Hard Rules (Fail Validation)

Hard rules represent critical structural constraints. Any violation in the clean dataset must halt pipeline execution and fail Phase 2 validation:

| Rule ID | Constraint Description | Clean Pipeline Action |
|---|---|---|
| **DQ-01** | `student_id` is unique, non-null, and matches format `^S[0-9]{4}$`. | Deduplicate duplicate raw rows; reject invalid formats. |
| **DQ-02** | All non-conditional fields (`age`, `gender`, `branch`, `cgpa`, `placed`, etc.) are non-null. | Impute documented non-critical fields or quarantine unfixable rows. |
| **DQ-03** | Numeric fields strictly satisfy data dictionary ranges. | Correct formatting variants (e.g. string numbers) or reject out-of-bounds anomalies. |
| **DQ-04** | Categorical variables strictly belong to authorized allowed sets. | Normalize case/spacing variants (e.g., `"cse"` → `"CSE"`); reject unknown categories. |
| **DQ-05** | Technical skill flags and `placed` are strictly binary (`0` or `1`). | Parse `"Yes"`/`"True"` to `1` and `"No"`/`"False"` to `0`; reject non-binary values. |
| **DQ-06** | Placement linkage integrity: `placed=1` ↔ `package_lpa > 0` and non-null `company_type`; `placed=0` ↔ both `NULL`. | Enforce logical consistency; quarantine rows violating structural placement rules. |

---

## 3. Soft Rules & Distribution Checks

Soft rules require inspection and profiling to ensure synthetic data realism and detect generation anomalies:

- **Branch Distribution:** Every branch must contain sufficient records (`CSE` ~30%, `IT` ~25%, `ECE` ~20%, `EEE` ~10%, `ME` ~8%, `CE` ~7%). No branch < 50 records.
- **Placement Class Balance:** Overall placement rate must fall between **60% and 70%** (neither 0% nor 100%).
- **Package Distribution:** Placed student salary packages must exhibit realistic positive skewness (e.g. median package ~6.0–8.0 LPA, max package ≤ 50.0 LPA).
- **Score Distributions:** Assessment scores (`coding_score`, `aptitude_score`, `communication_score`) must display continuous variation spanning 20.0 to 100.0 without artificial clustering at boundary endpoints.
- **Outlier Screening:** Profile distributions using IQR and z-score checks. Legitimate high performers (e.g., CGPA 9.8, package 45 LPA) are preserved, while invalid values outside dictionary ranges are flagged.

---

## 4. Controlled Raw Defect Injection Strategy

To demonstrate robust cleaning and profiling capabilities in Phase 2, raw generation will inject controlled defects into `data/raw/placementlens_students_raw.csv`:

| Defect Type | Target Field(s) | Estimated Raw Rate | Objective / Recovery Plan |
|---|---|---|---|
| Case Inconsistency | `branch`, `company_type` | ~2.0% of rows | Test string normalization routines (`str.upper()`, `str.title()`). |
| Whitespace Padding | `branch`, `gender`, `company_type` | ~1.5% of rows | Test whitespace trimming routines (`str.strip()`). |
| String-Binary Variant | `python_skill`, `sql_skill`, `placed` | ~1.0% of rows | Test type-casting and boolean mapping routines. |
| Missing Score / Count | `communication_score`, `projects` | ~1.0% of rows | Test documented missing-data imputation strategies. |
| Duplicate Raw Rows | `student_id` | ~0.5% (5–8 rows) | Test deduplication logic retaining first valid row. |

*Crucial Rule:* Raw defects are controlled, deliberate, documented, and recoverable. Core structural linkage between `placed` and compensation parameters (`package_lpa`, `company_type`) will remain intact in underlying probabilistic generation logic.
