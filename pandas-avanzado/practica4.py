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
El gerente de ventas quiere saber, por cliente: cuántos pedidos hizo en total, y con 
cuántos empleados distintos trabajó (para ver si siempre lo atiende la misma persona o rota).

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
c=pd.read_sql("select CustomerID, CompanyName from Customers", engine)
o=pd.read_sql("select OrderID, EmployeeID, CustomerID from Orders", engine)

# merge:
eo=pd.merge(e,o,on="EmployeeID")
eo_c=pd.merge(eo,c,on="CustomerID")


# pivot:
eo_c=eo_c.groupby(["CustomerID","CompanyName"]).agg({
    "OrderID":"nunique",
    "EmployeeID":"nunique"
})
print(eo_c)
# python practica4.py
