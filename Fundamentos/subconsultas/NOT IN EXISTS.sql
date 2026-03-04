use Northwind;
--productos que nunca se vendieron
SELECT ProductName
FROM Products
WHERE ProductID NOT IN (
    select ProductID from [Order Details]);

--clientes que no hicieron pedidos
Select CustomerID, CompanyName from Customers where CustomerID NOT IN
	(select CustomerID from Orders)

--clientes que si hicieron pedidos
SELECT CustomerID, CompanyName
FROM Customers c
WHERE EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.CustomerID = c.CustomerID
);
-- Clientes que nuncca compraron con not exists (más pro porque pueden aparecer nulls)
Select CustomerID, CompanyName from Customers c
where not exists
(select 1 from Orders o where o.CustomerID=c.CustomerID)