import pandas as pd
import pyodbc
import numpy as np

#pd.set_option('display.max_rows', None) #para no mostrar todas las filas...

# 1. CONEXIÓN
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=FERCHUSERVER;'
    'DATABASE=Northwind;'
    'Trusted_Connection=yes;'
)

"""
Ejercicio: Detectar empleados sin pedidos Y pedidos sin empleado asignado
Pregunta de negocio: ¿Hay empleadas que nunca gestionaron un pedido, 
o pedidos que quedaron sin empleado asignado?

"""
#1: traigo las tablas que necesito
empleados = pd.read_sql("SELECT EmployeeID, LastName FROM Employees", conn)
ordenes   = pd.read_sql("SELECT OrderID, EmployeeID FROM Orders", conn)

#2: Hago merge con las tablas (las uno, en este caso 
# con outer trae todo: filas con y sin match de ambas tablas (muestra los 2 lados, puedo
# usar un solo merge para ver todo y de ahí usar 2 filtros distintos)
emp_ordenes = pd.merge(empleados, ordenes, on = 'EmployeeID', how='outer')

#3: Ahora filtro: empleados sin ordenes:
emp_ordenes = emp_ordenes[emp_ordenes['OrderID'].isna()]

#4: Ahora filtro ordenes que no tienen empleados asignados:
sin_empleados = emp_ordenes[emp_ordenes['EmployeeID'].isna()]


print(emp_ordenes)

print(sin_empleados)

# python 12_pandas_outer.py