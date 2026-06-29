import pandas as pd

df_ventas = pd.DataFrame({
    "vendedor": ["Laura", "Pedro", "Laura", "Carlos", "Pedro"],
    "categoria": ["Bebidas", "Lácteos", "Bebidas", "Lácteos", "Bebidas"],
    "monto": [1500, 800, 2000, 950, 1200]
})

"""
Agrupar por "vendedor" y calcular la suma de "monto"
Usar reset_index()
Mostrar el resultado con print()

"""

df_calculado = df_ventas.groupby("vendedor")["monto"].sum().sort_values(ascending=False).reset_index()

print(df_calculado)

# python dobles3.py