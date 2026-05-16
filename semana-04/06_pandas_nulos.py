import pandas as pd
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=FERCHUSERVER;'
    'DATABASE=Northwind;'
    'Trusted_Connection=yes;'
)

clientes = pd.read_sql("SELECT * FROM Customers", conn)

print(clientes.isnull().sum())
# en este caso dropna me hace perder 60 clientes, por eso es mejor usar fillna
clientes_sin_nulos = clientes.dropna(subset=['Region'])
print(clientes_sin_nulos.shape)

# esto va ANTES del fillna
print(clientes[clientes['PostalCode'].isnull()])

clientes_completos = clientes.fillna({
    'Region': 'Sin región', 
    'Fax': 'Sin fax',
    'PostalCode': 'Sin código postal'
})
print(clientes_completos.isnull().sum())



print(clientes_completos[clientes_completos['PostalCode'].isnull()])

# python 06_pandas_nulos.py