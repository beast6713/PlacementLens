#!/usr/bin/env python3
"""
PlacementLens — Synthetic Dataset Generator (Phase 1 Part 3)
============================================================
Author: PlacementLens Data Engineering Team
Seed: 42
Version: v1.0
Target Intended Students: 1,500
Physical Raw Rows (with 5 controlled duplicates): 1,505

This script reproducibly generates the canonical raw dataset for PlacementLens.
It follows all specifications locked in Phase 0, Phase 1 Part 1, and Phase 1 Part 2.

Workflow:
1. Initialize deterministic random seeds (Python random & NumPy).
2. Generate clean synthetic dataset of 1,500 student records according to schema v1.0.
3. Validate clean dataset against dictionary bounds, placement linkage rules, and null semantics.
4. Inject controlled, documented raw data defects (case inconsistency, whitespace, string binary flags, missing non-critical values, duplicate rows).
5. Export raw dataset CSVs (data/raw/placementlens_students_raw.csv and data/raw/placement_raw.csv).
6. Export raw defect manifest (data/raw/raw_defect_manifest.csv).
7. Execute self-reproducibility check.
"""

import os
import sys
import math
import random
import hashlib
import pandas as pd
import numpy as np

# Set standard output encoding to utf-8 if possible
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# -----------------------------------------------------------------------------
# CONFIGURATION & SEED
# -----------------------------------------------------------------------------
SEED = 42
TOTAL_STUDENTS = 1500

BRANCH_ALLOCATIONS = {
    'CSE': 450,  # 30.0%
    'IT':  375,  # 25.0%
    'ECE': 300,  # 20.0%
    'EEE': 150,  # 10.0%
    'ME':  120,  #  8.0%
    'CE':  105   #  7.0%
}

GENDER_PROBS = {
    'Female': 0.40,
    'Male': 0.55,
    'Non-binary': 0.03,
    'Prefer not to say': 0.02
}

def set_seeds(seed=SEED):
    random.seed(seed)
    np.random.seed(seed)

