from sqlalchemy import create_engine #copie
import pandas as pd #me habia olvidado de importar


# Conexión (copiada)
engine = create_engine(
    "mssql+pyodbc://FERCHUSERVER/Northwind"
    "?driver=SQL+Server&trusted_connection=yes"
)

# Tenés Northwind en SQL Server — conectate con SQLAlchemy, 
# traé la tabla Orders y calculá la cantidad de pedidos por cliente. 
# Sin mirar archivos anteriores.

ordenes = pd.read_sql("SELECT OrderID, CustomerID FROM ORDERS", engine)

print(ordenes)

ordenes = ordenes.groupby("CustomerID").count()

ordenes = ordenes[ordenes["OrderID"] > 10].sort_values("OrderID", ascending=False)

print(ordenes)

# python repaso_01.py