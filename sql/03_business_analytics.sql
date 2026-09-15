-- PlacementLens — Phase 3 Part 4: SQL Business Analytics Queries
-- Target Schema/Table: public.students / students
-- Answers Frozen Business Questions BQ01 – BQ21 using PostgreSQL SQL semantics

-- ============================================================
-- BQ01: OVERALL PLACEMENT RATE
-- ============================================================
-- Query ID: Q01_Overall_Placement
SELECT 
    COUNT(*) AS total_students,
    SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS placed_students,
    SUM(CASE WHEN placed IN (FALSE, 0) THEN 1 ELSE 0 END) AS unplaced_students,
    ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0), 2) AS placement_rate_pct
FROM students;


-- ============================================================
-- BQ02: PLACEMENT RATE BY BRANCH (WITH WINDOW RANKING)
-- ============================================================
-- Query ID: Q02_Branch_Placement
WITH branch_metrics AS (
    SELECT 
        branch,
        COUNT(*) AS total_students,
        SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS placed_students,
        SUM(CASE WHEN placed IN (FALSE, 0) THEN 1 ELSE 0 END) AS unplaced_students,
        ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0), 2) AS placement_rate_pct
    FROM students
    GROUP BY branch
)
SELECT 
    branch,
    total_students,
    placed_students,
    unplaced_students,
    placement_rate_pct,
    DENSE_RANK() OVER (ORDER BY placement_rate_pct DESC) AS placement_rank
FROM branch_metrics
ORDER BY placement_rank ASC;


-- ============================================================
-- BQ03: PLACEMENT ACROSS CGPA BANDS
-- ============================================================
-- Query ID: Q03_CGPA_Placement
WITH cgpa_banded AS (
    SELECT 
        student_id,
        placed,
        CASE 
            WHEN cgpa < 6.00 THEN '1. < 6.0'
            WHEN cgpa < 7.00 THEN '2. 6.0 – 6.99'
            WHEN cgpa < 8.00 THEN '3. 7.0 – 7.99'
            WHEN cgpa < 9.00 THEN '4. 8.0 – 8.99'
            ELSE '5. 9.0 – 10.0'
        END AS cgpa_band
    FROM students
)
SELECT 
    cgpa_band,
    COUNT(*) AS total_students,
    SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS placed_students,
    SUM(CASE WHEN placed IN (FALSE, 0) THEN 1 ELSE 0 END) AS unplaced_students,
    ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0), 2) AS placement_rate_pct
FROM cgpa_banded
GROUP BY cgpa_band
ORDER BY cgpa_band ASC;


-- ============================================================
-- BQ04: CODING SCORE BANDS VS PLACEMENT
-- ============================================================
-- Query ID: Q04_Coding_Placement
WITH coding_banded AS (
    SELECT 
        student_id,
        placed,
        CASE 
            WHEN coding_score < 50.0 THEN '1. < 50'
            WHEN coding_score < 65.0 THEN '2. 50 – 64'
            WHEN coding_score < 80.0 THEN '3. 65 – 79'
            WHEN coding_score < 90.0 THEN '4. 80 – 89'
            ELSE '5. 90 – 100'
        END AS coding_score_band
    FROM students
)
SELECT 
    coding_score_band,
    COUNT(*) AS total_students,
    SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS placed_students,
    SUM(CASE WHEN placed IN (FALSE, 0) THEN 1 ELSE 0 END) AS unplaced_students,
    ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0), 2) AS placement_rate_pct
FROM coding_banded
GROUP BY coding_score_band
ORDER BY coding_score_band ASC;


-- ============================================================
-- BQ05: APTITUDE SCORE BANDS VS PLACEMENT
-- ============================================================
-- Query ID: Q05_Aptitude_Placement
WITH aptitude_banded AS (
    SELECT 
        student_id,
        placed,
        CASE 
            WHEN aptitude_score < 50.0 THEN '1. < 50'
            WHEN aptitude_score < 65.0 THEN '2. 50 – 64'
            WHEN aptitude_score < 80.0 THEN '3. 65 – 79'
            WHEN aptitude_score < 90.0 THEN '4. 80 – 89'
            ELSE '5. 90 – 100'
        END AS aptitude_score_band
    FROM students
)
SELECT 
    aptitude_score_band,
    COUNT(*) AS total_students,
    SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS placed_students,
    SUM(CASE WHEN placed IN (FALSE, 0) THEN 1 ELSE 0 END) AS unplaced_students,
    ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0), 2) AS placement_rate_pct
