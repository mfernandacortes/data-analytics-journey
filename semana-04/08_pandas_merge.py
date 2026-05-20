import pandas as pd
import pyodbc

# 1. CONEXIÓN
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=FERCHUSERVER;'
    'DATABASE=Northwind;'
    'Trusted_Connection=yes;'
)

# 2. CARGA — cada tabla en su propio DataFrame
order_details = pd.read_sql("SELECT OrderID, ProductID, Discount FROM [Order Details]", conn)
products      = pd.read_sql("SELECT ProductID, ProductName, CategoryID FROM Products", conn)
categories    = pd.read_sql("SELECT CategoryID, CategoryName FROM Categories", conn)
ordenes       = pd.read_sql("SELECT OrderID, EmployeeID FROM Orders", conn)
empleados     = pd.read_sql("SELECT EmployeeID, LastName FROM Employees", conn)

# 3. TRANSFORMACIONES — columnas nuevas, booleanos, etc.
order_details['tiene_descuento'] = order_details['Discount'] > 0



# 4. MERGE Y ANÁLISIS — groupby, rankings, etc.(el dataframe se va agregando de más columnas en cada merge)

cat_emp = pd.merge(order_details, products, on='ProductID')
cat_emp = pd.merge(cat_emp, categories, on='CategoryID')
cat_emp = pd.merge(cat_emp, ordenes, on='OrderID')
cat_emp = pd.merge(cat_emp, empleados, on='EmployeeID')


# Muestra apellido de empleados que vendieron con descuentos y las categorías q descontaron

print(cat_emp.groupby(['LastName', 'CategoryName'])['tiene_descuento'].sum().sort_values(ascending=False))