import pandas as pd
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=FERCHUSERVER;'
    'DATABASE=Northwind;'
    'Trusted_Connection=yes;'
)


empleados = pd.read_sql("SELECT * FROM Employees", conn)
ordenes = pd.read_sql("SELECT * FROM Orders", conn)
order_details = pd.read_sql("SELECT * FROM [Order Details]", conn)

# Unir Employees con Orders por EmployeeID:
empleados_ordenes= pd.merge(empleados, ordenes, on='EmployeeID')

# Unir el resultado con Order Details por OrderID
emp_or_det = pd.merge(empleados_ordenes, order_details, on='OrderID')

print(emp_or_det.shape) #acá muestra por tuplas

#ahora calcular como en SQL agregación SUM:
#cli_od['Monto'] = cli_od['UnitPrice'] * cli_od['Quantity'] * (1 - cli_od['Discount'])
emp_or_det['Monto'] = emp_or_det['UnitPrice'] * emp_or_det['Quantity'] * (1- emp_or_det['Discount'])

print(emp_or_det.shape) #muestra ordenado por tuplas
#mostrar calculo para chequear}
print(emp_or_det['Monto'].head())

#correr el groupby
print(emp_or_det.groupby(['EmployeeID','LastName']).agg({'Monto': ['sum', 'mean', 'count']}).sort_values(('Monto', 'sum'), ascending=False))

#

# python 05_pandas_empleados_revenue.py