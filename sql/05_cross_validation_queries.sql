-- PlacementLens — Phase 3 Part 5: SQL Cross-Validation Support Queries
-- Target Schema/Table: public.students / students
-- Extracts cross-validation metrics for direct verification against Python EDA outputs

-- 1. Population & Placement Overview
SELECT 
    COUNT(*) AS total_students,
    SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS placed_count,
    SUM(CASE WHEN placed IN (FALSE, 0) THEN 1 ELSE 0 END) AS unplaced_count,
    ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / COUNT(*), 2) AS placement_rate_pct
FROM students;

-- 2. Branch Placement Rates & Student Counts
SELECT 
    branch,
    COUNT(*) AS total_students,
    SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS placed_students,
    SUM(CASE WHEN placed IN (FALSE, 0) THEN 1 ELSE 0 END) AS unplaced_students,
    ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / COUNT(*), 2) AS placement_rate_pct
FROM students
GROUP BY branch
ORDER BY branch ASC;

-- 3. Technical Skill Flag Counts & Placement Spreads
WITH skill_unions AS (
    SELECT 'python_skill' AS skill_name, python_skill AS has_skill, placed FROM students
    UNION ALL SELECT 'sql_skill', sql_skill, placed FROM students
    UNION ALL SELECT 'excel_skill', excel_skill, placed FROM students
    UNION ALL SELECT 'power_bi_skill', power_bi_skill, placed FROM students
    UNION ALL SELECT 'dsa_skill', dsa_skill, placed FROM students
    UNION ALL SELECT 'cloud_skill', cloud_skill, placed FROM students
    UNION ALL SELECT 'cybersecurity_skill', cybersecurity_skill, placed FROM students
)
SELECT 
    skill_name,
    SUM(CASE WHEN has_skill = 1 THEN 1 ELSE 0 END) AS holder_count,
    ROUND(100.0 * SUM(CASE WHEN has_skill = 1 AND placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN has_skill = 1 THEN 1 ELSE 0 END), 0), 2) AS holder_rate_pct,
    SUM(CASE WHEN has_skill = 0 THEN 1 ELSE 0 END) AS non_holder_count,
    ROUND(100.0 * SUM(CASE WHEN has_skill = 0 AND placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN has_skill = 0 THEN 1 ELSE 0 END), 0), 2) AS non_holder_rate_pct,
    ROUND(
        ROUND(100.0 * SUM(CASE WHEN has_skill = 1 AND placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN has_skill = 1 THEN 1 ELSE 0 END), 0), 2) -
        ROUND(100.0 * SUM(CASE WHEN has_skill = 0 AND placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN has_skill = 0 THEN 1 ELSE 0 END), 0), 2), 2
    ) AS spread_pp
FROM skill_unions
GROUP BY skill_name
ORDER BY skill_name ASC;

-- 4. Compensation Metrics (Placed Cohort N=950 Only)
SELECT 
    COUNT(package_lpa) AS placed_count,
    ROUND(AVG(package_lpa), 2) AS mean_package_lpa,
    ROUND(MIN(package_lpa), 2) AS min_package_lpa,
    ROUND(MAX(package_lpa), 2) AS max_package_lpa
FROM students
WHERE placed IN (TRUE, 1) AND package_lpa IS NOT NULL;
