import pandas as pd
from sqlalchemy import create_engine 
"""
Ejercicio concat con Northwind real:

s a FERCHUSERVER con SQLAlchemy
Traer los pedidos del año 1996 en un DataFrame llamado pedidos_1996
Traer los pedidos del año 1997 en un DataFrame llamado pedidos_1997
Unirlos en un solo DataFrame llamado pedidos_concat usando concat con ignore_index=True
Mostrar cuántas filas tiene el resultado con .shape
"""
# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traigo tablas:

pedidos= pd.read_sql("select * from Orders", engine)

pedidos_1996 = pedidos[(pedidos["OrderDate"] >= '1996-01-01') & (pedidos["OrderDate"] <= '1996-12-31')]

pedidos_1997 = pedidos[(pedidos["OrderDate"] >='1997-01-01') & (pedidos["OrderDate"] <= '1997-12-31')]
#print(pedidos_1996)
#print(pedidos_1997)
#df_total = pd.concat([clientes_arg, clientes_bra], ignore_index=True)
pedidos_concat = pd.concat([pedidos_1996, pedidos_1997], ignore_index=True)


print(pedidos_concat.shape)
#       python concaten.py