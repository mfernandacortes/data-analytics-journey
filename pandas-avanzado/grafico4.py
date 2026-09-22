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
Analizar el total vendido por país de cliente y trimestre, armando un pivot 
con index="Trimestre", columns="Country", values="monto", y graficarlo con 
.plot(kind="bar").

"""

# traer tablas:
c=pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
co=pd.merge(c,o,on="CustomerID")
co_od=pd.merge(co,od,on="OrderID")

# calcular monto:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])
co_od["trimestre"]=co_od["OrderDate"].dt.quarter
# pivot:
print(co_od)
informe=pd.pivot_table(
    co_od,
    index="Country",
    columns="trimestre",
    values="monto",
    aggfunc="sum",
    fill_value=0
)

print(informe)
# para el gráfico voy a invertir el pivot:
informe2=pd.pivot_table(
    co_od,
    index="trimestre",
    columns="Country",
    values="monto",
    aggfunc="sum",
    fill_value=0
)

# gráfico:
import matplotlib.pyplot as plt

informe2.plot(kind="bar")
# correr la referencia de paises:
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
"""
python grafico4.py
"""