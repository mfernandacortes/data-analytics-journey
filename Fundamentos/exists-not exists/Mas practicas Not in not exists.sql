use Northwind;
Select c.CustomerID, c.CompanyName
from Customers c Where c.CustomerID in(
	select o.CustomerID from Orders o
	where c.CustomerID=o.CustomerID)

	SELECT CustomerID, CompanyName
FROM Customers
WHERE CustomerID IN (
    SELECT CustomerID FROM Orders
);
Select c.CustomerID, c.CompanyName
from
Customers c where c.CustomerID
NOT IN(
	select o.CustomerID from Orders o)

Select c.CustomerID, c.CompanyName
from Customers c WHERE
	NOT EXISTS
		(select 1 from Orders o
		where c.CustomerID=o.CustomerID)

--Clientes que compraron chain:
Select c.CustomerID, c.CompanyName 
from Customers c
where not exists(
	select 1 from Orders o
		join [Order Details] od
		ON od.OrderID=o.OrderID
		join Products p
		on 
		p.ProductID=od.ProductID
		where 
		c.CustomerID=o.CustomerID and
		p.ProductName like 'Chai%'
		)

