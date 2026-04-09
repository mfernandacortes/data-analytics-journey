use Northwind;

SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > (
    SELECT AVG(UnitPrice) FROM Products
);
SELECT ProductName
FROM Products
WHERE UnitPrice > (
    SELECT AVG(UnitPrice)
    FROM Products
);

SELECT *
FROM (
    SELECT CustomerID, COUNT(*) as total
    FROM Orders
    GROUP BY CustomerID
) t
WHERE total > 5;
use Northwind;
select c.CompanyName
from Customers c
where not exists(
	select 1 from Orders o
	where c.CustomerID = o.CustomerID)

select ProductName
from Products
where UnitPrice > (select AVG(UnitPrice) from products)