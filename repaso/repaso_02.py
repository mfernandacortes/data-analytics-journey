"""
Encontrar los 5 empleados que más ingresos generaron, mostrando solo los que superan el promedio general de ventas, ordenados de mayor a menor.

Conectar a Northwind con SQLAlchemy
Traer las tablas que necesitás
Calcular el monto total por empleado
Filtrar y ordenar
"""
import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traer tablas:
ordenes = pd.read_sql("select OrderID, EmployeeID from Orders", engine)
items = pd.read_sql("select OrderID, UnitPrice, Quantity from [Order Details]", engine)

empleados = pd.read_sql("select EmployeeID, LastName from Employees", engine)

# merge de tablas:
ordenes_item = ordenes.merge(items, on="OrderID") 
ordenes_item_emp = ordenes_item.merge(empleados, on="EmployeeID")

#group by:

ordenes_item_emp["monto"] = ordenes_item_emp["UnitPrice"] * ordenes_item_emp["Quantity"]
ordenes_item_emp=ordenes_item_emp.groupby(["EmployeeID", "LastName"])["monto"].sum().reset_index()

print(ordenes_item_emp)
#filtrar por 5 mejores empleados que hayan vendido por encima del promedio:

cinco_emp=ordenes_item_emp[ordenes_item_emp["monto"] > ordenes_item_emp["monto"].mean()] 

print(cinco_emp.sort_values("monto", ascending= False))

# Hallazgo: solo 4 empleados superan el promedio general de ventas
# Peacock lidera con $250.187 — más del doble que los empleados de menor rendimiento
