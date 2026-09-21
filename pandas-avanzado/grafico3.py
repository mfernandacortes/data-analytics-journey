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
Analizar la evolución de ventas por categoría y año, usando 
(["CategoryName", "Año"]), y graficar el resultado con plt.bar() 
aplicando reset_index().

"""

# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, CategoryID from Products", engine)
o=pd.read_sql("select OrderID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)


# merge:
ca_p=pd.merge(ca,p,on="CategoryID")
cap_od=pd.merge(ca_p,od,on="ProductID")
df=pd.merge(cap_od,o,on="OrderID")

# calcular monto:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])
# sacar el anio con dt:
df["anio"]=df["OrderDate"].dt.year
print(df)

# pivot:
informe=pd.pivot_table(
    df,
    index=["CategoryID", "CategoryName"],
    columns="anio",
    values="monto",
    aggfunc="sum",
    fill_value=0
)

print(informe)

# gráfico:
informe = informe.reset_index()
informe.set_index("CategoryName").plot(kind="bar")
plt.show()
# python grafico3.py

