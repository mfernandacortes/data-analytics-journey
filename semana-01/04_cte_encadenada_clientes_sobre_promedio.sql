-- Clientes que gastaron más que el promedio general
-- CTE 1: calcula el total gastado por cada cliente
-- CTE 2: calcula el promedio general usando el resultado de la CTE 1
-- Filtro final: muestra solo los clientes que superan ese promedio

WITH clientes_may_montos AS (
	select c.CustomerID, c.CompanyName, sum(od.Quantity * od.UnitPrice * (1 - od.Discount)) as Monto
	from Customers c
	join Orders o
	ON c.CustomerID = o.CustomerID
	join [Order Details] od
	ON o.OrderID = od.OrderID
	group by c.CustomerID, c.CompanyName
),
	promedio_gral AS (
		select AVG(Monto) as prom from clientes_may_montos 
)
select * from clientes_may_montos, promedio_gral
	where Monto > prom
