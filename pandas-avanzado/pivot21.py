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
Necesito saber en qué trimestre se concentran más pedidos, y qué día de la semana 
tiene más movimiento — para planificar mejor la carga de personal.

Partí de tu eo_od (o el que tengas a mano con OrderDate), agregá dos columnas 
nuevas —trimestre y nombre del día— y con eso armá un value_counts()

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo=pd.merge(e,o,on="EmployeeID")
eo_od=pd.merge(eo,od,on="OrderID")

# calcular monto:
eo_od["monto"]= eo_od["Quantity"] * eo_od["UnitPrice"] * (1 - eo_od["Discount"])

print(eo_od)

# pivot:
# python pivot21.py

"""
HALLAZGO:

"""