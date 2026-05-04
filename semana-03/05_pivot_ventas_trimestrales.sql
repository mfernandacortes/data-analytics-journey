-- PIVOT manual de ventas trimestrales por año
-- Transforma filas de trimestres en columnas T1, T2, T3, T4
-- Herramientas: DATEPART + CASE WHEN + SUM + GROUP BY anio
--
/* HALLAZGO: empezó muy bien, tuvo un crecimiento sostenido, 
viendo en montos no parece tan grave...el primer trimestre de 1998 
duplicó sus ventas, que, por lo observado, sea probablemente por una 
liquidación de stock, al otro trimestre cayó la venta a menos de la mitad,
que es donde se termina el dataset.*/

use Northwind;
WITH ventas_trimestrales AS (
	select YEAR(o.OrderDate) as anio, DATEPART(quarter, o.OrderDate) as trimestre,
	SUM(od.Quantity * od.UnitPrice * (1 - Discount)) as Monto
	from Orders o
	JOin [Order Details] od
	ON o.OrderID = od.OrderID
	GROUP BY YEAR(o.OrderDate), DATEPART(quarter, o.OrderDate)

),
pivoteado AS (
    SELECT anio,
        SUM(CASE WHEN trimestre = 1 THEN Monto END) as T1,
        SUM(CASE WHEN trimestre = 2 THEN Monto END) as T2,
        SUM(CASE WHEN trimestre = 3 THEN Monto END) as T3,
        SUM(CASE WHEN trimestre = 4 THEN Monto END) as T4
    FROM ventas_trimestrales
    GROUP BY anio
)
  select * from pivoteado order by anio