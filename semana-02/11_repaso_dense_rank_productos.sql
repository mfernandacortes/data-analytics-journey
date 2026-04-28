-- Repaso Window Functions: DENSE_RANK por categoría
-- Top 5 productos por monto vendido dentro de cada categoría
-- PARTITION BY CategoryID: rankea dentro de cada categoría
-- WHERE ranking <= 5: filtra top 5 de cada categoría (no 5 en total)
-- Error frecuente detectado: ON p.CategoryID = p.CategoryID une Products consigo misma

use Northwind;
WITH monto_total_prod AS (
	select p.ProductID, p.ProductName, c.CategoryID, c.CategoryName,
	sum(od.Quantity * od.UnitPrice * (1 - od.Discount)) AS Monto
	from Products p
	join Categories c
	ON c.CategoryID = p.CategoryID
	join [Order Details] od 
	ON p.ProductID = od.ProductID
	group by p.ProductID, p.ProductName, c.CategoryID, c.CategoryName
), 
   ranking_prod AS (
	select ProductID, ProductName, CategoryID, CategoryName, Monto,
	DENSE_RANK() OVER(PARTITION BY CategoryID order by Monto desc) as ranking
	from monto_total_prod
)
  select ProductID, ProductName, CategoryName, Monto, ranking
	from ranking_prod
	where ranking <= 5
	order by CategoryID, ranking;