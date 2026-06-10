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
df = pd.read_sql("Select UnitPrice, Quantity, Discount from[Order Details]", engine)

#creo la función para calcular monto
def calcular_monto(precio, cantidad, descuento):
    monto = precio * cantidad * (1 - descuento)
    return monto

#creo una nueva columna llamada monto_con_iva y guardo el cálculo usando lambda 

df["monto_con_iva"] = df.apply(lambda row: calcular_monto(row["UnitPrice"], row["Quantity"], row["Discount"]), axis = 1 ) * 1.21
print(df)

"""
Sobre Products de Northwind, traé UnitPrice y agregá una columna 
precio_dolar dividiendo por 1400 (tipo de cambio). Solo lambda, sin función propia.
"""

# como es una sola columna no se necesita ni axis ni row:


df["precio_dolar"] = df["UnitPrice"].apply(lambda x: x / 1400)

print(df)

# python combinados4.py
 