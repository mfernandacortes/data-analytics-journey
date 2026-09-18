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
Calcular la cantidad de pedidos por cliente usando count() y nunique() sobre el 
merge de Orders + Order Details, y comparar los resultados para identificar la 
diferencia entre ambos.

"""

# traer tablas:
c=pd.read_sql("select CustomerID, CompanyName from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID from [Order Details]", engine)

# merge:
co=pd.merge(c,o,on="CustomerID")
co_od=pd.merge(co,od,on="OrderID")



df1=co_od.copy()
"""
informe=pd.pivot_table(
    co_od,
    index="ShipCountry",
    values=["monto"],
    aggfunc=["sum","mean"],
    fill_value=0
)
"""


informe1=pd.pivot_table(
    df1,
    index=["CustomerID","CompanyName"],
    values=["OrderID"],
    aggfunc=["nunique","count"],
    fill_value=0
)

print(informe1)

## count vs nunique — Pedidos por cliente
# se utilizan las dos funciones para mostrar como trabajan


# python practica11.py
