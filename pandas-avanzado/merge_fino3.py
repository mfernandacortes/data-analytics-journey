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
Usando un merge tipo left con indicator=True, encontrar los empleados que nunca 
tuvieron un pedido asignado (Employees sin match en Orders).

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID from Orders", engine)

# merge:
eo=pd.merge(e,o,on="EmployeeID", how="left", indicator=True)

# filtro para encontrar los empleados sin pedido:
emp_sin_pedidos = eo[eo["_merge"] == "left_only"]
print(emp_sin_pedidos)

# python merge_fino3.py

"""
HALLAZGO:

Se encontró sólo un registro (Nro 11: Prueba) para probar consultas que hice, 
que no existe ningún empleado sin pedidos y la consulta funciona bien ya que 
devuelve solo el registro de prueba.
"""
