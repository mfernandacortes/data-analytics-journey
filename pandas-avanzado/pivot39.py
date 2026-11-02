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
La gerencia pide ver cuántas unidades (Quantity) se vendieron en cada país del cliente 
(Country en las filas) por año (en las columnas).
"""

# traer tablas:
c=pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select CustomerID, OrderID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity from [Order Details]", engine)

# merge:
co=pd.merge(c, o, on="CustomerID")
co_od=pd.merge(co, od, on="OrderID")

# colunma año:
co_od["anio"]=co_od["OrderDate"].dt.year

# pivot:
informe=pd.pivot_table(
    co_od,
    index="Country",
    columns="anio",
    values="Quantity",
    aggfunc="sum",
    fill_value=0
)

print(informe)
"""
python pivot39.py

"""