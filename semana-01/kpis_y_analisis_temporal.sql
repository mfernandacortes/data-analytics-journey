-- ========================================
--  KPIs Y ANÁLISIS TEMPORAL
-- ========================================
-- Consultas orientadas a indicadores clave del negocio:
--
-- - ventas totales (ingresos reales con descuento)
-- - cantidad total de pedidos
-- - pedidos por cliente
-- - clientes activos en un período
-- - evolución de ventas por año
--
-- Se utilizan funciones de agregación (SUM, COUNT, COUNT DISTINCT)
-- y funciones de fecha para análisis temporal.
-- ========================================

use Northwind;
Select SUM(od.Quantity * od.UnitPrice * (1-od.discount)) as vtastot
From Orders o
Join 
[Order Details] od
ON o.OrderID=od.OrderID


select count(*) as total_pedidos
from orders 


Select count(*) as total
From Orders o
Join Customers c
ON o.CustomerID=c.CustomerID
Group by c.CustomerID, c.CompanyName
Order by total desc

SELECT COUNT(*) AS total_pedidos
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE o.OrderDate >= '1997-12-31'  -- últimos 12 meses
GROUP BY c.CustomerID, c.CompanyName
ORDER BY total_pedidos DESC;

Select year(o.orderDate) as anio, SUM(od.Quantity * od.UnitPrice * (1-od.discount)) as tot_anio
From Orders o
Join 
[Order Details] od
ON o.OrderID=od.OrderID
Group by  year(o.OrderDate)
Order by tot_anio desc

Select year(o.orderDate) as anio, 
SUM(od.Quantity * od.UnitPrice * (1-od.discount)) as tot_anio 
From Orders o Join [Order Details] od ON o.OrderID=od.OrderID 
Group by year(o.OrderDate) Order by tot_anio desc

Use Northwind
SELECT COUNT(DISTINCT CustomerID)
FROM Orders

SELECT COUNT(DISTINCT c.CustomerID) AS ClientesActivos
FROM Customers c
JOIN Orders o
    ON c.CustomerID = o.CustomerID
WHERE o.OrderDate >= '1997-01-01'
  AND o.OrderDate <= '1997-12-31';
