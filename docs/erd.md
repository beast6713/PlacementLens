# Entity Relationship & Data Flow Specification

## 1. Physical Database Model (PostgreSQL)

The primary database architecture for PlacementLens (`placementlens`) consists of the canonical analytical table `public.students`.

```mermaid
erDiagram
    STUDENTS {
        VARCHAR_10 student_id PK "Unique Student Key (S0001-S1500)"
        SMALLINT age "18-25"
        VARCHAR_20 gender "Demographic Category"
        VARCHAR_10 branch "CSE, IT, ECE, EEE, ME, CE"
        NUMERIC_4_2 cgpa "0.00 - 10.00"
        NUMERIC_5_2 coding_score "0.00 - 100.00"
        NUMERIC_5_2 aptitude_score "0.00 - 100.00"
        NUMERIC_5_2 communication_score "0.00 - 100.00"
        SMALLINT internships "0 - 5"
        SMALLINT projects "0 - 10"
        SMALLINT python_skill "0 or 1"
        SMALLINT sql_skill "0 or 1"
        SMALLINT excel_skill "0 or 1"
        SMALLINT power_bi_skill "0 or 1"
        SMALLINT dsa_skill "0 or 1"
        SMALLINT cloud_skill "0 or 1"
        SMALLINT cybersecurity_skill "0 or 1"
        SMALLINT placed "Target Variable: 0 or 1"
        VARCHAR_20 company_type "Product, Service, Startup, Other, NULL"
        NUMERIC_4_2 package_lpa "0.00 - 50.00 LPA, NULL"
    }
```

---

## 2. Power BI Tabular & Logical Dimension Architecture

For visualization and interactive reporting in Power BI Desktop, `public.students` serves as the primary Fact / Analytical table. Logical dimension groupings are mapped cleanly without requiring physical table splitting:

```mermaid
classDiagram
    class StudentsFactTable {
        +VARCHAR student_id PK
        +NUMERIC cgpa
        +NUMERIC coding_score
        +NUMERIC aptitude_score
        +NUMERIC communication_score
        +SMALLINT placed
        +NUMERIC package_lpa
    }

    class AcademicDemographics {
        +VARCHAR branch
        +SMALLINT age
        +VARCHAR gender
    }

    class TechnicalSkills {
        +SMALLINT python_skill
        +SMALLINT sql_skill
        +SMALLINT excel_skill
        +SMALLINT power_bi_skill
        +SMALLINT dsa_skill
        +SMALLINT cloud_skill
        +SMALLINT cybersecurity_skill
    }

    class ExperienceMetrics {
        +SMALLINT internships
        +SMALLINT projects
    }

    class RecruiterTier {
        +VARCHAR company_type
    }

    StudentsFactTable *-- AcademicDemographics
    StudentsFactTable *-- TechnicalSkills
    StudentsFactTable *-- ExperienceMetrics
    StudentsFactTable *-- RecruiterTier
```

---

## 3. End-to-End Data Lineage Architecture

```mermaid
flowchart TD
    A["Python Generator Script<br>(SEED = 42)"] -->|"Inject Controlled Defects"| B["data/raw/placementlens_students_raw.csv<br>(Raw Unconstrained Source)"]
    B -->|"Phase 2 Ingestion & ETL Cleaning"| C["Pandas Validation & Profiling Engine"]
    C -->|"Export Validated Dataset"| D["data/processed/placementlens_students_clean.csv<br>(Canonical Clean CSV)"]
    D -->|"Bulk Load COPY / DDL"| E["PostgreSQL Database<br>(placementlens.students)"]
    D -->|"Optional SQLite Sync"| F["SQLite Database<br>(placementlens.db)"]
    E -->|"SQL Catalog Queries (AQ-001 to AQ-017)"| G["Jupyter Notebooks & SQL Findings"]
    E -->|"PostgreSQL Direct Import"| H["Power BI Desktop Dashboard"]
    D -->|"Readiness Index Calculation"| I["Placement Readiness Index Export"]
```

---

## 4. Key Relationships & Integrity Rules

- **Primary Key:** `students.student_id` is unique, non-null, and immutable across the data pipeline.
- **Cardinally:** 1 row = 1 student record (1,500 total rows).
- **Referential Actions:** No child foreign key tables exist in the baseline canonical model, eliminating orphan record risks.
- **Table Constraint:**
  $$\text{placed} = 0 \iff (\text{company\_type IS NULL} \land \text{package\_lpa IS NULL})$$
  $$\text{placed} = 1 \iff (\text{company\_type IS NOT NULL} \land \text{package\_lpa IS NOT NULL})$$
