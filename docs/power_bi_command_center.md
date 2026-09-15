# PlacementLens — Power BI Page 01: Command Center Specification

> **Document Status:** FROZEN & APPROVED PAGE SPECIFICATION  
> **Phase Target:** Phase 5 Part 4 — Page 01 Command Center Dashboard  
> **Dependencies:** P5-P1 Model, P5-P2 DAX Metric Contract & P5-P3 UI Design System  

---

## 1. Page Purpose & Identity

- **Page Name:** `Page 01 — Command Center`
- **Page Title:** `Placement Intelligence Command Center`
- **Page Subtitle:** `A consolidated view of student placement outcomes, preparation and readiness`
- **Executive Entry Point:** Serves as the executive decision-support overview for PlacementLens. It answers at a glance:
  - How many total students are being analyzed ($N=1,500$)?
  - How many students were placed ($N=950$)?
  - What is the overall observed placement rate ($63.33\%$)?
  - What is the mean Placement Readiness Index score ($65.59$)?
  - How does observed placement vary across academic branches ($CE: 68.57\%$ to $ME: 56.44\%$)?
  - How are students distributed across validated readiness tiers ($High: 82$, $Moderate: 862$, $Needs Imp: 540$, $High Imp Priority: 16$)?
  - What are the technical skill prevalence signals across the student population?

---

## 2. Page Architecture & Canvas Layout

```
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ PlacementLens | Placement Intelligence Command Center                [Synthetic Snapshot] │
├───────────────┬───────────────────────────────────────────────────────────────────────────┤
│               │ PAGE TITLE: Placement Intelligence Command Center                         │
│               │ [Filter Context: Branch: All | Gender: All | Placement: All]              │
│   SIDEBAR     ├───────────────────────────────────────────────────────────────────────────┤
│               │ SLICER BAR: [Select Branch ▾]  [Select Gender ▾]  [Select Placement Status ▾]│
│  01 Command   ├───────────────────────────────────────────────────────────────────────────┤
│  02 Student   │ EXECUTIVE KPI ROW                                                         │
│  03 Company   │ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐       │
│  04 Reports   │ │Total Students│ │Placed Student│ │Placement Rate│ │ Average PRI  │       │
│               │ │    1,500     │ │     950      │ │    63.33%    │ │    65.59     │       │
│               │ └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘       │
│               ├───────────────────────────────────────────┬───────────────────────────────┤
│               │ PRIMARY VISUAL GRID                       │ READINESS TIER DISTRIBUTION   │
│               │ Placement Rate by Branch                  │ (High, Mod, Needs, HighImp)   │
│               │ (Horizontal Bar Chart)                    │ (Clustered Column Chart)      │
│               ├───────────────────────────────────────────┼───────────────────────────────┤
│               │ TECHNICAL SKILL PREVALENCE SIGNAL         │ EXECUTIVE KEY INTELLIGENCE    │
│               │ (SQL, Python, Excel, Power BI, DSA, Cloud)│ (Phase 4 Validated Insights)  │
│               │ (Horizontal Bar Chart)                    │ (Narrative Panel)             │
├───────────────┴───────────────────────────────────────────┴───────────────────────────────┤
│ PlacementLens v1.0 | Synthetic Cohort (N=1,500) | Non-Causal Observational Analytics      │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Visual & KPI Inventory

Exported in `outputs/powerbi/16_command_center_visual_inventory.csv`:

1. **`CC-HDR-01` (Global Header Bar):** Top branding header anchored with PlacementLens logo mark and scope tag.
2. **`CC-NAV-01` (Navigation Sidebar):** Fixed left navigation menu with `01 Command Center` link active (`#38BDF8` accent).
3. **`CC-FLT-01` (Filter Context Indicator):** Dynamic DAX indicator displaying active slicer selections.
4. **`CC-SLC-01` (Branch Dropdown Slicer):** Slices page metrics by `Students[branch]`.
5. **`CC-SLC-02` (Gender Dropdown Slicer):** Slices page metrics by `Students[gender]`.
6. **`CC-SLC-03` (Placement Status Slicer):** Slices page metrics by `Students[placed]`.
7. **`CC-KPI-01` (Total Students KPI Card):** Consumes `[Total Students]` ($N=1,500$).
8. **`CC-KPI-02` (Placed Students KPI Card):** Consumes `[Placed Students]` ($N=950$).
9. **`CC-KPI-03` (Placement Rate KPI Card):** Consumes `[Placement Rate]` ($63.33\%$).
10. **`CC-KPI-04` (Average PRI KPI Card):** Consumes `[Average PRI]` ($65.59$).
11. **`CC-VIS-01` (Placement Rate by Branch):** Horizontal bar chart displaying placement rates across all 6 branches.
12. **`CC-VIS-02` (Readiness Tier Distribution):** Clustered column chart displaying student population across 4 readiness tiers.
13. **`CC-VIS-03` (Technical Skill Prevalence Signal):** Horizontal bar chart displaying prevalence percentages across 7 technical skills.
14. **`CC-INS-01` (Executive Key Intelligence Panel):** Narrative callout box displaying validated Phase 4 findings.
15. **`CC-FTR-01` (Methodology Footer Bar):** Bottom canvas footer with dataset and non-causal disclaimer.

