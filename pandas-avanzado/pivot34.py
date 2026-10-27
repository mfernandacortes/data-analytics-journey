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
La gerencia pide ver cuántas unidades (Quantity) se enviaron con cada 
transportista (ShipperID y CompanyName en las filas) por año (en las columnas).

"""

# traer tablas:
sh=pd.read_sql("select ShipperID, CompanyName from Shippers", engine)
o=pd.read_sql("select OrderID, ShipVia, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity from [Order Details]", engine)

# merge:
sh_o=pd.merge(sh, o, left_on="ShipperID", right_on="ShipVia")
df=pd.merge(sh_o, od, on="OrderID")

# año:
df["anio"]=df["OrderDate"].dt.year
print(df)

# pivot:
informe=pd.pivot_table(
    df,
    index=["ShipperID", "CompanyName"],
    columns="anio",
    values="Quantity",
    aggfunc="sum",
    fill_value=0
)

print(informe)
"""
python pivot34.py

"""