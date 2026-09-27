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
Graficar con barras horizontales con los 10 productos más vendidos por Quantity. 
"""

# traer tablas:
p=pd.read_sql("select ProductID, ProductName from Products", engine)
od=pd.read_sql("select ProductID, Quantity from [Order Details]", engine)

# merge:

p_od=pd.merge(p,od,on="ProductID")

print(p_od)


# pivot:


"""
python grafico9.py

"""