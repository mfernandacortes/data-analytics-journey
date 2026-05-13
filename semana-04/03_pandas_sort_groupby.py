import pandas as pd
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=FERCHUSERVER;'
    'DATABASE=Northwind;'
    'Trusted_Connection=yes;'
)

clientes = pd.read_sql("SELECT * FROM Customers", conn)
# python 03_pandas_sort_groupby.py
# sort por país
print(clientes.sort_values('Country', ascending=True)[['CompanyName', 'Country']])

# el equivalente al distinct en SQL
print(clientes['Country'].unique())
# con cantidad de rows (filas):
print(clientes['Country'].nunique())

# paso a csv el DataFrame clientes:
clientes.to_csv('clientes_limpios.csv', index=False)

# ordenar ahora por dos columnas
print(clientes.sort_values(['Country', 'CompanyName'], ascending=True))

"""Pasar de SQL a pandas: SELECT Country, COUNT(*) 
FROM Customers 
GROUP BY Country"""

print(clientes.groupby('Country').size())

#Ahora agregar el orden de mayor a menor:

print(clientes.groupby('Country').size().sort_values(ascending=False))

#SELECT Country, SUM(UnitPrice * Quantity) as total
#FROM Orders
#GROUP BY Country

ordenes = pd.read_sql("SELECT * FROM Orders", conn)

print(ordenes.head())

# el JOIN de SQL con customers y orders:
clientes_ordenes = pd.merge(clientes, ordenes, on='CustomerID')
print(clientes_ordenes.head())

# cargar Order Details:
order_details = pd.read_sql("SELECT * FROM [Order Details]", conn)
print(order_details.head())