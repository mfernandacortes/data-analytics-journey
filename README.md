# Data Analytics Journey

SQL, Python and BI practice with business-oriented data analysis.  
Focus: writing queries and analyses that answer real business questions, not just technical exercises.

---

## Featured projects

| Project | What it shows | Tools |
| --- | --- | --- |
| [AdventureWorks sales analysis](./adventureworks/) | Three business questions on a bike-company database: who buys, what sells, how much and when. Includes an ERD and written findings. | SQL Server · Python · Pandas |
| [Consumer protection complaints dashboard](https://github.com/mfernandacortes/defensoria-consumidor-powerbi) | Analysis of 33,000+ consumer complaints (2019 vs. 2020) | Power BI · DAX |
| [Northwind with Pandas](https://github.com/mfernandacortes/northwind-pandas) | Multi-table merges, groupby, pivots and a reproducible pipeline | Python · Pandas |
| [Northwind dashboard](https://github.com/mfernandacortes/northwind-powerbi-sql) | SQL queries plus a Power BI dashboard on sales performance | SQL Server · Power BI |
| [Burnout analytics dashboard](https://github.com/mfernandacortes/burnout-analytics-powerbi) | Dashboard with README and screenshots | Power BI |

---

## About this project

This repository documents my learning journey into data analytics.

I started with SQL on the Northwind database, then moved to Python and Pandas, statistics and dashboards. I practice not only syntax, but also understanding the data and extracting insights from a business perspective. The goal is to move from technical exercises to analytical thinking.

**Stack:** SQL Server · Python (Pandas) · Power BI · Git

---

## What I've built

| Block | Topics | Business focus |
| --- | --- | --- |
| [Week 1](./semana-01/) | CTEs, chained CTEs, subqueries, aggregations | Sales performance by employee and customer |
| [Week 2](./semana-02/) | Window functions: RANK, ROW_NUMBER, LAG, LEAD | Customer behavior, churn signals, ranking analysis |
| [Week 3](./semana-03/) | CASE WHEN, conditional logic | Returns analysis, business rules and classification |
| [Week 4](./semana-04/) | Python and Pandas | Replicating SQL analyses in notebooks |
| [AdventureWorks](./adventureworks/) | JOINs across schemas, composite keys, monthly pivots | Customers, products and sales over time |

---

## Findings

Detailed analyses: [HALLAZGOS.md](./HALLAZGOS.md) · Data quality notes: [ANALISIS_CALIDAD_DATOS.md](./ANALISIS_CALIDAD_DATOS.md)

---

## Techniques covered

- Common Table Expressions (CTEs): single and chained
- Subqueries in `WHERE` and `FROM`
- Aggregate functions with `GROUP BY`
- Window functions: `RANK()`, `ROW_NUMBER()`, `LAG()`, `LEAD()`
- Multi-table `JOIN` (3+ tables) and `LEFT JOIN` to find missing matches
- Pandas: `merge`, `groupby`, `agg`, `pivot_table`, `apply`
- Revenue calculation with discount: `UnitPrice * Quantity * (1 - Discount)`
- Reading schemas: composite keys and bridge tables

---

## Repository structure

```
data-analytics-journey/
├── semana-01/ ... semana-04/   # SQL and Pandas, week by week
├── Fundamentos/                # SQL fundamentals
├── python-basico/              # Python basics
├── pandas-intermedio/          # Pandas, intermediate
├── pandas-avanzado/            # Pandas, advanced and pivots
├── repaso/                     # review exercises
├── adventureworks/             # AdventureWorks project
├── english-practice/           # English practice for remote work
├── images/                     # visual outputs from queries
├── HALLAZGOS.md
├── ANALISIS_CALIDAD_DATOS.md
└── README.md
```

---

## What's next

- [x] Python + Pandas: replicate SQL analyses in notebooks
- [x] Power BI: build a dashboard from Northwind data
- [x] End-to-end project with a public dataset
- [ ] Compare same-period sales in AdventureWorks (Jan-Jun 2024 vs. 2025)
- [ ] Data modeling: design a star schema for sales

---

*Currently learning and building in public. Open to feedback.*
