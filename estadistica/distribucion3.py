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
Calcular el skew() de UnitPrice por categoría (CategoryID y CategoryName) 
y ordenar de mayor a menor sesgo.

"""

# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories",engine)
p=pd.read_sql("select ProductID, CategoryID, UnitPrice from Products",engine)

# merge:
ca_p=pd.merge(ca,p,on="CategoryID")

# agrupar:
agrup=ca_p.groupby(["CategoryID","CategoryName"])


# distribución:
sesgo=agrup["UnitPrice"].skew()
sesgo=sesgo.sort_values(ascending=False)
print(sesgo)
# python distribucion3.py