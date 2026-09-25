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
Graficar la evolución mensual de la cantidad total de unidades vendidas (Quantity) 
en Northwind, como línea, con título.

"""

# traer tablas:
o=pd.read_sql("select OrderID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity from [Order Details]", engine)

# merge:
o_od=pd.merge(o,od,on="OrderID")

# columna año y mes:
o_od["anio"]=o_od["OrderDate"].dt.year
o_od["mes"]=o_od["OrderDate"].dt.month


# pivot:
print(o_od)

"""
python grafico7.py

"""