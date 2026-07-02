"""
Conectar a FERCHUSERVER con SQLAlchemy
Traer la tabla Products con ProductName y UnitPrice
Crear una columna "precio_ars" multiplicando UnitPrice por 1500 usando apply
Crear una columna "rango" con "caro" si UnitPrice es mayor a 50, "barato" si no
Mostrar el resultado con print()

"""

import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traigo tablas que necesito:
prod= pd.read_sql("select ProductID, ProductName, UnitPrice, UnitsInStock from Products", engine)

prod["precio_ars"]=prod["UnitPrice"].apply(lambda x:x * 1500)

#condición: recordando que antes del if va el valor asignado

prod["rango"]=prod["UnitPrice"].apply(lambda x: "caro" if x > 30 else "barato")

print(prod)
"""
Usando la misma tabla Products:

Crear una columna "descuento_10" aplicando un descuento del 10% al UnitPrice usando apply
Crear una columna "estado" con:

"sin stock" si UnitsInStock es 0
"stock bajo" si UnitsInStock es menor a 10
"ok" si no

"""
prod["descuento_10"]= prod["UnitPrice"].apply(lambda x: x * 0.90)

print(prod)
# error (elif no existe en lambda):
# prod["estado"]= prod["UnitsInStock"].apply(lambda x: "sin stock" if x == 0 elif "ok" if x > 10 else "stock bajo")

prod["estado"]=prod["UnitsInStock"].apply(lambda x: "sin stock" if x == 0 else "stock bajo" if x < 10 else "ok")

print(prod)

"""
La sintaxis es correcta. Ejercicio rápido con Northwind:

Traer ProductName y UnitPrice de Products
Crear columna "precio_doble" multiplicando UnitPrice por 2 con apply
Crear columna "rango" con "caro" si UnitPrice > 30, "barato" si no
"""

prod["precio_doble"]=prod["UnitPrice"].apply(lambda x: x * 2)

prod["rango"]= prod["UnitPrice"].apply(lambda x: "caro" if x > 30 else "barato")

print(prod)

"""
Traer ProductName y UnitPrice de Products
Crear columna "impuesto" agregando 21% al UnitPrice con apply
"""

prod["impuesto"]= prod["UnitPrice"].apply(lambda x : x * 1.21)

print(prod)

#  python funciones.py