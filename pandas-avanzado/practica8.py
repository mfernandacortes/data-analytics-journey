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
Consigna: El equipo de RRHH quiere ver, en una sola tabla, el total facturado por empleado 
(filas) y por año (columnas), para evaluar performance año a año.

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo=pd.merge(e,o,on="EmployeeID")
eo_od=pd.merge(eo,od,on="OrderID")
print(eo_od)
# calcular monto:
eo_od["monto"]=eo_od["Quantity"] * eo_od["UnitPrice"] * (1 - eo_od["Discount"])
# agregar columna anio:
eo_od["anio"]=eo_od["OrderDate"].dt.year
# pivot:
informe=pd.pivot_table(
    eo_od,
    index=["EmployeeID","LastName"],
    columns="anio",
    values="monto",
    aggfunc="sum",
    fill_value=0
)
print(informe)
# python practica8.py

"""
HALLAZGO:
Crecimiento fuerte de 1996 a 1997 en casi todos, con caída parcial en 1998 — aunque hay una 
excepción interesante: Dodsworth es el único que sigue creciendo en 1998 (de $26k a $41k), 
mientras que Peacock, que lideraba en 1997 con $128k, cae fuerte a $54k.
"""