import pandas as pd
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=FERCHUSERVER;'
    'DATABASE=Northwind;'
    'Trusted_Connection=yes;'
)


ordenes = pd.read_sql("SELECT OrderID, EmployeeID, OrderDate, ShippedDate FROM Orders", conn)

empleados = pd.read_sql("SELECT * FROM Employees", conn)

ordenes['dias_entrega'] = (ordenes['ShippedDate'] - ordenes['OrderDate']).dt.days

ordenes['urgente'] = ordenes['dias_entrega'] <= 3

print(ordenes.head(10))

print(ordenes['urgente'].value_counts())

empleados_ordenes= pd.merge(empleados, ordenes, on='EmployeeID')
print(empleados_ordenes.groupby('LastName')['urgente'].sum().sort_values(ascending=False))

