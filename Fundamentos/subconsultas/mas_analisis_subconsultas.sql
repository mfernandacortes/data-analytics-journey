-- ========================================
--  ANÁLISIS DE VENTAS Y MÉTRICAS
-- ========================================
-- Consultas orientadas a análisis de negocio sobre la base Northwind.
-- Incluye:
-- - cantidad de pedidos por cliente y empleado
-- - cálculo de ingresos reales (considerando descuentos)
-- - productos más y menos vendidos
-- - clientes con y sin actividad
-- - análisis temporal (por año)
-- - promedios de precios
--
-- Se utilizan funciones de agregación (COUNT, SUM, AVG)
-- y diferentes tipos de JOIN y subconsultas.
-- ========================================

--total pedidos por cliente
use Northwind;
Select c.CompanyName, count(*) as total
From Orders o
Join Customers c
ON o.CustomerID=c.CustomerID
Group by c.CustomerID, c.CompanyName
Order by total desc

--total gastado por cliente:
Select c.CustomerID, c.CompanyName, SUM(od.quantity * od.UnitPrice * (1 - od.Discount)) as subtotal
From [Order Details] od
Join Orders o
ON od.OrderID=o.OrderID
Join Customers c
ON c.CustomerID=o.CustomerID
Group by c.CustomerID, c.CompanyName
Order by subtotal desc

Select c.CustomerID, c.CompanyName
From Customers c
Left join
Orders o
ON c.CustomerID=o.CustomerID
where o.OrderID is null

Select top 5 WITH TIES p.ProductID, p.ProductName, sum(od.quantity) as total_vendido
From Products p
Join
[Order Details] od
ON p.ProductID=od.ProductID
Group by p.ProductID, p.ProductName
Order by total_vendido desc

select p.ProductID, p.ProductName 
from Products p
where not exists(
		select 1 from [Order Details] od
			where p.ProductID=od.ProductID)

Select AVG(p.UnitPrice) as promedio_precios
From Products p
Order by promedio_precios asc



Select p.CategoryID, AVG(p.UnitPrice) as promedio_por_cate
From Products p
Group by p.CategoryID

Select YEAR(o.OrderDate) as anio, count(o.OrderID) as tot_ped_anio
From Orders o
Group by YEAR(o.OrderDate)
Order by tot_ped_anio desc

Select YEAR(o.ShippedDate) as anio, count(o.OrderID) as tot_hechos_anio
From Orders o 

Group by YEAR(o.ShippedDate)
Order by tot_hechos_anio desc

Select year(o.orderDate) as anio, SUM(od.Quantity * od.UnitPrice * (1-od.discount)) as tot_anio
From Orders o
Join 
[Order Details] od
ON o.OrderID=od.OrderID
Group by  year(o.OrderDate)
Order by tot_anio desc

SELECT *
FROM Orders
WHERE EmployeeID IS NULL;


Select e.LastName, e.FirstName, count(o.OrderID) as cantidadPedidosEmp
From Orders o
Join
Employees e
ON o.EmployeeID=e.EmployeeID
Group by e.EmployeeID, e.LastName, e.FirstName
Order by cantidadPedidosEmp desc

Select e.LastName, e.FirstName, sum(od.Quantity * od.UnitPrice * (1-od.discount)) as tot_vtas_emp
From Employees e
Join Orders o ON e.EmployeeID=o.EmployeeID
join [Order Details] od ON o.OrderID=od.OrderID
Group by e.EmployeeID, e.LastName, e.FirstName
Order by tot_vtas_emp desc

SELECT e.LastName, e.FirstName, 
       SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) AS tot_vtas_emp
FROM Employees e
JOIN Orders o ON e.EmployeeID = o.EmployeeID
JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY e.EmployeeID, e.LastName, e.FirstName
ORDER BY tot_vtas_emp DESC;



