use Northwind;
with ventas_totales AS(

	SELECT c.CustomerID, c.CompanyName, SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) as Monto
	FROM Customers c
	join
	Orders o
	on c.CustomerID=o.CustomerID
	join [Order Details] od
	on o.OrderID=od.OrderID
	group by c.CustomerID, c.CompanyName

)
	select * from ventas_totales where Monto > 10000


with pedidos_empleados AS(
	SELECT e.EmployeeID, e.LastName, count(o.OrderID) as pedido_emp
	from Employees e
	join Orders o
	on e.EmployeeID=o.EmployeeID
	group by e.EmployeeID, e.LastName, e.FirstName
)
	SELECT * from pedidos_empleados where pedido_emp > 50
	order by pedido_emp desc

with productos_prom AS(
	SELECT c.CategoryID, c.CategoryName, AVG(p.UnitPrice) as promedio
	from Products p
	join Categories c
	On p.CategoryID=c.CategoryID
	group by c.CategoryID, c.CategoryName
)
	select * from productos_prom where promedio > 30