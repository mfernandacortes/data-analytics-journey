-- Mini proyecto parte 3: Crecimiento vs decrecimiento por categoría
-- Ventas mensuales por categoría usando LAG para ver variación
--
-- HALLAZGO: En mayo 1998 todas las categorías cayeron fuertemente.
-- Beverages: -871 unidades vs mes anterior.
-- Condiments y el resto: caída similar generalizada.
-- CONCLUSIÓN: No es un problema de categoría específica sino del negocio completo.
-- Esto confirma el hallazgo de la parte 2 — la caída de Fuller y King
-- no fue personal, fue una caída general de toda la empresa en ese período.

WITH Productos_vendidos AS (
	select c.CategoryID, c.CategoryName, 
	sum(od.Quantity) as tot_prod,
	YEAR(o.OrderDate) as anio,
	MONTH(o.OrderDate) as mes
	FROM Categories c
	JOIN Products p
	ON c.CategoryID = p.CategoryID
	JOIN [Order Details] od
	ON p.ProductID = od.ProductID
	JOIN Orders o
	ON od.OrderID = o.OrderID
	GROUP BY c.CategoryID, c.CategoryName, YEAR(o.OrderDate), MONTH(o.OrderDate)
)
  SELECT CategoryName, tot_prod, anio, mes,
	
  LAG(tot_prod) OVER (PARTITION BY CategoryID
  order by anio, mes) as mes_ant,
  tot_prod - LAG(tot_prod) 
  OVER (PARTITION BY CategoryID
  order by anio, mes) as   
  variación
  FROM Productos_vendidos
  order by CategoryID, anio, mes;