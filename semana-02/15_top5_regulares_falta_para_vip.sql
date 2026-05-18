-- ACTUALIZACIÓN: HUNGO (Hungry Owl All-Night Grocers) es el caso más urgente:
-- su monto real es 49.979, le faltan menos de 21 pesos para cruzar el umbral VIP.
-- Cualquier compra mínima lo convierte en VIP inmediatamente.
-- Prioridad 1 dentro del plan piloto de conversión.

use Northwind;
WITH clientes_mas_gastaron AS (
	select c.CustomerID, c.CompanyName, SUM(od.Quantity * od.UnitPrice * (1- od.Discount)) as Monto
	from Customers c
	join Orders o
	ON c.CustomerID = o.CustomerID
	join [Order Details] od
	ON o.OrderID = od.OrderID
	group by c.CustomerID, c.CompanyName
),
  clasificacion_clientes AS (
	select CustomerID, CompanyName, Monto,
	CASE
     	   WHEN Monto < 10000 then 'Ocasional'
           WHEN Monto >= 10000 and Monto <=50000 then 'Regular'
           WHEN Monto > 50000 then 'VIP'
	END AS Clasificacion
	from clientes_mas_gastaron

),
  falta_para_vip AS (
	select top 5 CustomerID, CompanyName, Monto, Clasificacion, (50000 - Monto) as diferencia
	from clasificacion_clientes
	where clasificacion = 'Regular'
	order by Monto desc
)
  select CustomerID, CompanyName, Monto, Clasificacion, diferencia
  from falta_para_vip 