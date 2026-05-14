import pandas as pd
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=FERCHUSERVER;'
    'DATABASE=Northwind;'
    'Trusted_Connection=yes;'
)

clientes = pd.read_sql("SELECT * FROM Customers", conn)
ordenes = pd.read_sql("SELECT * FROM Orders", conn)
order_details = pd.read_sql("SELECT * FROM [Order Details]", conn)

print(order_details.head())

# Unir Orders con Order Details:
ordenes_detalles= pd.merge(ordenes, order_details, on='OrderID')

# Unir el resultado con Customers por CustomerID (clientes)

cli_od = pd.merge(clientes, ordenes_detalles, on='CustomerID') # cli_od: se guarda el join de customers mas el join anterior ordenes_detalles

print(cli_od.shape) #acá muestra por tuplas

#ahora calcular como en SQL agregación SUM:
cli_od['Monto'] = cli_od['UnitPrice'] * cli_od['Quantity'] * (1 - cli_od['Discount'])

print(cli_od.shape) #muestra ordenado por tuplas
#mostrar calculo para chequear}
print(cli_od['Monto'].head())

#correr el groupby
print(cli_od.groupby('Country').agg({'Monto': 'sum'}).sort_values('Monto', ascending=False))

#

#ejercicio: correr varias funciones agregación en misma columna
print(cli_od.groupby('Country').agg({'Monto': ['sum', 'mean', 'count']}).sort_values(('Monto', 'sum'), ascending=False))

