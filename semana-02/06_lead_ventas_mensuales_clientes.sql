-- Ventas mensuales por cliente con mes siguiente usando LEAD
-- LEAD() mira la fila siguiente dentro de la partición
-- NULL en mes_siguiente = último mes de compra del cliente
-- Confirma el hallazgo de LAG: ALFKI no volvió a comprar después de abril 1998



WITH ventas_mens AS (
	select c.CustomerID, c.CompanyName, count(o.OrderID) as pedidos,
	YEAR(o.OrderDate) as anio,
	MONTH(o.OrderDate) as mes
	from Customers c
	join Orders o
	ON c.CustomerID = o.OrderID
	group by c.CustomerID, c.CompanyName

)

select c.CompanyName, anio, mes, LEAD(pedidos) OVER (
	PARTITION BY CustomerID
	ORDER BY anio, mes
	) as mes_anterior,
	pedidos - LAG(pedidos) OVER(
	PARTITION BY CustomerID
	order by anio, mes
) AS variacion

FROM ventas_mens 
order by CustomerID, anio, mes
