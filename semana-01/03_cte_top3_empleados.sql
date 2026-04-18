-- Objetivo: obtener los 3 empleados con más órdenes gestionadas
-- Herramienta: CTE + TOP 3 con ORDER BY
WITH cantidad_ordenes AS (
    select e.EmployeeID, e.LastName, count(o.OrderID) as pedidos
    from Employees e
    join Orders o
    ON e.EmployeeID = o.EmployeeID
    group by e.EmployeeID, e.LastName
)    
    select top 3 LastName, pedidos from cantidad_ordenes
    order by pedidos desc
