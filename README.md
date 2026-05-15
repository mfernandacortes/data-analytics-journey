# Data Analytics Journey

SQL practice and business-oriented data analysis using the Northwind database.  
Focus: writing queries that answer real business questions, not just technical exercises.

---

## About this project

This repository documents my learning journey into data analytics using SQL.

Each week I explore the Northwind database, not only to practice syntax, 
but to understand the data and extract meaningful insights from a business perspective.
The goal is to progressively move from technical exercises to analytical thinking.

**Stack:** SQL Server · Northwind DB · Git

---

## What I'm building

| Week | Topics | Business focus |
|------|--------|---------------|
| [Week 1](./semana-01/) | CTEs, chained CTEs, subqueries, aggregations | Sales performance by employee and customer |
| [Week 2](./semana-02/) | Window functions: RANK, ROW_NUMBER, LAG, LEAD | Customer behavior, churn signals, ranking analysis |
| [Week 3](./semana-03/) | CASE WHEN, conditional logic | Returns analysis, business rules and classification |

---

## Análisis y hallazgos

Ver análisis detallados → [HALLAZGOS.md](./HALLAZGOS.md)

---

## SQL techniques covered

- Common Table Expressions (CTEs) — single and chained
- Subqueries in `WHERE` and `FROM`
- Aggregate functions with `GROUP BY`
- Window functions: `RANK()`, `ROW_NUMBER()`, `LAG()`, `LEAD()`
- `DATEDIFF` for time-based analysis
- Multi-table `JOIN` (3+ tables)
- Revenue calculation with discount: `UnitPrice * Quantity * (1 - Discount)`

---

## Repository structure

data-analytics-journey/
├── semana-01/          # CTEs, aggregations, subqueries
├── semana-02/          # Window functions, churn analysis
├── semana-03/          # CASE WHEN, business scenarios
├── semana-04/          # Python — Pandas
├── images/             # visual outputs from queries
├── HALLAZGOS.md
├── ANALISIS_CALIDAD_DATOS.md
└── README.md

---

## What's next

- [ ] Python + Pandas: replicate SQL analyses in notebooks
- [ ] Power BI: build a dashboard from Northwind data
- [ ] End-to-end project with a public dataset (Airbnb or similar)

---

*Currently learning and building in public. Open to feedback.*