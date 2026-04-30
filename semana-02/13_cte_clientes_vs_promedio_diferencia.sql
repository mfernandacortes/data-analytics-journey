-- Clientes con total gastado vs promedio general
-- Objetivo: ver qué clientes están por encima y por debajo del promedio


/*
Análisis:
Los primeros 3 clientes están parejos con respecto al promedio(14222) ya que los 3 lo superan
en más de 90 mil, ya a partir del cuarto cae abruptamente la diferencia de promedio 
ya que se encuentra en casi 37 mil, o sea el doble del promedio, casi igual que el quinto.Del 6to al 9no están cerca del promedio.Del 9no al 30 por debajo del promedio y 
los restantes 57 clientes la diferencia es negativa con respecto al promedio.

*/

WITH clientes_total_gastado AS (
select c.CustomerID, c.CompanyName, SUM(od.Quantity * UnitPrice * (1 - od.Discount)) as Monto
from Customers c
JOIN Orders o
ON c.CustomerID = o.CustomerID
JOIN [Order Details] od
ON o.OrderID = od.OrderID
group by c.CustomerID, c.CompanyName
)
promedio_gral AS (
    SELECT AVG(Monto) as promedio
    FROM clientes_total_gastado
)
SELECT 
    c.CustomerID, c.CompanyName, c.Monto,
    p.promedio,
    c.Monto - p.promedio as diferencia
FROM clientes_total_gastado c, promedio_gral p
ORDER BY c.Monto DESC


