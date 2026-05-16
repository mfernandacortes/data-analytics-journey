-- ============================================
-- ANÁLISIS DE VENTAS — NORTHWIND
-- 10 consultas organizadas por bloque temático
-- Base de datos: SQL Server - Northwind
-- ============================================


-- ============================================
-- BLOQUE 1: CLIENTES
-- ============================================

-- Consulta 1: Total de pedidos por cliente
SELECT c.CompanyName, COUNT(*) AS total
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
GROUP BY c.CustomerID, c.CompanyName
ORDER BY total DESC


-- Consulta 2: Total gastado por cliente
-- Tablas: Customers, Orders, Order Details
SELECT c.CustomerID, c.CompanyName,
       SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) AS total_gastado
FROM [Order Details] od
JOIN Orders o ON od.OrderID = o.OrderID
JOIN Customers c ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CompanyName
ORDER BY total_gastado DESC


-- Consulta 3: Clientes que nunca compraron
SELECT c.CustomerID, c.CompanyName
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL

-- Alternativa con NOT EXISTS (más robusta ante NULLs)
SELECT c.CustomerID, c.CompanyName
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.CustomerID = c.CustomerID
)


-- ============================================
-- BLOQUE 2: PRODUCTOS
-- ============================================

-- Consulta 4: Top 5 productos más vendidos por cantidad
-- WITH TIES incluye empates en el puesto 5
SELECT TOP 5 WITH TIES p.ProductID, p.ProductName,
       SUM(od.Quantity) AS total_vendido
FROM Products p
JOIN [Order Details] od ON p.ProductID = od.ProductID
GROUP BY p.ProductID, p.ProductName
ORDER BY total_vendido DESC


-- Consulta 5: Productos que nunca se vendieron
SELECT p.ProductID, p.ProductName
FROM Products p
WHERE NOT EXISTS (
    SELECT 1
    FROM [Order Details] od
    WHERE p.ProductID = od.ProductID
)


-- Consulta 6a: Precio promedio general de productos
SELECT AVG(UnitPrice) AS promedio_precios
FROM Products


-- Consulta 6b: Precio promedio por categoría
SELECT p.CategoryID, AVG(p.UnitPrice) AS promedio_por_categoria
FROM Products p
GROUP BY p.CategoryID
ORDER BY promedio_por_categoria DESC


-- ============================================
-- BLOQUE 3: TIEMPO
-- ============================================

-- Consulta 7a: Cantidad de pedidos por año (por fecha de pedido)
SELECT YEAR(o.OrderDate) AS anio, COUNT(o.OrderID) AS total_pedidos_anio
FROM Orders o
GROUP BY YEAR(o.OrderDate)
ORDER BY total_pedidos_anio DESC

-- Consulta 7b: Pedidos enviados por año (por fecha de envío)
SELECT YEAR(o.ShippedDate) AS anio, COUNT(o.OrderID) AS total_enviados_anio
FROM Orders o
WHERE o.ShippedDate IS NOT NULL
GROUP BY YEAR(o.ShippedDate)
ORDER BY total_enviados_anio DESC


-- Consulta 8: Ventas totales por año
SELECT YEAR(o.OrderDate) AS anio,
       SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) AS total_anio
FROM Orders o
JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY YEAR(o.OrderDate)
ORDER BY total_anio DESC


-- ============================================
-- BLOQUE 4: EMPLEADOS
-- ============================================

-- Consulta 9: Cantidad de pedidos por empleado
SELECT e.LastName, e.FirstName, COUNT(o.OrderID) AS cantidad_pedidos
FROM Orders o
JOIN Employees e ON o.EmployeeID = e.EmployeeID
GROUP BY e.EmployeeID, e.LastName, e.FirstName
ORDER BY cantidad_pedidos DESC


-- Consulta 10: Ventas totales por empleado
SELECT e.LastName, e.FirstName,
       SUM(od.Quantity * od.UnitPrice * (1 - od.Discount)) AS total_ventas
FROM Employees e
JOIN Orders o ON e.EmployeeID = o.EmployeeID
JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY e.EmployeeID, e.LastName, e.FirstName
ORDER BY total_ventas DESC
