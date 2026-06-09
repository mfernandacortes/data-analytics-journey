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

def calcular_monto(precio, cantidad, descuento):
    monto = precio * cantidad * (1 - descuento)
    return monto


#lambda row: calcular_monto(row["UnitPrice"], row["Quantity"], row["Discount"])
#df["Monto"] = df.apply(calcular_monto)

# asi está bien:Cuando se necesita aplicar una función a cada fila usás axis=1. Sin él, 
# apply() intenta recorrer columnas y no funciona para lo que se necesita. Línea correcta:

df["Monto"] = df.apply(lambda row: calcular_monto(row["UnitPrice"], row["Quantity"], row["Discount"]), axis=1)
print(df)
"""
Sobre Order Details de Northwind — traé UnitPrice, Quantity y Discount. Escribí una función con def que clasifique cada venta como:

Mayor a 500 → "venta grande"
Entre 100 y 500 → "venta media"
Menor a 100 → "venta chica"
"""
def clasificar_venta(monto_venta):
    if monto_venta >= 500:
        categoria = 'Venta Grande'
    elif monto_venta < 500 and monto_venta >= 100:
        categoria ="Venta media"
    else:
        categoria = "Venta chica"
    return categoria

df["Categoria"] = df.apply(lambda row: clasificar_venta(row["Monto"]), axis=1)

print(df)
# python combinados3.py
