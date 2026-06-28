"""
Crear dos DataFrames df_productos_local y df_productos_importados con las columnas "producto",
"categoria" y "precio" — inventá 3 filas cada uno, con algún nulo en cada DataFrame
Unirlos con concat
Reemplazar nulos de "producto" con "Sin nombre"
Reemplazar nulos de "categoria" con "Sin categoría"
Reemplazar nulos de "precio" con 0
Mostrar el resultado con print()

"""

import pandas as pd

df_productos_local = pd.DataFrame({
    "producto": ["Agua mineral sin gas 1 lt", "Gaseosa 2 lt", None],
    "categoria": ["Bebidas", "Quesos", None],
    "precio": [1500, None, 800]
})

df_productos_importados = pd.DataFrame({
    "producto": ["Papas Pringles", None, "Latas chocolate"],
    "categoria":["Golosinas", None, "Delicatessen"],
    "precio": [2000, 950, None]
})

# ojo que en uno de los df puse categoría con acento y me generó dos columnas de categoria, una 
# sin acento y otra con acento... 
df_productos= pd.concat([df_productos_local, df_productos_importados], ignore_index=True)

# fillna actúa por columna: 
df_productos["producto"] = df_productos["producto"].fillna("Sin nombre")
df_productos["categoria"] = df_productos["categoria"].fillna("Sin categoría")
df_productos["precio"] = df_productos["precio"].fillna(0)

print(df_productos)
# python dobles2.py

