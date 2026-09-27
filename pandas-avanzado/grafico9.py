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
Graficar con barras horizontales con los 10 productos más vendidos por Quantity. 
"""

# traer tablas:
p=pd.read_sql("select ProductID, ProductName from Products", engine)
od=pd.read_sql("select ProductID, Quantity from [Order Details]", engine)

# merge:

p_od=pd.merge(p,od,on="ProductID")

# antes de agrupar copio el df:
df=p_od.copy()
df=df.groupby(["ProductID", "ProductName"]).sum()

# ordenar de mayor a menor y mostrar los primeros 10:

df=df.sort_values(by="Quantity", ascending=False).head(10).reset_index()


# gráfico:
import matplotlib.pyplot as plt
df.plot(kind="barh", x="ProductName", y="Quantity")
plt.title("Top 10 Productos Más vendidos")
plt.show()


"""
python grafico9.py

"""