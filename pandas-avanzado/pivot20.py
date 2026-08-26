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
Mostrar, por transportista (Shippers), el monto total y el monto promedio de 
las líneas de pedido, para saber cuál mueve más volumen y cuál tiene los 
pedidos de mayor valor.

Ojo: Orders.ShipVia se relaciona con Shippers.ShipperID — nombres de columna 
distintos, así que vas a necesitar left_on/right_on en ese merge

"""

# traer tablas:
s=pd.read_sql("select ShipperID, CompanyName from Shippers", engine)
o=pd.read_sql("select OrderID, ShipVia from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
so=pd.merge(s,o,left_on="ShipperID", right_on="ShipVia")
so_od=pd.merge(so,od,on="OrderID")

# calcular monto:
so_od["monto"]=so_od["Quantity"] * so_od["UnitPrice"] * (1 - so_od["Discount"])
print(so_od)

# pivot:
# python pivot20.py

"""
HALLAZGO:

"""