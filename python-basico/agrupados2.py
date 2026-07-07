"""
Partiendo de las tablas Products, Categories y Order Details de Northwind:

Hacé merge entre las tres tablas para tener, en un mismo DataFrame, el nombre de la 
categoría, el producto, la cantidad vendida (Quantity) y el precio (UnitPrice) de cada 
línea de pedido.
Agrupá por CategoryName y calculá con un solo .agg({...}):

La cantidad total de unidades vendidas (Quantity) → sum
La cantidad de productos distintos vendidos en esa categoría → pensá qué columna usar y
qué función (pista: es la misma que usaste hoy para pedidos distintos, pero aplicada 
a ProductID)
El precio promedio (UnitPrice) → mean


Ordená de mayor a menor por unidades vendidas.

"""

import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traigo las tablas que necesito:

cat = pd.read_sql("Select CategoryID, CategoryName from Categories", engine)
prod = pd.read_sql("Select ProductID, ProductName, UnitPrice, CategoryID from Products", engine)
od = pd.read_sql("Select OrderID, ProductID, Quantity, UnitPrice from [Order Details]", engine)
"""
Hacer merge entre las tres tablas para tener, en un mismo DataFrame, el nombre de la 
categoría, el producto, la cantidad vendida (Quantity) y el precio (UnitPrice) de cada 
línea de pedido.

Agrupar por CategoryName y calcular con un solo .agg({...}):

- La cantidad total de unidades vendidas (Quantity)
- La cantidad de productos distintos vendidos en esa categoría
- El precio promedio (UnitPrice)

Ordenar de mayor a menor por unidades vendidas.

"""


#merge
c_prod = pd.merge(cat, prod, on="CategoryID")
# como el nombre UnitPrice se repite en cada df, tengo que diferenciarlos:
c_prod_od = pd.merge(c_prod, od, on="ProductID", suffixes=("_producto", "pedido"))

#print(c_prod_od)

#agrupo por categoría para saber cuantos productos se vendieron

# nombre del df nuevo=df a agrupar. groupby("campo a agrupar")["columna"].funcion()
#agrup = c_prod_od.groupby("CategoryName")["Quantity"].sum()


# ahora con agg:
agrup_agg = c_prod_od.groupby("CategoryName").agg({"ProductID": "nunique", "Quantity": ["sum", "mean"], "UnitPrice_producto":["mean"]})

print(agrup_agg.sort_values(("Quantity", "sum"), ascending=False))

#  python agrupados2.py