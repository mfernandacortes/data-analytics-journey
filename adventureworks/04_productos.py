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

"""

# traer tablas:
q = """
SELECT TOP 10 ProductID, Name, Color, ListPrice
FROM Production.Product
ORDER BY ProductID
"""
print(pd.read_sql(q, engine))


q = """
SELECT TOP 10 ProductID, Name, Color, ListPrice
FROM Production.Product
WHERE ListPrice > 0
ORDER BY ListPrice DESC
"""
print(pd.read_sql(q, engine))

qc = """
SELECT Color, COUNT(*) AS cantidad
FROM Production.Product
GROUP BY Color
ORDER BY cantidad DESC
"""
print(pd.read_sql(qc, engine))

df_color = pd.read_sql(qc, engine)
print(df_color["cantidad"].sum())

# python 04_productos.py