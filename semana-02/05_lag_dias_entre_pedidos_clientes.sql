/*Del cliente ID ALFKI
hay algo curioso, los días entre pedidos fueron muy variados
pero hubo una brecha grande entre abril 1998 y enero 1999 y ese
fue su último pedido. En 1997 pasaban 30 días, 60 días, 10 días, pero
esta brecha se generó entre 1998 y 1999 casi un año.Alfred Futterkiste.*/
-- Días entre pedidos por cliente usando LAG y DATEDIFF
-- Hallazgo: clientes con brechas grandes pueden indicar churn
-- Próxima pregunta: ¿cambió el empleado asignado antes de la brecha?

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