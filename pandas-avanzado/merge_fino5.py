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
print(su_p)
# python merge_fino5.py


"""
HALLAZGO:

"""