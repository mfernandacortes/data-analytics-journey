-- Pedidos por empleado clasificados en urgentes (<=3 días), normales (>3 días) y sin enviar (ShippedDate NULL)
-- Hallazgo: Peacock tiene 5 pedidos sin enviar — investigar causa: stock, cobranza o política de envío

select e.EmployeeID, e.LastName, count(o.OrderID) as Total_pedidos,
SUM(CASE WHEN (DATEDIFF(day, o.OrderDate, o.ShippedDate) <= 3) THEN 1 ELSE 0 END) as Pedidos_urgentes,
SUM(CASE WHEN (DATEDIFF(day, o.OrderDate, o.ShippedDate) > 3) THEN 1 ELSE 0 END) as Pedidos_normales,
SUM(CASE WHEN ShippedDate IS NULL THEN 1 ELSE 0 END) as Pedidos_sin_enviar

from Employees e
join Orders o
on e.EmployeeID = o.EmployeeID
group by e.EmployeeID, e.LastName



