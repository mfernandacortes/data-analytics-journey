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
El gerente quiere una columna que clasifique cada pedido como "con descuento" o "sin 
descuento", pero además marque como "descuento alto" si el descuento supera el 15%.

"""

# traer tablas:

o=pd.read_sql("select OrderID, EmployeeID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
df=pd.merge(o,od, on="OrderID")

print(df)

#     python practica6.py



