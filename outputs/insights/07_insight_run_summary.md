# Phase 4 Part 2 — Analytical Insight Extraction Run Summary

## 1. Execution Overview
- **Phase:** Phase 4 Part 2 (Analytical Insight Extraction)
- **Status:** COMPLETED — PASS
- **Dataset Input:** `data/processed/placementlens_students_clean.csv`
- **Clean MD5 Hash:** `96023d297eec5a9a47563eaddc157d0d` (Verified Match)
- **Raw MD5 Hash:** `59c04ee15a0112806c510225d8e75779` (Verified Match)
- **Population:** N=1,500 students (950 Placed, 550 Unplaced)

## 2. Extraction Results Summary
- **Candidate Patterns Reviewed:** 19
- **Validated Insights Extracted:** 15
- **Rejected Candidate Patterns:** 4
- **Priority Distribution:**
  - **HIGH Priority:** 7 Insights
  - **MEDIUM Priority:** 5 Insights
  - **LOW / DESCRIPTIVE Priority:** 3 Insights

## 3. Compliance & Governance Certification
- **Non-Causal Language:** 100% Compliant (`ASSOCIATION ≠ CAUSATION` strictly enforced).
- **Target Leakage:** 0 Target Leakage defects (Outcome variables `package_lpa` and `company_type` restricted to post-placement N=950 analysis).
- **NULL Semantics:** 100% Preserved (Unplaced package LPA remains `NULL`).
- **PRI Scope Boundary:** PRI score calculations strictly deferred to P4-P5 (`INS-READINESS-001` marked DEFERRED).

## 4. Generated Artifacts Inventory
All 8 required artifacts created under `outputs/insights/`:
1. `01_insight_inventory.csv`
2. `02_insight_register.csv`
3. `03_insight_evidence.csv`
4. `04_insight_validation.csv`
5. `05_insight_priority.csv`
6. `06_insight_summary.csv`
7. `07_insight_run_summary.md`
8. `analytical_insights.md`
