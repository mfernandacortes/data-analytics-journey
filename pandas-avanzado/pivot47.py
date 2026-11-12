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
La gerencia pide ver cuánto vendió cada empleado (EmployeeID y LastName en las filas) de los productos 
de cada país de proveedor (Country de Suppliers en las columnas), con monto = UnitPrice * Quantity * 
(1 - Discount).

"""

# traer tablas:
su=pd.read_sql("select SupplierID, CompanyName, Country from Suppliers", engine)
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
p=pd.read_sql("select ProductID, SupplierID from Products", engine)
o=pd.read_sql("select OrderID, EmployeeID from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
su_p=pd.merge(su, p, on="SupplierID")
sup_od=pd.merge(su_p, od, on="ProductID")
supod_o=pd.merge(sup_od, o, on="OrderID")
df=pd.merge(supod_o, e, on="EmployeeID")

# calcular monto:
print(df)

# pivot:


"""

python pivot47.py

"""