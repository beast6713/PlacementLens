# PlacementLens — Power BI UI/UX Design System Specification

> **Document Status:** FROZEN & APPROVED UI/UX SPECIFICATION  
> **Phase Target:** Phase 5 Part 3 — Power BI UI Design System & Visual Language  
> **Dependencies:** P5-P1 Data Architecture (`v1.0-clean`, MD5: `96023d297eec5a9a47563eaddc157d0d`) & P5-P2 DAX Metric Contract  

---

## 1. Design Philosophy & Aesthetic Identity

The **PlacementLens** Power BI UI/UX Design System provides a unified, professional, high-density visual language across all four dashboard pages. 

### Aesthetic Direction
- **Cybersecurity-Inspired Visual Language:** Dark obsidian (`#0B0F19`) and slate dark (`#0F172A`) analytical environment combined with sharp cyber cyan (`#38BDF8`) and indigo (`#818CF8`) accents.
- **Institutional Placement Intelligence:** Modern BI interface designed for both executive stakeholders (Placement Cell, Deans, Leadership) and student career advisors.
- **High Signal-to-Noise Ratio:** Clean card hierarchy, high data-ink ratio, zero decorative 3D effects or rainbow color palettes.
- **Scope Guardrail:** The cybersecurity theme is an aesthetic visual environment ONLY. The domain remains strictly student placement analytics, academic preparation, skill gaps, readiness tiers, and salary package distributions.

---

## 2. Source-of-Truth & Data Compatibility Separation

```
                       ANALYTICAL TRUTH
             Phase 4 Insights + Segments + PRI
                            │
                            ▼
             Phase 3 Dual-Path Cross-Validation
                            │
                            ▼
           P5-P1 Model & P5-P2 DAX Semantic Layer
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│               POWER BI UI DESIGN SYSTEM                 │
│                                                         │
│  Visual Tokens  │  Color Semantics  │  Layout Grid      │
│  KPI Cards      │  Chart Standards  │  Navigation       │
└───────────────────────────┬─────────────────────────────┘
                            │
                            ▼
           DASHBOARD PAGES (P5-P4 to P5-P7)
```

> [!IMPORTANT]
> **Zero Data Fabrication Rule**: The visual design system CANNOT introduce components that require fields missing from the backend data model. Unsupported concepts (`academic_year`, `batch`, `eligibility`, individual `company_name` leaderboards, `offer_count`, `recruitment_date` calendar velocity) are strictly PROHIBITED from UI layouts.

---

## 3. Brand System

- **Brand Name:** PlacementLens
- **Product Descriptor:** Student Placement Analytics & Business Intelligence Platform
- **Header Identity:** Top banner anchored with PlacementLens logo mark, page category title, and dataset scope declaration (`Synthetic Placement Snapshot | N=1,500 Students`).
- **Footer Identity:** Bottom bar on every page specifying analytical context (`PlacementLens v1.0 | Non-Causal Observational Analytics`).

---

## 4. Color System & Semantic Tokens

Exported in `outputs/powerbi/10_powerbi_design_tokens.csv` and `outputs/powerbi/13_powerbi_color_semantics.csv`:

### Master Color Tokens
- `color.bg.primary`: `#0B0F19` (Obsidian Dark canvas background)
- `color.bg.secondary`: `#0F172A` (Slate Dark container background)
- `color.surface.primary`: `#1E293B` (Dark Slate visual card surface)
- `color.surface.secondary`: `#151D2A` (Deep Slate table inset surface)
- `color.border`: `#334155` (Subtle 1px card outline border)
- `color.text.primary`: `#F8FAFC` (Pure White headings & KPI numbers)
- `color.text.secondary`: `#94A3B8` (Muted Slate subtitles & field labels)
- `color.text.muted`: `#64748B` (Dark Muted Slate footnotes & axis labels)
- `color.accent.primary`: `#38BDF8` (Cyber Cyan primary interactive accent)
- `color.accent.secondary`: `#818CF8` (Indigo secondary accent)

### Semantic Color Rules
- **Placed / Positive:** Emerald Green (`#10B981`)
- **Unplaced / Neutral:** Slate Gray (`#64748B`)
- **Attention / Needs Improvement:** Amber (`#F59E0B`)
- **Critical / High Support Priority:** Rose Red (`#EF4444`)

---

## 5. Readiness & Segmentation Color Semantics

