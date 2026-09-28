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
Graficar en barras horizontales los 10 productos más caros de Northwind, 
con nombre, según UnitPrice.

"""

# traer tablas:
p=pd.read_sql("select ProductID, ProductName, UnitPrice from Products", engine)

# ordenar de mayor a menor por precios:
df=p.sort_values(by="UnitPrice", ascending=False)
# top 10:
df=df.head(10)

# gráfico:
import matplotlib.pyplot as plt
df.plot(kind="barh", x="ProductName", y="UnitPrice")
plt.title("Top 10 Productos Más caros")
plt.show()
