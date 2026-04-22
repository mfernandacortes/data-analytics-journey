use Northwind;
-- Ventas mensuales con variación respecto al mes anterior
-- LAG() trae el valor de la fila anterior dentro de la partición
WITH ventas_mensuales AS (
    SELECT 
        YEAR(o.OrderDate) as anio,
        MONTH(o.OrderDate) as mes,
        SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) as total_ventas
    FROM Orders o
    JOIN [Order Details] od ON o.OrderID = od.OrderID
    GROUP BY YEAR(o.OrderDate), MONTH(o.OrderDate)
)
SELECT 
    anio,
    mes,
    total_ventas,
    LAG(total_ventas) OVER (ORDER BY anio, mes) as ventas_mes_anterior,
    total_ventas - LAG(total_ventas) OVER (ORDER BY anio, mes) as variacion
FROM ventas_mensuales
ORDER BY anio, mes