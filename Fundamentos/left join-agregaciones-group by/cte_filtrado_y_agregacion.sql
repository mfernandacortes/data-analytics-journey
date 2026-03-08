use Northwind;
WITH ventas_por_cliente AS (
    SELECT 
        o.CustomerID,
        SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS total
    FROM Orders o
    JOIN [Order Details] od 
        ON o.OrderID = od.OrderID
    GROUP BY o.CustomerID
)

SELECT 
    MAX(total) AS max_venta,
    MIN(total) AS min_venta,
    AVG(total) AS promedio
FROM ventas_por_cliente;

WITH logica_ventas AS (
	SELECT CustomerID,
    count(*) AS cant_pedidos
	FROM Orders 
    GROUP BY CustomerID
    )
    select * 
    from logica_ventas
    where cant_pedidos > 5

    Mostrar los pedidos realizados después de 1997

WITH ventas_cte as (
	select OrderID, CustomerID, OrderDate
	from Orders
    group by OrderDate
    )
    select * 
    from ventas_cte 
    where OrderDate > '1997-12-31';

WITH nombre_cte AS (
    SELECT columnas
    FROM tabla
    WHERE condicion_opcional
)
SELECT columnas
FROM nombre_cte
WHERE otra_condicion;
🧠 Traducido a lenguaje humano

👉 Siempre pensalo así:

WITH → defino una “tabla lógica”
SELECT final → la uso
📌 Tu ejemplo completo (bien armado)

Usando Northwind

;WITH pedidos AS (
    SELECT 
        OrderID,
        CustomerID,
        OrderDate
    FROM Orders
)
SELECT *
FROM pedidos
WHERE OrderDate > '1997-01-01';

WITH pedidos AS (
    SELECT 
        OrderID,
        CustomerID,
        OrderDate
    FROM Orders
)
SELECT *
FROM pedidos
WHERE OrderDate > '1997-01-01';