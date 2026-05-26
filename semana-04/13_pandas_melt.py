import pandas as pd
# ejemplo: llega este dataset:
data = {
    "empleado": ["Ana", "Luis", "María", "Pedro"],
    "ventas_ene": [100, 200, 150, 120],
    "ventas_feb": [150, 180, 130, 110],
    "ventas_mar": [120, 210, 170, 140],
    "ventas_abr": [120, 210, 170, 150]
}

df = pd.DataFrame(data)
print(df)
# con melt transformamos a columnas:
df_largo = df.melt(
    id_vars="empleado",       # columna que se queda fija
    var_name="mes",           # nombre para la columna de los encabezados
    value_name="ventas"       # nombre para la columna de los valores
)


print(df_largo)

# sacamos la palabra ventas y dejamos vacío:
df_largo["mes"] = df_largo["mes"].str.replace("ventas_", "")
print(df_largo)
# se agrupa
resumen = df_largo.groupby("mes")["ventas"].sum().reset_index()
print(resumen)

# los meses están ordenados alfabéticamente, los quiero ordenar cronológicamente,
# defino la lista orden:
orden = ["ene", "feb", "mar", "abr"]
resumen["mes"] = pd.Categorical(resumen["mes"], categories=orden, ordered=True)
resumen = resumen.sort_values("mes").reset_index(drop=True)
print(resumen)
#agrupo por empleado y mes para ver las ventas ordenados en forma descendente:
resumen_emp=df_largo.groupby(["empleado", "mes"])["ventas"].sum().sort_values(ascending=False)
print(resumen_emp)

#para ver el mejor mes de cada empleado, me quedo con la primer fila:
resumen_emp = resumen_emp.reset_index()
resultado = resumen_emp.groupby("empleado").first()
print(resultado)
# python 13_pandas_melt.py