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

Sacar 3 muestras al azar de 30 filas de Quantity, calcular el promedio de 
cada una y mostrarlos con print().
"""

# traer tablas:
od=pd.read_sql("select Quantity from [Order Details]", engine)

# media:
promedio=od["Quantity"].mean()
print(promedio)
# muestras:
muestra1=od["Quantity"].sample(30)
muestra2=od["Quantity"].sample(30)
muestra3=od["Quantity"].sample(30)


# mostrar:

print(muestra1.mean())
print(muestra2.mean())
print(muestra3.mean())


