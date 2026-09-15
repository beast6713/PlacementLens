# PlacementLens — Power BI DAX Development Guidelines

> **Document Status:** APPROVED ENGINEERING GUIDELINES  
> **Phase Target:** Phase 5 Part 2 — DAX Measures & Metric Contract  

---

## 1. Naming & Formatting Conventions

- **Clear Business Names:** Use descriptive names in Title Case (e.g. `[Placement Rate]`, `[Average Package]`, `[Python Skill Placement Spread]`).
- **Forbidden Names:** Never use generic or temporary names like `[Measure 1]`, `[Test]`, `[Calc]`, or `[Final]`.
- **Formatting Standards:**
  - Counts: `#,##0` (e.g., `1,500`)
  - Percentages / Rates: `0.00%` (e.g., `63.33%`)
  - Salary Packages: `0.00 "LPA"` (e.g., `10.62 LPA`)
  - Scores & PRI: `0.00` (e.g., `65.59`)

---

## 2. Measure vs. Calculated Column Policy

- **Calculated Columns:** Used ONLY for static, row-level attributes provided in the source model (e.g., `student_id`, `branch`, `pri_score`, `readiness_category`, `preparation_segment`).
- **DAX Measures:** Used for ALL aggregations, rates, averages, medians, differences, and slice-dependent ratios.
- **Rule:** Never duplicate a validated Phase 4 column as a competing DAX calculated column.

---

## 3. Safe Division & Filter Context Guidelines

- **DIVIDE Protection:** Always use `DIVIDE(numerator, denominator, 0)` for division to eliminate division-by-zero errors.
- **Filter Awareness:** Measures must respond naturally to slicers (Branch, Gender, Placement Status, PRI Tier, Segment).
- **FILTER Removal Prohibition:** Do NOT use `ALL()`, `REMOVEFILTERS()`, or `ALLEXCEPT()` unless creating an explicit fixed-population benchmark measure (e.g., `[Total Cohort Students]`).

---

## 4. NULL Semantics & Compensation Contract

- **Unplaced Packages:** Unplaced students ($N=550$) have `package_lpa = NULL`.
- **DAX Behavior:** `AVERAGE(Students[package_lpa])` and `MEDIAN(Students[package_lpa])` naturally ignore `NULL` rows in DAX, evaluating strictly over the 950 placed students.
- **Forbidden Patterns:** Do NOT use `COALESCE(package_lpa, 0)` or `IF(ISBLANK(package_lpa), 0, package_lpa)`.

---

## 5. Target Leakage Controls & Non-Causal Phrasing

- **Formula Isolation:** `placed`, `package_lpa`, and `company_type` MUST NOT enter PRI formula calculation logic.
- **Observational Language:** Use neutral terms like `Spread` or `Observed Difference` (e.g., `[SQL Skill Placement Spread]`) rather than causal claims like `Impact` or `Effect`.

---

## 6. Centralized Measure Organization

- All DAX measures are stored in a dedicated `Measures` table.
- Measures are organized into 9 numerical display folders:
  - `01 — Population`
  - `02 — Academic`
  - `03 — Preparation`
  - `04 — Differences`
  - `05 — Skills`
  - `06 — Compensation`
  - `07 — Readiness`
  - `08 — Segmentation`
  - `09 — Validation`

---

## 7. Performance & Interview Defensibility

- **Simplicity & Maintainability:** Prefer readable, modular base measures (`[Total Students]`, `[Placed Students]`) that feed downstream ratio measures (`[Placement Rate]`).
- **Interview Defensibility:** Every measure must be easy to explain in a technical interview (e.g., explaining numerator/denominator context transitions cleanly).
