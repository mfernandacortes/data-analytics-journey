use Northwind;

SELECT 
    YEAR(o.OrderDate) AS anio,
    MONTH(o.OrderDate) AS mes,
    SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS total_ventas
FROM [Order Details] od
JOIN Orders o ON o.OrderID = od.OrderID
GROUP BY YEAR(o.OrderDate), MONTH(o.OrderDate)
ORDER BY anio, mes;

select p.ProductName, SUM(od.Quantity) as subt
from Products p
join
[Order Details] od
ON p.ProductID =od .ProductID
group by p.ProductID, p.ProductName
having SUM(od.Quantity) > 100
order by subt desc;