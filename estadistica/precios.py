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

Mostrar los productos de la categoría Beverages (ProductID, ProductName, 
UnitPrice) ordenados de mayor a menor precio.
"""

# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories " \
"where CategoryName='Beverages'", engine)
p=pd.read_sql("select ProductID, CategoryID, ProductName, UnitPrice from Products", engine)

# merge:
ca_p=pd.merge(ca,p,on="CategoryID")
print(ca_p)

# ordenar:
ordenados=ca_p.sort_values(by="UnitPrice", ascending=False)
print(ordenados)
