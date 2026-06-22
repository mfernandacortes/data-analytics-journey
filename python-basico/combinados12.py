import pandas as pd

data = {
    "ProductID": [1, 2, 3, 4, 5],
    "ProductName": ["Chai", None, "Syrup", "Cajun", None],
    "UnitPrice": [18.0, 19.0, None, 22.0, 21.0]
}

df = pd.DataFrame(data)
"""
df.isnull().sum() — para detectar nulos por columna
df.dropna() — para eliminar filas con nulos
Guardarlo en variable nueva y printearlo
"""

nulos_col= df.isnull().sum()
filas_nulos= df.dropna()

print(nulos_col)
print(filas_nulos)
"""
Ejercicio:
Usando el mismo data de antes:

Rellenar los nulos de ProductName con el texto "Sin nombre"
Rellenar los nulos de UnitPrice con el promedio de esa columna
Guardar en variable nueva y printear
"""



df_limpio = df.fillna("Sin nombre")
df_limpio["UnitPrice"] = df_limpio["UnitPrice"].fillna(df["UnitPrice"].mean())


print(df_limpio)
# python combinados12.py
