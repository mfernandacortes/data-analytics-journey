--la subconsulta busca productos vendidos usando exists
--vendidos en el año 1997

use Northwind;

Select p.ProductID, p.ProductName
from Products p
where exists(select 1 from [Order Details] od
	join Orders o 
	on od.OrderID=o.OrderID

	WHERE od.ProductID = p.ProductID AND
	o.OrderDate > '1997-01-01' and o.OrderDate <'1997-12-31');

	SELECT distinct p.ProductID, p.ProductName, o.OrderDate
FROM Products p
JOIN [Order Details] od ON p.ProductID = od.ProductID
JOIN Orders o ON od.OrderID = o.OrderID

where o.OrderDate >= '1997-01-01'
  AND o.OrderDate < '1998-01-01';

                         