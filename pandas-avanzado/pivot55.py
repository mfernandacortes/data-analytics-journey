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
La gerencia quiere ver cuántas unidades (Quantity) se vendieron por producto (ProductName en filas) y 
por año (columnas).

"""

# traer tablas:
p=pd.read_sql("select ProductID, ProductName from Products", engine)
o=pd.read_sql("select OrderID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity from [Order Details]", engine)

# merge:
p_od=pd.merge(p, od, on="ProductID")
df=pd.merge(p_od, o, on="OrderID")


# año:
df["anio"]=df["OrderDate"].dt.year



# pivot:

informe=pd.pivot_table(
    df,
    index="ProductName",
    columns="anio",
    values="Quantity",
    aggfunc="sum",
    fill_value=0
)

print(informe)

"""
python pivot55.py

"""