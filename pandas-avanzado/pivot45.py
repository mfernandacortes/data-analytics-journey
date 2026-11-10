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
La gerencia pide ver cuántas unidades (Quantity) se enviaron con cada transportista 
(CompanyName en las filas) en cada categoría de producto (CategoryName en las columnas).

"""

# traer tablas:

ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, CategoryID from Products", engine)
o=pd.read_sql("select OrderID, ShipVia from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity from [Order Details]", engine)
sh=pd.read_sql("select ShipperID, CompanyName from Shippers", engine)

# merge:
ca_p=pd.merge(ca, p, on="CategoryID")
cap_od=pd.merge(ca_p, od, on="ProductID")
capod=pd.merge(cap_od, o, on="OrderID")
df=pd.merge(capod, sh, left_on="ShipVia", right_on="ShipperID")



# pivot:
informe=pd.pivot_table(
    df,
    index=["ShipperID", "CompanyName"],
    columns=["CategoryID", "CategoryName"],
    values="Quantity",
    aggfunc="sum",
    fill_value=0
)

print(informe)

