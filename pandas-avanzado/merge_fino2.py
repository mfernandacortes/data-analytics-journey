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
Usando un merge tipo left con indicator=True, encontrar los clientes que nunca 
hicieron un pedido (Customers sin match en Orders).

"""

# traer tablas:
c=pd.read_sql("select CustomerID, CompanyName from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)

# merge:
co=pd.merge(c, o, on="CustomerID", how="left", indicator=True)

#ahora tengo que filtrar los clientes que nunca compraron por el valor left_only:
inactivos = co[co["_merge"] == "left_only"]
print(inactivos)
# python merge_fino2.py

"""
HALLAZGO:
Clientes que no realizaron pedidos:
FISSA Fabrica Inter. Salchichas S.A.      
Paris spécialités      
Insight: Hablar con los vendedores para ver quien los atiende o asignarles un 
vendedor.
Averiguar los motivos, se puede pensar en ofrecer algún descuento para atraerlos.
"""
