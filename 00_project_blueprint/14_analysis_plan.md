# Analysis Plan

## Sequence

1. Profile raw data and confirm schema (Phase 1).
2. Clean and validate using documented rules; publish a quality report (Phase 2).
3. Build reproducible Python descriptive analysis, distributions, comparisons, and association screens (Phase 3).
4. Load the same clean data into SQLite and cross-check key calculations through SQL (Phase 3).
5. Create findings only after results exist; use the insight template (Phase 4).
6. Calculate readiness and gap indicators from the published formula (Phase 4).
7. Build and reconcile the dashboard; complete portfolio assets (Phase 5).

## Methods and interpretation

- Descriptive: counts, rates, means, medians, percentiles, distributions.
- Comparative: placed/unplaced and grouped summaries, with sample sizes.
- Association screen: point-biserial/Pearson or Spearman correlation as appropriate, contingency tables, and optionally confidence intervals/tests if assumptions are documented.
- No multivariate prediction model is in scope. No causal conclusion is permitted.

## Required reproducible assets

Planned notebooks: `01_data_understanding.ipynb`, `02_cleaning_validation.ipynb`, `03_eda.ipynb`, `04_statistical_analysis.ipynb`, `05_readiness_gap_analysis.ipynb`. Each must have explicit inputs, outputs, and validation notes.

