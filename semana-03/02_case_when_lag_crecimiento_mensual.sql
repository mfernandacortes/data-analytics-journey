-- Ventas mensuales clasificadas como Crecimiento, Caída o Igual
-- Combina LAG (mes anterior) con CASE WHEN (clasificación)
-- Sin PARTITION BY porque es una sola línea de tiempo de toda la empresa
-- HALLAZGO: debajo de la query.

use Northwind;

WITH ventas_por_mes AS (
  select
  YEAR(o.OrderDate) as anio,
  MONTH(o.OrderDate) as mes,
  SUM(od.Quantity * od.UnitPrice * 1 - od.Discount) as Monto
  from Orders o 
  join [Order Details] od
  ON o.OrderID = od.OrderID
  group by YEAR(o.OrderDate), MONTH(o.OrderDate) --recordar que acá no va alias, sino la función completa
),
 ver_crecimiento AS (
  select 
  anio, mes, Monto,
  LAG(Monto) over (order by anio, mes) AS mes_anterior
  from ventas_por_mes  --en lag en este caso no necesito partition by porque quiero comparar con las ventas del mes anterior sin agrupar ni x empleado ni x nada...--
  )
  select 
     anio, mes, Monto, mes_anterior,
     CASE
	WHEN Monto > mes_anterior THEN 'Crecimiento'
	WHEN Monto  < mes_anterior THEN 'Caida'
	WHEN Monto  = mes_anterior THEN 'Igual'
     END AS crecimiento
     from ver_crecimiento
     Order by anio, mes

/*
Fueron 15 meses de crecimiento y 7 de caída,
en sí, por lo que se ve, hay dos meses consecutivos
de caída y se recupera, luego hay unos meses (5 meses contínuos) 
de crecimiento, luego dos de caída, y vuelve el crecimiento,
fluctúa así.
Agosto muestra caída en ambos años disponibles, pero el dataset es insuficiente para confirmar estacionalidad.
Se requieren más períodos para validar el patrón.
*/
