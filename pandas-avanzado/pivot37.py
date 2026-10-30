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
La gerencia pide saber cuánto vendió cada empleado (EmployeeID y LastName en las 
filas) en cada país de los clientes (Country en las columnas).

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
c=pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID, EmployeeID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo=pd.merge(e, o, on="EmployeeID")
eo_c=pd.merge(eo, c, on="CustomerID")
df=pd.merge(eo_c, od, on="OrderID")

# calcular monto:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])

# pivot:
print(df)

"""
python pivot37.py

"""