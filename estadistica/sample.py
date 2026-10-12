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
predecir: la media real de Quantity es 23.81. Si se saca una muestra al azar de 
100 filas, ¿se espera que el promedio dé exactamente 23.81, o parecido pero 
distinto?

"""

# traer tablas:
od=pd.read_sql("select Quantity from [Order Details]", engine)

# muestras al azar:
muestra1 = od["Quantity"].sample(1000)
# media:
media=od["Quantity"].mean()
print(muestra1.mean())
muestra2= od["Quantity"].sample(1000)
print(muestra2.mean())
muestra3=od["Quantity"].sample(1000)
print(muestra3.mean())
