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
la gerencia quiere ver cuántos pedidos (OrderID) despachó cada transportista (CompanyName en filas) 
por año (columnas).

"""

# traer tablas:
sh=pd.read_sql("select ShipperID, CompanyName from Shippers", engine)
o=pd.read_sql("select OrderID, OrderDate, ShipVia from Orders", engine)


# merge:
sh_o=pd.merge(sh, o, left_on="ShipperID", right_on="ShipVia")


# año:
sh_o["anio"]=sh_o["OrderDate"].dt.year


# pivot:
print(sh_o)

informe=pd.pivot_table(
    sh_o,
    index="CompanyName",
    columns="anio",
    values="OrderID",
    aggfunc="count",
    fill_value=0
)
print(informe)
"""
python pivot56.py

"""