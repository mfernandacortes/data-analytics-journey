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
Calcular el total de Quantity vendida por país de cliente (Country), 
usando groupby puro (no pivot). Ordenar de mayor a menor.

"""

# traer tablas:
c=pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity from [Order Details]", engine)

# merge:
co=pd.merge(c,o,on="CustomerID")
co_od=pd.merge(co,od,on="OrderID")

# agrupar por cantidades:
co_od=co_od.groupby("Country")["Quantity"].sum()

# ordenar:
co_od = co_od.sort_values(ascending=False)
co_od=co_od.head(10)
print(co_od)

# grafico:
import matplotlib.pyplot as plt

co_od.plot(kind="pie")
plt.title("Cantidades vendidas por pais")
plt.ylabel("")
plt.show()

"""
python grafico_torta1.py

"""