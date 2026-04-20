-- Historial de pedidos por cliente numerados por fecha
-- ROW_NUMBER() OVER (PARTITION BY CustomerID): numeración independiente por cliente
-- El número 1 es el pedido más reciente de cada cliente

select c.CustomerID, c.CompanyName,
o.OrderID, o.OrderDate,
RANK() OVER (PARTITION BY c.CustomerID ORDER BY o.OrderDate desc) as ranking_clientes
from Customers c
join Orders o
On c.CustomerID = o.CustomerID