use Northwind;
Select top 5 c.CompanyName, 
SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS tot
from Customers c
inner join Orders o
on c.CustomerID=o.CustomerID
inner join [Order Details] od
on o.OrderID=od.OrderID


group by c.CustomerID, CompanyName

order by tot desc

select * from [Order Details]