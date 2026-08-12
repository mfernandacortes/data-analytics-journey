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
Tablas: Employees, Orders, Order Details.

Traer las tres con read_sql (traer OrderDate de Orders, y LastName + EmployeeID de Employees).
Merge encadenado:
  1) Order Details + Orders (por OrderID)
  2) + Employees (por EmployeeID) → para tener LastName

Columna calculada: monto = Quantity * UnitPrice * (1 - Discount)
Columna calculada: anio = usar .dt.year sobre OrderDate

PIVOT:
Con pd.pivot_table, armar una tabla cruzada:
  - index = LastName (empleados en filas)
  - columns = anio (años en columnas)
  - values = monto
  - aggfunc = "sum"
  - fill_value = 0

Guardar el resultado en una variable nueva.
"""
# merge:

# monto:

# python pivot2.py