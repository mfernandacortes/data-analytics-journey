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
Calcular las estadísticas descriptivas de la columna Quantity en el DataFrame 
de Order Details.

"""

# traer tablas:
od=pd.read_sql("select Quantity from [Order Details]", engine)

# muestra los valores estadísticos descriptivos
print(od["Quantity"].describe())



"""

"""