FROM aptitude_banded
GROUP BY aptitude_score_band
ORDER BY aptitude_score_band ASC;


-- ============================================================
-- BQ06: COMMUNICATION SCORE BANDS VS PLACEMENT
-- ============================================================
-- Query ID: Q06_Communication_Placement
WITH comm_banded AS (
    SELECT 
        student_id,
        placed,
        CASE 
            WHEN communication_score < 50.0 THEN '1. < 50'
            WHEN communication_score < 65.0 THEN '2. 50 – 64'
            WHEN communication_score < 80.0 THEN '3. 65 – 79'
            WHEN communication_score < 90.0 THEN '4. 80 – 89'
            ELSE '5. 90 – 100'
        END AS communication_score_band
    FROM students
)
SELECT 
    communication_score_band,
    COUNT(*) AS total_students,
    SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS placed_students,
    SUM(CASE WHEN placed IN (FALSE, 0) THEN 1 ELSE 0 END) AS unplaced_students,
    ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0), 2) AS placement_rate_pct
FROM comm_banded
GROUP BY communication_score_band
ORDER BY communication_score_band ASC;


-- ============================================================
-- BQ07: PROJECTS COUNT VS PLACEMENT
-- ============================================================
-- Query ID: Q07_Projects_Placement
SELECT 
    projects AS project_count,
    COUNT(*) AS total_students,
    SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS placed_students,
    SUM(CASE WHEN placed IN (FALSE, 0) THEN 1 ELSE 0 END) AS unplaced_students,
    ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0), 2) AS placement_rate_pct
FROM students
GROUP BY projects
ORDER BY projects ASC;


-- ============================================================
-- BQ08: INTERNSHIPS COUNT VS PLACEMENT
-- ============================================================
-- Query ID: Q08_Internships_Placement
SELECT 
    internships AS internship_count,
    COUNT(*) AS total_students,
    SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS placed_students,
    SUM(CASE WHEN placed IN (FALSE, 0) THEN 1 ELSE 0 END) AS unplaced_students,
    ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0), 2) AS placement_rate_pct
FROM students
GROUP BY internships
ORDER BY internships ASC;


-- ============================================================
-- BQ09: TECHNICAL SKILL OWNERSHIP & IMPACT SPREAD
-- ============================================================
-- Query ID: Q09_Skill_Ownership
WITH skill_unions AS (
    SELECT 'python_skill' AS skill_name, python_skill AS has_skill, placed FROM students
    UNION ALL
    SELECT 'sql_skill', sql_skill, placed FROM students
    UNION ALL
    SELECT 'excel_skill', excel_skill, placed FROM students
    UNION ALL
    SELECT 'power_bi_skill', power_bi_skill, placed FROM students
    UNION ALL
    SELECT 'dsa_skill', dsa_skill, placed FROM students
    UNION ALL
    SELECT 'cloud_skill', cloud_skill, placed FROM students
    UNION ALL
    SELECT 'cybersecurity_skill', cybersecurity_skill, placed FROM students
),
skill_aggs AS (
    SELECT 
        skill_name,
        SUM(CASE WHEN has_skill = 1 THEN 1 ELSE 0 END) AS holder_count,
        SUM(CASE WHEN has_skill = 1 AND placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS holder_placed_count,
        ROUND(100.0 * SUM(CASE WHEN has_skill = 1 AND placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN has_skill = 1 THEN 1 ELSE 0 END), 0), 2) AS holder_placement_rate_pct,
        SUM(CASE WHEN has_skill = 0 THEN 1 ELSE 0 END) AS non_holder_count,
        SUM(CASE WHEN has_skill = 0 AND placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS non_holder_placed_count,
        ROUND(100.0 * SUM(CASE WHEN has_skill = 0 AND placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN has_skill = 0 THEN 1 ELSE 0 END), 0), 2) AS non_holder_placement_rate_pct
    FROM skill_unions
    GROUP BY skill_name
)
SELECT 
    skill_name,
    holder_count,
    holder_placed_count,
    holder_placement_rate_pct,
    non_holder_count,
    non_holder_placed_count,
    non_holder_placement_rate_pct,
    ROUND(holder_placement_rate_pct - non_holder_placement_rate_pct, 2) AS skill_impact_spread_pp
