--Mostrá el top 3 de clientes que más gastaron en total:
-- Nota: TOP 3 + ORDER BY es suficiente acá, RANK no es necesario

Select top 3 c.CustomerID, c.CompanyName, SUM(od.Quantity * od.UnitPrice) * (1 - od.Discount)) as Monto 

from Customers c
Join Orders o
ON c.CustomerID = o.CustomerID
join [Order Details] od
ON o.OrderID = od.OrderID
group by c.CustomerID, c.CompanyName
order by Monto desc