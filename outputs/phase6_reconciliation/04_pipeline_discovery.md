# PlacementLens — Automated Pipeline Discovery

## 1. Discovered Pipeline & Validation Scripts
- **Master Validation Suite:** `scripts/validate_phase5_dashboard.py`
  - Verifies Raw CSV MD5 (`59c04ee15a0112806c510225d8e75779`) and Clean CSV MD5 (`96023d297eec5a9a47563eaddc157d0d`).
  - Verifies baseline counts (1,500 total, 950 placed, 63.33% rate, 10.62 LPA mean package).
  - Tests PRI monotonicity, boundary conditions, and zero target leakage.
  - Generates 14 deliverable matrices in `outputs/powerbi/`.
  - Execution Result: **25 / 25 PASS**.

- **Data Export Pipeline:** `scripts/export_dashboard_data.py`
  - Re-reads clean CSV data, computes derived skill counts, PRI scores, and quadrant segmentations.
  - Exports JSON data asset `dashboard/src/data/placementData.json` consumed by React web dashboard.

## 2. Status
**COMPLETE** — Master validation runner and data asset export scripts exist and run cleanly.
