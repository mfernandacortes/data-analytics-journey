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
Calcular el skew() de la columna Quantity de 
Order Details y mostrarlo con print().

"""

# traer tablas:
od=pd.read_sql("select Quantity from [Order Details]", engine)

# distribución:
print(od["Quantity"].skew())

# python distribucion2.py