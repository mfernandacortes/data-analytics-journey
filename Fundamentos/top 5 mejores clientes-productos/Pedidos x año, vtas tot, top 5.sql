use Northwind;

Select YEAR(o.OrderDate) as anio, count(o.OrderID) as tot_ped_anio
From Orders o
Group by YEAR(o.OrderDate)
Order by tot_ped_anio desc

SELECT 
    SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) AS TotalVentas
FROM [Order Details] od;

SELECT *
FROM Orders
--join [Order Details] od on Orders.OrderID = od.OrderID
WHERE YEAR(OrderDate) = 1999
Select top 5 WITH TIES p.ProductID, p.ProductName, sum(od.quantity) as total_vendido
From Products p
Join
[Order Details] od
ON p.ProductID=od.ProductID
Group by p.ProductID, p.ProductName
Order by total_vendido desc
