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
La gerencia pide saber cuánto se vendió de los productos de cada país de 
proveedor (Country de Suppliers en las filas) por año (en las columnas), 
con monto = UnitPrice * Quantity * (1 - Discount).

"""

# traer tablas:
su=pd.read_sql("select SupplierID, CompanyName, Country from Suppliers", engine)
p=pd.read_sql("select ProductID, SupplierID from Products", engine)
o=pd.read_sql("select OrderID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)


# merge:
su_p=pd.merge(su, p, on="SupplierID")
sup_od=pd.merge(su_p, od, on="ProductID")
df=pd.merge(sup_od, o, on="OrderID")

# calcular monto y columna año:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])
df["anio"]=df["OrderDate"].dt.year

print(df)

# pivot:
informe=pd.pivot_table(
    df,
    index="Country",
    columns="anio",
    values="monto",
    aggfunc="sum",
    fill_value=0
)

print(informe)

