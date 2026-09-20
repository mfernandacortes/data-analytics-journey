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
El área comercial 
necesita un informe que cruce la información de pedidos, detalle de productos 
vendidos y datos de clientes, para poder evaluar el volumen de compra de 
cada cliente y clasificar los pedidos según su magnitud.

Objetivo:
Armar un pipeline de datos que permita responder: "¿cuáles son los pedidos 
más importantes y qué clientes los generan?"

"""

# traer tablas:
c=pd.read_sql("select CustomerID, CompanyName from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)
# merge:
co=pd.merge(c,o,on="CustomerID")
co_od=pd.merge(co,od,on="OrderID")

# calcular monto:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])

# mostrar:
print(co_od)

"""
python practica12.py

"""