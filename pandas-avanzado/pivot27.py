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
Mostrar las unidades vendidas (Quantity) por empleado (EmployeeID y LastName 
en las filas) y por año (en las columnas).
"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity from [Order Details]", engine)

# merge:
eo=pd.merge(e, o, on="EmployeeID")
eo_od=pd.merge(eo, od, on="OrderID")

# año:
eo_od["anio"]=eo_od["OrderDate"].dt.year

print(eo_od)

# pivot:
informe=pd.pivot_table(
    eo_od,
    index=["EmployeeID", "LastName"],
    columns="anio",
    values="Quantity",
    aggfunc="sum",
    fill_value=0
)

print(informe)
