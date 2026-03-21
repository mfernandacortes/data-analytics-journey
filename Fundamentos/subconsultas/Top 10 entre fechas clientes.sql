select top 10 C.CustomerID, C.CompanyName, count(O.OrderID) as totalPed 
from Orders O
join
Customers C on C.CustomerID = O.CustomerID
where O.OrderDate >= '1996-01-01' 
and O.OrderDate < '1997-01-01'
group by C.CustomerID, C.CompanyName
order by totalPed desc