# -----------------------------------------------------------------------------
# 1. CLEAN SYNTHETIC DATA GENERATION
# -----------------------------------------------------------------------------
def generate_clean_dataset(seed=SEED, count=TOTAL_STUDENTS):
    set_seeds(seed)
    
    records = []
    
    # Generate branch array according to exact allocation
    branches = []
    for branch_code, b_count in BRANCH_ALLOCATIONS.items():
        branches.extend([branch_code] * b_count)
    random.shuffle(branches)
    
    gender_choices = list(GENDER_PROBS.keys())
    gender_weights = list(GENDER_PROBS.values())
    
    for i in range(count):
        student_id = f"S{i+1:04d}"
        branch = branches[i]
        
        # Demographic attributes
        age = int(np.clip(np.random.normal(21.5, 1.1), 18, 25))
        gender = np.random.choice(gender_choices, p=gender_weights)
        
        # Academic attributes (CGPA)
        cgpa_raw = np.random.normal(7.3, 1.1)
        cgpa = float(np.round(np.clip(cgpa_raw, 4.00, 9.85), 2))
        
        # Experience attributes
        internships_probs = [0.45, 0.35, 0.14, 0.04, 0.015, 0.005]
        internships = int(np.random.choice(range(6), p=internships_probs))
        
        projects_probs = [0.10, 0.25, 0.35, 0.18, 0.08, 0.02, 0.01, 0.005, 0.002, 0.002, 0.001]
        projects = int(np.random.choice(range(11), p=projects_probs))
        
        # Assessment scores (0 to 100)
        coding_base = 30.0 + (cgpa / 10.0) * 45.0 + (projects * 3.5) + np.random.normal(0, 10.0)
        if branch in ['CSE', 'IT']:
            coding_base += 6.0
        coding_score = float(np.round(np.clip(coding_base, 25.0, 98.5), 2))
        
        aptitude_base = 35.0 + (cgpa / 10.0) * 50.0 + np.random.normal(0, 11.0)
        aptitude_score = float(np.round(np.clip(aptitude_base, 30.0, 97.0), 2))
        
        comm_base = 40.0 + np.random.normal(30.0, 14.0) + (cgpa * 1.5)
        communication_score = float(np.round(np.clip(comm_base, 35.0, 96.0), 2))
        
        # Technical Skill Flags (0 or 1)
        p_python = 0.35 + (coding_score / 200.0) + (0.10 if branch in ['CSE', 'IT'] else 0.0)
        python_skill = 1 if np.random.rand() < np.clip(p_python, 0.15, 0.90) else 0
        
        p_sql = 0.40 + (coding_score / 250.0) + (0.10 if python_skill == 1 else 0.0)
        sql_skill = 1 if np.random.rand() < np.clip(p_sql, 0.20, 0.88) else 0
        
        p_excel = 0.65 + (aptitude_score / 400.0)
        excel_skill = 1 if np.random.rand() < np.clip(p_excel, 0.40, 0.92) else 0
        
        p_pbi = 0.20 + (0.25 if sql_skill == 1 else 0.0) + (0.15 if excel_skill == 1 else 0.0)
        power_bi_skill = 1 if np.random.rand() < np.clip(p_pbi, 0.10, 0.80) else 0
        
        p_dsa = 0.25 + (coding_score / 180.0) + (0.15 if branch in ['CSE', 'IT'] else -0.10)
        dsa_skill = 1 if np.random.rand() < np.clip(p_dsa, 0.08, 0.85) else 0
        
        p_cloud = 0.15 + (0.15 if python_skill == 1 else 0.0) + (0.10 if branch in ['CSE', 'IT'] else 0.0)
        cloud_skill = 1 if np.random.rand() < np.clip(p_cloud, 0.05, 0.65) else 0
        
        p_sec = 0.10 + (0.10 if dsa_skill == 1 else 0.0) + (0.05 if branch in ['CSE', 'IT'] else 0.0)
        cybersecurity_skill = 1 if np.random.rand() < np.clip(p_sec, 0.05, 0.50) else 0
        
        skill_sum = python_skill + sql_skill + excel_skill + power_bi_skill + dsa_skill + cloud_skill + cybersecurity_skill
        
        # Latent Preparation Index & Probabilistic Placement Outcome
        prep_index = (
            0.22 * (cgpa / 10.0) +
            0.22 * (coding_score / 100.0) +
            0.18 * (aptitude_score / 100.0) +
            0.15 * (communication_score / 100.0) +
            0.10 * min(internships / 3.0, 1.0) +
            0.08 * min(projects / 4.0, 1.0) +
            0.05 * (skill_sum / 7.0)
        )
        
        z = 7.5 * (prep_index - 0.575) + np.random.normal(0, 0.75)
        prob_placed = 1.0 / (1.0 + math.exp(-z))
        
        placed = 1 if np.random.rand() < prob_placed else 0
        
        # Placement Compensation & Recruiter Tier
        if placed == 1:
            if prep_index > 0.75 and np.random.rand() < 0.55:
                company_type = 'Product'
            elif prep_index > 0.65 and np.random.rand() < 0.35:
                company_type = 'Startup' if np.random.rand() < 0.5 else 'Product'
            else:
                c_choices = ['Service', 'Product', 'Startup', 'Other']
                c_weights = [0.55, 0.20, 0.18, 0.07]
                company_type = np.random.choice(c_choices, p=c_weights)
            
            if company_type == 'Product':
                base_pkg = np.random.lognormal(mean=2.45, sigma=0.35)
                pkg_val = max(6.5, min(base_pkg + (coding_score / 20.0), 48.0))
            elif company_type == 'Startup':
                base_pkg = np.random.lognormal(mean=2.15, sigma=0.30)
                pkg_val = max(5.0, min(base_pkg + (coding_score / 25.0), 30.0))
            elif company_type == 'Service':
                base_pkg = np.random.normal(4.5, 0.9)
                pkg_val = max(3.2, min(base_pkg + (cgpa / 5.0), 12.0))
            else:  # Other
                base_pkg = np.random.normal(5.2, 1.2)
                pkg_val = max(3.5, min(base_pkg, 15.0))
            
            package_lpa = float(np.round(pkg_val, 2))
        else:
            company_type = None
            package_lpa = None
            
        records.append({
            'student_id': student_id,
            'age': age,
            'gender': gender,
            'branch': branch,
            'cgpa': cgpa,
            'internships': internships,
            'projects': projects,
            'coding_score': coding_score,
            'aptitude_score': aptitude_score,
            'communication_score': communication_score,
            'python_skill': python_skill,
            'sql_skill': sql_skill,
            'excel_skill': excel_skill,
            'power_bi_skill': power_bi_skill,
            'dsa_skill': dsa_skill,
            'cloud_skill': cloud_skill,
            'cybersecurity_skill': cybersecurity_skill,
            'placed': placed,
            'company_type': company_type,
            'package_lpa': package_lpa
        })
        
    df = pd.DataFrame(records)
    return df

