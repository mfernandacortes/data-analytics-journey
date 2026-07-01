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
prod= pd.read_sql("select ProductID, ProductName, UnitPrice from Products", engine)

prod["precio_ars"]=prod["UnitPrice"].apply(lambda x:x * 1500)

#condición: recordando que antes del if va el valor asignado

prod["rango"]=prod["UnitPrice"].apply(lambda x: "caro" if x > 30 else "barato")

print(prod)

#  python funciones.py