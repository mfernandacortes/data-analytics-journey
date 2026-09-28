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
Comparar precios de todos los productos.

"""

# traer tablas:
p=pd.read_sql("select ProductID, ProductName, UnitPrice from Products", engine)



# gráfico:
import matplotlib.pyplot as plt
p["UnitPrice"].plot(kind="hist")
plt.title("Comparar precios")
plt.show()



"""
HALLAZGO:
la primera barra dice que más de 50 productos cuestan menos de unos $27. 
La segunda, unos 19 entre $27 y $53. Después casi nada, y hay uno solo por 
los $250. O sea: la mayoría son baratos y hay un par de caros que estiran 
el gráfico hacia la derecha.

"""