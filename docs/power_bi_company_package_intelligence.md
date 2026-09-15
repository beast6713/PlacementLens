# PlacementLens — Page 03 Company & Package Intelligence Specification Document

> **Document Version:** 1.0.0  
> **Phase Assignment:** Phase 5 — Part 6 (P5-P6)  
> **Target Page:** Page 03 — Company & Package Intelligence  
> **Status:** FROZEN & VALIDATED (100% QA PASS)  

---

## 1. Page Identity & Purpose

### 1.1 Identity
- **Page Name:** `PAGE 03 COMPANY & PACKAGE INTELLIGENCE`
- **Recommended Page Title:** `Company & Package Intelligence`
- **Recommended Subtitle:** `Compensation outcomes and company-type patterns among placed students`
- **Navigation Position:** Page 03 in Global Sidebar (Active Highlight: `03 Company & Package`)

### 1.2 Purpose & Core Analytical Questions
Page 03 focuses exclusively on placement compensation outcomes (`package_lpa`) and employer categories (`company_type`) for the placed student cohort ($N=950$).

Stakeholders use Page 03 to answer:
1. What is the average and median compensation package among placed students?
2. How are placement packages distributed (range, central tendency, IQR dispersion)?
3. How are placed students distributed across employer company types (Product, Startup, Service, Other)?
4. How do compensation statistics vary by company type?
5. How do compensation statistics vary across academic branches?
6. What is the sample size ($N$) underlying each company-type and branch package summary?

---

## 2. Critical Data Limitations & Zero Fabrication Mandate

### 2.1 Available Fields in Data Model
- `company_type` (`Product`, `Startup`, `Service`, `Other`)
- `package_lpa` (Valid for placed students $N=950$; `NULL` for unplaced $N=550$)
- Student demographics, academic branch, gender, and skills.

### 2.2 Absent Fields & Prohibited UI Concepts
The underlying dataset does **NOT** contain: `company_name`, `offer_count`, `recruitment_date`, `placement_date`, `academic_year`, `batch`, `active_companies`, `new_companies`, `historical_company_activity`, or `eligibility`.

Therefore, Page 03 strictly **PROHIBITS**:
- ❌ Company leaderboards or company-wise rankings (no TCS, Infosys, Amazon, Microsoft, Deloitte, Google).
- ❌ Company hiring activity or recruitment timelines.
- ❌ Active companies / new companies KPI cards.
- ❌ Placement trend by year or YoY package growth charts (no valid date field exists).
- ❌ Company-specific package comparisons or offer counts.

---

## 3. Package Semantics & NULL Handling

### 3.1 Placed Population Scope
`package_lpa` is meaningful **ONLY** for placed students ($N=950$). Unplaced students ($N=550$) have `package_lpa = NULL`.

### 3.2 Strict NULL Protection Rules
- **Rule 1:** `package_lpa = NULL` must **NEVER** be converted to ₹0.
- **Rule 2:** Unplaced students must **NEVER** be included in the denominator of package average or median calculations.
- **Rule 3:** The denominator for all package metrics is strictly the valid placed package population ($N=950$).
- **Rule 4:** If filters produce zero placed records, visuals must display an explicit `NO PACKAGE DATA` state rather than ₹0.

---

## 4. Page Architecture & Grid Layout

The layout uses the responsive grid established in P5-P3:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ PAGE HEADER & CONTEXT BAR                                                    │
│ Company & Package Intelligence | Branch: All | Gender: All | Company: All   │
├──────────────────────────────────────────────────────────────────────────────┤
│ ANALYTICAL SLICER BAR                                                        │
│ [Branch Dropdown] [Gender Dropdown] [Company Type Dropdown]                  │
├──────────────────────────────────────────────────────────────────────────────┤
│ KPI 01            KPI 02            KPI 03            KPI 04                 │
│ PLACED STUDENTS   AVERAGE PACKAGE   MEDIAN PACKAGE    PACKAGE IQR            │
│ 950               ₹10.62 LPA        ₹9.70 LPA         8.22 LPA               │
├───────────────────────────────┬──────────────────────────────────────────────┤
│ PACKAGE DISTRIBUTION          │ COMPANY-TYPE DISTRIBUTION                    │
│ Placed Students by LPA Band   │ Placed Students Count & % by Company Type    │
├───────────────────────────────┼──────────────────────────────────────────────┤
│ PACKAGE BY COMPANY TYPE       │ PACKAGE BY BRANCH                            │
│ Mean & Median Package by Type │ Mean & Median Package by Branch (N context)  │
├───────────────────────────────┴──────────────────────────────────────────────┤
│ DETAILED COMPANY-TYPE COMPENSATION MATRIX                                    │
│ Company Type | Placed Count | % of Placed | Mean Package | Median Package    │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Visual Inventory & Component Mappings

