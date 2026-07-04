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
prod= pd.read_sql("select ProductID, ProductName, UnitPrice, UnitsInStock, Discontinued from Products", engine)

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

"""
Traer ProductName y UnitPrice de Products
Crear columna "precio_mayorista" aplicando un descuento del 25% con apply
"""
prod["precio_mayorista"]= prod["UnitPrice"].apply(lambda x: x * 0.75)

print(prod)

"""
Sobre el DataFrame de Products de Northwind, crear una columna nueva llamada 
estado_stock que clasifique cada producto según estas condiciones combinadas:

Si UnitsInStock == 0 y Discontinued == 1 → "Sin stock - discontinuado"
Si UnitsInStock == 0 y Discontinued == 0 → "Sin stock - reponer"
Si UnitsInStock > 0 → "Disponible"
"""
prod["Estado_stock"]=prod["UnitsInStock"].apply(lambda x: "Sin stock" if x ==0 else "Disponible")

print(prod)

prod_dfnuevo=prod.copy()
"""
Sobre el DataFrame Products de Northwind, crear una función llamada clasificar_stock que reciba una fila 
y devuelva:

"Sin stock - discontinuado" si UnitsInStock == 0 y Discontinued == 1
"Sin stock - reponer" si UnitsInStock == 0 y Discontinued == 0
"Disponible" si UnitsInStock > 0

Aplicar esa función con apply sobre un DataFrame nuevo (sin tocar el original) y guardar el resultado en una columna llamada estado_stock.
"""
def clasificar(row):
    if row["UnitsInStock"] == 0 and row["Discontinued"] == 1:
        return "Sin stock, discontinuado"
    elif row["UnitsInStock"] ==0 and row["Discontinued"] == 0:
        return "Sin stock, reponer"
    else:
        return "Disponible"


prod_dfnuevo["clasificar_stock"] = prod_dfnuevo.apply(clasificar, axis = 1)

print(prod_dfnuevo)
#  python funciones.py