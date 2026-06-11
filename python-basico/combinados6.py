import pandas as pd
from sqlalchemy import create_engine 
"""
Sobre Order Details de Northwind — traé UnitPrice, Quantity y Discount. Con lambda y axis=1, 
agregá una columna tiene_descuento que diga "Sí" si Discount > 0 y "No" si Discount == 0.
Pista: vas a necesitar un if/else dentro de la lambda — eso se escribe así: "Sí" if condicion else "No".
"""
# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traigo tablas que necesito:
df = pd.read_sql("Select UnitPrice, Quantity, Discount from [Order Details]", engine)

# df["tiene_descuento"] = df.apply(lambda row:if row["Discount"] == 0 "No" else "Si")

df["tiene descuento"]= df.apply(lambda row: "No" if row["Discount"] == 0 else "Sí", axis = 1)

print(df)

