# Unsupported Fields Audit

## 1. Audit Criteria
Search for non-canonical or fabricated entity fields (`academic_year`, `batch`, `eligibility`, `company_name`, `offer_count`, `recruitment_date`, `placement_date`, `active_companies`, `company_leaderboard`).

## 2. Findings
- **`company_name`:** 0 instances (Only 4 macro `company_type` categories used).
- **`academic_year` / `batch`:** 0 instances (Single cohort 1,500 students).
- **`offer_count` / `recruitment_date`:** 0 instances.
- **Design Mockup Values Audit:** 0 instances of non-project design mockup numbers (842, 617, 73%, ₹8.4L) in production analytics.

## 3. Status
**PASS** — Zero unsupported analytical fields or fabricated entity data introduced.