### Placement Readiness Index (PRI) Tiers
- **High Readiness** (PRI $\ge 80.00$): Emerald Green (`#10B981`)
- **Moderate Readiness** ($60.00 \le \text{PRI} < 80.00$): Cyber Cyan (`#38BDF8`)
- **Needs Improvement** ($40.00 \le \text{PRI} < 60.00$): Amber (`#F59E0B`)
- **High Improvement Priority** ($\text{PRI} < 40.00$): Rose Red (`#EF4444`)

### Student Preparation Quadrants (Segments)
- **Comprehensive High Performers** (`SEG-Q1`): Emerald Green (`#10B981`)
- **Technical Specialists** (`SEG-Q2`): Cyber Cyan (`#38BDF8`)
- **Academic Generalists** (`SEG-Q3`): Indigo (`#818CF8`)
- **High Support Priority** (`SEG-Q4`): Rose Red (`#EF4444`)

---

## 6. Typography & Numerical Formatting Standards

- **Font Family:** `Inter, Segoe UI, sans-serif`
- **Dashboard Title:** 22pt Bold (`#F8FAFC`)
- **Section Header:** 14pt Semi-Bold (`#F8FAFC`)
- **KPI Primary Value:** 28pt Bold (`#F8FAFC`)
- **Card Body / Table Text:** 10pt Regular (`#94A3B8`)

### Numerical Precision & Display Rules
- **Placement Rate / Percentages:** `0.00%` (e.g., `63.33%`)
- **Salary Packages:** `0.00 "LPA"` (e.g., `10.62 LPA`)
- **CGPA:** `0.00` (e.g., `7.59`)
- **Scores & PRI:** `0.00` (e.g., `65.59`)
- **Student Counts:** `#,##0` (e.g., `1,500`)

---

## 7. Layout Grid & Component Spacing

- **Page Grid:** 12-column grid layout with 16px gutter spacing and 20px outer margin.
- **Card Styling:** Dark Slate background (`#1E293B`), 8px border radius, 1px subtle border (`#334155`).
- **Spacing Scale:**
  - `space.xs` (4px): Badge padding
  - `space.sm` (8px): Label-to-value gap
  - `space.md` (16px): Card internal padding & grid gutter
  - `space.lg` (24px): Section gap
  - `space.xl` (32px): Major block separation

---

## 8. Common Page Template Architecture

```
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ PlacementLens | Student Placement Intelligence                         [Dataset Snapshot] │
├───────────────┬───────────────────────────────────────────────────────────────────────────┤
│               │ PAGE TITLE & SUBTITLE                                                     │
│               │ [Filter Context Indicator: Branch = All | Status = All | Segment = All]   │
│   SIDEBAR     ├───────────────────────────────────────────────────────────────────────────┤
│               │ EXECUTIVE KPI ROW (4 Standard Cards)                                      │
│  01 Command   ├───────────────────────────────────────────────────────────────────────────┤
│  02 Student   │ PRIMARY ANALYTICAL VISUAL GRID (2x2 or 2x3 Chart Container Cards)        │
│  03 Company   │                                                                           │
│  04 Reports   ├───────────────────────────────────────────────────────────────────────────┤
│               │ EXECUTIVE NARRATIVE INSIGHT CALLOUT PANEL                                 │
├───────────────┴───────────────────────────────────────────────────────────────────────────┤
│ PlacementLens v1.0 | Synthetic Cohort (N=1,500) | Non-Causal Observational Analytics      │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 9. KPI Card System

### Component Standards
- **`PL-KPI-Executive`**: 28pt Bold metric value, 10pt muted upper label, compact secondary context text (e.g. `950 / 1,500 students`), optional status badge.
- **`PL-KPI-Readiness`**: Primary PRI score display with colored readiness tier badge (`High`, `Moderate`, `Needs Imp`, `High Imp Priority`).
- **`PL-KPI-Context`**: Filter context bar displaying active slicer selections dynamically.

---

## 10. Chart & Table Standards

Exported in `outputs/powerbi/12_powerbi_visual_standards.csv`:
- **Horizontal Bar Charts:** Used for branch placement rates, skill prevalence, and company-type comparisons. Sorted descending by metric value. Cyber Cyan bars with Emerald highlight for top rank.
- **Clustered Column Charts:** Used for readiness tier distributions and quadrant student counts. Preserves natural ordinal tier order.
- **Scatter Plots:** Used for CGPA vs. Aptitude/Coding score distribution. Dots color-coded by Placement Status (Emerald = Placed, Slate = Unplaced). Non-causal disclaimers applied.
- **Data Matrix Tables:** Dark Slate background (`#1E293B`), alternate row shading (`#151D2A`), right-aligned numbers, status badge conditional formatting.

---

## 11. Navigation Sidebar System

