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
La gerencia pide ver cuántas unidades (Quantity) se enviaron con cada transportista 
(CompanyName en las filas) a cada país del cliente (Country en las columnas).

"""

# traer tablas:
sh=pd.read_sql("select ShipperID, CompanyName from Shippers", engine)
c=pd.read_sql("select CustomerID, CompanyName as Cliente, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID, ShipVia from Orders", engine)
od=pd.read_sql("select OrderID, Quantity from [Order Details]", engine)


# merge:
sh_o=pd.merge(sh, o, left_on="ShipperID", right_on="ShipVia")
sho_od=pd.merge(sh_o, od, on="OrderID")
df=pd.merge(sho_od, c, on="CustomerID")


print(df)
# pivot:
informe=pd.pivot_table(
    df,
    index=["ShipperID", "CompanyName"],
    columns="Country",
    values="Quantity",
    aggfunc="sum",
    fill_value=0
)

print(informe)
