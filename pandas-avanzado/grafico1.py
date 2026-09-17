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
Graficar la evolución de ventas mensuales de Northwind con matplotlib.

"""

# traer tablas:
o=pd.read_sql("select OrderID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)


# merge:
o_od=pd.merge(o,od,on="OrderID")

# calcular monto:
o_od["monto"]=o_od["Quantity"] * o_od["UnitPrice"] * (1 - o_od["Discount"])
df=o_od.copy()

# mes:
df['anio'] = df['OrderDate'].dt.year
df['mes'] = df['OrderDate'].dt.month
ventas_mensuales = df.groupby(['anio', 'mes'])['monto'].sum()

# gráfico
import matplotlib.pyplot as plt

plt.plot(ventas_mensuales.values)
plt.title('Ventas mensuales')
plt.show()
# python grafico1.py


"""
HALLAZGO:

"""