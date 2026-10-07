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
Graficar un histograma de UnitPrice de Products (ya lo hiciste antes) y, al lado 
o después, calcular la métrica que mide el sesgo numéricamente: skew().

"""

# traer tablas:
p=pd.read_sql("select UnitPrice from Products", engine)

# distribución:
print(p["UnitPrice"].skew())

"""
python distribucion.py

"""