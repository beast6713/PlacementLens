-- PlacementLens — Phase 3 Part 4: SQL Quality & Metric Validation Script
-- Target Schema/Table: public.students / students

-- 1. Total Student Population & Primary Key Unique Count (Expected: 1,500)
SELECT 
    COUNT(*) AS total_students,
    COUNT(DISTINCT student_id) AS unique_students,
    MIN(student_id) AS min_student_id,
    MAX(student_id) AS max_student_id
FROM students;

-- 2. Placed & Unplaced Cohort Counts & Placement Rate (Expected: 950 Placed, 550 Unplaced, 63.33%)
SELECT 
    COUNT(*) AS total_students,
    SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS placed_count,
    SUM(CASE WHEN placed IN (FALSE, 0) THEN 1 ELSE 0 END) AS unplaced_count,
    ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / COUNT(*), 2) AS placement_rate_pct
FROM students;

-- 3. Branch Student Distribution & Placement Rates (6 Branches)
SELECT 
    branch,
    COUNT(*) AS branch_students,
    SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS branch_placed,
    ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / COUNT(*), 2) AS placement_rate_pct
FROM students
GROUP BY branch
ORDER BY branch ASC;

-- 4. NULL Linkage Integrity (Expected: 0 Violations)
SELECT 
    SUM(CASE WHEN placed IN (FALSE, 0) AND (package_lpa IS NOT NULL OR company_type IS NOT NULL) THEN 1 ELSE 0 END) AS unplaced_null_violations,
    SUM(CASE WHEN placed IN (TRUE, 1) AND (package_lpa IS NULL OR company_type IS NULL) THEN 1 ELSE 0 END) AS placed_null_violations
FROM students;

-- 5. Binary Skill Flag Bounds & Prevalence Summary
SELECT 
    SUM(python_skill)       AS python_cnt,
    SUM(sql_skill)          AS sql_cnt,
    SUM(excel_skill)        AS excel_cnt,
    SUM(power_bi_skill)     AS power_bi_cnt,
    SUM(dsa_skill)          AS dsa_cnt,
    SUM(cloud_skill)        AS cloud_cnt,
    SUM(cybersecurity_skill) AS cybersecurity_cnt
FROM students;

-- 6. Compensation Package Averages & Ranges (Placed Cohort N=950 Only)
SELECT 
    COUNT(package_lpa) AS placed_count,
    ROUND(AVG(package_lpa), 2) AS mean_package_lpa,
    ROUND(MIN(package_lpa), 2) AS min_package_lpa,
    ROUND(MAX(package_lpa), 2) AS max_package_lpa
FROM students
WHERE placed IN (TRUE, 1);
