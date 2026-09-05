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
CONSIGNA: (continuación practica4.py):
al reporte de pedidos y empleados distintos por cliente, agregarle el monto total facturado,
mostrando tanto la suma como el promedio.

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
c=pd.read_sql("select CustomerID, CompanyName from Customers", engine)
o=pd.read_sql("select OrderID, EmployeeID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo=pd.merge(e,o,on="EmployeeID")
eo_c=pd.merge(eo,c,on="CustomerID")
eoc_od=pd.merge(eo_c,od,on="OrderID")

# calcular monto:
eoc_od["monto"]=eoc_od["Quantity"] * eoc_od["UnitPrice"] * (1 - eoc_od["Discount"])
df=eoc_od.copy()
eoc_od=eoc_od.groupby(["CustomerID","CompanyName"]).agg({
    "OrderID":"nunique",
    "EmployeeID":"nunique",
    "monto":["sum","mean"]
})
# print(eoc_od)
"""
Consigna: Encontrar cuál pedido de ALFKI no tiene ningún producto cargado en Order Details.

Pasos:

Filtrar los pedidos de Orders donde CustomerID == "ALFKI".
Hacer un merge con Order Details usando how="left".
Filtrar con .isna() sobre alguna columna de Order Details (por ejemplo Quantity) para 
encontrar el pedido sin match.
"""
#     python practica5.py

do=o.copy()
do=pd.merge(do,od,on="OrderID", how="left")
print(do[do["CustomerID"]=='ALFKI'])


