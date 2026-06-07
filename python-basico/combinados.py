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

def clasificar(precio):
	if precio >= 50:
		clasif = 'caro'
	elif precio < 50 and precio >= 20:
		clasif = 'medio'
	else:
		clasif = 'barato'
	return clasif


#print(clasificar(50))

#precios = pd.Series([5, 25, 75, 15, 55, 30])

print(precios.apply(clasificar))

"""Primer caso práctico — sobre la tabla Products de Northwind:
Traé ProductName y UnitPrice, y usá apply() con una función propia 
que clasifique cada producto como "caro", "medio" o "barato" según 
el precio. Ya tenés la función clasificar hecha"""
df2= pd.read_sql("select ProductID, ProductName, UnitPrice, CategoryID from Products", engine)
print(df2["ProductName"], df2["UnitPrice"].apply(clasificar))
#print(df2["UnitPrice"].apply(clasificar))
print("holiien combinados")
#print(df2["UnitPrice"].apply(clasificar))
# python combinados.py
# python combinados.py