---

## 4. DAX Measure Mapping Matrix

Exported in `outputs/powerbi/17_command_center_measure_mapping.csv`:
- `CC-KPI-01` → `[Total Students]` (`DISTINCTCOUNT(Students[student_id])`, Target: `1,500`, Status: **PASS**)
- `CC-KPI-02` → `[Placed Students]` (`CALCULATE(COUNTROWS(Students), Students[placed]=1)`, Target: `950`, Status: **PASS**)
- `CC-KPI-03` → `[Placement Rate]` (`DIVIDE([Placed Students], [Total Students], 0)`, Target: `63.33%`, Status: **PASS**)
- `CC-KPI-04` → `[Average PRI]` (`AVERAGE(Students[pri_score])`, Target: `65.59`, Status: **PASS**)
- `CC-VIS-01` → `[Placement Rate]` by `branch` (Target: `CE: 68.57%` to `ME: 56.44%`, Status: **PASS**)
- `CC-VIS-02` → `[Total Students]` by `readiness_category` (Target: `High: 82`, `Mod: 862`, `Needs: 540`, `HighImp: 16`, Status: **PASS**)
- `CC-VIS-03` → `[<Skill> Skill Prevalence]` across 7 skills (Target: `Excel: 43.13%` to `Cyber: 39.33%`, Status: **PASS**)

---

## 5. Filter Interaction Matrix

Exported in `outputs/powerbi/18_command_center_filter_interaction_matrix.csv`:
- **Branch Slicer (`CC-SLC-01`)**: Filters `CC-KPI-01` to `CC-KPI-04`, `CC-VIS-01` (highlights selected bar), `CC-VIS-02` (tier breakdown for selected branch), `CC-VIS-03` (skill prevalence for selected branch).
- **Gender Slicer (`CC-SLC-02`)**: Filters all KPI cards and visual containers.
- **Placement Status Slicer (`CC-SLC-03`)**: Filters all KPI cards and visual containers.
- **Cross-Highlighting:** Enabled between Branch Chart (`CC-VIS-01`) and Readiness Chart (`CC-VIS-02`).

---

## 6. QA Scorecard Results (25/25 Passed)

Exported in `outputs/powerbi/19_command_center_validation.csv`:
- Data integrity (1,500 students, 950 placed, 63.33% rate, 65.59 mean PRI): **PASS**
- Centralized P5-P2 DAX measure consumption: **PASS**
- Zero hard-coded live numbers: **PASS**
- 6 branches displayed in descending rate order: **PASS**
- 4 readiness tiers sum to 1,500 students: **PASS**
- 7 technical skills prevalence signal verified: **PASS**
- Active Filter Context indicator updating dynamically: **PASS**
- Target leakage controls (0 outcome variables in formula scoring): **PASS**
- Data gap register enforcement (0 unsupported fields): **PASS**
- Non-causal observational phrasing enforced: **PASS**
- Accessibility WCAG AA contrast & double encoding: **PASS**
- Source raw and clean CSV MD5 hashes immutable: **PASS**

---

## 7. Phase 5 Part 5 Handoff Contract

Page 01 — Command Center is **CERTIFIED AND FROZEN**. Phase 5 Part 5 (Student & Placement Analytics Page 02) is authorized to consume this foundation:

```
PAGE 01 COMMAND CENTER:      PASS 100%
VISUAL INVENTORY FROZEN:     PASS (15 visual elements registered)
MEASURE MAPPING FROZEN:      PASS (100% P5-P2 measures mapped)
FILTER INTERACTIONS VALID:   PASS (Dynamic context + cross-highlighting)
QA SCORECARD PASSED:         PASS (25/25 validation checks passed)
DOCUMENTATION COMPLETE:      PASS

CHECKPOINT-05-PART-04:       PASS
```
