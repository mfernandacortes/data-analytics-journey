import pandas as pd
from sqlalchemy import create_engine 

# conexión, descomentar según de donde trabaje, por defecto es la de escritorio
engine = create_engine( 
    # ESCRITORIO:
     "mssql+pyodbc://FERCHUSERVER/Northwind?driver=SQL+Server&trusted_connection=yes"
    # NOTEBOOK:
    # "mssql+pyodbc://.\\SQLEXPRESS/Northwind?driver=SQL+Server&trusted_connection=yes"

)

"""
CONSIGNA:
La gerencia pide ver cuántos pedidos (OrderID) hizo cada país de los clientes (Country en las filas) 
por año (en las columnas).

"""

# traer tablas:
c=pd.read_sql("select CustomerID, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID, OrderDate from Orders", engine)

# merge:
co=pd.merge(c, o, on="CustomerID")

# año:
co["anio"]=co["OrderDate"].dt.year

print(co)
# pivot:
informe=pd.pivot_table(
    co,
    index="Country",
    columns="anio",
    values="OrderID",
    aggfunc="nunique",
    fill_value=0
)

print(informe)

