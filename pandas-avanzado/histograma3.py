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
Histograma de Quantity vendida por pedido (de Order Details), para ver si la 
mayoría de los pedidos son de pocas unidades o de muchas.

Mismo patrón: sin merge, directo sobre Order Details, columna Quantity

"""

# traer tablas:
od=pd.read_sql("select OrderID, Quantity from [Order Details]", engine)



# gráfico:
import matplotlib.pyplot as plt

od["Quantity"].plot(kind="hist")
plt.title("Cantidades")
plt.show()

"""
HALLAZGO: Distribución de cantidades por pedido (Quantity): La mayoría de las 
líneas de pedido son de pocas unidades (hasta 25-30). Muy pocos pedidos llegan 
a cantidades grandes (80-130), lo que sugiere que el grueso del negocio son 
ventas chicas y frecuentes, no pocos pedidos grandes.

"""