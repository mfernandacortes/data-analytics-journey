-- Mini proyecto parte 2: Evolución mes a mes de los 3 mejores empleados
-- Empleados analizados: Fuller (2), Peacock (4), King (7)
-- Período: diciembre 1997 - mayo 1998

--Análisis: 
/* hay algo llamativo...entre abril 1998 y mayo 1998 las ventas de Fuller y King cayeron un 90%, solo Peacock mantuvo que tambien le bajó pero se mantuvo más estable que los otro dos, ya que los otros tuvieron un gran volúmen de compra, o sea, que la variación fue mucho más amplia*/

WITH ventas_por_emp AS (
  SELECT e.EmployeeID, e.LastName, 
        YEAR(o.OrderDate) as anio,
        MONTH(o.OrderDate) as mes,
        SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) as Monto
    FROM Employees e
    JOIN Orders o ON e.EmployeeID = o.EmployeeID
    JOIN [Order Details] od ON o.OrderID = od.OrderID
    WHERE o.OrderDate >= '1997-12-01' AND o.OrderDate < '1998-06-01'
    GROUP BY e.EmployeeID, e.LastName, YEAR(o.OrderDate), MONTH(o.OrderDate)      
)
SELECT 
    EmployeeID, LastName, anio, mes, Monto,
    LAG(Monto) OVER (PARTITION BY EmployeeID ORDER BY anio, mes) as mes_anterior,
    Monto - LAG(Monto) OVER (PARTITION BY EmployeeID ORDER BY anio, mes) as variacion
FROM ventas_por_emp
WHERE EmployeeID IN (2, 4, 7)  -- los 3 del ranking anterior
ORDER BY EmployeeID, anio, mes
