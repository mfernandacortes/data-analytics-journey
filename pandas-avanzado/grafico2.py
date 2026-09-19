import pandas as pd
from sqlalchemy import create_engine 
import matplotlib.pyplot as plt

# conexión, descomentar según de donde trabaje, por defecto es la de escritorio
engine = create_engine( 
    # ESCRITORIO:
     "mssql+pyodbc://FERCHUSERVER/Northwind?driver=SQL+Server&trusted_connection=yes"
    # NOTEBOOK:
    # "mssql+pyodbc://.\\SQLEXPRESS/Northwind?driver=SQL+Server&trusted_connection=yes"

)

"""
CONSIGNA:
Graficar el total de ventas por categoría de producto en un gráfico de barras, 
usando plt.bar().

"""

# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, CategoryID, ProductName from Products", engine)
od=pd.read_sql("select ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)


# merge:
ca_p=pd.merge(ca,p,on="CategoryID")
df=pd.merge(ca_p, od, on="ProductID")

# calcular monto:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])
agrup=df.copy()

# agrupar por categoria:
agrup=agrup.groupby(["CategoryID","CategoryName"])["monto"].sum().sort_values(ascending=False)

agrup = agrup.reset_index()
plt.bar(agrup["CategoryName"], agrup["monto"])
plt.show()

