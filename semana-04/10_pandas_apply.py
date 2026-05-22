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
Ejercicio — Clasificar pedidos por tamaño y calcular comisión
Pregunta de negocio: ¿Cuánto comisión le corresponde a cada empleada según el tamaño de sus pedidos?
Regla de negocio:

Pedido menor a $500 → comisión 3%
Pedido entre $500 y $2000 → comisión 5%
Pedido mayor a $2000 → comisión 8%

"""
# 2 Cargo tablas: Order, Order Details y Employees

od = pd.read_sql("SELECT OrderID, UnitPrice, Quantity, Discount FROM [Order Details]", conn)
ordenes       = pd.read_sql("SELECT OrderID, EmployeeID FROM Orders", conn)
empleados     = pd.read_sql("SELECT EmployeeID, LastName FROM Employees", conn)

# 3 Calcular Monto (por OrderID)

od['Monto'] = (od['Quantity'] * od['UnitPrice'] * (1 - od['Discount']))


# 4 Agrupar por OrderID, para eso tengo que hacer merges
od_ordenes = pd.merge(od, ordenes, on= 'OrderID')
od_ordenes = pd.merge(od_ordenes, empleados, on = 'EmployeeID')

# 5 Análisis:
#total_clientes = od_ordenes.groupby(['CustomerID', 'CompanyName'])['Monto'].sum().reset_index().sort_values('Monto', ascending=False)
#total_clientes = od_ordenes.groupby(['OrderID'], ['EmployeeID']) ['Monto'].sum().reset_index().sort_values('Monto', ascending = False)
total_clientes = od_ordenes.groupby(['OrderID', 'EmployeeID'])['Monto'].sum().reset_index().sort_values('Monto', ascending=False)
# print(total_clientes)
# Mergear con empleados para traer el apellido de cada uno...
total_clientes= pd.merge(total_clientes, empleados, on = 'EmployeeID')
# ahora defino una función según la regla de negocio:
def clasificar_pedido(monto):
    if monto < 500:
        return 'Chico'
    elif monto <= 2000:
        return 'Mediano'
    else:
        return 'Grande'

# ahora aplico la función creada a Monto (nombre dataframe, creo columna tamaño), y ejecuto la función:
total_clientes['tamaño'] = total_clientes['Monto'].apply(clasificar_pedido)




# calcular la comisión: crear función
def calcular_comision(monto):
    if monto < 500:
        return monto * 0.03
    elif monto <= 2000:
        return monto * 0.05
    else:
        return monto * 0.08
# aplicarla y crear columna comisión
total_clientes['comision'] = total_clientes['Monto'].apply(calcular_comision)

# muestro:
print(total_clientes)
# cuanto cobra de comisión cada empleado:
print(total_clientes.groupby('LastName')['comision'].sum().round(2).sort_values(ascending=False))
# python 10_pandas_apply.py