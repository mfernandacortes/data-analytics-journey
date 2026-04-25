-- Mini proyecto: Top 3 empleados con mejor performance últimos 6 meses
-- Período: diciembre 1997 - mayo 1998
-- Métrica: monto total vendido con descuento aplicado

WITH ventas_por_emp AS (
    SELECT e.EmployeeID, e.LastName, 
        YEAR(o.OrderDate) as anio,
        MONTH(o.OrderDate) as mes,
        SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) as Monto
    FROM Employees e
    JOIN Orders o ON e.EmployeeID = o.EmployeeID
    JOIN [Order Details] od ON o.OrderID = od.OrderID
    WHERE o.OrderDate >= '1997-12-01' AND o.OrderDate < '1998-06-01'
    GROUP BY e.EmployeeID, e.LastName, YEAR(o.OrderDate), MONTH(o.OrderDate)
)
SELECT TOP 3 EmployeeID, LastName, SUM(Monto) as total,
    RANK() OVER (ORDER BY SUM(Monto) DESC) as ranking
FROM ventas_por_emp
GROUP BY EmployeeID, LastName
ORDER BY total DESC