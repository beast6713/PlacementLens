# SQL Requirements

## Platform and design

SQLite is the approved initial database because it is portable and adequate for 1,500 records. Use a normalized analytical design: `students`, `student_skills`, and `student_experience`, joined by `student_id`. The clean CSV is the sole data source. PostgreSQL migration is deferred.

## Required query coverage

Create 15–20 meaningful queries, each with question, source tables, expected grain, and validation note. Across the set include `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `CASE`, aggregates, `JOIN`, subquery, CTE, and window functions.

## Minimum query topics

1. total students, placed count, and placement rate; 2. placement by branch; 3. package by branch; 4. placement by CGPA band; 5. placed/unplaced CGPA; 6. internship comparison; 7. project comparison; 8. skill adoption; 9. skill-wise placement; 10–12. coding, aptitude, communication comparisons; 13. package distribution; 14. company-type split; 15. top packages; 16. rank placed students within branch; 17. branch threshold via HAVING; 18. CTE readiness summary; 19. subquery high-readiness candidates; 20. cross-check key overview metrics.

Query results must be reconciled to Python for AQ-001–AQ-013 before CHECKPOINT-03.

