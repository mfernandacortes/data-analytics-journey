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
La gerencia quiere ver cuánto se gastó en flete (Freight) por transportista (
CompanyName de Shippers, en filas) y por año (columnas).

"""

# traer tablas:
sh=pd.read_sql("select ShipperID, CompanyName from Shippers", engine)
o=pd.read_sql("select OrderID, ShipVia, OrderDate from Orders", engine)

# merge:
df=pd.merge(sh, o, left_on="ShipperID", right_on="ShipVia")

# año:
df["anio"]=df["OrderDate"].dt.year


# pivot:
print(df)

"""
python pivot54.py

"""