/*Clientes que en 1997:

hicieron más de 3 órdenes
gastaron más que el promedio
mostrar:
nombre
cantidad de órdenes
total gastado*/
use Northwind

select c.CustomerID, c.CompanyName, count(distinct o.orderID) as pedidos_cant
from Customers c
join Orders o
on c.CustomerID=o.CustomerID
where year(OrderDate) = 1997
group by c.CustomerID, c.CompanyName

having count(distinct o.orderID) >3
order by pedidos_cant desc

