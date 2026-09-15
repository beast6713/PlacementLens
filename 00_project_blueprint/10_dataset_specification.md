# Dataset Specification

## Decision

Phase 1 will create a **synthetic** dataset of exactly **1,500** de-identified student records. This choice avoids privacy risk and unverified public-data licensing. It must be labeled synthetic in the README, dashboard, notebooks, SQL documentation, and portfolio narrative.

## Grain and deliverables

- Grain: one row per synthetic student at a single placement-cycle snapshot.
- Raw deliverable: `data/raw/placementlens_students_raw.csv`.
- Clean deliverable: `data/processed/placementlens_students_clean.csv`.
- Identifier: generated `student_id` only; it has no link to a real person.
- Planned branches: `CSE`, `IT`, `ECE`, `EEE`, `ME`, `CE`.
- Planned gender values: `Female`, `Male`, `Non-binary`, `Prefer not to say`.
- Planned company types for placed students: `Product`, `Service`, `Startup`, `Other`.

## Approved fields

`student_id`, `age`, `gender`, `branch`, `cgpa`, `internships`, `projects`, `coding_score`, `aptitude_score`, `communication_score`, `python_skill`, `sql_skill`, `excel_skill`, `power_bi_skill`, `dsa_skill`, `cloud_skill`, `cybersecurity_skill`, `placed`, `company_type`, `package_lpa`.

## Generation design constraints (to implement in Phase 1)

- Use a fixed documented random seed and save the generator assumptions/version.
- Include plausible variation; avoid deterministic relationships or perfectly separable outcomes.
- Deliberately introduce a small, documented set of benign quality issues in the raw file (for example nulls, capitalization differences, and invalid values) solely to demonstrate Phase 2 validation. The clean dataset must not retain invalid data.
- Placement and package values must be internally consistent after cleaning: unplaced students have `company_type = NULL` and `package_lpa = NULL`; placed students have non-null valid values.
- Do not generate PII or make the data appear to represent a real college.

## Unresolved-but-nonblocking parameter

The exact random seed and raw-data defect rates are implementation parameters. They must be selected before generator execution, recorded in the Phase 1 source note, and frozen at CHECKPOINT-01.

