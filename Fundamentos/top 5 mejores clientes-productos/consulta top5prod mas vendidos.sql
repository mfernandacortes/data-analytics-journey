--Mostrar nombres de productos en las tablas de ordenes:
use Northwind;
go

Select od.ProductID, p.ProductName
from [Order Details] od
join Products p on od.ProductID=p.ProductID;

Select ProductID, SUM(quantity) as subtotal from [Order Details]


Select top 5 SUM(od.Quantity) as subt, p.ProductName
from [Order Details] od

join Products p 
ON od.ProductID=p.ProductID
group by p.ProductName
order by subt desc;
