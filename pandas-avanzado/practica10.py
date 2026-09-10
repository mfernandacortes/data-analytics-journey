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
Necesito ver, para cada empleado, el total de ventas y la cantidad de pedidos distintos 
que manejó, desglosado por año.

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)
# merge:
eo=pd.merge(e, o, on="EmployeeID")
eo_od=pd.merge(eo,od,on="OrderID")

# calcular monto:
eo_od["monto"]=eo_od["Quantity"] * eo_od["UnitPrice"] * (1 - eo_od["Discount"])
eo_od["anio"]=eo_od["OrderDate"].dt.year
# pivot:
informe=pd.pivot_table(
    eo_od,
    index=["EmployeeID","LastName"],
    columns="anio",
    values=["monto","OrderID"],
    aggfunc={"monto":"sum","OrderID":"nunique"},
    fill_value=0
)
# python practica10.py
print(informe)
