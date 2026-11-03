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
La gerencia pide ver cuántas unidades (Quantity) vendió cada empleado (EmployeeID y 
LastName en las filas) con cada transportista (CompanyName en las columnas).

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
sh=pd.read_sql("select ShipperID, CompanyName from Shippers", engine)
o=pd.read_sql("select OrderID, ShipVia, EmployeeID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity from [Order Details]", engine)

# merge:
eo=pd.merge(e, o, on="EmployeeID")
eo_sh=pd.merge(eo, sh, left_on="ShipVia", right_on="ShipperID")
df=pd.merge(eo_sh, od, on="OrderID")

print(df)

# pivot:
informe=pd.pivot_table(
    df,
    index=["EmployeeID", "LastName"],
    columns=["ShipperID", "CompanyName"],
    values="Quantity",
    aggfunc="sum",
    fill_value=0
)

print(informe)

"""
python pivot40.py

"""