- **Layout Anchor:** Fixed left sidebar spanning 100% canvas height.
- **Visual Style:** Dark slate container (`#0F172A`) with subtle right border (`#334155`).
- **Navigation Links:**
  1. `01 Command Center` (Executive Overview)
  2. `02 Student Analytics` (Student Preparation & Skills)
  3. `03 Company Intelligence` (Company Type & Compensation)
  4. `04 Reports & Intelligence` (Readiness Drillthrough & Insights)
- **Active State:** Cyber Cyan left border accent (`#38BDF8`) + pure white text (`#F8FAFC`).

---

## 12. Component Inventory (16 Standard Components)

Exported in `outputs/powerbi/11_powerbi_component_inventory.csv`:
`PL-Header`, `PL-Sidebar`, `PL-PageTitle`, `PL-KPI-Executive`, `PL-KPI-Analytical`, `PL-KPI-Readiness`, `PL-KPI-Context`, `PL-SectionHeader`, `PL-Slicer`, `PL-Chart`, `PL-Table`, `PL-Badge`, `PL-InsightCard`, `PL-Tooltip`, `PL-Footer`, `PL-EmptyState`.

---

## 13. Data/UI Compatibility & Anti-Pattern Prohibition

Exported in `outputs/powerbi/14_powerbi_data_ui_compatibility.csv`:

### Prohibited Anti-Patterns & Unsupported Concepts
1. **No Individual Company Leaderboards:** Individual company names (TCS, Infosys, Deloitte) do not exist. Visuals MUST use `company_type` (`Service`, `Product`, `Startup`, `MNC`).
2. **No Batch / Graduation Year Slicers:** `academic_year` does not exist. Dataset is a single static placement snapshot cohort ($N=1,500$).
3. **No Placement Eligibility Controls:** `eligibility` metadata does not exist. Assume 100% of 1,500 students are eligible.
4. **No Multiple Offer Trackers:** `offer_count` does not exist. Dataset records binary placement outcome (`placed` 1/0).
5. **No Monthly Recruitment Velocity Trends:** `recruitment_date` timestamps do not exist. Time-series date calendars are PROHIBITED.
6. **No 3D Charts, Gauges, or Rainbow Palette Gradients.**

---

## 14. Accessibility & Non-Causal UX Rules

- **Double-Encoding:** Status indicators use BOTH explicit text labels and distinct semantic colors (never color alone).
- **High Contrast:** All text tokens exceed WCAG AA contrast ratio against dark background (`#F8FAFC` on `#1E293B` contrast = 12.8:1).
- **Observational Terminology:** All visual titles, tooltips, and narrative callouts use neutral phrasing (`Observed Spread`, `Observed Difference`, `Readiness Distribution`). Words like `Causation`, `Impact`, or `Prediction` are PROHIBITED.

---

## 15. Four-Page Visual Identity Freeze

```
PAGE 01 — COMMAND CENTER
  → Purpose: Executive placement overview, headline KPIs, branch benchmarks, tier distribution.

PAGE 02 — STUDENT & PLACEMENT ANALYTICS
  → Purpose: Academic preparation, coding/aptitude/communication scores, 7 technical skill spreads.

PAGE 03 — COMPANY & PACKAGE INTELLIGENCE
  → Purpose: Salary package distributions (placed N=950), company_type breakdown, branch packages.

PAGE 04 — REPORTS & INTELLIGENCE
  → Purpose: Detailed student readiness investigation, preparation quadrant profiles, narrative insights.
```

---

## 16. Phase 5 Part 4 Handoff Contract

The Power BI UI Design System & Visual Language is **CERTIFIED AND FROZEN**. Phase 5 Part 4 (Command Center Dashboard Page) is authorized to consume this design system:

```
DESIGN SYSTEM FROZEN:          YES
COLOR TOKENS REGISTERED:       PASS (14 tokens frozen)
SEMANTIC MAPPINGS FROZEN:      PASS (10 semantic rules)
TYPOGRAPHY STANDARDS:          PASS (Inter stack + numerical precision)
LAYOUT GRID SPECIFIED:         PASS (12-column grid, 8px radius, 16px gutter)
COMPONENT INVENTORY:           PASS (16 components mapped to Power BI controls)
VISUAL STANDARDS FROZEN:       PASS (Bar, Column, Scatter, Histogram, Table, Slicer)
DATA/UI COMPATIBILITY:         PASS (100% supported concepts, 6 unsupported logged)
NON-CAUSAL UX RULES:           PASS (Observational language enforced)
ACCESSIBILITY REVIEW:          PASS (WCAG AA contrast + double encoding)

CHECKPOINT-05-PART-03:         PASS
```
