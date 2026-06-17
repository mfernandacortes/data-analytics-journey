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
cli= pd.read_sql("Select OrderID, CustomerID, EmployeeID from Orders", engine)
od= pd.read_sql("Select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)
#emp=pd.read_sql("Select EmployeeID, LastName from Employees"), engine


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

#prod=prod.groupby("CategoryID")["UnitPrice"].mean().sort_values(ascending=False)


#print(prod)


"""
Usando la tabla Products de Northwind, agrupá por CategoryID y calculá en una sola línea:

El precio promedio (UnitPrice)
El precio máximo (UnitPrice)
La cantidad de productos (ProductID)

Guardá el resultado en una variable y printealo


"""


prod = prod.groupby("CategoryID").agg({"UnitPrice": ["mean", "max"],"ProductID" : "size"})

print(prod)

"""
Calcular la suma total de ventas por empleado usando las tablas Orders y Order Details, 
ordenar de mayor a menor y mostrar los 5 primeros.Calcular la suma total de ventas por 
empleado usando las tablas Orders y Order Details, ordenar de mayor a menor y mostrar los 5 primeros.
"""



#primero creo la columna con el calculo:
od["monto_total"] = od["UnitPrice"] * od["Quantity"] * (1 - od["Discount"])

od= od.groupby("OrderID")["monto_total"].sum()
print(od.sort_values(ascending=False).head())

