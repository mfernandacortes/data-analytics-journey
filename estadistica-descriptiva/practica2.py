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
Sobre UnitPrice, identificar cuáles son los productos que caen en el cuartil más 
barato (Q1) — o sea, filtrar los que cuestan $13,44 o menos.

"""

# traer tablas:
p=pd.read_sql("select ProductID, ProductName, UnitPrice from Products", engine)

df=p.copy()

# cuartiles:
# Q1 (25% mas barato) = 13.44, segun .describe() de UnitPrice (practica1.py)
baratos=df[df["UnitPrice"] <= 13.44]

print(baratos)
"""
python practica2.py

"""