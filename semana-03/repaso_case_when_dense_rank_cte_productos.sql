/*Mostrá los 5 productos más vendidos por categoría usando DENSE_RANK, y clasificá cada producto como "Estrella"
 si está en el top 1 de su categoría, normal si está en el 2 o 
"Secundario" si está en el 3 al 5.*/

WITH cant_prod_vend AS (
    SELECT c.CategoryID,
           c.CategoryName,
           p.ProductID,
           p.ProductName,
           SUM(od.Quantity) AS Cantidad
    FROM Categories c
    JOIN Products p
        ON c.CategoryID = p.CategoryID
    JOIN [Order Details] od
        ON p.ProductID = od.ProductID
    GROUP BY c.CategoryID,
             c.CategoryName,
             p.ProductID,
             p.ProductName
),

ranking_prod AS (
    SELECT CategoryID,
           CategoryName,
           ProductID,
           ProductName,
           Cantidad,
           DENSE_RANK() OVER (
               PARTITION BY CategoryID
               ORDER BY Cantidad DESC
           ) AS ranking
    FROM cant_prod_vend
),

clasificacion AS (
    SELECT CategoryName,
           ProductName,
           Cantidad,
           ranking,
           CASE
               WHEN ranking = 1 THEN 'Estrella'
               WHEN ranking BETWEEN 3 AND 5 THEN 'Secundario'
               ELSE 'Normal'
           END AS Clasificacion
    FROM ranking_prod
)

SELECT CategoryName,
       ProductName,
       Cantidad,
       ranking,
       Clasificacion
FROM clasificacion
WHERE ranking <= 5;

