import pandas as pd
from sqlalchemy import create_engine 
"""
Sobre la tabla Order Details de Northwind — traé UnitPrice, Quantity y Discount, 
y usá apply() con una función propia que calcule el monto real de cada fila (con 
descuento incluido). Guardalo como columna nueva monto.

"""
# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traigo tablas que necesito:
df = pd.read_sql("Select ProductID, ProductName, UnitPrice from Products", engine)

# convierto los precios a dolar con lambda
df["precio_dolar"] = df["UnitPrice"].apply(lambda x: x / 1400)

# lambda es la función sin nombre con x que es la variable donde alojo resultado y x * 1400 es el cálculo
df["precio_argentino"] = df["UnitPrice"].apply(lambda x: x * 1400)

df = df.sort_values("precio_argentino", ascending=False)
print(df)

# python combinados5.py
