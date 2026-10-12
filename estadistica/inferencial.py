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
Calcular el intervalo de confianza de la media de Quantity con una muestra de 100 
filas y mostrar el límite inferior y el superior con print().

"""

# traer tablas:
od=pd.read_sql("select Quantity from [Order Details]", engine)

muestra = od["Quantity"].sample(100)
media = muestra.mean()
error = 1.96 * (muestra.std() / 100 ** 0.5)
print(media - error, media + error)


"""
python inferencial.py

"""