import pandas as pd

df_empleados = pd.DataFrame({
    "empleado_id": [1, 2, 3],
    "nombre": ["Laura", "Pedro", "Sofía"]
})

df_ventas = pd.DataFrame({
    "venta_id": [200, 201, 202, 203],
    "empleado_id": [1, 1, 2, 4],
    "monto": [1000, 1500, 700, 900]
})

"""
Unir ambos DataFrames con merge usando "empleado_id"
Mostrar el resultado con print()
"""
# repaso merge - inner join, filas sin match excluidas

emp_ventas = pd.merge(df_empleados, df_ventas, on="empleado_id")
print(emp_ventas)

#  python dobles5.py