use Northwind;
SELECT 
    p.ProductID,
    p.ProductName,
    COALESCE(COUNT(DISTINCT od.OrderID), 0) AS CantidadPedidos
FROM Products p
LEFT JOIN [Order Details] od
    ON p.ProductID = od.ProductID
GROUP BY p.ProductID, p.ProductName
ORDER BY CantidadPedidos DESC;

Select p.ProductID, p.ProductName,
COALESCE(SUM(od.Quantity), 0) AS subtotal
from Products p
left join
[Order Details] od
ON p.ProductID = od.ProductID
group by p.ProductID, p.ProductName
order by subtotal desc

SELECT 
    CompanyName,
    COALESCE(Phone, Fax, 'sin contacto') as contacto
FROM Customers;

INSERT INTO Customers (
    CustomerID,
    CompanyName,
    ContactName,
    City,
    Country,
    Phone,
    Fax
)
VALUES (
    'TEST1',
    'Cliente Sin Contacto',
    'Maria Prueba',
    'Rosario',
    'Argentina',
    NULL,
    NULL
);

SELECT 
    CompanyName,
    COALESCE(Phone, Fax, 'sin contacto') as contacto
FROM Customers
order by CompanyName;

SELECT 
    customerID, CompanyName,
    COALESCE(Phone, Fax, 'sin contacto') as contacto
    FROM Customers
        WHERE COALESCE(Phone, Fax) IS NULL;

        SELECT * 
FROM Customers

SELECT 
    CustomerID, CompanyName, phone, fax,
    COALESCE(Phone, Fax, 'sin contacto') AS contacto
FROM Customers

select p.ProductID, p.ProductName, sum(od.Quantity * od.UnitPrice) as tot
from Products p
join
[Order Details]od
ON p.ProductID=od.ProductID
group by p.ProductID, p.ProductName
order by tot desc


select p.ProductID, p.ProductName, COALESCE(sum(od.Quantity * od.UnitPrice), 0) as tot
from Products p
left join
[Order Details]od
ON p.ProductID=od.ProductID
group by p.ProductID, p.ProductName
order by tot desc

