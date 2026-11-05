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
LastName en las filas) en cada categoría de producto (CategoryName en las columnas).

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity from [Order Details]", engine)
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, CategoryID, ProductName from Products", engine)

# merge:
eo=pd.merge(e,o,on="EmployeeID")
eo_od=pd.merge(eo, od, on="OrderID")
ca_p=pd.merge(eo_od, p, on="ProductID")
df=pd.merge(ca_p, ca, on="CategoryID")
# calcular monto:
print(df)

# pivot:
informe=pd.pivot_table(
    df,
    index=["EmployeeID", "LastName"],
    columns=["CategoryID", "CategoryName"],
    values="Quantity",
    aggfunc="sum",
    fill_value=0
)

print(informe)
"""

python pivot41.py
"""