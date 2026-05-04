-- Clasificación de productos por precio unitario
-- Económico: menos de $20 | Medio: $20-$50 | Premium: más de $50
-- CASE WHEN directo sin CTE — no hay agregaciones, trabaja fila por fila

select
ProductID, ProductName, UnitPrice,
CASE 
  WHEN UnitPrice < 20 THEN 'Económico'
  WHEN UnitPrice >= 20 AND UnitPrice <= 50 THEN 'Medio'
  WHEN UnitPrice > 50 THEN 'Premium'
END AS Clasificación
from Products
order by UnitPrice desc