"""
Sobre la tabla Products de Northwind:

Filtrar los productos de categoría 1 o 2
Sobre ese resultado, calculá el precio promedio por categoría
"""

import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traigo tablas que necesito:

df = pd.read_sql("select ProductID, ProductName, UnitPrice, CategoryID from Products", engine)

#filtar resultados de categoria 1 o 2:

df = df[(df["CategoryID"] == 1) | (df["CategoryID"]  == 2)] 

print(df)



df = df.groupby("CategoryID")["UnitPrice"].mean()

print(df)

def calcular_monto(precio, cantidad, descuento):
    monto = (precio * cantidad) * (1 - descuento) 
    return(monto)

print(calcular_monto(10, 5, 0.1))


#lambda: función de una sola línea que tiene ese nombre:
lambda precio, cantidad, descuento: (precio * cantidad) * (1 - descuento)


precios = pd.Series([10, 20, 30, 40])
lambda precios: precios * 1.21

print(lambda precios: precios * 1.21)

resultado = precios.apply(lambda x: x * 1.21)
print(resultado)

def el_mayor(num1, num2):
    if(num1 > num2):
        mayor = num1
    else:
        mayor = num2
    return mayor


print(el_mayor(3,4))
# python combinados.py