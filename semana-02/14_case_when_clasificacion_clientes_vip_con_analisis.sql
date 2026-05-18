Clasificá a los clientes de Northwind según cuánto gastaron en total, usando CASE WHEN dentro de una CTE. Las categorías son:

VIP → más de $50.000
Regular → entre $10.000 y $50.000
Ocasional → menos de $10.000

El resultado tiene que mostrar: CustomerID, CompanyName, el monto total y la categoría asignada. Ordenado de mayor a menor monto.

use Northwind;
WITH clientes_mas_gastaron AS (
	select c.CustomerID, c.CompanyName, SUM(od.Quantity * od.UnitPrice - (1- od.Discount)) as Monto
	from Customers c
	join Orders o
	ON c.CustomerID = o.CustomerID
	join [Order Details] od
	ON o.OrderID = od.OrderID
	group by c.CustomerID, c.CompanyName
),
  clasificacion_clientes AS (
	select CustomerID, CompanyName, Monto,
	CASE
     	   WHEN Monto < 10000 then 'Ocasional'
           WHEN Monto >= 10000 and Monto <=50000 then 'Regular'
           WHEN Monto > 50000 then 'VIP'
	END AS Clasificacion
	from clientes_mas_gastaron
)
  select CustomerID, CompanyName, Monto, Clasificacion
  from clasificacion_clientes order by Monto desc

/*Análisis:
de 89 clientes, hay 5 que son VIP: gastaron más de 50000
35 regulares donde sus montos oscilan entre 10000 y 50000
y 49 ocasionales que gastaron menos de 10000.
Si activamos a los siguientes primeros 6 clientes para que 
superen los 50000, (es decir, que incrementen sus montos en 15000).
Para ello necesitamos ver cuales son sus vendedores para estudiar alguna
estrategia de incremento y ofrecer a vendedores una comisión extra, de esta 
manera duplicamos los clientes VIP.
----
Al querer identificar los empleados responsables de cada cliente, se descubrió que
Northwind no tiene un vendedor fijo asignado por cliente — cualquier empleado puede
atender cualquier pedido. Esto representa una debilidad en el modelo de atención 
comercial. La recomendación es asignar un vendedor fijo a los 5 clientes Regular 
más cercanos al umbral VIP, con un objetivo de incremento de 20.000 y una comisión
extra como incentivo. Si la estrategia funciona con este grupo piloto, se puede 
extender a los siguientes 5 clientes en una segunda etapa.*/

