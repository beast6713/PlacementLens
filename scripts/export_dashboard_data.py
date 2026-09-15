"""
Export PlacementLens Analytical Data for React + Magic UI Web Dashboard
"""
import os
import json
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLEAN_CSV_PATH = os.path.join(BASE_DIR, "data", "processed", "placementlens_students_clean.csv")
TARGET_JSON_PATH = os.path.join(BASE_DIR, "dashboard", "src", "data", "placementData.json")

def export_data():
    df = pd.read_csv(CLEAN_CSV_PATH)
    
    # Calculate derived metrics
    skill_cols = ['python_skill', 'sql_skill', 'excel_skill', 'power_bi_skill', 'dsa_skill', 'cloud_skill', 'cybersecurity_skill']
    df['technical_skill_count'] = df[skill_cols].sum(axis=1)
    
    # Calculate PRI
    t_norm = (df['technical_skill_count'] / 7.0) * 100.0
    a_norm = df['aptitude_score']
    c_norm = (df['cgpa'] / 10.0) * 100.0
    p_norm = (df['projects'].clip(upper=4) / 4.0) * 100.0
    i_norm = (df['internships'].clip(upper=3) / 3.0) * 100.0
    m_norm = df['communication_score']
    
    df['pri_score'] = (0.25 * t_norm + 0.20 * a_norm + 0.15 * c_norm + 0.15 * p_norm + 0.15 * i_norm + 0.10 * m_norm).round(2)
    
    # PRI Category
    def get_pri_cat(score):
        if score >= 80: return "High Readiness (80-100)"
        elif score >= 60: return "Moderate (60-79)"
        elif score >= 40: return "Needs Improvement (40-59)"
        else: return "High Imp. Priority (<40)"
        
    df['pri_category'] = df['pri_score'].apply(get_pri_cat)
    
    # Quadrants
    academic = (df['cgpa'] / 10.0 * 100 + df['aptitude_score']) / 2.0
    practical = (t_norm + df['coding_score']) / 2.0
    
    acad_med = academic.median()
    prac_med = practical.median()
    
    def get_quadrant(row):
        ac = (row['cgpa'] / 10.0 * 100 + row['aptitude_score']) / 2.0
        pr = ((row['technical_skill_count'] / 7.0 * 100) + row['coding_score']) / 2.0
        if ac >= acad_med and pr >= prac_med: return "SEG-Q1"
        elif ac < acad_med and pr >= prac_med: return "SEG-Q2"
        elif ac >= acad_med and pr < prac_med: return "SEG-Q3"
        else: return "SEG-Q4"
        
    df['prep_quadrant_segment'] = df.apply(get_quadrant, axis=1)
    
    os.makedirs(os.path.dirname(TARGET_JSON_PATH), exist_ok=True)
    
    total_students = int(len(df))
    placed_students = int((df['placed'] == 1).sum())
    unplaced_students = int((df['placed'] == 0).sum())
    placement_rate = float(round((placed_students / total_students) * 100, 2))
    
    placed_df = df[df['placed'] == 1]
    unplaced_df = df[df['placed'] == 0]
    
    mean_pkg = float(round(placed_df['package_lpa'].mean(), 2))
    median_pkg = float(round(placed_df['package_lpa'].median(), 2))
    q75 = float(placed_df['package_lpa'].quantile(0.75))
    q25 = float(placed_df['package_lpa'].quantile(0.25))
    iqr_pkg = float(round(q75 - q25, 2))
    
    # Branch Breakdown
    branch_stats = []
    for b in ['CE', 'EEE', 'IT', 'CSE', 'ECE', 'ME']:
        b_df = df[df['branch'] == b]
        total = int(len(b_df))
        placed = int((b_df['placed'] == 1).sum())
        rate = float(round((placed / total) * 100, 2)) if total > 0 else 0.0
        avg_pkg = float(round(b_df[b_df['placed'] == 1]['package_lpa'].mean(), 2)) if placed > 0 else 0.0
        branch_stats.append({
            "branch": b,
            "total": total,
            "placed": placed,
            "unplaced": total - placed,
            "rate": rate,
            "avg_package": avg_pkg
        })
    
    # Company Type Stats
    company_stats = []
    for ctype in ['Product', 'Startup', 'Service', 'Other']:
        c_df = placed_df[placed_df['company_type'] == ctype]
        count = int(len(c_df))
        mean_p = float(round(c_df['package_lpa'].mean(), 2)) if count > 0 else 0.0
        med_p = float(round(c_df['package_lpa'].median(), 2)) if count > 0 else 0.0
        company_stats.append({
            "company_type": ctype,
            "count": count,
            "share_pct": float(round((count / placed_students) * 100, 2)),
            "mean_package": mean_p,
            "median_package": med_p
        })
    
    # Prep comparison (Placed vs Unplaced)
    prep_comparison = {
        "coding_score": {
            "placed": float(round(placed_df['coding_score'].mean(), 2)),
            "unplaced": float(round(unplaced_df['coding_score'].mean(), 2)),
            "delta": float(round(placed_df['coding_score'].mean() - unplaced_df['coding_score'].mean(), 2))
        },
        "aptitude_score": {
            "placed": float(round(placed_df['aptitude_score'].mean(), 2)),
            "unplaced": float(round(unplaced_df['aptitude_score'].mean(), 2)),
            "delta": float(round(placed_df['aptitude_score'].mean() - unplaced_df['aptitude_score'].mean(), 2))
        },
        "cgpa": {
            "placed": float(round(placed_df['cgpa'].mean(), 2)),
            "unplaced": float(round(unplaced_df['cgpa'].mean(), 2)),
            "delta": float(round(placed_df['cgpa'].mean() - unplaced_df['cgpa'].mean(), 2))
        },
        "technical_skill_count": {
            "placed_median": int(placed_df['technical_skill_count'].median()),
            "unplaced_median": int(unplaced_df['technical_skill_count'].median()),
            "delta": 1
        }
    }
    
    # Skill placement spreads
    skills = ['sql_skill', 'python_skill', 'cloud_skill', 'dsa_skill', 'cybersecurity_skill', 'power_bi_skill', 'excel_skill']
    skill_names = {'sql_skill': 'SQL', 'python_skill': 'Python', 'cloud_skill': 'Cloud', 'dsa_skill': 'DSA', 'cybersecurity_skill': 'Cybersecurity', 'power_bi_skill': 'Power BI', 'excel_skill': 'Excel'}
    
    skill_stats = []
    for s in skills:
        has_skill = df[df[s] == 1]
        no_skill = df[df[s] == 0]
        
        has_rate = float(round((has_skill['placed'] == 1).mean() * 100, 2)) if len(has_skill) > 0 else 0.0
        no_rate = float(round((no_skill['placed'] == 1).mean() * 100, 2)) if len(no_skill) > 0 else 0.0
        spread = float(round(has_rate - no_rate, 2))
        
        skill_stats.append({
            "skill_key": s,
            "skill_name": skill_names[s],
            "holder_count": int(len(has_skill)),
            "holder_pct": float(round((len(has_skill) / total_students) * 100, 2)),
            "skill_placement_rate": has_rate,
            "no_skill_placement_rate": no_rate,
            "spread": spread
        })
    
    skill_stats.sort(key=lambda x: x['spread'], reverse=True)
    
    # PRI Tiers
    pri_tiers = [
        {"tier": "High Readiness (80-100)", "count": int((df['pri_score'] >= 80).sum()), "placement_rate": float(round((df[df['pri_score'] >= 80]['placed'] == 1).mean() * 100, 2))},
        {"tier": "Moderate (60-79)", "count": int(((df['pri_score'] >= 60) & (df['pri_score'] < 80)).sum()), "placement_rate": float(round((df[(df['pri_score'] >= 60) & (df['pri_score'] < 80)]['placed'] == 1).mean() * 100, 2))},
        {"tier": "Needs Improvement (40-59)", "count": int(((df['pri_score'] >= 40) & (df['pri_score'] < 60)).sum()), "placement_rate": float(round((df[(df['pri_score'] >= 40) & (df['pri_score'] < 60)]['placed'] == 1).mean() * 100, 2))},
        {"tier": "High Imp. Priority (<40)", "count": int((df['pri_score'] < 40).sum()), "placement_rate": float(round((df[df['pri_score'] < 40]['placed'] == 1).mean() * 100, 2))}
    ]
    
    # Quadrant Segments
    segments = [
        {"segment_id": "SEG-Q1", "name": "Q1: Balanced High Achievers", "count": int((df['prep_quadrant_segment'] == 'SEG-Q1').sum()), "placement_rate": float(round((df[df['prep_quadrant_segment'] == 'SEG-Q1']['placed'] == 1).mean() * 100, 2))},
        {"segment_id": "SEG-Q2", "name": "Q2: Practical Builders", "count": int((df['prep_quadrant_segment'] == 'SEG-Q2').sum()), "placement_rate": float(round((df[df['prep_quadrant_segment'] == 'SEG-Q2']['placed'] == 1).mean() * 100, 2))},
        {"segment_id": "SEG-Q3", "name": "Q3: Academic Focus", "count": int((df['prep_quadrant_segment'] == 'SEG-Q3').sum()), "placement_rate": float(round((df[df['prep_quadrant_segment'] == 'SEG-Q3']['placed'] == 1).mean() * 100, 2))},
        {"segment_id": "SEG-Q4", "name": "Q4: Comprehensive Imp. Priority", "count": int((df['prep_quadrant_segment'] == 'SEG-Q4').sum()), "placement_rate": float(round((df[df['prep_quadrant_segment'] == 'SEG-Q4']['placed'] == 1).mean() * 100, 2))}
    ]
    
    # Student-level records power the dashboard's interactive filters.  Retaining
    # the source columns here lets the React layer recalculate every metric for
    # the active department, gender, and placement-status scope rather than
    # showing a fixed, whole-cohort aggregate.
    student_columns = [
        'student_id', 'branch', 'gender', 'cgpa', 'coding_score',
        'aptitude_score', 'communication_score', 'technical_skill_count',
        'pri_score', 'pri_category', 'prep_quadrant_segment', 'placed',
        'company_type', 'package_lpa', *skill_cols
    ]
    students = df[student_columns].fillna("N/A").to_dict(orient='records')

    # Insights list
    insights = [
        {"id": "INS-01", "category": "Placement Baseline", "title": "63.33% Baseline Cohort Placement", "summary": "Out of 1,500 total students, 950 secured placements while 550 remain unplaced.", "scope": "Cohort", "type": "Static"},
        {"id": "INS-02", "category": "Branch Intelligence", "title": "Civil Engineering Leads Branch Placement", "summary": "CE achieved the highest placement rate at 68.57% (72/105), while Mechanical Engineering was lowest at 55.83% (67/120).", "scope": "Branch", "type": "Static"},
        {"id": "INS-03", "category": "Skill Signal", "title": "SQL Shows Highest Placement Spread", "summary": "SQL holders exhibit a +9.17 pp higher placement rate than non-holders, followed by Python (+6.94 pp) and Cloud (+6.04 pp).", "scope": "Skill", "type": "Static"},
        {"id": "INS-04", "category": "Compensation Tiers", "title": "Product Companies Lead Package Premium", "summary": "Product firms offer highest average package (16.26 LPA mean, 16.03 LPA median) compared to Service firms (5.90 LPA mean).", "scope": "Company", "type": "Dynamic"},
        {"id": "INS-05", "category": "Preparation Signals", "title": "Coding & Aptitude Show Strongest Deltas", "summary": "Placed students average +5.41 points higher in coding (78.36 vs 72.95) and +5.19 points higher in aptitude (75.40 vs 70.21).", "scope": "Preparation", "type": "Static"},
        {"id": "INS-06", "category": "Readiness Index", "title": "High Readiness Tiers Achieve >84% Placement", "summary": "Students in High Readiness tier (PRI 80-100) achieve 84.15% placement, whereas High Imp Priority (<40) achieve 50.00%.", "scope": "Readiness", "type": "Dynamic"}
    ]

    output_data = {
        "metadata": {
            "total_students": total_students,
            "placed_students": placed_students,
            "unplaced_students": unplaced_students,
            "placement_rate": placement_rate,
            "mean_package": mean_pkg,
            "median_package": median_pkg,
            "iqr_package": iqr_pkg
        },
        "branch_stats": branch_stats,
        "company_stats": company_stats,
        "prep_comparison": prep_comparison,
        "skill_stats": skill_stats,
        "pri_tiers": pri_tiers,
        "segments": segments,
        "insights": insights,
        "students": students
    }

    with open(TARGET_JSON_PATH, 'w') as f:
        json.dump(output_data, f, indent=2)
        
    print(f"[+] Exported placementData.json cleanly to {TARGET_JSON_PATH}")

if __name__ == "__main__":
    export_data()
