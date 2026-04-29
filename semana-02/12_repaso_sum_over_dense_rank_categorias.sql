-- Repaso Window Functions: DENSE_RANK + SUM() OVER() por categoría
-- Top 5 productos por monto vendido dentro de cada categoría
-- monto_categoria: total de toda la categoría repetido en cada fila
-- HALLAZGO: Côte de Blaye domina Beverages con 141396 vs 23526 del segundo
-- Diferencia del 501% — producto estrella que concentra las ventas de su categoría
-- Ordenado por monto_categoria DESC para ver primero la categoría más vendida

use Northwind;

WITH monto_por_prod AS (
  select c.CategoryID, c.CategoryName, p.ProductID, p.ProductName, SUM(od.Quantity * od.UnitPrice * (1-od.Discount)) 
  as Monto_prod
from Categories c
join Products p
ON c.CategoryID = p.CategoryID
join [Order Details] od
ON p.ProductID = od.ProductID
group by c.CategoryID, c.CategoryName, p.ProductID, p.ProductName

),
  ranking_prod_cat AS (
	select CategoryID, CategoryName, ProductID, ProductName, Monto_prod,
	DENSE_RANK() over(partition by CategoryID order by Monto_prod desc) as ranking,
	SUM(Monto_prod) OVER (PARTITION BY CategoryID) as monto_categoria
	from monto_por_prod
)
  select * from ranking_prod_cat where ranking <=5
  ORDER BY monto_categoria DESC, ranking