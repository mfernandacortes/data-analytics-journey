"""
Calcular el promedio de UnitPrice por CategoryID en Products, guardar el resultado en una variable nueva 
y aplicar reset_index().
Después hacer dos prints: uno sin reset_index() y otro con, para ver la diferencia visual.
"""

import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)


# traigo tablas que necesito:


prod= pd.read_sql("select ProductID, ProductName, CategoryID, UnitPrice from Products", engine)
cat= pd.read_sql("select CategoryID, CategoryName from Categories", engine)

od_prod_cat= pd.merge(prod, cat, on ="CategoryID")

#print(od_prod_cat)

promedio= od_prod_cat.groupby("CategoryID")["UnitPrice"].mean()
print(promedio)
promedio_reset=promedio.reset_index()

print(promedio_reset)
#  python combinados11.py