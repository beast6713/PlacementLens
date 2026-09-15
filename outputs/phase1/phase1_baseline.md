# PlacementLens — Phase 1 Frozen Baseline Record

**Phase Status:** **PHASE 1 COMPLETE — READY FOR PHASE 2**  
**Baseline Lock Date:** `2026-09-16`  
**Checkpoint Signature:** `CHECKPOINT-01-PHASE-1-COMPLETE`

---

## 1. Locked Raw Dataset & Environment Parameters

| Parameter | Frozen Baseline Value | Technical & Integrity Notes |
|---|---|---|
| **Dataset Title** | PlacementLens Synthetic Student Placement Dataset | Privacy-first synthetic portfolio analytics dataset |
| **Dataset Version** | `v1.0 Baseline` | Frozen canonical baseline |
| **Schema Version** | `v1.0 PostgreSQL DDL` | Option A single canonical `public.students` table |
| **Intended Unique Population** | **1,500 students** | Canonical student keys `S0001` to `S1500` |
| **Physical Raw CSV Rows** | **1,505 rows** | Includes 5 controlled duplicate physical rows at tail |
| **Student ID Key Range** | `S0001` – `S1500` | Format regex `^S[0-9]{4}$` 100% compliant |
| **Primary Raw CSV Path** | `data/raw/placementlens_students_raw.csv` | Immutable unconstrained raw source CSV |
| **Raw Alias CSV Path** | `data/raw/placement_raw.csv` | Immutable unconstrained raw alias CSV |
| **Defect Manifest Path** | `data/raw/raw_defect_manifest.csv` | Audit manifest of 95 injected raw defects |
| **Primary Raw CSV MD5 Hash** | `59c04ee15a0112806c510225d8e75779` | Verified 100% immutable across Part 3, 4, 5, and 6 |
| **Random Generator Seed** | `SEED = 42` | Python `numpy` & `random` deterministic seed |
| **Generator Script Path** | `scripts/generate_dataset.py` | 100% byte-for-byte reproducible |
| **Total Controlled Defects** | **95 defects** | Reconciled against manifest (0 unexpected defects) |
| **Overall Placement Rate** | **63.33%** | 950 Placed students, 550 Unplaced students |
| **Package LPA Summary** | Median: **9.70 LPA** | Min: 3.29 LPA, Max: 48.00 LPA (Unplaced = 100% `NULL`) |
| **Phase 2 Handoff Status** | **READY FOR PHASE 2** | Authorized to begin Phase 2 Data Cleaning & Validation |

---

## 2. Immutability Declaration

The raw dataset files listed above are officially **FROZEN AND IMMUTABLE**. 

- No cleaning, deduplication, imputation, case conversion, or manual editing has been performed on the raw files.
- The 95 controlled defects and 5 duplicate rows remain in `data/raw/placementlens_students_raw.csv` as mandatory test cases for the Phase 2 ETL pipeline.
- Future phases MUST treat `data/raw/placementlens_students_raw.csv` as read-only.
