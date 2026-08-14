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
Tablas: Customers, Orders, Order Details (las de siempre)

merge + monto (igual que siempre)
columna nueva: mes = OrderDate.dt.month

pivot_table(df, index="Country", columns="mes",
            values="monto", aggfunc="sum", fill_value=0)

"""

# traer tablas:
c=pd.read_sql("Select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("Select OrderID, CustomerID, OrderDate from Orders", engine)
od=pd.read_sql("Select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)


# merge:
co=pd.merge(c,o,on="CustomerID")
co_od=pd.merge(co,od,on="OrderID")

# calcular monto:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])

# colmna nueva:
co_od["mes"]=co_od.OrderDate.dt.month
# pivot:
df=pd.pivot_table(
    co_od,
    index="Country",
    columns="mes",
    values="monto",
    aggfunc="sum",
    fill_value=0
)
print(df)
"""
HALLAZGO:

"""