FROM skill_aggs
ORDER BY skill_impact_spread_pp DESC;


-- ============================================================
-- BQ10: SKILL PREVALENCE
-- ============================================================
-- Query ID: Q10_Skill_Prevalence
WITH skill_counts AS (
    SELECT 'python_skill' AS skill_name, SUM(python_skill) AS holder_count FROM students
    UNION ALL
    SELECT 'sql_skill', SUM(sql_skill) FROM students
    UNION ALL
    SELECT 'excel_skill', SUM(excel_skill) FROM students
    UNION ALL
    SELECT 'power_bi_skill', SUM(power_bi_skill) FROM students
    UNION ALL
    SELECT 'dsa_skill', SUM(dsa_skill) FROM students
    UNION ALL
    SELECT 'cloud_skill', SUM(cloud_skill) FROM students
    UNION ALL
    SELECT 'cybersecurity_skill', SUM(cybersecurity_skill) FROM students
)
SELECT 
    skill_name,
    holder_count,
    (SELECT COUNT(*) FROM students) AS total_students,
    ROUND(100.0 * holder_count / (SELECT COUNT(*) FROM students), 2) AS prevalence_pct
FROM skill_counts
ORDER BY prevalence_pct DESC;


-- ============================================================
-- BQ11: SKILL PLACEMENT-RATE DIFFERENCE & RANKING
-- ============================================================
-- Query ID: Q11_Skill_Spread_Ranking
WITH skill_unions AS (
    SELECT 'python_skill' AS skill_name, python_skill AS has_skill, placed FROM students
    UNION ALL
    SELECT 'sql_skill', sql_skill, placed FROM students
    UNION ALL
    SELECT 'excel_skill', excel_skill, placed FROM students
    UNION ALL
    SELECT 'power_bi_skill', power_bi_skill, placed FROM students
    UNION ALL
    SELECT 'dsa_skill', dsa_skill, placed FROM students
    UNION ALL
    SELECT 'cloud_skill', cloud_skill, placed FROM students
    UNION ALL
    SELECT 'cybersecurity_skill', cybersecurity_skill, placed FROM students
),
skill_rates AS (
    SELECT 
        skill_name,
        ROUND(100.0 * SUM(CASE WHEN has_skill = 1 AND placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN has_skill = 1 THEN 1 ELSE 0 END), 0), 2) AS holder_rate_pct,
        ROUND(100.0 * SUM(CASE WHEN has_skill = 0 AND placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN has_skill = 0 THEN 1 ELSE 0 END), 0), 2) AS non_holder_rate_pct
    FROM skill_unions
    GROUP BY skill_name
),
spread_calc AS (
    SELECT 
        skill_name,
        holder_rate_pct,
        non_holder_rate_pct,
        ROUND(holder_rate_pct - non_holder_rate_pct, 2) AS spread_pp
    FROM skill_rates
)
SELECT 
    skill_name,
    holder_rate_pct,
    non_holder_rate_pct,
    spread_pp,
    DENSE_RANK() OVER (ORDER BY spread_pp DESC) AS spread_rank
FROM spread_calc
ORDER BY spread_rank ASC;


-- ============================================================
-- BQ12: TECHNICAL SKILL COUNT VS PLACEMENT
-- ============================================================
-- Query ID: Q12_Skill_Count_Placement
WITH student_skill_counts AS (
    SELECT 
        student_id,
        placed,
        (python_skill + sql_skill + excel_skill + power_bi_skill + dsa_skill + cloud_skill + cybersecurity_skill) AS technical_skill_count
    FROM students
)
SELECT 
    technical_skill_count,
    COUNT(*) AS total_students,
    SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) AS placed_students,
    SUM(CASE WHEN placed IN (FALSE, 0) THEN 1 ELSE 0 END) AS unplaced_students,
    ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0), 2) AS placement_rate_pct
