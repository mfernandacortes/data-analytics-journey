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

## HALLAZGO:
# En Northwind los precios están muy concentrados en lo barato. Más de 50 de los 
# 78 productos cuestan menos de unos $28, y hay un caso extremo: Côte de Blaye, 
# a $263,50, más del doble que el segundo más caro (Thüringer Rostbratwurst, 
# $123,79).

# Cruzando con el top 10 de cantidades, Côte de Blaye no figura entre los más 
# vendidos por unidades. En cambio Raclette Courdavault ($55) y Tarte au sucre 
# ($49,30) aparecen en las dos listas: están entre los más caros y también entre 
# los más vendidos. Con estos gráficos no se puede saber cuál pesa más en la 
# facturación, porque eso pide combinar precio y cantidad (Quantity * UnitPrice).
