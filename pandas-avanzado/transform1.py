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
Agregar a la tabla de productos una columna nueva con el precio promedio de su 
categoría (usando transform), y otra columna que calcule la diferencia entre el 
precio del producto y ese promedio.

"""

# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, CategoryID, ProductName, UnitPrice from Products", engine)

# merge:
ca_p=pd.merge(ca,p,on="CategoryID")

# agregar columna promedio:
ca_p["promedio"]=ca_p.groupby("CategoryName")["UnitPrice"].transform("mean")

# agrego la columna con la diferencia entre precio y promedio:
ca_p["diferencia"]=ca_p["UnitPrice"] - ca_p["promedio"]



"""

Usando la misma tabla de productos+categorías, agregar una columna que muestre 
el puesto (ranking) de cada producto según su UnitPrice, dentro de su propia 
categoría — o sea, el más caro de Beverages es el puesto 1 de Beverages, no el 
puesto 1 de todo el dataset.

"""
ca_p["ranking"]=ca_p.groupby("CategoryName")["UnitPrice"].rank(ascending=False)

print(ca_p)