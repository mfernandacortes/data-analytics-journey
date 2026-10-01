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
Distribución de UnitPrice en Products, sin merge ni groupby, directo 
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
HALLAZGO: Distribución de precios (UnitPrice): La mayoría de los productos de 
Northwind (más de 50 de 78) cuestan hasta unos $25-28. Hay un caso extremo, 
Côte de Blaye a $263,50, muy por encima del resto — un outlier que estira el 
gráfico hacia la derecha.

"""