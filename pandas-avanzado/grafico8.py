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
HALLAZGO:
Hallazgo: En Northwind, la mayoría de las categorías se mantienen relativamente 
estables trimestre a trimestre, pero Beverages y Seafood muestran un pico fuerte 
en el primer trimestre de 1998 (Beverages ronda 2.350, Seafood cerca 
de 1.950), muy por encima de su propio promedio histórico. El resto de las 
categorías (Condiments, Grains/Cereals, Produce) no acompaña ese pico, lo que 
sugiere que no es un fenómeno de temporada generalizado sino algo puntual de esas 
dos categorías en ese trimestre.

"""