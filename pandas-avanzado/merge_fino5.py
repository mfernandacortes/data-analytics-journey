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
Determinar si hay proveedores (suppliers) que nunca fueron asociados a ningún 
producto — un dato útil para saber si conviene depurar la lista de proveedores 
cargados en el sistema.

"""

# traer tablas:
su=pd.read_sql("select SupplierID, CompanyName from Suppliers", engine)
p=pd.read_sql("select ProductID, ProductName, SupplierID from Products", engine)

# merge:
su_p=pd.merge(su,p,on="SupplierID", how="left", indicator=True)

# python merge_fino5.py

# filtrar para ver cuales son los proveedores que no están asociados a ningún producto:
proveed=su_p[su_p["_merge"]=="left_only"]
print(proveed)
"""
HALLAZGO:
DataFrame vacío — los 29 suppliers del dataset tienen al menos un producto 
asociado. No hay proveedores "huérfanos" para depurar.
"""