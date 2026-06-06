"""
Sobre la tabla Products de Northwind:

Filtrar los productos de categoría 1 o 2
Sobre ese resultado, calculá el precio promedio por categoría
"""

import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traigo tablas que necesito:

df = pd.read_sql("select ProductID, ProductName, UnitPrice, CategoryID from Products", engine)

#filtar resultados de categoria 1 o 2:

df = df[(df["CategoryID"] == 1) | (df["CategoryID"]  == 2)] 

print(df)


# seguir mañana: df.groupby("columna_agrupacion")["columna_a_calcular"].mean()
#df = df.groupby("CategoryID").df["UnitPrice"].mean()
print(df)
# python combinados.py