import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

"""
Ejercicio:
Usando Northwind:

Cargar Orders y Employees
Hacer merge por EmployeeID
Calcular cuántos pedidos hizo cada empleado (groupby + count)
Mostrar el resultado ordenado de mayor a menor

Pasos:

Cargar las dos tablas
Merge
Groupby + count
Ordenar

"""

# traigo tablas que necesito:
od= pd.read_sql("Select OrderID, EmployeeID from Orders", engine)
emp= pd.read_sql("Select EmployeeID, LastName from Employees", engine)

od_emp=pd.merge(od, emp, on="EmployeeID")
od_emp=od_emp.groupby(["EmployeeID", "LastName"])["OrderID"].count()

print(od_emp.sort_values(ascending=False))

# python combinados9.py
