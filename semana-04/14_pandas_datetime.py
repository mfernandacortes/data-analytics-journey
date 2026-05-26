import pandas as pd

data = {
    "empleado": ["Ana", "Luis", "María", "Pedro", "Ana", "Luis"],
    "fecha_venta": ["2024-01-15", "2024-02-03", "2024-02-20", 
                    "2024-03-10", "2024-03-25", "2024-04-01"],
    "monto": [100, 200, 150, 120, 180, 210]
}

df = pd.DataFrame(data)
print(df.dtypes)

df["fecha_venta"] = pd.to_datetime(df["fecha_venta"])
print(df.dtypes)

df["anio"] = df["fecha_venta"].dt.year
df["mes"] = df["fecha_venta"].dt.month
df["dia"] = df["fecha_venta"].dt.day

print(df)

#agrupo por ventas
por_mes = df.groupby("mes")["monto"].sum().reset_index()
print(por_mes)

# diferencia entre fechas:

df["dias_desde_primera"] = (df["fecha_venta"] - df["fecha_venta"].min()).dt.days
print(df[["empleado", "fecha_venta", "dias_desde_primera"]])

# python 14_pandas_datetime.py