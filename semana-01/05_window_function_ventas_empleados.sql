-- Ventas por empleado con porcentaje sobre el total general
-- Window Function: SUM() OVER () calcula el total general sin colapsar filas
-- No se puede mezclar Window Function con GROUP BY en SQL Server
-- Solución: CTE previa para agrupar, Window Function en el SELECT final

WITH ventas_por_empleado AS (
...
WITH ventas_por_empleado AS (
    SELECT 
        e.EmployeeID, e.LastName,
        SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) as total_empleado
    FROM Employees e
    JOIN Orders o ON e.EmployeeID = o.EmployeeID
    JOIN [Order Details] od ON o.OrderID = od.OrderID
    GROUP BY e.EmployeeID, e.LastName
)
SELECT 
    EmployeeID, LastName, total_empleado,
    SUM(total_empleado) OVER () as total_general,
    (total_empleado / SUM(total_empleado) OVER ()) * 100 as porcentaje
FROM ventas_por_empleado
order by total_empleado desc;
