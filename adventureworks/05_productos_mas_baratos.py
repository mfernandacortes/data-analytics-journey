import pandas as pd
from sqlalchemy import create_engine 

# conexión, descomentar según de donde trabaje, por defecto es la de escritorio
engine = create_engine( 
    # ESCRITORIO:
     "mssql+pyodbc://FERCHUSERVER/AdventureWorks2025?driver=SQL+Server&trusted_connection=yes"
    # NOTEBOOK:
    # "mssql+pyodbc://.\\SQLEXPRESS/AdventureWorks2025?driver=SQL+Server&trusted_connection=yes"

)

"""
CONSIGNA:
El área de compras pide ver cuáles son los 5 productos más baratos que realmente se venden, con nombre, 
color y precio de lista. Los componentes internos, con precio 0, no deben aparecer.

"""

# traer tablas:

p=pd.read_sql("select ProductID, Name, Color, ListPrice from Production.Product", engine)


# parte 1: ver los productos más baratos vendibles:
prod_vendibles=p[p["ListPrice"] > 0]

print(prod_vendibles)

top5=prod_vendibles.sort_values(by="ListPrice", ascending=True).head(5)
top10=prod_vendibles.sort_values(by="ListPrice", ascending=True).head(10)

print(top5)
print(top10)


