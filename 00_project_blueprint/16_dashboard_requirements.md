# Dashboard Requirements

## Global design

Power BI consumes only the Phase-2 clean export (and approved derived readiness export). Include a visible synthetic-data/association disclaimer, last-refresh date, filters for branch, gender, CGPA band, and placement status where meaningful, and an accessible color palette.

## Page 1 — Placement Overview

- KPI cards: total students, placement rate, average/median/highest placed package.
- Placement rate by branch and CGPA band; placed vs unplaced count; package distribution.
- Tooltips show denominator/count, not only percentages.

## Page 2 — Skills & Performance

- Skill adoption and skill-wise placement rate.
- Coding, aptitude, and communication comparison by outcome.
- Internship and project comparisons.

## Page 3 — Student Readiness

- Readiness distribution, readiness by branch, readiness by placement outcome.
- Aggregate skill-gaps and priority-improvement areas; avoid an individual hiring-style leaderboard.
- Visible explanation that index is project-designed, not predictive.

## Measure reconciliation

Define every DAX measure in `dashboard/README.md` and reconcile selected filter states to Python/SQL. Metric differences may only be display rounding and must be logged.

