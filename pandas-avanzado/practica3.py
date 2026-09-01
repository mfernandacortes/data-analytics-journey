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
El equipo de marketing necesita una lista de clientes que nunca hicieron 
pedido, para armar una campaña de reactivación.

"""

# traer tablas: Customers y Orders
c=pd.read_sql("select CustomerID, CompanyName from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)

# merge: Como son clientes inactivos, tengo que ver todos, uso left:
co=pd.merge(c,o,on="CustomerID", how="left")
#ver df:
print(co)
# ahora con isna() veo esos datos:

clientes_inactivos=co[co["OrderID"].isna()]

print(clientes_inactivos)
"""
HALLAZGO:
Detecté 2 clientes sin pedidos registrados (FISSA, PARIS) usando 
un left join entre Customers y Orders. Son candidatos para campaña 
de reactivación:

 CustomerID                           CompanyName  OrderID
199      FISSA  FISSA Fabrica Inter. Salchichas S.A.      NaN
512      PARIS                     Paris spécialités      NaN

"""
# python practica3.py

