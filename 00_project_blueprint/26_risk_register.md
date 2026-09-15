# Risk Register

| ID | Risk | Impact | Likelihood | Mitigation | Trigger / owner action |
|---|---|---|---|---|---|
| R-01 | Poor or invalid source data | High | Medium | DQ rules, generator constraints, test gate | Hard validation failure: stop at Phase 2. |
| R-02 | Unrealistic synthetic relationships | High | Medium | Distribution/consistency review; no perfect rules | Implausible patterns: revise generator, rerun downstream. |
| R-03 | Scope creep | High | Medium | Scope document, backlog, approval rule | New feature: log and defer unless approved. |
| R-04 | Incorrect SQL calculations | High | Medium | Query catalog and Python reconciliation | Metric mismatch: root-cause process. |
| R-05 | Dashboard mismatch | High | Medium | DAX documentation and sampled filter-state checks | KPI mismatch: invalidate dashboard output. |
| R-06 | Weak or fabricated insights | High | Medium | AQ-led analysis and insight template | Missing evidence: do not publish finding. |
| R-07 | Seven-day time shortage | High | Medium | Checkpoint gates and priority order | Missed day: preserve core scope, defer backlog. |
| R-08 | Privacy/ethical misuse | High | Low | Synthetic data disclosure and non-decision policy | PII or predictive claim: remove/correct immediately. |
| R-09 | Handoff failure | Medium | Medium | README, checkpoints, change log, source notes | New agent unclear: update documentation before work. |

