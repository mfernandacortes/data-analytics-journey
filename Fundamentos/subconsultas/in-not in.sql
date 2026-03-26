use Northwind;
--lista de clientes que hicieron pedidos

Select c.CustomerID, c.CompanyName from Customers c
	where c.CustomerID in(select o.CustomerID from Orders o)

select c.CompanyName from Customers c where c.CustomerID
	not in(select o.CustomerID from Orders o)

Select ProductName, AVG(UnitPrice) as prom
from Products 
where UnitPrice > AVG(UnitPrice)


Select ProductID, ProductName, AVG(UnitPrice) as prom
from Products  where (select UnitPrice > prom from Products)

Select ProductID, ProductName, UnitPrice
from Products
where UnitPrice > (
    select AVG(UnitPrice)
    from Products
)

select o.OrderID from Orders o
where o.OrderID > (select sum(od.quantity) as cantidades from [Order Details] od
			group by o.OrderID
			order by cantidades desc)
			

select o.OrderID
from Orders o
where (
    select sum(od.Quantity)
    from [Order Details] od
    where od.OrderID = o.OrderID
) > 100