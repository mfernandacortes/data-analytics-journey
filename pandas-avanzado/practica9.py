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
Pedido de un cliente: "Necesito ver, para cada categoría de producto, el total facturado 
por trimestre. Quiero categorías en filas y trimestres en columnas, y donde no haya ventas 
que aparezca 0 en vez de vacío."

"""

# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("Select ProductID, CategoryID from Products", engine)
o=pd.read_sql("select OrderID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)
# merge:
cap=pd.merge(ca,p,on="CategoryID")
cap_od=pd.merge(cap,od,on="ProductID")
df=pd.merge(cap_od,o,on="OrderID")

# calcular monto:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])
# agregar columna trimestre:
df["trimestre"]=df["OrderDate"].dt.quarter
# pivot:
informe=pd.pivot_table(
    df,
    index=["CategoryID", "CategoryName"],
    columns="trimestre",
    values="monto",
    aggfunc="sum",
    fill_value=0
)
print(informe)
# python practica9.py

"""
HALLAZGO:

"""