FROM student_skill_counts
GROUP BY technical_skill_count
ORDER BY technical_skill_count ASC;


-- ============================================================
-- BQ13: PACKAGE DISTRIBUTION (PLACED COHORT N=950 ONLY)
-- ============================================================
-- Query ID: Q13_Package_Distribution
SELECT 
    COUNT(package_lpa) AS placed_count,
    ROUND(AVG(package_lpa), 2) AS mean_package_lpa,
    ROUND(MIN(package_lpa), 2) AS min_package_lpa,
    ROUND(MAX(package_lpa), 2) AS max_package_lpa,
    ROUND(STDDEV(package_lpa), 2) AS std_package_lpa
FROM students
WHERE placed IN (TRUE, 1) AND package_lpa IS NOT NULL;


-- ============================================================
-- BQ14: MEDIAN & MEAN PACKAGE BY BRANCH (PLACED COHORT ONLY)
-- ============================================================
-- Query ID: Q14_Package_By_Branch
SELECT 
    branch,
    COUNT(package_lpa) AS placed_students,
    ROUND(AVG(package_lpa), 2) AS mean_package_lpa,
    ROUND(MIN(package_lpa), 2) AS min_package_lpa,
    ROUND(MAX(package_lpa), 2) AS max_package_lpa
FROM students
WHERE placed IN (TRUE, 1) AND package_lpa IS NOT NULL
GROUP BY branch
ORDER BY mean_package_lpa DESC;


-- ============================================================
-- BQ15: MEDIAN & MEAN PACKAGE BY COMPANY TYPE (PLACED COHORT ONLY)
-- ============================================================
-- Query ID: Q15_Package_By_Company
SELECT 
    company_type,
    COUNT(package_lpa) AS placed_students,
    ROUND(AVG(package_lpa), 2) AS mean_package_lpa,
    ROUND(MIN(package_lpa), 2) AS min_package_lpa,
    ROUND(MAX(package_lpa), 2) AS max_package_lpa
FROM students
WHERE placed IN (TRUE, 1) AND company_type IS NOT NULL AND package_lpa IS NOT NULL
GROUP BY company_type
ORDER BY mean_package_lpa DESC;


-- ============================================================
-- BQ16: PREPARATION INDICATORS ACROSS PACKAGE BANDS (PLACED ONLY)
-- ============================================================
-- Query ID: Q16_Package_Band_Preparation
WITH package_banded AS (
    SELECT 
        student_id,
        cgpa,
        coding_score,
        aptitude_score,
        communication_score,
        projects,
        internships,
        (python_skill + sql_skill + excel_skill + power_bi_skill + dsa_skill + cloud_skill + cybersecurity_skill) AS technical_skill_count,
        package_lpa,
        CASE 
            WHEN package_lpa < 4.00 THEN '1. < 4.0 LPA'
            WHEN package_lpa < 6.00 THEN '2. 4.0 – 6.0 LPA'
            WHEN package_lpa < 10.00 THEN '3. 6.0 – 10.0 LPA'
            ELSE '4. 10.0+ LPA'
        END AS package_band
    FROM students
    WHERE placed IN (TRUE, 1) AND package_lpa IS NOT NULL
)
SELECT 
    package_band,
    COUNT(*) AS placed_students,
    ROUND(AVG(cgpa), 2) AS avg_cgpa,
    ROUND(AVG(coding_score), 2) AS avg_coding_score,
    ROUND(AVG(aptitude_score), 2) AS avg_aptitude_score,
    ROUND(AVG(communication_score), 2) AS avg_communication_score,
    ROUND(AVG(projects), 2) AS avg_projects,
    ROUND(AVG(internships), 2) AS avg_internships,
    ROUND(AVG(technical_skill_count), 2) AS avg_technical_skill_count
