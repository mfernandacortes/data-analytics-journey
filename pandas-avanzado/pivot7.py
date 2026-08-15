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

Cliente: "Quiero comparar el precio promedio de venta por categoría 
de producto, y ver cómo varía según el país al que le vendemos."

Tablas: Customers, Orders, Order Details, Products, Categories.

Merge encadenado:
  1) Order Details + Orders (por OrderID)
  2) + Customers (por CustomerID) → para tener Country
  3) + Products (por ProductID) → puente hacia Categories
  4) + Categories (por CategoryID) → para tener CategoryName

Columna calculada: precio_venta = UnitPrice_x * (1 - Discount)
  (UnitPrice_x = precio de Order Details, el de la venta real;
   NO UnitPrice_y, que es el precio de catálogo en Products)

PIVOT:
  - index = CategoryName (categorías en filas)
  - columns = Country (países en columnas)
  - values = precio_venta
  - aggfunc = "mean"
  - fill_value = 0

"""

# traer tablas:
c= pd.read_sql("Select CustomerID, CompanyName, Country from Customers", engine)
ca=pd.read_sql("Select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("Select ProductID, ProductName, CategoryID, UnitPrice from Products", engine)
o=pd.read_sql("Select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("Select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)
# merge:
co=pd.merge(c,o,on="CustomerID")
co_od=pd.merge(co,od,on="OrderID")
co_odp=pd.merge(co_od,p,on="ProductID")
coodp_ca=pd.merge(co_odp,ca,on="CategoryID")

df=coodp_ca.copy()
# calcular precio de venta y monto:
df["precio_venta"] = df["UnitPrice_x"] * (1 - df["Discount"])
df["monto"]=df["Quantity"] * df["UnitPrice_x"] * (1 - df["Discount"])

# pivot:
informe=pd.pivot_table(
    df,
    index=["CategoryID","CategoryName"],
    columns="Country",
    values="precio_venta",
    aggfunc="mean",
    fill_value=0
)

print(informe)

# python pivot7.py
"""
HALLAZGO:

"""