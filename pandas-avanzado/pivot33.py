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
La gerencia pide ver cuántas unidades (Quantity) se vendieron por categoría 
(CategoryID y CategoryName en las filas) y por año (en las columnas).

"""

# traer tablas:
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, ProductName, CategoryID from Products", engine)
o=pd.read_sql("select OrderID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)


# merge:
ca_p=pd.merge(ca, p, on="CategoryID")
df1=pd.merge(ca_p, od, on="ProductID")
df=pd.merge(df1, o, on="OrderID")

# año:
df["anio"]=df["OrderDate"].dt.year

print(df)

# pivot:
informe=pd.pivot_table(
    df,
    index=["CategoryID", "CategoryName"],
    columns="anio",
    values="Quantity",
    aggfunc="sum",
    fill_value=0
)

print(informe)
"""
python pivot33.py

"""