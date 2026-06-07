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
#print(df2["UnitPrice"].apply(clasificar))

#print(df2["UnitPrice"].apply(clasificar))
# 
# python combinados2.py
