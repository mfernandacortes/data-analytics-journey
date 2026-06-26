import pandas as pd

df1 = pd.DataFrame({"nombre": ["Ana", "Carlos"], "pais": ["Argentina", "Argentina"]})
df2 = pd.DataFrame({"nombre": ["João", None], "pais": ["Brasil", "Brasil"]})

"""
Unir los dos DataFrames con concat
Reemplazar el nulo de "nombre" con "Sin nombre"
Mostrar el resultado con print()

"""

# primero concat(unir los dataframe)
df_total = pd.concat([df1, df2], ignore_index=True)

# luego limpio los nulos: 

df_total["nombre"] = df_total["nombre"].fillna("sin nombre")
print(df_total)

#  python repaso.py