| Visual ID | Visual Name | Visual Type | Dimension | DAX Measure / Field | Population Scope |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **P3-HEADER** | Global Header Banner | Header Banner | N/A | Static Title & Subtitle | All Students (1,500) |
| **P3-SIDEBAR**| Navigation Sidebar | Menu | Page Name | Active Highlight: `03 Company & Package` | System Canvas |
| **P3-FILTERS**| Analytical Slicers | Slicer Bar | `branch`, `gender`, `company_type` | N/A | Slicer Context |
| **P3-FILTER-CONTEXT** | Active Context Bar | Dynamic Text | Slicer Context | `[Active Filter Context]` | Filtered Cohort |
| **P3-KPI-01** | Placed Students Card | Card | N/A | `[Placed Students]` | Placed Cohort (950) |
| **P3-KPI-02** | Average Package Card | Card | N/A | `[Average Package]` | Valid Placed (950) |
| **P3-KPI-03** | Median Package Card | Card | N/A | `[Median Package]` | Valid Placed (950) |
| **P3-KPI-04** | Package IQR Card | Card | N/A | `[Package IQR]` | Valid Placed (950) |
| **P3-PACKAGE-01**| Package Distribution | Histogram | `package_band` | `[Placed Students]`, `[Average Package]` | Placed Cohort (950) |
| **P3-COMPANYTYPE-01**| Placed by Company Type| Horizontal Bar | `company_type` | `[Placed Students]` | Placed Cohort (950) |
| **P3-COMPANYTYPE-02**| Package by Company Type| Clustered Bar | `company_type` | `[Average Package]`, `[Median Package]` | Placed by Type |
| **P3-BRANCH-01**| Package by Branch | Clustered Column | `branch` | `[Average Package]`, `[Median Package]`, `[Placed Students]` | Placed by Branch |
| **P3-TABLE-01**| Company-Type Detail Grid| Data Table | `company_type` | `[Placed Students]`, `[Average Package]`, `[Median Package]` | Placed by Type |

---

## 6. Baseline Reconciliation & Unfiltered Reference Values

All numbers originate dynamically from P5-P2 DAX measures:

| Metric Name | DAX Expression | Unfiltered Baseline Value | QA Status |
| :--- | :--- | :---: | :---: |
| **Placed Students** | `CALCULATE(COUNTROWS(Students), Students[placed]=1)` | **950** | Verified |
| **Average Package** | `AVERAGE(Students[package_lpa])` | **₹10.62 LPA** | Verified |
| **Median Package** | `MEDIAN(Students[package_lpa])` | **₹9.70 LPA** | Verified |
| **Package IQR** | `PERCENTILE.INC(package_lpa, 0.75) - PERCENTILE.INC(package_lpa, 0.25)` | **8.22 LPA** | Verified |
| **Product Mean Package** | `CALCULATE([Average Package], company_type="Product")` | **₹16.26 LPA** | Verified ($N=304$) |
| **Product Median Package**| `CALCULATE([Median Package], company_type="Product")` | **₹15.57 LPA** | Verified ($N=304$) |
| **Startup Mean Package** | `CALCULATE([Average Package], company_type="Startup")` | **₹12.09 LPA** | Verified ($N=222$) |
| **Startup Median Package**| `CALCULATE([Median Package], company_type="Startup")` | **₹11.71 LPA** | Verified ($N=222$) |
| **Service Mean Package** | `CALCULATE([Average Package], company_type="Service")` | **₹5.90 LPA** | Verified ($N=381$) |
| **Service Median Package**| `CALCULATE([Median Package], company_type="Service")` | **₹6.03 LPA** | Verified ($N=381$) |
| **Other Mean Package** | `CALCULATE([Average Package], company_type="Other")` | **₹5.02 LPA** | Verified ($N=43$) |
| **Other Median Package** | `CALCULATE([Median Package], company_type="Other")` | **₹5.03 LPA** | Verified ($N=43$) |

---

## 7. Company-Type & Branch Compensation Analysis

### 7.1 Company-Type Placed Distribution
- **Service:** $381$ placed ($40.11\%$) | Mean = ₹5.90 LPA | Median = ₹6.03 LPA
- **Product:** $304$ placed ($32.00\%$) | Mean = ₹16.26 LPA | Median = ₹15.57 LPA
- **Startup:** $222$ placed ($23.37\%$) | Mean = ₹12.09 LPA | Median = ₹11.71 LPA
- **Other:** $43$ placed ($4.53\%$) | Mean = ₹5.02 LPA | Median = ₹5.03 LPA

### 7.2 Branch Compensation Breakdown
- **CSE:** $287$ placed | Mean = ₹10.82 LPA | Median = ₹9.91 LPA
- **IT:** $244$ placed | Mean = ₹10.76 LPA | Median = ₹9.86 LPA
- **ECE:** $181$ placed | Mean = ₹9.93 LPA | Median = ₹8.74 LPA
- **EEE:** $99$ placed | Mean = ₹10.60 LPA | Median = ₹10.45 LPA
- **CE:** $72$ placed | Mean = ₹10.45 LPA | Median = ₹7.89 LPA
- **ME:** $67$ placed | Mean = ₹11.33 LPA | Median = ₹10.39 LPA

---

## 8. Tooltip & Formatting Rules

### 8.1 Tooltip Requirements
All package tooltips must explicitly expose sample size ($N$) and population scope:
```text
Company Type: Product
Mean Package: ₹16.26 LPA
Median Package: ₹15.57 LPA
Sample Size (N): 304 placed students
Population: Placed students with valid package record
```

### 8.2 Formatting Precision
- **Package Values:** `₹X.XX LPA` (e.g., `₹10.62 LPA`)
- **Percentages:** `X.X%` or `X.XX%`
- **Counts:** `#,##0` (e.g., `950`)

---

## 9. QA Audit & Certification

- **Total QA Checks:** 25 Validation Checks
- **Pass Rate:** 100% (25/25)
- **Script Executor:** `scripts/build_company_intelligence.py`
- **Validation Scorecard CSV:** `outputs/powerbi/29_company_package_validation.csv`
- **Summary Report:** `outputs/powerbi/30_company_package_qa_summary.md`

```
PAGE 03 STATUS: PASS 100%
HANDOFF TARGET: PHASE 5 PART 7 — REPORTS & INTELLIGENCE (PAGE 04)
```
