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
Mostrar, por país de envío (ShipCountry de Orders), el monto total y el monto 
promedio de las líneas de pedido, para identificar qué países no solo compran 
más sino con tickets más altos.

"""

# traer tablas:
c=pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID, ShipCountry  from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)
# merge:
co=pd.merge(c,o,on="CustomerID")
co_od=pd.merge(co,od,on="OrderID")

# calcular monto:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])
print(co_od)

# pivot:
informe=pd.pivot_table(
    co_od,
    index="ShipCountry",
    values=["monto"],
    aggfunc=["sum","mean"],
    fill_value=0
)

print(informe)
# python pivot19.py


"""
HALLAZGO:
Austria tiene el ticket promedio más alto (1024) pero está lejos 
de ser el que más factura en total (128 mil, contra 245 mil de USA 
o 230 mil de Germany).
"""