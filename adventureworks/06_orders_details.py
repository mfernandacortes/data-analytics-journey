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
Tabla nueva: Sales.SalesOrderHeader. Es el encabezado del pedido, el equivalente de Orders en Northwind. 
Ya la tenés en tu diagrama, con SalesOrderID, OrderDate y CustomerID. Las líneas del pedido están en 
SalesOrderDetail, como Order Details allá. Todo lo demás (JOIN, GROUP BY, pivot) ya lo sabés.

Paso 1, solo mirar:

En Object Explorer abrí Sales.SalesOrderHeader > Columns y mirá qué columnas trae. Fijate cuáles te sirven para saber cuándo y cuáles para saber cuánto.
Escribí vos una consulta con TOP 10 que muestre SalesOrderID, OrderDate y CustomerID, ordenada por 
OrderDate.

"""

# traer tablas:
sho=pd.read_sql("select SalesOrderID, OrderDate, CustomerID from Sales.SalesOrderHeader", engine)
sod=pd.read_sql("select SalesOrderID, OrderQty, UnitPrice, UnitPriceDiscount from Sales.SalesOrderDetail", engine)


# merge:
df=pd.merge(sho, sod, on="SalesOrderID")

# monto_
df["monto"]=df["OrderQty"] * df["UnitPrice"] * (1 - df["UnitPriceDiscount"])

# año:
df["anio"]=df["OrderDate"].dt.year


print(df)
# agrupo por año:

agrup=df.groupby("anio")["monto"].sum().round(2)

print(df["monto"].sum())

print(agrup)


