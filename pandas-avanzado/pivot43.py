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
La gerencia pide ver cuánto se vendió de cada producto (ProductID y ProductName en las filas) 
por año (en las columnas), con monto = UnitPrice * Quantity * (1 - Discount).
"""

# traer tablas:
p=pd.read_sql("select ProductID, ProductName from Products", engine)
o=pd.read_sql("select OrderID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
p_od=pd.merge(p, od, on="ProductID")
df=pd.merge(p_od, o, on="OrderID")

# calcular monto:
print(df)

# pivot:


"""
python pivot43.py

"""