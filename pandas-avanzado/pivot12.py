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
Cliente: "Quiero ver, por país, cuántos pedidos distintos hicieron
y el monto total facturado."
"""

# traer tablas:
c=pd.read_sql("Select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity,UnitPrice,Discount from [Order Details]", engine)


# merge:
co=pd.merge(c,o,on="CustomerID")
co_od=pd.merge(co,od,on="OrderID")

# creo una columna llamada monto:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])
print(co_od)


# pivot:
informe=pd.pivot_table(
    co_od,
    index="Country",
    values=["OrderID","monto"],
    aggfunc={"OrderID":"nunique", "monto":"sum"},
    fill_value=0
)
print(informe)
# python pivot12.py

