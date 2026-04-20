-- Ranking de productos por cantidad vendida dentro de cada categoría
-- RANK() OVER (PARTITION BY CategoryName): rankea dentro de cada categoría
-- CTE previa necesaria porque Window Functions no conviven con GROUP BY


WITH productos_mas_vendidos AS (
    SELECT p.ProductID, p.ProductName, c.CategoryName, 
           SUM(od.Quantity) as tot_prod 
    FROM Products p
    JOIN Categories c ON p.CategoryID = c.CategoryID
    JOIN [Order Details] od ON od.ProductID = p.ProductID
    GROUP BY p.ProductID, p.ProductName, c.CategoryName
),
ranking_productos AS (
    SELECT *,
        RANK() OVER (PARTITION BY CategoryName ORDER BY tot_prod DESC) as ranking
    FROM productos_mas_vendidos
)
SELECT * FROM ranking_productos
ORDER BY CategoryName, ranking