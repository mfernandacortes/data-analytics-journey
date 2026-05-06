

WITH ventas_por_categoria AS (
	select YEAR(o.OrderDate) as anio,
	c.CategoryID, c.CategoryName,
	SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) as Monto --cálculo del monto vendido
	from Orders o
	join [Order Details] od
	ON o.OrderID = od.OrderID
	join Products p
	on od.ProductID = p.ProductID
	join Categories c
	on c.CategoryID= p.CategoryID
	group by YEAR(o.OrderDate), c.CategoryID, c.CategoryName
),
  pivoteado AS (
     --son 3 columnas, una por año y las llama A1, A2, A3
      SELECT CategoryID, CategoryName,
        SUM(CASE WHEN anio = 1996 THEN Monto END) as A1,
        SUM(CASE WHEN anio = 1997 THEN Monto END) as A2,
        SUM(CASE WHEN anio = 1998 THEN Monto END) as A3    
     FROM ventas_por_categoria
     GROUP BY CategoryID, CategoryName
),   
 clasificacion AS (
    --ahora se necesita otra CTE para poder clasificar la columna del último año 
    --donde coteja con el primer año
    SELECT CategoryID, CategoryName, A1, A2, A3,
        CASE
            WHEN A3 > A1 THEN 'En crecimiento'
            WHEN A3 < A1 THEN 'En declive'
            ELSE 'Estable'
        END AS tendencia
    FROM pivoteado
)
   SELECT CategoryID, CategoryName, A1, A2, A3, tendencia
   FROM clasificacion
   ORDER BY tendencia, CategoryName