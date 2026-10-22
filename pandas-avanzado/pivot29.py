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
Mostrar el monto vendido por categoría (CategoryID y CategoryName en las filas) 
y por transportista (CompanyName en las columnas), con monto = UnitPrice * 
Quantity * (1 - Discount).

"""

# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, CategoryID from Products", engine)
sh=pd.read_sql("select ShipperID, CompanyName from Shippers", engine)
o=pd.read_sql("select OrderID, ShipVia from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)


# merge:
ca_p=pd.merge(ca, p, on="CategoryID")
cap_od=pd.merge(ca_p, od, on="ProductID")
capod_o=pd.merge(cap_od, o, on="OrderID")
df=pd.merge(capod_o, sh, left_on="ShipVia", right_on="ShipperID")

print(df)
# calcular monto:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])

# pivot: 
informe=pd.pivot_table(
    df,
    index=["CategoryID", "CategoryName"],
    columns=["ShipperID", "CompanyName"],
    values="monto",
    aggfunc="sum",
    fill_value=0
)

print(informe)

