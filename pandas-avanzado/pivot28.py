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
Mostrar el monto vendido por país del cliente (Country en las filas) y por 
transportista (CompanyName en las columnas), con monto = UnitPrice * Quantity 
* (1 - Discount).

"""

# traer tablas:
sh=pd.read_sql("select ShipperID, CompanyName from Shippers", engine)
c=pd.read_sql("select CustomerID, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID, ShipVia from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
so_o=pd.merge(sh, o, right_on="ShipVia", left_on="ShipperID")
df=pd.merge(so_o, od, on="OrderID")
df1=pd.merge(df, c, on="CustomerID")
print(df1)
# calcular monto: 

# pivot:


"""
python pivot28.py


"""