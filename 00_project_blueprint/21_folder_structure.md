# Folder Structure

```text
PlacementLens/
├── 00_project_blueprint/  # Phase-0 source of truth; do not bypass
├── data/
│   ├── raw/               # Frozen synthetic source CSV and source note
│   └── processed/         # Validated clean CSV and derived readiness export
├── notebooks/             # Ordered notebooks 01–05
├── sql/                   # DDL, load script, query catalog, 15–20 queries
├── dashboard/             # PBIX, DAX/data notes, screenshots
├── docs/                  # Findings, methodology, handoff, portfolio narrative
├── tests/                 # Data-quality and reconciliation checks
├── outputs/               # Generated charts/tables; never manually authoritative
└── README.md              # Entry point and recovery instructions
```

Naming rule: use sortable numeric prefixes for sequential artifacts and descriptive `snake_case` elsewhere. Do not store raw PII, database credentials, temporary IDE files, or manually edited metric exports in the repository.

