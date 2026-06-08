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

# print(precios.apply(clasificar))

"""Primer caso práctico — sobre la tabla Products de Northwind:
Traé ProductName y UnitPrice, y usá apply() con una función propia 
que clasifique cada producto como "caro", "medio" o "barato" según 
el precio. Ya tenés la función clasificar hecha"""

#print(df["ProductName"], df["UnitPrice"].apply(clasificar))
# agrego una nueva columna:categoria para clasificar precios
df["categoria"] = df["UnitPrice"].apply(clasificar)
print(df)

"""
Segundo caso práctico — sobre la misma tabla, escribir una función con def 
que calcule el precio con IVA (21%) y agregarla como columna nueva precio_con_iva. 
Sin lambda esta vez — función propia.
"""

def calcular_iva(precio):
	subtotal = precio * 1.21
	return subtotal

# df["precio_con_iva"] = df["UnitPrice"].apply(calcular_iva) # se comenta para probar lambda q hace lo mismo

# print(df)
"""
Tercer caso práctico — ahora con lambda. Hacé lo mismo pero en una sola línea con 
lambda en vez de def. Sin guardarla en variable — directamente dentro del apply().
"""
df["precio_con_iva"] = df["UnitPrice"].apply(lambda x: x * 1.21)
print(df)
# python combinados2.py
