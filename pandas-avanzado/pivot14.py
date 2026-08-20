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
Cliente: "Quiero ver, por categoría de producto, cuántas unidades vendimos 
y el monto total facturado, separado por trimestre."

"""
# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, CategoryID, ProductName from Products", engine)
o=pd.read_sql("Select OrderID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)
# merge:
ca_p=pd.merge(ca,p,on="CategoryID")
cap_od=pd.merge(ca_p,od,on="ProductID")
df=pd.merge(cap_od,o,on="OrderID")

# calcular monto:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])
df["trimestre"]=df["OrderDate"].dt.quarter

# pivot:
informe=pd.pivot_table(
    df,
    index=["CategoryID", "CategoryName"],
    columns="trimestre",
    values=["monto","Quantity"],
    aggfunc={"monto":"sum", "Quantity":"sum"}
)
print(informe)
# python pivot14.py



"""
HALLAZGO:

"""