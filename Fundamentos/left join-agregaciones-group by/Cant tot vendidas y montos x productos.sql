use Northwind;
select p.ProductID, p.ProductName, COALESCE(SUM(od.Quantity), 0) as totcant
from Products p
left join
[Order Details] od
ON p.ProductID=od.ProductID
group by p.ProductID, p.ProductName
order by totcant desc

select p.ProductID, p.ProductName, COALESCE(sum(od.Quantity * od.UnitPrice), 0) as tot
from Products p
left join
[Order Details]od
ON p.ProductID=od.ProductID
group by p.ProductID, p.ProductName
order by tot desc