import pandas as pd

df_ventas_enero = pd.DataFrame({
    "vendedor": ["Laura", "Pedro", None],
    "monto": [1500, None, 800]
})

df_ventas_febrero = pd.DataFrame({
    "vendedor": ["Laura", None, "Carlos"],
    "monto": [2000, 950, None]
})

"""

Unir los dos DataFrames con concat
Reemplazar nulos de "vendedor" con "Sin nombre"
Reemplazar nulos de "monto" con 0
Mostrar el resultado con print()

"""
ventas_totales = pd.concat([df_ventas_enero, df_ventas_febrero], ignore_index=True)


ventas_limpias = ventas_totales.copy()
ventas_limpias["vendedor"] = ventas_limpias["vendedor"].fillna("Sin nombre")
ventas_limpias["monto"] = ventas_limpias["monto"].fillna(0)

print (ventas_limpias)

#    python dobles.py