# -----------------------------------------------------------------------------
# 2. CLEAN DATASET VALIDATION
# -----------------------------------------------------------------------------
def validate_clean_dataset(df):
    assert len(df) == TOTAL_STUDENTS, f"Expected {TOTAL_STUDENTS} rows, got {len(df)}"
    assert df['student_id'].nunique() == TOTAL_STUDENTS, "Student IDs not unique in clean dataset"
    
    unplaced_df = df[df['placed'] == 0]
    assert unplaced_df['company_type'].isnull().all(), "Unplaced student has non-null company_type"
    assert unplaced_df['package_lpa'].isnull().all(), "Unplaced student has non-null package_lpa"
    
    placed_df = df[df['placed'] == 1]
    assert placed_df['company_type'].notnull().all(), "Placed student has null company_type"
    assert placed_df['package_lpa'].notnull().all(), "Placed student has null package_lpa"
    assert (placed_df['package_lpa'] > 0).all(), "Placed student package_lpa <= 0"
    
    assert df['cgpa'].between(0.0, 10.0).all(), "CGPA out of bounds"
    assert df['coding_score'].between(0.0, 100.0).all(), "coding_score out of bounds"
    assert df['aptitude_score'].between(0.0, 100.0).all(), "aptitude_score out of bounds"
    assert df['communication_score'].between(0.0, 100.0).all(), "communication_score out of bounds"
    assert df['internships'].between(0, 5).all(), "internships out of bounds"
    assert df['projects'].between(0, 10).all(), "projects out of bounds"
    
    skill_cols = ['python_skill', 'sql_skill', 'excel_skill', 'power_bi_skill', 'dsa_skill', 'cloud_skill', 'cybersecurity_skill', 'placed']
    for c in skill_cols:
        assert df[c].isin([0, 1]).all(), f"Field {c} has non-binary values in clean dataset"
        
    print("[OK] Clean dataset validation passed perfectly!")

