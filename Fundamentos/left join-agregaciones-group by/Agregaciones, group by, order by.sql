use Northwind
go
Select * from Orders Details 
where ShippedDate is null
order by OrderDate asc
go

--Clientes de Brasil, mostrando nombre y ciudad, ordenados por nombre de empresa

Select CompanyName, City from Customers
where Country like 'Bra%il'
order by CompanyName asc
go
--chatSELECT columna_producto, SUM(Quantity)
--FROM tabla
--GROUP BY columna_producto;

--Total vendido por producto y ordenado en forma descendente
use Northwind
Select ProductID, SUM(quantity) as subtotal from [Order Details]
group by ProductId
order by subtotal desc

--Total de pedidos por cliente
Select CustomerID, count(*) as tot_ped from Orders
group by CustomerID
order by tot_ped desc


--Los 3 clientes con más pedidos
select top 3 CustomerID, count(*) as tot_ped
from Orders
group by CustomerID
order by tot_ped desc





