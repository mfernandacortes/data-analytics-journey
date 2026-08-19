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
Cliente: "Quiero ver, para cada empleado, cuántos pedidos distintos gestionó 
y cuál fue el monto promedio de esos pedidos, separado por trimestre."


"""

# traer tablas:
e=pd.read_sql("Select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("Select OrderID, EmployeeID, OrderDate from Orders", engine)
od=pd.read_sql("Select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo=pd.merge(e,o,on="EmployeeID")
eo_od=pd.merge(eo,od,on="OrderID")

# calcular monto:
print(eo_od)

# pivot:


"""
HALLAZGO:

"""