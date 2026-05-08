import pandas as pd
import pyodbc

# Conexión a SQL Server Northwind
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=FERCHUSERVER;'
    'DATABASE=Northwind;'
    'Trusted_Connection=yes;'
)
# Reemplazar FERCHUSERVER con el nombre de tu servidor SQL Server local

# Traer clientes
df = pd.read_sql("SELECT CustomerID, CompanyName, Country FROM Customers", conn)
print(df.head())

# Cuántos clientes hay por país
paises = df.groupby('Country').size().reset_index(name='cantidad')
print(paises.sort_values('cantidad', ascending=False))