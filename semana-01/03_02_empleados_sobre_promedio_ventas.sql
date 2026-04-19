/*
Consulta: Empleados con ventas superiores al promedio

Descripción:
Calcula el total de ventas por empleado y obtiene el promedio general de ventas.
Luego filtra aquellos empleados cuyo monto total vendido supera dicho promedio.

Objetivo:
Identificar empleados con rendimiento superior a la media de ventas.

Lógica:
1. Se calcula el total vendido por cada empleado (CTE: Empleados_mayores_ventas).
2. Se calcula el promedio general de ventas entre todos los empleados (CTE: promedio_gral).
3. Se filtran los empleados cuyo total de ventas es mayor al promedio.

Tablas utilizadas:
- Employees
- Orders
- Order Details

Conceptos aplicados:
- CTE (Common Table Expressions)
- Funciones de agregación: SUM(), AVG()
- JOIN entre múltiples tablas
- Filtrado con valores calculados

Resultado:
Listado de empleados con ventas por encima del promedio, ordenados de mayor a menor.

*/

use Northwind;



  WITH  Empleados_mayores_ventas AS(
    Select e.EmployeeID, e.LastName, sum(od.UnitPrice * od.Quantity * (1-     od.discount)) as Monto
    from Employees e
    Join Orders o 
    ON e.EmployeeID=o.EmployeeID
    join [Order Details] od
    ON o.OrderID=od.OrderID
    group by e.EmployeeID, e.LastName
),
  promedio_gral AS(
    Select AVG(Monto) as prom from Empleados_mayores_ventas
)
  select * from Empleados_mayores_ventas, promedio_gral where Monto > prom
  order by Monto desc