"""
========================================
EJERCICIO: Conexión a SQL Server con pandas
Semana 04 - Data Analytics Journey
========================================

Base de datos: Northwind (SQL Server)
Objetivo: Leer tablas SQL con pandas usando read_sql()

Tablas consultadas:
- Customers: datos de clientes
- Employees: datos de empleados

Nota: El código genera un UserWarning porque pandas recomienda
usar SQLAlchemy en lugar de una conexión directa. 
Es algo que voy a incorporar más adelante.
"""

import pandas as pd
import pyodbc

# Conexión a Northwind
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=FERCHUSERVER;'
    'DATABASE=Northwind;'
    'Trusted_Connection=yes;'
)

# Traer tabla Customers completa
clientes = pd.read_sql("SELECT * FROM Customers", conn)

# Ver las primeras 5 filas
print(clientes.head())

# Traer la tabla Employees completa

empleados = pd.read_sql("SELECT * FROM Employees", conn)

#Ver las primeras 5 filas
print(empleados.head())

clientes = pd.read_sql("SELECT * FROM Customers", conn)

# Ejercicio 1
print(clientes['CompanyName'])

# Ejercicio 2  
print(clientes[['CompanyName', 'City', 'Country']])

# Ejercicio 3: mostrar clientes solo de Argentina

#--clientes_arg = clientes[clientes['Country'] == 'Argentina']
#print(clientes_arg[['CompanyName', 'City']])
# python 02_pandas_clientes.py
# Ejercicio 4: clientes de Germany en una sola línea

print(clientes[clientes['Country']=='Germany'][['CompanyName','ContactName']])

#Ejercicio 5: elegir de la ciudad de Berlín y CompanyName, City y ContactName

# hice yo (bien razonamiento): print(clientes[clientes['Country']]==('Germany') & ('City'=='Berlin')[['CompanyName', 'City', 'ContactName']])

# correcto:
print(clientes[(clientes['Country'] == 'Germany') & (clientes['City'] == 'Berlin')][['CompanyName', 'City', 'ContactName']])