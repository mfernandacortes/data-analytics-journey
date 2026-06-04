"""
Calculá el monto total vendido por producto, mostrando solo los productos 
que superan el promedio general. Ordenados de mayor a menor.
Tablas que necesitás: Products, Order Details.
"""

import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traigo tablas que necesito:

od = pd.read_sql("select ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)
prod = pd.read_sql("select ProductID, ProductName from Products", engine)

#merge:
od_prod= od.merge(prod, on="ProductID")

#print(od_prod)

# group by:
#crear una columna nueva llamada monto: va el dataframe y en corchetes el nombre del campo o columna
od_prod["Monto"] = od_prod["UnitPrice"] * od_prod["Quantity"] * (1 - od_prod["Discount"])

# revisar y segurir:
# od_prod= od_prod.groupby(["ProductID", "ProductName"]).sum("Monto")
# od_prod["Promedio"] = od_prod["Monto"].mean("Monto")

print(od_prod)
# python repaso_03.py