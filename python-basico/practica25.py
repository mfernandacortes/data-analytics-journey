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
Tablas: Orders, Order Details, Customers.

Cargá las tres con read_sql (acordate: SELECT * FROM [Order Details] con corchetes por el espacio en el nombre).
Merge en dos pasos: Order Details + Orders por OrderID, y ese resultado + Customers por CustomerID.
Columna calculada: monto = Quantity * UnitPrice * (1 - Discount).
Agrupá por Country (la de Customers) y en un solo agg:
monto_total → sum de monto
ticket_promedio → mean de monto
pedidos → nunique de OrderID
clientes → nunique de CustomerID
Ordená de mayor a menor por monto_total.
Con apply + def (axis=1), agregá una columna mercado:
"Clave" si monto_total supera 100000
"Medio" si supera 30000 (y no es clave)
"Chico" en cualquier otro caso

"""

# traer tablas:
c=pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from[Order Details]", engine)

# merge:
co=pd.merge(c,o,on="CustomerID")
co_od=pd.merge(co,od, on="OrderID")


# calcular monto:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])

# agrupar y agg:
agrup_pais=co_od.copy()
agrup_pais=agrup_pais.groupby("Country").agg(
    monto_total =("monto","sum"),
    ticket_promedio=("monto","mean"),
    pedidos = ("OrderID","nunique"),
    clientes = ("CustomerID","nunique")
)
print(agrup_pais)
# python practica25.py
# ordenar:


# clasificar (apply):


"""
HALLAZGO:

"""