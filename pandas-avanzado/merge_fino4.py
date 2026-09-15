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
Merge tipo left con indicator=True: Shippers vs Orders, para ver si hay 
transportistas que nunca se usaron.

"""

# traer tablas:
s=pd.read_sql("select ShipperID, CompanyName from Shippers", engine)
o=pd.read_sql("select OrderID, ShipVia from Orders", engine)

# merge:
so=pd.merge(s,o,left_on="ShipperID", right_on="ShipVia", how="left", indicator=True)
print(so)
# filtro para encontrar los transportistas nunca usados:
transp = so[so["_merge"] == "left_only"]

print(transp)

# python merge_fino4.py

"""
HALLAZGO:
Todos los transportistas fueron usados al menos una vez.

"""
