import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traer tablas que necesito:

p = pd.read_sql("Select ProductID, ProductName, UnitPrice, UnitsInStock from Products", engine)


"""
Usar el DataFrame de Products de Northwind (columnas UnitPrice y UnitsInStock) para crear 
una función llamada evaluar_producto que reciba una fila y devuelva:

- "Reponer urgente" si UnitsInStock es menor a 10 y UnitPrice es mayor a $20
- "Reponer" si UnitsInStock es menor a 10 (y no cumple la condición anterior)
- "Stock ok" en cualquier otro caso

Aplicar esa función con apply sobre un DataFrame nuevo (sin tocar el original), guardando 
el resultado en una columna llamada estado.

"""
prod = p.copy()

def evaluar_producto(row):
    if (row["UnitsInStock"] < 10) & (row["UnitPrice"] > 20):
            return "Reponer Urgente"
    elif row["UnitsInStock"] < 10:
            return "Reponer"
    else:
            return "Stock ok"


prod["estado"]=prod.apply(evaluar_producto, axis = 1)

print(prod)

#  python evaluacion2.py