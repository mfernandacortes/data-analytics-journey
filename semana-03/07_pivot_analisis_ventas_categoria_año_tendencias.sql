-- Ventas anuales por categoría con PIVOT y clasificación de tendencia
-- PIVOT: una columna por año (1996, 1997, 1998)
-- CASE WHEN: clasifica como En crecimiento o En declive comparando A1 vs A3
--
-- HALLAZGO: Todas las categorías están En crecimiento comparando 1996 vs 1998
-- A2 (1997) fue el pico máximo — A3 (1998) parece menor pero el dataset
-- termina en mayo 1998, no es un año completo
-- Si 1998 fuera año completo probablemente superaría a 1997


use Northwind;

WITH ventas_por_categoria AS (
	select YEAR(o.OrderDate) as anio,
	c.CategoryID, c.CategoryName,
	SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) as Monto
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
    SELECT CategoryID, CategoryName,
        SUM(CASE WHEN anio = 1996 THEN Monto END) as A1,
        SUM(CASE WHEN anio = 1997 THEN Monto END) as A2,
        SUM(CASE WHEN anio = 1998 THEN Monto END) as A3
        
    FROM ventas_por_categoria
    GROUP BY CategoryID, CategoryName
), 
 clasificacion AS (
    SELECT CategoryID, CategoryName, A1, A2, A3,
        CASE
            WHEN A3 > A1 THEN 'En crecimiento'
            WHEN A3 < A1 THEN 'En declive'
            ELSE 'Estable'
        END AS tendencia
    FROM pivoteado
)
SELECT * FROM clasificacion
ORDER BY tendencia, CategoryName