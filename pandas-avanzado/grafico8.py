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
Crear línea mensual de Quantity, abierta por categoría (usando CategoryName, no ID).

"""

# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, CategoryID, ProductName from Products", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity from [Order Details]", engine)
o=pd.read_sql("Select OrderID, OrderDate from Orders", engine)
# merge:
ca_p=pd.merge(ca, p, on="CategoryID")
cap_od=pd.merge(ca_p, od, on="ProductID")
df=pd.merge(cap_od, o, on="OrderID")

# nueva columna de mes y anio:
df["anio"]=df["OrderDate"].dt.year
df["trimestre"]=df["OrderDate"].dt.quarter

print(df)

# pivot:
informe=pd.pivot_table(
    df,
    index=["anio","trimestre"],
    columns="CategoryName",
    values="Quantity",
    aggfunc="sum",
    fill_value=0
)

print(informe)
# gráfico:
import matplotlib.pyplot as plt
informe.plot()
plt.title('Ventas trimestrales por año por categoría')
plt.show()
"""
python grafico8.py

"""