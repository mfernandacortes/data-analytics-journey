import pandas as pd
from sqlalchemy import create_engine 

# conexión, descomentar según de donde trabaje, por defecto es la de escritorio
engine = create_engine( 
    # ESCRITORIO:
     "mssql+pyodbc://FERCHUSERVER/AdventureWorks2025?driver=SQL+Server&trusted_connection=yes"
    # NOTEBOOK:
    # "mssql+pyodbc://.\\SQLEXPRESS/AdventureWorks2025?driver=SQL+Server&trusted_connection=yes"

)

"""
CONSIGNA:
la gerencia quiere saber si 2025 realmente vendió menos que 2024. Para eso pide comparar el monto 
de enero a junio de 2024 contra el de enero a junio de 2025.

"""

# traer tablas:
o=pd.read_sql("select SalesOrderID, OrderDate from Sales.SalesOrderHeader", engine)
sod=pd.read_sql("select SalesOrderID, OrderQty, UnitPrice, UnitPriceDiscount from Sales.SalesOrderDetail", engine)

# merge:
df=pd.merge(o, sod, on="SalesOrderID")

# calcular monto:
df["monto"]=df["OrderQty"] * df["UnitPrice"] * (1 - df["UnitPriceDiscount"])

# año:
df["anio"]=df["OrderDate"].dt.year

# mes:
df["mes"]=df["OrderDate"].dt.month

# agrupar por año y mes:
agrup=df.groupby(["anio", "mes"])["monto"].sum().round(2)
print(agrup)

# pivot:
informe=pd.pivot_table(
    df,
    index="mes",
    columns="anio",
    values="monto",
    aggfunc="sum",
    fill_value=0

)

print(informe)
"""
python 07_comparativo_ventas.py

"""