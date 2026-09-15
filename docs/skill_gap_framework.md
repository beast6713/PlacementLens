# PlacementLens — Skill Gap Analytical Framework

## 1. Executive Summary & Purpose

This document defines the **Skill Gap Analytical Framework** for Phase 4 of **PlacementLens**. Technical skills represent a core dimension of student preparation. This framework provides standardized definitions, metrics, and evaluation rules for identifying technical skill deficits across the 1,500-student dataset and establishing evidence-based skill prioritization.

---

## 2. Canonical Technical Skill Inventory

PlacementLens evaluates seven canonical binary technical skills. Each skill attribute is encoded as a discrete binary flag ($1 = \text{Present}$, $0 = \text{Absent}$).

| Skill Attribute | Skill Name | Domain / Focus Area | Canonical Range | Phase 3 Baseline Prevalence ($N=1,500$) |
| :--- | :--- | :--- | :---: | :---: |
| `python_skill` | Python Programming | Scripting & Data Analysis | $\{0, 1\}$ | 48.07% ($N=721$) |
| `sql_skill` | SQL Database | Data Querying & Relational DB | $\{0, 1\}$ | 47.27% ($N=709$) |
| `excel_skill` | Advanced Excel | Data Manipulation & Spreadsheets | $\{0, 1\}$ | 50.80% ($N=762$) |
| `power_bi_skill` | Power BI / BI Tools | Data Visualization & Dashboards | $\{0, 1\}$ | 49.33% ($N=740$) |
| `dsa_skill` | Data Structures & Algorithms | Core Problem Solving & CS Basics | $\{0, 1\}$ | 50.13% ($N=752$) |
| `cloud_skill` | Cloud Computing (AWS/Azure) | Infrastructure & Cloud Systems | $\{0, 1\}$ | 48.87% ($N=733$) |
| `cybersecurity_skill`| Cybersecurity Fundamentals | Security & Information Protection | $\{0, 1\}$ | 49.60% ($N=744$) |

---

## 3. Official Technical Skill Count Definition

The total technical skill breadth of a student is summarized by the composite metric `technical_skill_count`.

### 3.1 Mathematical Definition
$$\text{technical\_skill\_count}_i = \sum_{k=1}^{7} \text{Skill}_{i, k}$$

Where $\text{Skill}_{i, k} \in \{0, 1\}$ represents student $i$'s possession of skill $k$ across the 7 canonical skills:

$$\text{technical\_skill\_count} = \text{python\_skill} + \text{sql\_skill} + \text{excel\_skill} + \text{power\_bi\_skill} + \text{dsa\_skill} + \text{cloud\_skill} + \text{cybersecurity\_skill}$$

### 3.2 Property Rules
- **Canonical Bounded Range:** Integer values from $0$ to $7$.
- **Phase 3 Validated Baseline:** 
  - Placed Cohort Median = $4.0$ skills (IQR: $3.0 - 5.0$)
  - Unplaced Cohort Median = $3.0$ skills (IQR: $2.0 - 4.0$)
- **Immutability Rule:** This formula is frozen and MUST NOT be altered or weighted non-uniformly when calculating `technical_skill_count`.

---

## 4. Core Skill Gap Analytical Metrics

Skill gap evaluations across population cohorts (overall or branch-level) utilize four primary metrics:

### 4.1 Skill Prevalence Rate ($\text{Prev}_k$)
The percentage of students in a given cohort who possess skill $k$:
$$\text{Prev}_k = \frac{N_{\text{Holders}, k}}{N_{\text{Cohort}}} \times 100\%$$

### 4.2 Skill Absence / Gap Rate ($\text{Gap}_k$)
The percentage of students in a given cohort who lack skill $k$:
$$\text{Gap}_k = 100\% - \text{Prev}_k = \frac{N_{\text{Non-Holders}, k}}{N_{\text{Cohort}}} \times 100\%$$

### 4.3 Skill Placement Spread ($\text{Spread}_k$)
The absolute difference in observed placement rate between skill holders and non-holders:
$$\text{Spread}_k = \text{Placement Rate}_{\text{Holders}, k} - \text{Placement Rate}_{\text{Non-Holders}, k}$$
*(Expressed in percentage points, `pp`)*

### 4.4 Phase 3 Validated Skill Placement Spreads Baseline

| Skill Name | Holder Placement Rate | Non-Holder Placement Rate | Validated Placement Spread (`pp`) |
| :--- | :---: | :---: | :---: |
| **SQL Database** | 68.41% ($N=709$) | 59.24% ($N=791$) | **`+9.17 pp`** |
| **Python Programming** | 66.85% ($N=721$) | 59.91% ($N=779$) | **`+6.94 pp`** |
| **Cloud Computing** | 66.30% ($N=733$) | 60.26% ($N=767$) | **`+6.04 pp`** |
| **Advanced Excel** | 64.57% ($N=762$) | 61.98% ($N=738$) | **`+2.59 pp`** |
| **Data Structures & Algo** | 64.06% ($N=752$) | 62.59% ($N=748$) | **`+1.47 pp`** |
| **Power BI / Visuals** | 63.85% ($N=740$) | 62.83% ($N=760$) | **`+1.01 pp`** |
| **Cybersecurity** | 61.83% ($N=744$) | 64.81% ($N=756$) | **`-2.98 pp`** |

---

## 5. Multi-Criteria Skill Priority Methodology

A common analytical error is declaring the skill with the largest placement spread as automatically the "most important skill." Such single-metric ranking ignores skill prevalence, absence magnitude, and cohort size.

PlacementLens establishes a **Multi-Criteria Skill Priority Scoring Model** combining four weighted factors:

```
                    ┌─────────────────────────────────────────┐
                    │     MULTI-CRITERIA SKILL PRIORITY       │
                    └────────────────────┬────────────────────┘
                                         │
    ┌────────────────────┬───────────────┴───────────────┬────────────────────┐
    ▼                    ▼                               ▼                    ▼
Placement Spread     Skill Absence Gap           Cohort Prevalence      Subgroup Sample Size
  Weight: 45%           Weight: 35%                 Weight: 10%            Weight: 10%
```

### 5.1 Priority Evaluation Scoring Formula

$$\text{Priority Score}_k = 0.45 \times S_{\text{Spread}, k} + 0.35 \times S_{\text{Gap}, k} + 0.10 \times S_{\text{Prev}, k} + 0.10 \times S_{\text{Sample}, k}$$

Where all component sub-scores $S$ are normalized to a $0 - 100$ scale.

### 5.2 Priority Tiers

| Priority Tier | Score Range | Operational Definition & Strategic Action |
| :--- | :---: | :--- |
| **`HIGH PRIORITY`** | $75 - 100$ | High placement spread combined with substantial student absence gap. Immediate focus for curriculum enhancement and targeted bootcamps. |
| **`MEDIUM PRIORITY`** | $50 - 74$ | Moderate placement spread and noticeable skill gap. Recommended for elective tracks and supplementary workshops. |
| **`LOW PRIORITY`** | $25 - 49$ | Lower placement spread or high existing prevalence. General maintenance in baseline coursework. |
| **`MONITOR / REVIEW`**| $< 25$ | Negative or negligible placement spread. Requires qualitative review before institutional resource allocation. |

---

## 6. Execution Rules for Phase 4

1. **P4-P1 Freeze:** P4-P1 freezes these metrics, formulas, and evaluation matrices.
2. **P4-P3 Execution:** Full calculation of skill gap matrices across all branches and student segments will be performed in **P4-P3**.
3. **No Non-Causal Claims:** High priority status MUST NOT be communicated as "learning this skill guarantees placement."
