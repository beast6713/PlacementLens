# Placement Readiness Index Specification

## Purpose and guardrail

The Placement Readiness Index (PRI) is a transparent **project-designed analytical framework**, not an industry standard, probability, or placement prediction. It supports preparation reflection only.

## Components (0–100)

| Component | Calculation | Weight |
|---|---|---:|
| Technical skills | `(sum of seven binary skill flags / 7) × 100` | 25% |
| Aptitude | `aptitude_score` | 20% |
| CGPA | `(cgpa / 10) × 100` | 15% |
| Projects | `min(projects / 5, 1) × 100` | 15% |
| Internship | `min(internships / 2, 1) × 100` | 15% |
| Communication | `communication_score` | 10% |

`PRI = 0.25×technical + 0.20×aptitude + 0.15×cgpa_normalized + 0.15×projects_normalized + 0.15×internships_normalized + 0.10×communication`

Round only for display; retain calculation precision in data. Coding score is intentionally analyzed separately and not included, to prevent double-counting technical assessments without a validated weighting study. This decision is frozen for the initial project.

## Categories

| PRI | Category |
|---|---|
| 80–100 | High Readiness |
| 60–79.999… | Moderate Readiness |
| 40–59.999… | Needs Improvement |
| <40 | High Improvement Priority |

## Gap priority logic

For each student, list up to three lowest normalized components. Break ties by this fixed priority: Technical skills, Aptitude, Projects, Internship, Communication, CGPA. Phrase output as preparation priorities, never defects or hiring recommendations. Validate component bounds and total formula for every retained record.

