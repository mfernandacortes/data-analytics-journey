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
La gerencia pide ver cuánto se vendió en cada país del cliente (Country en las 
filas) por año (en las columnas).
"""

# traer tablas:
c=pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
co=pd.merge(c, o, on="CustomerID")
co_od=pd.merge(co, od, on="OrderID")

# calcular monto:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])

# crear la columna año:
co_od["anio"]=co_od["OrderDate"].dt.year

print(co_od)

# pivot:
informe=pd.pivot_table(
    co_od,
    index="Country",
    columns="anio",
    values="monto",
    aggfunc="sum",
    fill_value=0
)

print(informe)
