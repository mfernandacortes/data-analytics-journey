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
Usando Northwind, hacer un merge tipo left entre Products y Order Details, con 
indicator=True, para detectar productos que nunca se vendieron (sin ningún pedido 
asociado).

"""

# traer tablas:
p=pd.read_sql("select ProductID, ProductName from Products", engine)
o=pd.read_sql("select OrderID from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)


# merge:
pod=pd.merge(p,od,on="ProductID", how="left", indicator=True)

print(pod)
# _merge es el valor de la nueva columna y "left_only" es uno de los 3 posibles 
# valores q puede tomar esa columna, cuando puse indicator=True
sin_ventas = pod[pod["_merge"] == "left_only"]
print(sin_ventas)
# python merge_fino.py
