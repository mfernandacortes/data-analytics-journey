

use Northwind;
WITH reporte_integrador AS (
    SELECT 
        e.EmployeeID, e.LastName,
        c.CategoryID, c.CategoryName,
        YEAR(o.OrderDate) as anio,
        MONTH(o.OrderDate) as mes,
        SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) as Monto
    FROM Employees e
    JOIN Orders o ON e.EmployeeID = o.EmployeeID
    JOIN [Order Details] od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    JOIN Categories c ON p.CategoryID = c.CategoryID
    WHERE o.OrderDate >= '1997-12-01' AND o.OrderDate < '1998-06-01'
    AND e.EmployeeID IN (2, 4, 7)
    GROUP BY e.EmployeeID, e.LastName, c.CategoryID, c.CategoryName, 
             YEAR(o.OrderDate), MONTH(o.OrderDate)
)
SELECT 
    EmployeeID, LastName, CategoryName, anio, mes, Monto,
    LAG(Monto) OVER (PARTITION BY EmployeeID, CategoryID ORDER BY anio, mes) as mes_anterior,
    Monto - LAG(Monto) OVER (PARTITION BY EmployeeID, CategoryID ORDER BY anio, mes) as variacion
FROM reporte_integrador
ORDER BY EmployeeID, CategoryName, anio, mes