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
La gerencia pide saber cuántas unidades (Quantity) se vendieron de los productos 
de cada país de proveedor (Country de Suppliers en las filas) por categoría 
(CategoryName en las columnas).

"""

# traer tablas:
su=pd.read_sql("select SupplierID, CompanyName, Country from Suppliers", engine)
p=pd.read_sql("select ProductID, SupplierID, CategoryID from Products", engine)
od=pd.read_sql("select ProductID, Quantity from [Order Details]", engine)
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)

# merge:
su_p=pd.merge(su, p, on="SupplierID")
df1=pd.merge(su_p, od, on="ProductID")
df=pd.merge(df1, ca, on="CategoryID")
print(df)
# pivot:


"""
python pivot32.py

"""