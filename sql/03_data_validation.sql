-- PlacementLens — PostgreSQL Data Quality & Baseline Validation Queries
-- Table: public.students

-- 1. Row Count Validation (Expected: 1,500)
SELECT COUNT(*) AS total_rows FROM public.students;

-- 2. Primary Key Uniqueness & ID Range Validation (Expected: 1,500 unique IDs)
SELECT 
    COUNT(student_id) AS total_ids,
    COUNT(DISTINCT student_id) AS unique_ids,
    MIN(student_id) AS min_id,
    MAX(student_id) AS max_id
FROM public.students;

-- 3. Placement Cohort Distribution & Placement Rate (Expected: 950 Placed, 550 Unplaced, 63.33%)
SELECT 
    COUNT(*) AS total_students,
    SUM(CASE WHEN placed = TRUE THEN 1 ELSE 0 END) AS placed_students,
    SUM(CASE WHEN placed = FALSE THEN 1 ELSE 0 END) AS unplaced_students,
    ROUND(100.0 * SUM(CASE WHEN placed = TRUE THEN 1 ELSE 0 END) / COUNT(*), 2) AS placement_rate_pct
FROM public.students;

-- 4. NULL Semantics & Linkage Check (Expected: 0 invalid records)
SELECT 
    SUM(CASE WHEN placed = FALSE AND (package_lpa IS NOT NULL OR company_type IS NOT NULL) THEN 1 ELSE 0 END) AS unplaced_non_null_violations,
    SUM(CASE WHEN placed = TRUE AND (package_lpa IS NULL OR company_type IS NULL) THEN 1 ELSE 0 END) AS placed_null_violations
FROM public.students;

-- 5. Branch Counts & Placement Rate Breakdown
SELECT 
    branch,
    COUNT(*) AS total_students,
    SUM(CASE WHEN placed = TRUE THEN 1 ELSE 0 END) AS placed_students,
    ROUND(100.0 * SUM(CASE WHEN placed = TRUE THEN 1 ELSE 0 END) / COUNT(*), 2) AS placement_rate_pct
FROM public.students
GROUP BY branch
ORDER BY placement_rate_pct DESC;

-- 6. Technical Skill Flag Integrity & Prevalence Counts
SELECT 
    SUM(python_skill)       AS python_holders,
    SUM(sql_skill)          AS sql_holders,
    SUM(excel_skill)        AS excel_holders,
    SUM(power_bi_skill)     AS power_bi_holders,
    SUM(dsa_skill)          AS dsa_holders,
    SUM(cloud_skill)        AS cloud_holders,
    SUM(cybersecurity_skill) AS cybersecurity_holders
FROM public.students;

-- 7. Placed Compensation Metrics (Expected: 950 Placed, Median ~ 9.70 LPA)
SELECT 
    COUNT(package_lpa) AS placed_count,
    ROUND(AVG(package_lpa), 2) AS mean_package_lpa,
    ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY package_lpa)::NUMERIC, 2) AS median_package_lpa,
    MIN(package_lpa) AS min_package_lpa,
    MAX(package_lpa) AS max_package_lpa
FROM public.students
WHERE placed = TRUE;
