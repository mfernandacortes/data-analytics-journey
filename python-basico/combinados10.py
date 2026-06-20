import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

"""
Usando Products de Northwind:
Calcular el precio máximo y el precio mínimo de producto por categoría, 
ordenado de mayor a menor por el precio máximo.
"""

# traigo tablas que necesito:


prod= pd.read_sql("select ProductID, ProductName, CategoryID, UnitPrice from Products", engine)
cat= pd.read_sql("select CategoryID, CategoryName from Categories", engine)

od_prod_cat= pd.merge(prod, cat, on ="CategoryID")


#print(od_prod_cat)



precio_maximo= od_prod_cat.groupby(['CategoryID', 'CategoryName'])["UnitPrice"].max().sort_values(ascending=False)
print(precio_maximo)
# python combinados10.py
