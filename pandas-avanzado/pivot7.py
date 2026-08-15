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

Tablas: Customers, Orders, Order Details, Products, Categories.
(mismo merge de 5 tablas que ya hiciste para el primer pivot)

merge + monto (igual que siempre)

PIVOT:
pd.pivot_table(df, index="CategoryName", columns="Country",
                values="monto", aggfunc="mean", fill_value=0)

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
print(coodp_ca)
# calcular monto:


# pivot:
# python pivot7.py

"""
HALLAZGO:

"""