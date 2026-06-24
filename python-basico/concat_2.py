import pandas as pd

datos = {
    "producto": ["Chai", None, "Tofu", None, "Pavlova"],
    "categoria": ["Bebidas", "Lácteos", None, "Granos", None],
    "precio": [18.0, None, 23.25, 38.0, None]
}


#fillna: 
"""
dataframe original:

df_limpio = df.copy()
df_limpio["columna"] = df_limpio["columna"].fillna(valor)

""" 

df_productos = pd.DataFrame(datos)
productos_limpios = df_productos.copy()
"""
df["nombre"] = df["nombre"].fillna("Sin nombre")   # string
df["precio"] = df["precio"].fillna(0)              # número
df["region"] = df["region"].fillna("Desconocido")  # 
Crear una copia del DataFrame llamada df_productos_limpio
Reemplazar los nulos de "producto" con "Sin nombre"
Reemplazar los nulos de "categoria" con "Sin categoría"
Reemplazar los nulos de "precio" con 0
Mostrar el resultado con print()

"""
productos_limpios["producto"]=productos_limpios["producto"].fillna("Sin nombre")
productos_limpios["categoria"]=productos_limpios["categoria"].fillna("Sin categoría")
productos_limpios["precio"]=productos_limpios["precio"].fillna(0)

print(productos_limpios)

#  python concat_2.py