# -----------------------------------------------------------------------------
# 3. CONTROLLED RAW DEFECT INJECTION
# -----------------------------------------------------------------------------
def inject_controlled_defects(clean_df, seed=SEED):
    set_seeds(seed)
    raw_df = clean_df.copy()
    raw_df = raw_df.astype(object)
    
    manifest = []
    
    # Defect 1: Branch Case Inconsistency (~25 rows)
    case_indices = [15, 42, 88, 124, 167, 210, 255, 301, 345, 412, 480, 525, 590, 640, 710, 780, 835, 910, 960, 1020, 1115, 1205, 1280, 1340, 1420]
    for idx in case_indices:
        orig_val = raw_df.loc[idx, 'branch']
        injected_val = str(orig_val).lower()
        raw_df.loc[idx, 'branch'] = injected_val
        manifest.append({
            'defect_id': f"DEF-{len(manifest)+1:03d}",
            'defect_type': 'Case Inconsistency',
            'target_field': 'branch',
            'row_index': idx,
            'student_id': clean_df.loc[idx, 'student_id'],
            'original_value': orig_val,
            'injected_value': injected_val,
            'reason': 'Demonstrate case standardization (str.upper) in Phase 2 ETL',
            'expected_cleaning_action': 'Convert to uppercase'
        })
        
    # Defect 2: Recruiter Case & Space Inconsistency (~15 placed rows)
    placed_indices = raw_df[raw_df['placed'] == 1].index.tolist()
    recruiter_case_indices = placed_indices[5:20]
    for idx in recruiter_case_indices:
        orig_val = raw_df.loc[idx, 'company_type']
        if orig_val == 'Product':
            injected_val = 'product'
        elif orig_val == 'Service':
            injected_val = 'Service '
        else:
            injected_val = str(orig_val).lower()
        raw_df.loc[idx, 'company_type'] = injected_val
        manifest.append({
            'defect_id': f"DEF-{len(manifest)+1:03d}",
            'defect_type': 'Case & Space Inconsistency',
            'target_field': 'company_type',
            'row_index': idx,
            'student_id': clean_df.loc[idx, 'student_id'],
            'original_value': orig_val,
            'injected_value': injected_val,
            'reason': 'Demonstrate string stripping and capitalization normalization',
            'expected_cleaning_action': 'Strip whitespace and titlecase'
        })

    # Defect 3: Whitespace Padding (~20 rows)
    padding_indices = [30, 75, 140, 195, 260, 315, 380, 445, 510, 575, 630, 705, 770, 840, 915, 980, 1050, 1130, 1220, 1310]
    for idx in padding_indices:
        orig_val = raw_df.loc[idx, 'gender']
        injected_val = f" {orig_val} "
        raw_df.loc[idx, 'gender'] = injected_val
        manifest.append({
            'defect_id': f"DEF-{len(manifest)+1:03d}",
            'defect_type': 'Whitespace Padding',
            'target_field': 'gender',
            'row_index': idx,
            'student_id': clean_df.loc[idx, 'student_id'],
            'original_value': orig_val,
            'injected_value': injected_val,
            'reason': 'Demonstrate whitespace stripping in Phase 2 cleaning',
            'expected_cleaning_action': 'Apply str.strip()'
        })

    # Defect 4: String Binary Variant (~15 rows)
    binary_indices = [50, 110, 175, 230, 290, 350, 410, 470, 530, 610, 690, 760, 850, 940, 1030]
    for idx in binary_indices:
        orig_val = raw_df.loc[idx, 'python_skill']
        injected_val = "Yes" if orig_val == 1 else "No"
        raw_df.loc[idx, 'python_skill'] = injected_val
        manifest.append({
            'defect_id': f"DEF-{len(manifest)+1:03d}",
            'defect_type': 'String Binary Variant',
            'target_field': 'python_skill',
            'row_index': idx,
            'student_id': clean_df.loc[idx, 'student_id'],
            'original_value': orig_val,
            'injected_value': injected_val,
            'reason': 'Demonstrate boolean parsing / binary flag mapping in ETL',
            'expected_cleaning_action': 'Map "Yes"/"True"->1 and "No"/"False"->0'
        })

    # Defect 5: Missing Non-Critical Value (~15 rows)
    missing_indices = [60, 130, 215, 285, 360, 435, 520, 605, 680, 755, 845, 930, 1015, 1125, 1240]
    for idx in missing_indices:
        orig_val = raw_df.loc[idx, 'communication_score']
        injected_val = np.nan
        raw_df.loc[idx, 'communication_score'] = injected_val
        manifest.append({
            'defect_id': f"DEF-{len(manifest)+1:03d}",
            'defect_type': 'Missing Non-Critical Value',
            'target_field': 'communication_score',
            'row_index': idx,
            'student_id': clean_df.loc[idx, 'student_id'],
            'original_value': orig_val,
            'injected_value': 'NULL/Empty',
            'reason': 'Demonstrate documented missing-data imputation testing in Phase 2',
            'expected_cleaning_action': 'Impute with median communication score'
        })

    # Defect 6: Duplicate Raw Rows (5 rows)
    dup_indices = [119, 449, 779, 1099, 1349]
    dup_rows = raw_df.iloc[dup_indices].copy()
    
    for d_idx in dup_indices:
        manifest.append({
            'defect_id': f"DEF-{len(manifest)+1:03d}",
            'defect_type': 'Duplicate Raw Row',
            'target_field': 'student_id',
            'row_index': 'Appended at tail',
            'student_id': clean_df.loc[d_idx, 'student_id'],
            'original_value': 'Single row',
            'injected_value': f"Duplicate row for {clean_df.loc[d_idx, 'student_id']}",
            'reason': 'Demonstrate deduplication pipeline in Phase 2',
            'expected_cleaning_action': 'Deduplicate keeping first occurrence'
        })

    raw_df = pd.concat([raw_df, dup_rows], ignore_index=True)
    manifest_df = pd.DataFrame(manifest)
    
    return raw_df, manifest_df

