-- PlacementLens — PostgreSQL Performance Indexes
-- Table: public.students

-- 1. Index on branch for branch-level analytical aggregations
CREATE INDEX IF NOT EXISTS idx_students_branch 
ON public.students (branch);

-- 2. Index on placed status for cohort filtering (placed vs unplaced)
CREATE INDEX IF NOT EXISTS idx_students_placed 
ON public.students (placed);

-- 3. Composite index on placed and company_type for compensation breakdowns
CREATE INDEX IF NOT EXISTS idx_students_placed_company 
ON public.students (placed, company_type);

-- 4. Composite index on branch and placed for branch placement rate CTE queries
CREATE INDEX IF NOT EXISTS idx_students_branch_placed 
ON public.students (branch, placed);
