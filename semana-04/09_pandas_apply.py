import pandas as pd
import pyodbc
import numpy as np

pd.set_option('display.max_rows', None)

# 1. CONEXIÓN
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=FERCHUSERVER;'
    'DATABASE=Northwind;'
    'Trusted_Connection=yes;'
)

# 2. CARGA — cada tabla en su propio DataFrame
order_details = pd.read_sql("SELECT OrderID, ProductID, Quantity, UnitPrice, Discount FROM [Order Details]", conn)
ordenes       = pd.read_sql("SELECT OrderID, CustomerID FROM Orders", conn)
clientes      = pd.read_sql("SELECT CustomerID, CompanyName from CUSTOMERS", conn)

# 3. TRANSFORMACIONES
order_details['Monto'] = (order_details['Quantity'] * order_details['UnitPrice'] * (1 - order_details['Discount']))

# 4. MERGES
o_od = pd.merge(order_details, ordenes, on='OrderID')
o_od = pd.merge(o_od, clientes, on='CustomerID')

# 5. ANÁLISIS — segmentación de clientes por monto total
total_clientes = o_od.groupby(['CustomerID', 'CompanyName'])['Monto'].sum().reset_index().sort_values('Monto', ascending=False)
total_clientes['segmento'] = np.where(
    total_clientes['Monto'] > 10000, 'Alto',
    np.where(total_clientes['Monto'] > 5000, 'Medio', 'Bajo')
)
total_clientes['Monto'] = total_clientes['Monto'].round(2)

print(total_clientes)
print(total_clientes['segmento'].value_counts())