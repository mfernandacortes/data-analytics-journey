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
La gerencia quiere ver el monto vendido (Quantity * UnitPrice * (1 - Discount)) por país de cliente 
(filas) y por año (columnas).

"""

# traer tablas:
cu=pd.read_sql("select CustomerID, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
cu_o=pd.merge(cu, o, on="CustomerID")
df=pd.merge(cu_o, od, on="OrderID")

# calcular monto:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])

# año:
df["anio"]=df["OrderDate"].dt.year

print(df)
# pivot:
informe=pd.pivot_table(
    df,
    index="Country",
    columns="anio",
    values="monto",
    aggfunc="sum",
    fill_value=0
)

print(informe)