FROM package_banded
GROUP BY package_band
ORDER BY package_band ASC;


-- ============================================================
-- BQ17: PLACED VS UNPLACED COHORT COMPARISON
-- ============================================================
-- Query ID: Q17_Placed_VS_Unplaced
SELECT 
    CASE WHEN placed IN (TRUE, 1) THEN 'Placed' ELSE 'Unplaced' END AS cohort,
    COUNT(*) AS student_count,
    ROUND(AVG(cgpa), 2) AS avg_cgpa,
    ROUND(AVG(coding_score), 2) AS avg_coding_score,
    ROUND(AVG(aptitude_score), 2) AS avg_aptitude_score,
    ROUND(AVG(communication_score), 2) AS avg_communication_score,
    ROUND(AVG(projects), 2) AS avg_projects,
    ROUND(AVG(internships), 2) AS avg_internships,
    ROUND(AVG(python_skill + sql_skill + excel_skill + power_bi_skill + dsa_skill + cloud_skill + cybersecurity_skill), 2) AS avg_technical_skill_count
FROM students
GROUP BY placed
ORDER BY cohort DESC;


-- ============================================================
-- BQ18: STRONGEST OBSERVED PREPARATION ASSOCIATIONS
-- ============================================================
-- Query ID: Q18_Preparation_Association
WITH cohort_means AS (
    SELECT 
        AVG(CASE WHEN placed IN (TRUE, 1) THEN coding_score ELSE NULL END) AS placed_coding,
        AVG(CASE WHEN placed IN (FALSE, 0) THEN coding_score ELSE NULL END) AS unplaced_coding,
        AVG(CASE WHEN placed IN (TRUE, 1) THEN cgpa ELSE NULL END) AS placed_cgpa,
        AVG(CASE WHEN placed IN (FALSE, 0) THEN cgpa ELSE NULL END) AS unplaced_cgpa,
        AVG(CASE WHEN placed IN (TRUE, 1) THEN aptitude_score ELSE NULL END) AS placed_aptitude,
        AVG(CASE WHEN placed IN (FALSE, 0) THEN aptitude_score ELSE NULL END) AS unplaced_aptitude,
        AVG(CASE WHEN placed IN (TRUE, 1) THEN communication_score ELSE NULL END) AS placed_comm,
        AVG(CASE WHEN placed IN (FALSE, 0) THEN communication_score ELSE NULL END) AS unplaced_comm
    FROM students
)
SELECT 'coding_score' AS metric, ROUND(placed_coding, 2) AS placed_mean, ROUND(unplaced_coding, 2) AS unplaced_mean, ROUND(placed_coding - unplaced_coding, 2) AS mean_spread FROM cohort_means
UNION ALL
SELECT 'cgpa', ROUND(placed_cgpa, 2), ROUND(unplaced_cgpa, 2), ROUND(placed_cgpa - unplaced_cgpa, 2) FROM cohort_means
UNION ALL
SELECT 'aptitude_score', ROUND(placed_aptitude, 2), ROUND(unplaced_aptitude, 2), ROUND(placed_aptitude - unplaced_aptitude, 2) FROM cohort_means
UNION ALL
SELECT 'communication_score', ROUND(placed_comm, 2), ROUND(unplaced_comm, 2), ROUND(placed_comm - unplaced_comm, 2) FROM cohort_means
ORDER BY mean_spread DESC;


-- ============================================================
-- BQ19: BRANCH PREPARATION & SUPPORT PROFILE
-- ============================================================
-- Query ID: Q19_Branch_Support_Profile
SELECT 
    branch,
    COUNT(*) AS total_students,
    ROUND(100.0 * SUM(CASE WHEN placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0), 2) AS placement_rate_pct,
    ROUND(AVG(cgpa), 2) AS avg_cgpa,
    ROUND(AVG(coding_score), 2) AS avg_coding_score,
    ROUND(AVG(aptitude_score), 2) AS avg_aptitude_score,
    ROUND(AVG(communication_score), 2) AS avg_communication_score,
    ROUND(AVG(python_skill + sql_skill + excel_skill + power_bi_skill + dsa_skill + cloud_skill + cybersecurity_skill), 2) AS avg_skill_count
