# Data Integrity Audit

## 1. File Hash Verification
- **Raw Dataset:** `data/raw/placementlens_students_raw.csv`
  - Expected MD5: `59c04ee15a0112806c510225d8e75779`
  - Actual MD5: `59c04ee15a0112806c510225d8e75779`
  - Status: **EXACT MATCH (PASS)**

- **Clean Dataset:** `data/processed/placementlens_students_clean.csv`
  - Expected MD5: `96023d297eec5a9a47563eaddc157d0d`
  - Actual MD5: `96023d297eec5a9a47563eaddc157d0d`
  - Status: **EXACT MATCH (PASS)**

## 2. Record & Schema Audit
- **Rows:** 1,500 unique student records.
- **Columns:** 20 canonical columns.
- **NULL Semantics:** 550 unplaced students maintain NULL `package_lpa` and NULL `company_type`.
- **Status:** **DATA INTACT**
