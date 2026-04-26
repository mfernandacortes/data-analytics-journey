/*Del cliente ID ALFKI
hay algo curioso, los días entre pedidos fueron muy variados
pero hubo una brecha grande entre abril 1998 y enero 1999 y ese
fue su último pedido. En 1997 pasaban 30 días, 60 días, 10 días, pero
esta brecha se generó entre 1998 y 1999 casi un año.Alfred Futterkiste.*/
-- ANÁLISIS: Comportamiento de compra por cliente
-- Parte 1: Días entre pedidos usando LAG y DATEDIFF
-- Hallazgo: clientes con brechas grandes pueden indicar churn
-- Parte 2: Empleado asignado por pedido para investigar si el cambio de vendedor influyó
-- Próxima pregunta: ¿cambió el empleado asignado antes de la brecha grande?



WITH pedidos_cliente AS (
    SELECT 
        c.CustomerID, c.CompanyName,
        o.OrderID,
        o.OrderDate
    FROM Customers c
    JOIN Orders o ON c.CustomerID = o.CustomerID
)
SELECT 
    CustomerID, CompanyName,
    OrderID, OrderDate,
    LAG(OrderDate) OVER (PARTITION BY CustomerID ORDER BY OrderDate) as pedido_anterior,
    DATEDIFF(day, 
        LAG(OrderDate) OVER (PARTITION BY CustomerID ORDER BY OrderDate), 
        OrderDate) as dias_entre_pedidos
FROM pedidos_cliente
ORDER BY CustomerID, OrderDate

/*Segunda parte del análisis: que pasó con el cliente?
Se realizó una nueva consulta pero esta vez agregando los datos del empleado, vemos que
se interrumpió entre Leverling que fue el penúltimo vendedor, ahi pasaron 281 días,
volvió y ahi lo atendió Davolio. Es necesario hablar con los dos vendedores, con el cliente
para descartar que haya tenido otro tipo de problemas o alguna queja y de acuerdo a eso
proponer alguna promoción para recuperar clientes.*/

WITH pedidos_cliente AS (
    SELECT 
        c.CustomerID, c.CompanyName,
        o.OrderID,
        o.OrderDate, 
	e.EmployeeID, e.LastName
    FROM Customers c
    JOIN Orders o ON c.CustomerID = o.CustomerID
    JOIN Employees e ON o.EmployeeID = e.EmployeeID
)
SELECT 
    CustomerID, CompanyName,
    OrderID, OrderDate,
    LAG(OrderDate) OVER (PARTITION BY CustomerID ORDER BY OrderDate) as pedido_anterior,
    DATEDIFF(day, 
        LAG(OrderDate) OVER (PARTITION BY CustomerID ORDER BY OrderDate), 
        OrderDate) as dias_entre_pedidos, EmployeeID, LastName
FROM pedidos_cliente
ORDER BY CustomerID, OrderDate
