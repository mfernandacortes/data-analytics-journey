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