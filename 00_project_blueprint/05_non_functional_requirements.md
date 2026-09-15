# Non-Functional Requirements

- **Reproducibility:** a new agent can execute documented steps from raw data through outputs without manual metric edits.
- **Traceability:** every finding, recommendation, and dashboard metric links to a source calculation or query.
- **Accuracy:** phase gates block progression until validation criteria pass.
- **Usability:** dashboard uses clear labels, readable charts, tooltips, and filters; no chart should require hidden assumptions.
- **Maintainability:** stable names, ordered notebooks, modular SQL files, and a change log are mandatory.
- **Performance:** target data size is 1,500 rows; local analysis and dashboard refresh should complete comfortably on a typical laptop.
- **Security/privacy:** no PII, credentials, proprietary institutional data, or automated decision outputs.
- **Accessibility:** do not depend on color alone; provide titles, legends, and sufficient contrast.

