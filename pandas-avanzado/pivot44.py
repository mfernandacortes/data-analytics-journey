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

La gerencia comercial quiere saber en qué categorías se especializa cada vendedor.
Pide ver cuánto vendió cada empleado (EmployeeID y nombre completo en las filas)
en cada categoría de producto (CategoryName en las columnas),
con monto = UnitPrice * Quantity * (1 - Discount).

"""

# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, ProductName, CategoryID from Products", engine)
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
ca_p=pd.merge(ca, p, on="CategoryID")
cap_od=pd.merge(ca_p, od, on="ProductID")
capod_o=pd.merge(cap_od, o, on="OrderID")
df=pd.merge(capod_o, e, on="EmployeeID")


print(df)
print(df.isnull().sum())
# calcular monto:


# pivot:


"""
python pivot44.py

"""