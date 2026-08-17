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
Cliente: "Quiero comparar, para cada categoría de producto, cuántas unidades
vendimos en total, separado por año."

"""

# traer tablas:
ca=pd.read_sql("Select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("Select ProductID, CategoryID, ProductName from Products", engine)
o=pd.read_sql("Select OrderID, OrderDate from Orders", engine)
od=pd.read_sql("Select ProductID, Quantity, OrderID from [Order Details]", engine)

# merge:
ca_p=pd.merge(ca,p,on="CategoryID")
cap_pd=pd.merge(ca_p,od,on="ProductID")
cap_pdo=pd.merge(cap_pd,o,on="OrderID")

# creo una columna llamada anio:
cap_pdo["anio"]=cap_pdo["OrderDate"].dt.year

# pivot:
informe=pd.pivot_table(
    cap_pdo,
    index=["CategoryID","CategoryName"],
    columns="anio",
    values="Quantity",
    aggfunc="sum",
    fill_value=0
)
print(informe)
# python pivot10.py

