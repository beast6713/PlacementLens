# Data Privacy & Ethics Policy

## 1. Synthetic Data Disclosure & Zero PII Commitment

- **Synthetic Nature:** PlacementLens uses an internally generated **synthetic dataset** (`v1.0`). No real student data, institutional records, personal names, phone numbers, email addresses, government IDs, or private academic databases were accessed or utilized.
- **Mandatory Disclosure:** The synthetic nature of the dataset must be prominently disclosed in the project `README.md`, Jupyter Notebooks, SQL query scripts, Power BI dashboard footers, portfolio write-ups, and interview presentations.
- **Identifier Safety:** The `student_id` field (e.g. `S0001`) is a synthetic, sequential key with zero linkage to real individuals.

---

## 2. Ethical Requirements & Non-Discriminatory Policy

1. **Non-Causal Interpretations:** All statistical relationships observed in PlacementLens represent **associations**, not causal proofs. Finding a correlation between a skill (e.g., Python) and placement outcome does not prove that acquiring Python caused placement.
2. **No Automated Hiring / Selection:** PlacementLens is strictly an exploratory data analytics project designed for student self-reflection and institutional preparation strategy. It must **NEVER** be used to automate recruitment screening, rank students for job applications, or make admissions decisions.
3. **Gender Evaluation Guardrail:** Gender data (`Female`, `Male`, `Non-binary`, `Prefer not to say`) is included exclusively for aggregate demographic exploratory visualization. Gender is **strictly excluded** from Placement Readiness Index formulas, skill-gap calculations, and automated recommendation rules to prevent algorithmic bias or discriminatory profiling.
4. **No Unvalidated Performance Stigmatization:** Unplaced students or low-CGPA cohorts are presented constructively through preparation priority gap analysis, never as defective or non-viable candidates.

---

## 3. Responsible Portfolio Communication

When presenting PlacementLens in technical interviews or portfolio repositories:
- Explicitly state that `package_lpa` values are synthetic illustrative parameters and do not represent empirical market salary benchmarks.
- Clearly present dataset limitations and generation seed documentation (`SEED = 42`).
- Highlight data quality engineering practices (data validation, defect cleaning, reproducible generation) rather than claiming real-world predictive authority.
