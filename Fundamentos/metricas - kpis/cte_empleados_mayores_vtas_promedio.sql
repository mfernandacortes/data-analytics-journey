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