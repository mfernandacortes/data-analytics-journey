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
El gerente de ventas quiere identificar pedidos que están muy por encima o por 
debajo del promedio habitual de cada empleado, sin perder el detalle de cada 
pedido. Se pide agregar una columna al DataFrame con el monto promedio de cada 
empleado, repetido en cada una de sus filas.

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo=pd.merge(e,o,on="EmployeeID")
eo_od=pd.merge(eo,od,on="OrderID")

# calcular monto:
eo_od["monto"]=eo_od["Quantity"] * eo_od["UnitPrice"] * (1- eo_od["Discount"])

# crear la nueva columna para promedio usando transform:

eo_od["promedio"]=eo_od.groupby(["EmployeeID","LastName"])["monto"].transform("mean")

eo_od["diferencia"]=eo_od["monto"] - eo_od["promedio"]

print(eo_od)
