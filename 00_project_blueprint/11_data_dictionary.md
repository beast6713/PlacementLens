# Data Dictionary

| Column | Type | Nullable | Allowed values / valid range | Business meaning | Example | Validation rule |
|---|---:|---:|---|---|---|---|
| student_id | string | No | `S0001`–`S1500`, unique | Synthetic row identifier | S0001 | Unique, nonblank, regex `^S[0-9]{4}$` after cleaning |
| age | integer | No | 18–30 | Student age at snapshot | 21 | Integer in range |
| gender | category | No | Female, Male, Non-binary, Prefer not to say | Self-described demographic grouping | Female | Standardize allowed labels |
| branch | category | No | CSE, IT, ECE, EEE, ME, CE | Academic branch | CSE | Standardize allowed labels |
| cgpa | decimal | No | 0.00–10.00 | Academic-performance indicator | 8.14 | Numeric, inclusive range |
| internships | integer | No | 0–5 | Completed internships | 1 | Non-negative integer ≤5 |
| projects | integer | No | 0–10 | Completed academic/personal projects | 3 | Non-negative integer ≤10 |
| coding_score | decimal | No | 0–100 | Coding assessment score | 74.0 | Numeric, inclusive range |
| aptitude_score | decimal | No | 0–100 | Aptitude assessment score | 68.5 | Numeric, inclusive range |
| communication_score | decimal | No | 0–100 | Communication assessment score | 72.0 | Numeric, inclusive range |
| python_skill | boolean | No | 0/1 or false/true | Self-reported/assessed Python capability flag | 1 | Normalize to 0 or 1 |
| sql_skill | boolean | No | 0/1 or false/true | SQL capability flag | 1 | Normalize to 0 or 1 |
| excel_skill | boolean | No | 0/1 or false/true | Excel capability flag | 1 | Normalize to 0 or 1 |
| power_bi_skill | boolean | No | 0/1 or false/true | Power BI capability flag | 0 | Normalize to 0 or 1 |
| dsa_skill | boolean | No | 0/1 or false/true | Data structures and algorithms capability flag | 1 | Normalize to 0 or 1 |
| cloud_skill | boolean | No | 0/1 or false/true | Cloud capability flag | 0 | Normalize to 0 or 1 |
| cybersecurity_skill | boolean | No | 0/1 or false/true | Cybersecurity capability flag | 0 | Normalize to 0 or 1 |
| placed | boolean | No | 0/1 or false/true | Recorded placement outcome at snapshot | 1 | Normalize to 0 or 1 |
| company_type | category | Conditionally | Product, Service, Startup, Other | Type of company for placed student | Product | Required iff placed=1; null iff placed=0 |
| package_lpa | decimal | Conditionally | >0–50 | Annual package in lakh INR for placed student | 8.50 | Required iff placed=1; null iff placed=0; numeric >0 and ≤50 |

`package_lpa` is an illustrative synthetic compensation field and must not be presented as market data.

