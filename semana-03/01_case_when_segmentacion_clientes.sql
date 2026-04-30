-- Segmentación de clientes por monto total gastado
-- Categorías: VIP (>50.000), Regular (10.000-50.000), Ocasional (<10.000)
-- CASE WHEN permite clasificar datos en categorías dentro del SELECT

use Northwind;
WITH total_gastado_cliente AS (
  select c.CustomerID, c.CompanyName, SUM(od.Quantity * od.UnitPrice * 1- od.Discount) as Monto
  from Customers c
  join Orders o
  on c.CustomerID = o.CustomerID
  join [Order Details] od
  on o.OrderID = od.OrderID
  group by c.CustomerID, c.CompanyName

)
 select 
 CustomerID, CompanyName, Monto,
 case
	when Monto > 50000 then 'VIP'
	when Monto > 10000 and Monto < 50000 then 'Regular'
	when Monto < 10000 then 'Ocasional'
 end as categoria_cliente 
 from total_gastado_cliente
 order by categoria_cliente desc, Monto desc;

-- ANÁLISIS: 5 VIP, 35 Regular, 45 Ocasionales
-- Brecha entre VIP y Regular: 83.378 vs 24.165
/* Estrategia: 
Estrategia:
concentrarme en los 5 vip para duplicar ventas, algunas promos para regulares, 
y alguna estrategia para aumentar los vip elegir los primeros regulares para que puedan ser vip, 
para eso hay que ver el contexto de los regulares para saber si es posible...*/