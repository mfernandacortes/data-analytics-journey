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
Consigna: distribución de UnitPrice en Products, sin merge ni groupby, directo 
sobre la tabla.

"""

# traer tablas:
p=pd.read_sql("select ProductID, ProductName, UnitPrice from Products", engine)



# gráfico:
import matplotlib.pyplot as plt

p["UnitPrice"].plot(kind="hist")
plt.title("Precios de los Productos")
plt.show()

"""
python histograma2.py

"""