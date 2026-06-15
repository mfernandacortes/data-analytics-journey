"""
 Sobre la tabla Products de Northwind, traer ProductName, UnitPrice y UnitsInStock.
Con apply() y axis=1, crear una columna categoria_precio que diga:

"Económico" si UnitPrice es menor a 15
"Medio" si UnitPrice es entre 15 y 50
"Premium" si UnitPrice es mayor a 50

"""

import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traigo tablas que necesito:

prod= pd.read_sql("Select ProductID, ProductName, CategoryID, UnitPrice, UnitsInStock from Products", engine)
cli= pd.read_sql("Select OrderID, CustomerID from Orders", engine)


prod["columna_categoria"] = prod.apply(lambda row: "Económico" if row["UnitPrice"] <= 15 else "Medio" if (row["UnitPrice"] > 15) & (row["UnitPrice"] <= 50) else "Premium", axis = 1)

print(prod)

"""
Agrupar las órdenes por cliente y contar cuántas órdenes realizó cada uno, ordenado de mayor a menor.

"""
cli= cli.groupby("CustomerID").size().sort_values(ascending=False)

print(cli)

"""
Calcular el promedio de UnitPrice 
por categoría (CategoryID) en la tabla Products, ordenado de mayor a menor.
"""
#la estructura: primero la columna por la que agrupar(categoryID) luego por la q calcular promedio:UnitPrice y x último el órden)

prod=prod.groupby("CategoryID")["UnitPrice"].mean().sort_values(ascending=False)


print(prod)