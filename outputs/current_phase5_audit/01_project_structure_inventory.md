# PlacementLens — Current Project Structure Inventory

## 1. Directory Overview
- `00_project_blueprint/`: Contains project blueprints, change logs, and completion reports (00 through 64).
- `data/`: Contains raw dataset (`data/raw/placementlens_students_raw.csv`) and processed dataset (`data/processed/placementlens_students_clean.csv`).
- `docs/`: Contains specification documents for Phase 1 to Phase 5 (Data architecture, DAX guidelines, UI design system, page specifications, final QA handoff).
- `scripts/`: Contains Python data pipelines, EDA analysis, PRI calculation, student segmentation, dashboard build scripts, and validation suite (`validate_phase5_dashboard.py`).
- `sql/`: Contains PostgreSQL schema setup (`01_schema.sql`) and business analytical queries (`02_analytics.sql`).
- `dashboard/`: Contains the React + Vite + Tailwind CSS + Framer Motion + Magic UI interactive web dashboard application.
- `outputs/`: Contains analytical outputs, EDA figures, strategy files, Power BI QA matrices (46_ through 59_), and audit reports.

## 2. Source Data Inventory
- `data/raw/placementlens_students_raw.csv`: MD5 `59c04ee15a0112806c510225d8e75779` (1,500 rows, 20 columns)
- `data/processed/placementlens_students_clean.csv`: MD5 `96023d297eec5a9a47563eaddc157d0d` (1,500 rows, 20 columns)

## 3. Web Dashboard Inventory (`dashboard/`)
- `dashboard/src/App.jsx`: Main shell with sidebar navigation and global filter state.
- `dashboard/src/components/magicui/`: Magic UI components (`BorderBeam.jsx`, `NumberTicker.jsx`, `BentoGrid.jsx`, `ParticlesBackground.jsx`, `MagicMarquee.jsx`, `ShimmerButton.jsx`).
- `dashboard/src/components/pages/`: 4 dashboard page views (`CommandCenter.jsx`, `StudentAnalytics.jsx`, `CompanyIntelligence.jsx`, `ReportsIntelligence.jsx`).
- `dashboard/src/data/placementData.json`: Exported analytical dataset for frontend consumption.
