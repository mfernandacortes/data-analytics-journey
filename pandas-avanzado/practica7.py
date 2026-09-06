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
El equipo de producto quiere ver, en una sola tabla, el total facturado por categoría 
de producto (filas) y por año (columnas), para detectar de un vistazo qué categorías 
crecieron o cayeron entre 1996, 1997 y 1998.

"""

# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select CategoryID, ProductID, ProductName from Products", engine)
o=pd.read_sql("select OrderID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)


# merge:
ca_p=pd.merge(ca,p,on="CategoryID")
cap=pd.merge(ca_p,od,on="ProductID")
df=pd.merge(cap,o,on="OrderID")

# calcular monto:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])
df["anio"]=df["OrderDate"].dt.year
print(df)
# pivot:
informe=df.pivot_table(
    
    index=["CategoryID","CategoryName"],
    columns="anio",
    values="monto",
    aggfunc="sum",
    fill_value=0
)
print(informe)
# python practica7.py

"""
HALLAZGO:
Crecimiento fuerte de 1996 a 1997 en todas las categorías, con caída parcial en 1998 
(Beverages es la única que sigue creciendo incluso en 1998).
"""