# -----------------------------------------------------------------------------
# 4. EXPORT & REPRODUCIBILITY VERIFICATION
# -----------------------------------------------------------------------------
def run_pipeline():
    print("=" * 60)
    print("PlacementLens -- Dataset Generation Pipeline (Phase 1 Part 3)")
    print("=" * 60)
    
    print("1. Generating 1,500 clean synthetic student records (Seed = 42)...")
    clean_df = generate_clean_dataset(seed=SEED, count=TOTAL_STUDENTS)
    validate_clean_dataset(clean_df)
    
    print("2. Injecting controlled raw defects according to DQ rules...")
    raw_df, manifest_df = inject_controlled_defects(clean_df, seed=SEED)
    
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    raw_dir = os.path.join(base_dir, "data", "raw")
    os.makedirs(raw_dir, exist_ok=True)
    
    path_primary_raw = os.path.join(raw_dir, "placementlens_students_raw.csv")
    path_alias_raw = os.path.join(raw_dir, "placement_raw.csv")
    path_manifest = os.path.join(raw_dir, "raw_defect_manifest.csv")
    
    raw_df.to_csv(path_primary_raw, index=False)
    raw_df.to_csv(path_alias_raw, index=False)
    manifest_df.to_csv(path_manifest, index=False)
    
    print(f"[OK] Exported raw dataset to: {path_primary_raw} ({len(raw_df)} physical rows)")
    print(f"[OK] Exported raw dataset alias: {path_alias_raw}")
    print(f"[OK] Exported defect manifest: {path_manifest} ({len(manifest_df)} defects logged)")
    
    with open(path_primary_raw, 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    print(f"[OK] Primary Raw CSV MD5 Hash: {file_hash}")
    
    print("\n3. Testing 100% Reproducibility (Executing second run)...")
    clean_df2 = generate_clean_dataset(seed=SEED, count=TOTAL_STUDENTS)
    raw_df2, _ = inject_controlled_defects(clean_df2, seed=SEED)
    
    path_temp = os.path.join(raw_dir, "temp_test_repro.csv")
    raw_df2.to_csv(path_temp, index=False)
    with open(path_temp, 'rb') as f:
        file_hash2 = hashlib.md5(f.read()).hexdigest()
    os.remove(path_temp)
    
    assert file_hash == file_hash2, f"Reproducibility failure! Hash mismatch: {file_hash} vs {file_hash2}"
    print("[OK] REPRODUCIBILITY TEST PASSED! Hash matches 100% deterministically.")
    
    placed_count = (clean_df['placed'] == 1).sum()
    unplaced_count = (clean_df['placed'] == 0).sum()
    placement_rate = (placed_count / TOTAL_STUDENTS) * 100.0
    
    print("\n" + "=" * 60)
    print("GENERATION SUMMARY PROFILE")
    print("=" * 60)
    print(f"Intended Unique Students : {TOTAL_STUDENTS}")
    print(f"Physical Raw CSV Rows    : {len(raw_df)} (Includes 5 duplicate rows)")
    print(f"Placement Rate           : {placement_rate:.2f}% ({placed_count} placed, {unplaced_count} unplaced)")
    print(f"Branch Counts            : {clean_df['branch'].value_counts().to_dict()}")
    print(f"Company Type Breakdown   : {clean_df['company_type'].value_counts(dropna=False).to_dict()}")
    print(f"Package LPA Range        : Min={clean_df['package_lpa'].min():.2f}, Median={clean_df['package_lpa'].median():.2f}, Max={clean_df['package_lpa'].max():.2f}")
    print(f"Total Defects Injected   : {len(manifest_df)}")
    print("=" * 60)

if __name__ == "__main__":
    run_pipeline()
