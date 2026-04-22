use Northwind;
-- Ventas mensuales con variación respecto al mes anterior
-- LAG() trae el valor de la fila anterior dentro de la partición


WITH ventas_mensuales AS (
    SELECT 
        e.EmployeeID, 
        e.LastName, 
        YEAR(o.OrderDate) AS anio, 
        MONTH(o.OrderDate) AS mes,
        SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) AS ventas_totales
    FROM Employees e
    JOIN Orders o ON e.EmployeeID = o.EmployeeID
    JOIN [Order Details] od ON o.OrderID = od.OrderID
    GROUP BY 
        e.EmployeeID, 
        e.LastName,
        YEAR(o.OrderDate), 
        MONTH(o.OrderDate)
)

SELECT
    EmployeeID,
    LastName,
    anio,
    mes,
    ventas_totales,
    LAG(ventas_totales) OVER (
        PARTITION BY EmployeeID 
        ORDER BY anio, mes
    ) AS mes_anterior,
    ventas_totales - LAG(ventas_totales) OVER (
        PARTITION BY EmployeeID 
        ORDER BY anio, mes
    ) AS variacion
FROM ventas_mensuales
ORDER BY EmployeeID, anio, mes;