-- PlacementLens — PostgreSQL Schema DDL
-- Table: public.students
-- Canonical Fact Entity Table for Student Placement Analytics

CREATE TABLE IF NOT EXISTS public.students (
    student_id          VARCHAR(5)   NOT NULL PRIMARY KEY,
    age                 INTEGER      NOT NULL CHECK (age >= 18 AND age <= 30),
    gender              VARCHAR(20)  NOT NULL CHECK (gender IN ('Female', 'Male', 'Non-binary', 'Prefer not to say')),
    branch              VARCHAR(10)  NOT NULL CHECK (branch IN ('CSE', 'IT', 'ECE', 'EEE', 'ME', 'CE')),
    cgpa                NUMERIC(4,2) NOT NULL CHECK (cgpa >= 0.00 AND cgpa <= 10.00),
    internships         INTEGER      NOT NULL CHECK (internships >= 0),
    projects            INTEGER      NOT NULL CHECK (projects >= 0),
    coding_score        NUMERIC(5,2) NOT NULL CHECK (coding_score >= 0.00 AND coding_score <= 100.00),
    aptitude_score      NUMERIC(5,2) NOT NULL CHECK (aptitude_score >= 0.00 AND aptitude_score <= 100.00),
    communication_score NUMERIC(5,2) NOT NULL CHECK (communication_score >= 0.00 AND communication_score <= 100.00),
    python_skill        INTEGER      NOT NULL CHECK (python_skill IN (0, 1)),
    sql_skill           INTEGER      NOT NULL CHECK (sql_skill IN (0, 1)),
    excel_skill         INTEGER      NOT NULL CHECK (excel_skill IN (0, 1)),
    power_bi_skill      INTEGER      NOT NULL CHECK (power_bi_skill IN (0, 1)),
    dsa_skill           INTEGER      NOT NULL CHECK (dsa_skill IN (0, 1)),
    cloud_skill         INTEGER      NOT NULL CHECK (cloud_skill IN (0, 1)),
    cybersecurity_skill INTEGER      NOT NULL CHECK (cybersecurity_skill IN (0, 1)),
    placed              BOOLEAN      NOT NULL,
    company_type        VARCHAR(20)  NULL CHECK (company_type IN ('Product', 'Service', 'Startup', 'Other') OR company_type IS NULL),
    package_lpa         NUMERIC(6,2) NULL CHECK (package_lpa >= 0.00 OR package_lpa IS NULL),

    -- Domain Linkage Check Constraint: Unplaced students MUST have NULL company_type & package_lpa
    CONSTRAINT chk_placed_null_semantics CHECK (
        (placed = TRUE  AND company_type IS NOT NULL AND package_lpa IS NOT NULL) OR
        (placed = FALSE AND company_type IS NULL     AND package_lpa IS NULL)
    )
);

COMMENT ON TABLE  public.students IS 'PlacementLens canonical student placement dataset fact table.';
COMMENT ON COLUMN public.students.student_id IS 'Unique student identifier (S0001–S1500).';
COMMENT ON COLUMN public.students.placed IS 'Placement status flag (TRUE = Placed, FALSE = Unplaced).';
COMMENT ON COLUMN public.students.package_lpa IS 'Compensation package in LPA (NULL if unplaced).';
