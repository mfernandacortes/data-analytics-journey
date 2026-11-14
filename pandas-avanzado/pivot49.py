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
La gerencia pide ver cuántos pedidos (OrderID) tomó cada empleado (EmployeeID y LastName en las filas) 
por año (en las columnas).

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID, OrderDate from Orders", engine)

# merge:
eo=pd.merge(e, o, on="EmployeeID")

# año:
eo["anio"]=eo["OrderDate"].dt.year

print(eo)

# pivot:
informe=pd.pivot_table(
    eo,
    index=["EmployeeID", "LastName"],
    columns="anio",
    values="OrderID",
    aggfunc="nunique",
    fill_value=0
)

print(informe)
