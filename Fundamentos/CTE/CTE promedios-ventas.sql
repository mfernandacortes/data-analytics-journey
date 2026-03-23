use Northwind;

WITH total_vtas AS(

	Select c.CustomerID, c.CompanyName, SUM(od.UnitPrice * od.Quantity * (1- od.Discount)) as Monto
	from Customers c
	join Orders o
	on c.CustomerID=o.CustomerID
	join [Order Details] od
	on o.OrderID=od.OrderID
	group by c.CustomerID, c.CompanyName
	
),
promedio_general AS (
	select AVG(Monto) as Promedio
	from total_vtas
)

Select * 
from total_vtas, promedio_general
where Monto > Promedio

WITH total_ventas AS (
	select c.CustomerID, c.CompanyName, SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) as Monto
	from Customers c
	join Orders o
	on c.CustomerID = o.CustomerID
	join [Order Details] od
	on o.OrderID = od.OrderID
	group by c.CustomerID, c.CompanyName
	
),
promedio_general AS (
	select AVG(Monto) as Promedio from total_ventas
),
top_10 AS (
	select top 10 * from total_ventas
	order by Monto desc
)
select * from top_10