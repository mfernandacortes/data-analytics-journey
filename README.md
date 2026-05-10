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

## Key findings

### Churn signal detected — Customer ALFKI
*(File: [semana-02/05_lag_dias_entre_pedidos_clientes.sql](https://github.com/mfernandacortes/data-analytics-journey/blob/main/semana-02/05_lag_dias_entre_pedidos_clientes.sql))*


Using `LAG` and `DATEDIFF` to calculate days between orders per customer,  
I found an unusual pattern for customer **Alfred Futterkiste (ALFKI)**:

- In 1997: orders every 10–60 days (normal behavior)
- Between April 1998 and January 1999: **gap of almost 1 year**
- January 1999 was their **last order ever**

> This kind of gap is a classic churn signal.  
> Next question I'd investigate: *Did the assigned sales rep change before the gap started?*

This is the type of insight that matters in a real business context —  
a dashboard showing total orders would never catch it.

---

### Data quality issue — orphan order detected
*(File: [ANALISIS\_CALIDAD\_DATOS.md](./ANALISIS_CALIDAD_DATOS.md))*

During sales analysis I found an inconsistency between volume metrics and revenue:  
one order existed in `Orders` but had no rows in `Order Details`.

**Why it happens:** Northwind's referential integrity is one-directional.  
`Order Details` has a FK to `Orders` — but `Orders` has no constraint requiring details.  
Result: an order can exist with zero revenue contribution.

**Business impact:** Any dashboard comparing order count vs. revenue  
will show numbers that don't add up — without this validation, the discrepancy is invisible.

Full analysis → [ANALISIS\_CALIDAD\_DATOS.md](./ANALISIS_CALIDAD_DATOS.md)

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

```

data-analytics-journey/
├── semana-01/          # CTEs, aggregations, subqueries
├── semana-02/          # Window functions, churn analysis
├── semana-03/          # CASE WHEN, business scenarios
├── images/             # visual outputs from queries
├── ANALISIS_CALIDAD_DATOS.md
└── README.md
```

---

## What's next

- [ ] Python + Pandas: replicate SQL analyses in notebooks
- [ ] Power BI: build a dashboard from Northwind data
- [ ] End-to-end project with a public dataset (Airbnb or similar)

---

*Currently learning and building in public. Open to feedback.*
