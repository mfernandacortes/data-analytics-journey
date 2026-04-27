use Northwind;
-- Repaso Window Functions: DENSE_RANK por categoría
-- Top 5 productos más vendidos (por cantidad) dentro de cada categoría
-- WHERE ranking <= 5 filtra los 5 primeros de CADA categoría — no 5 en total
-- Nota: en proceso de automatizar la sintaxis
WITH prod_mas_vendidos AS (
    SELECT p.ProductID, p.ProductName, c.CategoryID, c.CategoryName, 
           SUM(od.Quantity) as cantidad
    FROM Products p
    JOIN Categories c ON c.CategoryID = p.CategoryID
    JOIN [Order Details] od ON p.ProductID = od.ProductID
    GROUP BY p.ProductID, p.ProductName, c.CategoryID, c.CategoryName
), 
ranking_prod AS (
    SELECT ProductID, ProductName, CategoryID, CategoryName, cantidad,  
        DENSE_RANK() OVER (PARTITION BY CategoryID ORDER BY cantidad DESC) as ranking
    FROM prod_mas_vendidos
)
SELECT * FROM ranking_prod
WHERE ranking <= 5
ORDER BY CategoryID, ranking
