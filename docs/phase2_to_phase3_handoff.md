# PlacementLens — Phase 2 to Phase 3 Handoff Specification

**Document Purpose:** Provide Phase 3 (Python EDA + SQL Analytics) with complete operational instructions, dataset input contracts, and analytical boundaries.

---

## 1. Project Status & Input Contract

- **Phase 2 Status:** **COMPLETE & FROZEN (`CHECKPOINT-02-PHASE-2-COMPLETE: PASS`)**
- **Canonical Input Path:** `data/processed/placementlens_students_clean.csv`
- **Dataset Hash (MD5):** `96023d297eec5a9a47563eaddc157d0d`
- **Dataset Version:** `v1.0-clean`
- **Population:** Exactly 1,500 unique student records (`S0001` through `S1500`).
- **Schema:** 20 columns conforming to `v1.0 DDL`.

---

## 2. Authorized Phase 3 Operations

Phase 3 is authorized to perform:
1. **Python EDA:** Descriptive statistics, distribution plots, correlation analysis, and skill frequency profiling.
2. **PostgreSQL Loading:** Ingesting `data/processed/placementlens_students_clean.csv` into `public.students` table.
3. **SQL Analytics:** Executing SQL queries for placement rates, branch performance, compensation percentiles, and skill combinations.
4. **Analytical Reporting:** Documenting business findings and data-driven insights.

---

## 3. Prohibited Phase 3 Actions & Target Leakage Prevention

Phase 3 MUST NOT:
1. **Modify Baseline CSV:** Overwrite or modify `data/processed/placementlens_students_clean.csv` or `data/raw/placementlens_students_raw.csv`.
2. **Re-Clean Baseline:** Re-run cleaning routines or alter historical Phase 2 transformations.
3. **Target Leakage:** Use `package_lpa` or `company_type` as predictors for placement status without explicitly controlling for leakage.
4. **Assume Causation:** Treat observational correlations in synthetic data as real-world causal mechanisms.

---

## 4. Known Synthetic Limitations

1. **Synthetic Nature:** Generated with fixed seed 42 to simulate placement dynamics.
2. **Scope Boundary:** Findings reflect the synthetic dataset distributions and rules established in Phase 1.
3. **Machine Learning & Scoring:** Placement Readiness Index scoring and predictive ML belong to Phase 4 (if enabled) and MUST NOT pollute Phase 3 baseline SQL tables.
