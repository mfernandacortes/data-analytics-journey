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
Sobre UnitPrice de la tabla Products, calculá media, mediana y desvío estándar.

"""

# traer tablas:
p= pd.read_sql("select UnitPrice from Products", engine)

# ver datos:

print(p["UnitPrice"].describe())



"""
HALLAZGO:
El precio promedio (mean) de los productos es $28,70, pero la mediana (50%) es 
bastante menor: $19,48. Esa brecha confirma numéricamente lo que ya se veía en 
el histograma: hay outliers (como Côte de Blaye, $263,50) que tiran la media 
hacia arriba, mientras que la mediana — al no verse afectada por valores extremos
— refleja mejor el precio "típico" real del catálogo. El desvío estándar alto 
($33,63, mayor incluso que la propia media) confirma que los precios están 
bastante dispersos, no concentrados cerca del promedio.

"""