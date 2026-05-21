import pandas as pd
import pyodbc
import numpy as np


# 1. CONEXIÓN
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=FERCHUSERVER;'
    'DATABASE=Northwind;'
    'Trusted_Connection=yes;'
)

# 2. CARGA — cada tabla en su propio DataFrame
order_details = pd.read_sql("SELECT OrderID, ProductID, Quantity, UnitPrice, Discount FROM [Order Details]", conn)
products      = pd.read_sql("SELECT ProductID, ProductName, CategoryID FROM Products", conn)

ordenes       = pd.read_sql("SELECT OrderID, CustomerID FROM Orders", conn)

clientes      = pd.read_sql("SELECT CustomerID, CompanyName from CUSTOMERS", conn)

order_details['Monto'] = (order_details['Quantity'] * order_details['UnitPrice'] * (1 - order_details['Discount']))

cat_emp = pd.merge(order_details, products, on='ProductID')
o_od= pd.merge(order_details, ordenes, on= 'OrderID')
o_od= pd.merge(o_od, clientes, on='CustomerID')
#python 09_pandas_apply.py


total_clientes = o_od.groupby(['CustomerID', 'CompanyName'])['Monto'].sum().reset_index().sort_values('Monto', ascending=False)
total_clientes['segmento'] = np.where(
    total_clientes['Monto'] > 10000, 'Alto',
    np.where(total_clientes['Monto'] > 5000, 'Medio', 'Bajo')
)

total_clientes['Monto'] = total_clientes['Monto'].round(2)
print(total_clientes)
#vemos cuantos clientes hay en cada segmento
print(total_clientes['segmento'].value_counts())