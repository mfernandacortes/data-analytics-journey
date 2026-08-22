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
Consigna: El gerente regional pide ver el total facturado por país y por categoría 
de producto, cruzado en una tabla. Pero además quiere, sin tener que sumar a mano,
el total general de cada país (todas sus categorías juntas) y el total general de 
cada categoría (todos los países juntos).

"""

# traer tablas:
ca=pd.read_sql("Select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("Select ProductID, CategoryID, ProductName from Products", engine)
od=pd.read_sql("Select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)
c=pd.read_sql("select CustomerID, Country from Customers", engine)

# merge:
ca_p=pd.merge(ca,p,on="CategoryID")
cap_od=pd.merge(ca_p,od,on="ProductID")
capod_o=pd.merge(cap_od,o,on="OrderID")
df=pd.merge(capod_o,c,on="CustomerID")

# calcular monto:
print(df)

# pivot:

# python pivot16.py

"""
HALLAZGO:

"""