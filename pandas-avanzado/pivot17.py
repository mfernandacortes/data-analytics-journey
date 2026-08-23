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
Consigna (cliente):

Un gerente de ventas pide un reporte que muestre, por empleado y por año, 
el monto total facturado y la cantidad de pedidos distintos que gestionó 
cada uno. El reporte debe incluir los totales generales por empleado y por año, 
y las combinaciones sin ventas registradas deben mostrarse como cero, no en blanco.

"""

# traer tablas:
e=pd.read_sql("Select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("Select OrderID, EmployeeID, OrderDate from Orders", engine)
od=pd.read_sql("Select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo=pd.merge(e,o,on="EmployeeID")
eo_od=pd.merge(eo,od,on="OrderID")

# calcular monto:
eo_od["monto"]=eo_od["Quantity"] * eo_od["UnitPrice"] * (1 - eo_od["Discount"])
# trear el año:
eo_od["anio"]=eo_od["OrderDate"].dt.year

# pivot:
informe=pd.pivot_table(
    eo_od,
    index=["EmployeeID", "LastName"],
    columns="anio",
    values=["monto", "OrderID"],
    aggfunc={"monto":"sum","OrderID":"nunique"},
    margins= True,
    margins_name="Total",
    fill_value=0
)
print(informe)
# python pivot17.py
