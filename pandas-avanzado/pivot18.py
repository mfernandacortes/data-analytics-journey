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
Generar un reporte por empleado que muestre, en una sola tabla, el monto total 
facturado y el monto promedio de sus líneas de pedido — para poder comparar 
ambas métricas lado a lado.

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID  from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)
# merge:
eo=pd.merge(e,o,on="EmployeeID")
eo_od=pd.merge(eo,od,on="OrderID")

# calcular monto:
eo_od["monto"]=eo_od["Quantity"] * eo_od["UnitPrice"] * (1 - eo_od["Discount"])

# pivot:
print(eo_od)
# python pivot18.py
"""
HALLAZGO:

"""