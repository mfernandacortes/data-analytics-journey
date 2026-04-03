--Ejercicios varios, explicación razonamiento

select CustomerId, CompanyName, ContactName, ContactTitle, City, Address, Country
from Customers
where Country = 'USA' or Country = 'Mexico'
Order by Country
go
--Si quiero saber cuales son los paises donde tengo más de 10 clientes:
--primero agrupo por país y que sume, pero tengo que filtrar más de 10 clientes, entonces
--uso having para filtrar: Count(*)> 10
Select Country, Count(*) as Contar
from Customers group by Country
having Count(*) > 10
-- Productos de más de 20 dólares
Select ProductID, ProductName, CategoryID, UnitPrice
from Products 

where UnitPrice  > 20
use Northwind
go
-- Averiguar cuales tres primeros productos son los más vendidos:
select * from [Order Details], sum(Quantity) as subtotal
group by ProductId
SELECT ProductID, SUM(Quantity) AS subtotal
FROM [Order Details]
GROUP BY ProductID
having max(subtotal)

SELECT TOP 3 p.ProductName, SUM(od.Quantity) AS total_vendido
FROM [Order Details] od
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY total_vendido DESC;