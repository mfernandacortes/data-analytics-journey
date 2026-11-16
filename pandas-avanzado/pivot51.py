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
La gerencia quiere ver cuántos pedidos (OrderID) hizo cada país de cliente (Country en filas) por año 
(columnas).

"""

# traer tablas:
cu=pd.read_sql("select CustomerID, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID, OrderDate from Orders", engine)

# merge:
df=pd.merge(cu, o, on="CustomerID")

# calcular monto:
print(df)

# pivot:


"""
python pivot51.py

"""