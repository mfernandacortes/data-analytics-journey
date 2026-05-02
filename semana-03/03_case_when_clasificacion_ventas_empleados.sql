
-- QUERY 1: Detalle mensual por empleado
-- (query completa con el detalle)

use Northwind;
WITH ventas_empleados_mes AS (
	select e.EmployeeID, e.LastName, 
	YEAR(o.OrderDate) as anio,
	MONTH(o.OrderDate) as mes,
	sum(od.Quantity * od.UnitPrice * (1 - od.Discount)) as Monto
	from Employees e
	join Orders o
	ON e.EmployeeID = o.EmployeeID
	join [Order Details] od
	ON o.OrderID = od.OrderID
	group by e.EmployeeID, e.LastName, YEAR(o.OrderDate), MONTH(o.OrderDate)
),
   mes_anterior_empleado AS (
	select EmployeeID, LastName, anio, mes, Monto,
	LAG(Monto) over(partition by EmployeeID order by employeeID, anio, mes) AS mes_ant
	from ventas_empleados_mes
),
  variacion_emp AS (
	select EmployeeID, LastName, anio, mes, Monto, mes_ant,
		(Monto - mes_ant) / mes_ant * 100 AS variacion
		from mes_anterior_empleado
  )

  select 
    EmployeeID, LastName, anio, mes, Monto, mes_ant, variacion,
    CASE
	WHEN variacion > 20 THEN 'Mejor mes'
	WHEN variacion < -20 THEN 'Peor mes'
	WHEN variacion >= -20 and variacion <= 20 THEN 'Estable'
    END AS Clasificación
  from variacion_emp
  order by EmployeeID, anio, mes, Monto desc


-- =============================================

-- QUERY 2: Resumen por empleado
-- (query con el resumen)

WITH ventas_empleados_mes AS (
    SELECT e.EmployeeID, e.LastName, 
        YEAR(o.OrderDate) as anio,
        MONTH(o.OrderDate) as mes,
        SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) as Monto
    FROM Employees e
    JOIN Orders o ON e.EmployeeID = o.EmployeeID
    JOIN [Order Details] od ON o.OrderID = od.OrderID
    GROUP BY e.EmployeeID, e.LastName, YEAR(o.OrderDate), MONTH(o.OrderDate)
),
mes_anterior_empleado AS (
    SELECT EmployeeID, LastName, anio, mes, Monto,
        LAG(Monto) OVER (PARTITION BY EmployeeID ORDER BY anio, mes) AS mes_ant
    FROM ventas_empleados_mes
),
variacion_emp AS (
    SELECT EmployeeID, LastName, anio, mes, Monto, mes_ant,
        (Monto - mes_ant) / mes_ant * 100 AS variacion
    FROM mes_anterior_empleado
),
clasificacion_emp AS (
    SELECT EmployeeID, LastName, anio, mes, Monto, variacion,
        CASE
            WHEN variacion > 20 THEN 'Mejor mes'
            WHEN variacion < -20 THEN 'Peor mes'
            WHEN variacion >= -20 AND variacion <= 20 THEN 'Estable'
            ELSE 'Sin datos'
        END AS Clasificacion
    FROM variacion_emp
),
resumen_empleados AS (
    SELECT EmployeeID, LastName,
        COUNT(CASE WHEN Clasificacion = 'Mejor mes' THEN 1 END) as mejor_mes,
        COUNT(CASE WHEN Clasificacion = 'Estable' THEN 1 END) as estable,
        COUNT(CASE WHEN Clasificacion = 'Peor mes' THEN 1 END) as peor_mes
    FROM clasificacion_emp
    GROUP BY EmployeeID, LastName
)
SELECT * FROM resumen_empleados
ORDER BY mejor_mes DESC