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
Usando Northwind, crear una tabla ancha con pivot_table — ventas totales por 
categoría (filas) y trimestre de pedido (columnas) — y después convertirla a 
formato largo con melt, dejando la categoría como identificador.

"""

# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, CategoryID, ProductName from Products", engine)
o=pd.read_sql("select OrderID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
ca_p=pd.merge(ca,p,on="CategoryID")
cap_od=pd.merge(ca_p,od,on="ProductID")
df=pd.merge(cap_od, o,on="OrderID")

# calcular monto:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1- df["Discount"])
df["trimestre"]=df["OrderDate"].dt.quarter

# pivot:
informe=pd.pivot_table(
    df,
    index=["CategoryID","CategoryName"],
    columns="trimestre",
    values="monto",
    aggfunc="sum",
    fill_value=0
)

# python melt1.py
informe = informe.reset_index()

informe2 = pd.melt(
    informe,
    id_vars=["CategoryID", "CategoryName"],
    value_vars=[1, 2, 3, 4],
    var_name="trimestre",
    value_name="monto"
)
print(informe2)
