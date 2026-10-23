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
filas) con cada transportista (CompanyName en las columnas).

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
sh=pd.read_sql("select ShipperID, CompanyName from Shippers", engine)
o=pd.read_sql("select OrderID, EmployeeID, ShipVia from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo=pd.merge(e, o, on="EmployeeID")
eo_sh=pd.merge(eo, sh, left_on="ShipVia", right_on="ShipperID")
df=pd.merge(eo_sh, od, on="OrderID")

print(df)
# calcular monto:


# pivot: 


"""
python pivot30.py

"""