FROM students
GROUP BY branch
ORDER BY placement_rate_pct ASC;


-- ============================================================
-- BQ20: SKILL IMPROVEMENT OPPORTUNITY GAP MATRIX
-- ============================================================
-- Query ID: Q20_Skill_Opportunity_Gap
WITH skill_unions AS (
    SELECT 'python_skill' AS skill_name, python_skill AS has_skill, placed FROM students
    UNION ALL
    SELECT 'sql_skill', sql_skill, placed FROM students
    UNION ALL
    SELECT 'excel_skill', excel_skill, placed FROM students
    UNION ALL
    SELECT 'power_bi_skill', power_bi_skill, placed FROM students
    UNION ALL
    SELECT 'dsa_skill', dsa_skill, placed FROM students
    UNION ALL
    SELECT 'cloud_skill', cloud_skill, placed FROM students
    UNION ALL
    SELECT 'cybersecurity_skill', cybersecurity_skill, placed FROM students
),
gap_metrics AS (
    SELECT 
        skill_name,
        ROUND(100.0 * SUM(CASE WHEN has_skill = 1 THEN 1 ELSE 0 END) / (SELECT COUNT(*) FROM students), 2) AS prevalence_pct,
        ROUND(100.0 * SUM(CASE WHEN has_skill = 1 AND placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN has_skill = 1 THEN 1 ELSE 0 END), 0), 2) AS holder_placement_rate_pct,
        ROUND(100.0 * SUM(CASE WHEN has_skill = 0 AND placed IN (TRUE, 1) THEN 1 ELSE 0 END) / NULLIF(SUM(CASE WHEN has_skill = 0 THEN 1 ELSE 0 END), 0), 2) AS non_holder_placement_rate_pct
    FROM skill_unions
    GROUP BY skill_name
)
SELECT 
    skill_name,
    prevalence_pct,
    holder_placement_rate_pct,
    non_holder_placement_rate_pct,
    ROUND(holder_placement_rate_pct - non_holder_placement_rate_pct, 2) AS spread_pp,
    CASE 
        WHEN prevalence_pct < 50.0 AND (holder_placement_rate_pct - non_holder_placement_rate_pct) > 5.0 THEN 'High Opportunity Gap (Low Prevalence, High Impact)'
        WHEN prevalence_pct >= 50.0 AND (holder_placement_rate_pct - non_holder_placement_rate_pct) > 5.0 THEN 'Core Foundation Skill (High Prevalence, High Impact)'
        ELSE 'Secondary Skill Domain'
    END AS strategic_category
FROM gap_metrics
ORDER BY spread_pp DESC;


-- ============================================================
-- BQ21: HIGH-PACKAGE PREPARATION PATTERNS (PLACED ONLY)
-- ============================================================
-- Query ID: Q21_High_Package_Patterns
SELECT 
    CASE WHEN package_lpa >= 10.00 THEN 'High Package (10.0+ LPA)' ELSE 'Standard Package (< 10.0 LPA)' END AS package_tier,
    COUNT(*) AS placed_students,
    ROUND(AVG(cgpa), 2) AS avg_cgpa,
    ROUND(AVG(coding_score), 2) AS avg_coding_score,
    ROUND(AVG(aptitude_score), 2) AS avg_aptitude_score,
    ROUND(AVG(communication_score), 2) AS avg_communication_score,
    ROUND(AVG(projects), 2) AS avg_projects,
    ROUND(AVG(internships), 2) AS avg_internships,
    ROUND(AVG(python_skill + sql_skill + excel_skill + power_bi_skill + dsa_skill + cloud_skill + cybersecurity_skill), 2) AS avg_skill_count
FROM students
WHERE placed IN (TRUE, 1) AND package_lpa IS NOT NULL
GROUP BY CASE WHEN package_lpa >= 10.00 THEN 'High Package (10.0+ LPA)' ELSE 'Standard Package (< 10.0 LPA)' END
ORDER BY package_tier ASC;
