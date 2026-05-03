-- Ventas trimestrales con crecimiento porcentual respecto al trimestre anterior
-- Herramientas: DATEPART + LAG + cálculo de porcentaje
--
/*HALLAZGO: según el dataset este negocio arrancó fuerte...el primer trimestre 
tuvo un gran crecimiento del 68%,  luego el crecimiento en el año 97 se estabilizó 
pero quedó en número bajo con respecto al 96 , ya que como máximo creció el 17 % el último trimestre. 
En 1998 el primer trimestre tuvo un gran crecimiento, del 62% pero una caída grande (50%) 
al próximo trimestre que es cuando termina el dataset. Estos números podrían indicar cierre de la empresa, 
el crecimiento del trimestre anterior podría deberse a liquidación de stock, quizás haya sido una decisión
por el bajo crecimiento de 1997.*/

use Northwind;
WITH ventas_totales AS (
	SELECT YEAR(o.OrderDate) as anio, DATEPART(quarter, o.OrderDate) as trimestre,
	SUM(od.Quantity * od.UnitPrice * 1 - od.Discount) as Monto
	FROM Orders o 
	JOIN [Order Details] od
	ON o.OrderID = od.OrderID
	GROUP BY YEAR(o.OrderDate), DATEPART(quarter, o.OrderDate)

), trim_ant AS (
	select anio, trimestre, Monto,
	LAG(Monto) OVER(ORDER BY anio, trimestre) AS trimestre_anterior
	from ventas_totales
), 
   porcentual_crec AS (
	select anio, Monto, trimestre, trimestre_anterior,
	((Monto - trimestre_anterior) / trimestre_anterior * 100) AS porcentual
	from trim_ant
)
   select anio, trimestre, Monto, trimestre_anterior, porcentual
   from porcentual_crec
   order by anio, trimestre;