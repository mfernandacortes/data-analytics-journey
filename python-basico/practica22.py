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
ANÁLISIS 1 — EMPLEADOS

1. Traer las tablas Employees, Orders y Order Details.
2. Merge de las tres por sus claves.
3. Calcular monto (Quantity * UnitPrice * (1 - Discount)).
4. Agrupar por EmployeeID y LastName con named aggregation, creando:
   - facturacion_total (suma de monto)
   - ticket_promedio (promedio de monto)
   - pedidos (nunique de OrderID)
5. Ordenar por facturación total, de mayor a menor.

"""
# traer tablas:
e=pd.read_sql("Select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("Select OrderID, EmployeeID from Orders", engine)
od=pd.read_sql("Select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo=pd.merge(e,o,on="EmployeeID")
eo_od=pd.merge(eo,od,on="OrderID")


# calcular monto:
eo_od["monto"]=eo_od["Quantity"] * eo_od["UnitPrice"] * (1 - eo_od["Discount"])
# agrupar y agg:
agrup_emp=eo_od.copy()
agrup_emp=agrup_emp.groupby(["EmployeeID","LastName"]).agg(
        facturacion_total=("monto", "sum"),
        ticket_promedio=("monto", "mean"),
        pedidos=("OrderID","nunique")
)
 
print(agrup_emp)
# ordenar:


# clasificar (apply):
# python practica22.py

"""
HALLAZGO:

"""