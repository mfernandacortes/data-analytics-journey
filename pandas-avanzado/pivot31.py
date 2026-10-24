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
La gerencia pide ver cuánto se vendió en cada país del cliente (Country en las 
filas) por categoría de producto (CategoryName en las columnas)

"""

# traer tablas:
c=pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, CategoryID from Products", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
ca_p=pd.merge(ca, p, on="CategoryID")
cap_od=pd.merge(ca_p, od, on="ProductID")
ord=pd.merge(cap_od, o, on="OrderID")
df=pd.merge(ord, c, on="CustomerID")

# calcular monto:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])

# pivot:
informe=pd.pivot_table(
    df,
    index="Country",
    columns=["CategoryID", "CategoryName"],
    values="monto",
    aggfunc="sum",
    fill_value=0
)

print(informe)
