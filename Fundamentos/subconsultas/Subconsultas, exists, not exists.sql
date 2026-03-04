use Northwind;
Select CustomerID, CompanyName
From Customers C
Where not exists(
   Select 1
from Orders o
where c.CustomerID=o.CustomerId);

Select CustomerID, CompanyName
From Customers c
where exists(
select 1 from Orders o
where c.CustomerID=o.CustomerID);


Select ProductID, ProductName
from Products p
where not exists(
	select 1 from [Order Details] od
	where p.ProductID=od.ProductID)
;

Select ProductID, ProductName 
from Products p where exists(
	SELECT 1 FROM [Order Details] od
	where p.ProductID=od.ProductID);

Select CustomerID, CompanyName 
from Customers c
where not exists(
	Select 1 from Orders o
	where c.CustomerID = o.CustomerID);

--Empleados que atendieron pedido
Select EmployeeID, LastName 
From Employees e
where exists(
	select 1 from Orders o
	where e.EmployeeID=o.EmployeeID
);

--Empleados que no atendieron pedidos
Select EmployeeID, LastName 
From Employees e
where not exists(
	select 1 from Orders o
	where e.EmployeeID=o.EmployeeID
);

INSERT INTO Employees
(
    LastName,
    FirstName,
    Title,
    TitleOfCourtesy,
    BirthDate,
    HireDate,
    Address,
    City,
    Country
)
VALUES
(
    'Prueba',
    'SinPedidos',
    'Tester',
    'Ms.',
    '1990-01-01',
    GETDATE(),
    'Calle Falsa 123',
    'Rosario',
    'Argentina'
);

Select p.ProductID, p.ProductName, o.OrderDate
from Products p
join [Order Details]od
ON p.ProductID=od.ProductID
--group by p.ProductID, p.ProductName
join Orders o 
ON od.OrderID=o.OrderID
where OrderDate>'1997-01-01' and OrderDate<'1998-01-01'

