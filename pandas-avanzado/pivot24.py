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
Mostrar el monto vendido por empleado (EmployeeID y LastName en las filas) y por 
categoría (CategoryName en las columnas), con monto = UnitPrice * Quantity * 
(1 - Discount).

"""

# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, CategoryID, ProductName from Products", engine)
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
ca_p=pd.merge(ca, p, on="CategoryID")
cap_od=pd.merge(ca_p, od, on="ProductID")
capod_o=pd.merge(cap_od, o, on="OrderID")
df=pd.merge(capod_o, e, on="EmployeeID")
print(df)
# calcular monto:


# pivot:


"""
python pivot24.py

"""