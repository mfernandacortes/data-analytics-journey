use northwind;

--✔ clientes con pedidos después de 1998
--✔ clientes SIN pedidos después de 1998
Select c.CompanyName
from Customers c
where exists(
	select 1 from Orders o
	where o.OrderDate > '1999-01-01')
	INSERT INTO Orders
(
    CustomerID,
    EmployeeID,
    OrderDate,
    ShipName,
    ShipAddress,
    ShipCity,
    ShipCountry
)
VALUES
(
    'ALFKI',       -- asegurate que exista en Customers
    1,             -- algún empleado existente
    '1999-01-15',  -- después de 1998 ✔
    'Prueba',
    'Calle Test 123',
    'Rosario',
    'Argentina'
);
DELETE FROM Orders WHERE ShipName = 'Prueba';

Select c.CompanyName
from Customers c
where exists(
	select 1 from Orders o
	where c.CustomerID=o.CustomerID
	and o.OrderDate > '1999-01-01')


Select c.CompanyName
from Customers c
where not exists(
	select 1 from Orders o
	where c.CustomerID=o.CustomerID
	and o.OrderDate > '1999-01-01')