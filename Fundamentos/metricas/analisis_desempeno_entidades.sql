use Northwind;
Select top 5 WITH TIES p.ProductID, p.ProductName, sum(od.quantity) as total_vendido
From Products p
Join
[Order Details] od
ON p.ProductID=od.ProductID
Group by p.ProductID, p.ProductName
Order by total_vendido desc

Select e.LastName, e.FirstName, count(o.OrderID) as cantidadPedidosEmp
From Orders o
Join
Employees e
ON o.EmployeeID=e.EmployeeID
Group by e.EmployeeID, e.LastName, e.FirstName
Order by cantidadPedidosEmp desc

Select c.CustomerID, c.CompanyName
From Customers c
Left join
Orders o
ON c.CustomerID=o.CustomerID
where o.OrderID is null


select p.ProductID, p.ProductName 
from Products p
where not exists(
		select 1 from [Order Details] od
			where p.ProductID=od.ProductID)

