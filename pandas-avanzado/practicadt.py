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
El equipo comercial necesita saber en qué meses se concentran más pedidos, 
para poder anticipar stock y personal en esos períodos. Se pide identificar 
el mes de cada pedido y contar cuántos pedidos hay por mes.

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("Select OrderID, EmployeeID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo=pd.merge(e,o,on="EmployeeID")
eo_od=pd.merge(eo,od,on="OrderID")

# calcular monto:
eo_od["monto"]=eo_od["Quantity"] * eo_od["UnitPrice"] * (1 - eo_od["Discount"])

print(eo_od)

#  python practicadt.py
