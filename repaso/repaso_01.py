from sqlalchemy import create_engine
import pandas as pd 


# Conexión
engine = create_engine(
    "mssql+pyodbc://FERCHUSERVER/Northwind"
    "?driver=SQL+Server&trusted_connection=yes"
)

# Con Northwind en SQL Server — conectar con SQLAlchemy, 
# traer la tabla Orders y calcular la cantidad de pedidos por cliente. 


ordenes = pd.read_sql("SELECT OrderID, CustomerID FROM ORDERS", engine)


ordenes_agrup = ordenes.groupby("CustomerID").count()

#ordenes = ordenes[ordenes["OrderID"] > 10].sort_values("OrderID", ascending=False)



ord_10_20 = ordenes_agrup[(ordenes_agrup["OrderID"] > 10) & (ordenes_agrup["OrderID"] < 20) ]

print(ord_10_20)

# python repaso_01.py