# =====================================================================
#  PRÁCTICA: named aggregation + tuplas
# =====================================================================
#
#  EL PORQUÉ (leelo una vez y no lo olvidás más):
#
#  Cuando hacés .agg(), cada resultado que declarás es literalmente
#  una tupla de DOS elementos:
#
#           nombre_nuevo = ("columna_origen", "función")
#                           └──────── esto es una tupla ────────┘
#
#  El primer elemento dice DE QUÉ columna sacar los datos.
#  El segundo dice QUÉ hacer con ellos ("sum", "mean", "count", etc.
#  o incluso una función tuya).
#  El nombre a la izquierda del = es cómo se va a llamar la columna
#  resultado. Por eso "named" aggregation: vos le ponés el nombre.
#
#  Ventaja frente al .agg() viejo con diccionarios: nombres limpios,
#  sin MultiIndex raro en las columnas, y podés repetir la misma
#  columna con funciones distintas sin pisarte.
#
#  INSTRUCCIONES:
#  - Resolvé cada ejercicio en el espacio marcado con  # TU CÓDIGO
#  - Compará tu resultado con la SALIDA ESPERADA (está como comentario)
#  - Recién si te trabás, andá a la sección SOLUCIONES del final
# =====================================================================

import pandas as pd

data = {
    "fecha": ["2024-03-01","2024-03-01","2024-03-02","2024-03-02","2024-03-03",
              "2024-03-03","2024-03-04","2024-03-05","2024-03-05","2024-03-06",
              "2024-03-06","2024-03-07","2024-03-08","2024-03-08","2024-03-09","2024-03-10"],
    "vendedor": ["Ana","Bruno","Ana","Carla","Bruno",
                 "Ana","Carla","Bruno","Ana","Carla",
                 "Bruno","Ana","Carla","Bruno","Ana","Carla"],
    "categoria": ["Bebidas","Lacteos","Bebidas","Snacks","Lacteos",
                  "Snacks","Bebidas","Bebidas","Lacteos","Snacks",
                  "Lacteos","Bebidas","Snacks","Bebidas","Lacteos","Bebidas"],
    "producto": ["Cafe","Yogur","Te","Papas","Leche",
                 "Mani","Cafe","Agua","Yogur","Papas",
                 "Leche","Te","Mani","Cafe","Yogur","Agua"],
    "cantidad": [10, 5, 8, 12, 6, 20, 15, 30, 4, 9, 7, 6, 18, 11, 5, 25],
    "precio_unitario": [3.5, 2.0, 3.0, 1.5, 1.8, 0.8, 3.5, 1.0, 2.0, 1.5, 1.8, 3.0, 0.8, 3.5, 2.0, 1.0],
    "region": ["Norte","Sur","Norte","Norte","Sur",
               "Norte","Sur","Sur","Norte","Sur",
               "Sur","Norte","Norte","Sur","Norte","Sur"],
}
df = pd.DataFrame(data)


# =====================================================================
#  EJERCICIO 1  —  Una sola agregación
# =====================================================================
#  Total de "cantidad" vendida por cada vendedor.
#  La columna resultado se tiene que llamar "cantidad_total".
#
#  SALIDA ESPERADA:
#            cantidad_total
#  vendedor
#  Ana                   53
#  Bruno                 59
#  Carla                 79

# TU CÓDIGO
agrup_vend=df.copy()
agrup_vend=agrup_vend.groupby("vendedor").agg(
    cantidad_total=("cantidad","sum")
)
print(agrup_vend)


# =====================================================================
#  EJERCICIO 2  —  Dos agregaciones a la vez (dos tuplas)
# =====================================================================
#  Por categoría: total de cantidad ("cantidad_total") y
#  precio_unitario promedio ("precio_promedio").
#
#  SALIDA ESPERADA:
#             cantidad_total  precio_promedio
#  categoria
#  Bebidas               105         2.642857
#  Lacteos                27         1.920000
#  Snacks                 59         1.150000

# TU CÓDIGO:

agrup_cat=df.copy()
agrup_cat=agrup_cat.groupby("categoria").agg(
    cantidad_total=("cantidad","sum"),
    precio_promedio=("precio_unitario","mean")
)
print(agrup_cat)


# python practica_named_agg.py
# =====================================================================
#  EJERCICIO 3  —  Columna calculada + agregar
# =====================================================================
#  Primero creá la columna "ingreso" = cantidad * precio_unitario.
#  Después, por región: ingreso total ("ingreso_total") y cantidad de
#  ventas ("ventas", usando count sobre "ingreso").
#
#  SALIDA ESPERADA:
#          ingreso_total  ventas
#  region
#  Norte           143.4       8
#  Sur             192.9       8

# TU CÓDIGO:

df["ingreso"]=df["cantidad"] * df["precio_unitario"]
agrup_region=df.copy()
agrup_region=agrup_region.groupby("region").agg(
    ingreso_total=("ingreso","sum"),
    ventas=("ingreso", "count")
)
print(agrup_region)



# =====================================================================
#  EJERCICIO 4  —  Agrupar por DOS claves + ordenar
# =====================================================================
#  Por vendedor Y región: ingreso total ("ingreso_total"),
#  ordenado de mayor a menor.
#  (Usá la columna "ingreso" del ejercicio 3.)
#
#  SALIDA ESPERADA:
#                   ingreso_total
#  vendedor region
#  Ana      Norte           111.0
#  Bruno    Sur             101.9
#  Carla    Sur              91.0
#           Norte            32.4

# TU CÓDIGO:
agrup=df.copy()
agrup=agrup.groupby(["vendedor","region"]).agg(
    ingreso_total=("ingreso","sum")
)
agrup=agrup.sort_values(by="ingreso_total", ascending=False)
print(agrup)
# =====================================================================
#  EJERCICIO 5  —  Función propia dentro de la tupla
# =====================================================================
#  Por categoría: precio mínimo ("precio_min"), precio máximo
#  ("precio_max") y el RANGO ("rango_precio" = max - min).
#  Para el rango, en el lugar de la función poné una lambda.
#
#  SALIDA ESPERADA:
#             precio_min  precio_max  rango_precio
#  categoria
#  Bebidas           1.0         3.5           2.5
#  Lacteos           1.8         2.0           0.2
#  Snacks            0.8         1.5           0.7

# TU CÓDIGO:

ej5=df.copy()
ej5=ej5.groupby("categoria").agg(
    precio_min=("precio_unitario","min"),
    precio_max=("precio_unitario","max"),
    rango_precio=("precio_unitario",lambda s: s.max() - s.min())
)
print(ej5)

# =====================================================================
#  EJERCICIO 6  —  nunique + count + reset_index
# =====================================================================
#  Por vendedor: cantidad de productos DISTINTOS ("productos_distintos",
#  con nunique) y cantidad total de operaciones ("operaciones", count).
#  Aplicá reset_index() para que "vendedor" vuelva a ser columna.
#
#  SALIDA ESPERADA:
#    vendedor  productos_distintos  operaciones
#  0      Ana                    4            6
#  1    Bruno                    4            5
#  2    Carla                    4            5

# TU CÓDIGO:
ej6 = df.groupby("vendedor").agg(
    productos_distintos=("producto", "nunique"),
    operaciones=("producto", "count"),
).reset_index()

print(ej6)

# python practica_named_agg.py
# =====================================================================
#  EJERCICIO 7  —  Combo completo (integrador)
# =====================================================================
#  Por categoría, todo junto y con reset_index, ordenado por ingreso
#  total descendente:
#    - "cant_total"      -> suma de cantidad
#    - "ingreso_total"   -> suma de ingreso
#    - "ticket_promedio" -> promedio de ingreso
#    - "vendedores"      -> vendedores distintos (nunique)
#
#  SALIDA ESPERADA:
#    categoria  cant_total  ingreso_total  ticket_promedio  vendedores
#  0   Bebidas         105          223.0        31.857143           3
#  1    Snacks          59           61.9        15.475000           2
#  2   Lacteos          27           51.4        10.280000           2

# TU CÓDIGO:



# =====================================================================
# =====================================================================
#   SOLUCIONES  —  no mires hasta intentar cada uno 🙈
# =====================================================================
# =====================================================================
"""
# --- EJ 1 ---
r1 = df.groupby("vendedor").agg(
    cantidad_total=("cantidad", "sum"),
)

# --- EJ 2 ---
r2 = df.groupby("categoria").agg(
    cantidad_total=("cantidad", "sum"),
    precio_promedio=("precio_unitario", "mean"),
)

# --- EJ 3 ---
df["ingreso"] = df["cantidad"] * df["precio_unitario"]
r3 = df.groupby("region").agg(
    ingreso_total=("ingreso", "sum"),
    ventas=("ingreso", "count"),
)

# --- EJ 4 ---
r4 = df.groupby(["vendedor", "region"]).agg(
    ingreso_total=("ingreso", "sum"),
).sort_values("ingreso_total", ascending=False)

# --- EJ 5 ---
r5 = df.groupby("categoria").agg(
    precio_min=("precio_unitario", "min"),
    precio_max=("precio_unitario", "max"),
    rango_precio=("precio_unitario", lambda s: s.max() - s.min()),
)

# --- EJ 6 ---
r6 = df.groupby("vendedor").agg(
    productos_distintos=("producto", "nunique"),
    operaciones=("producto", "count"),
).reset_index()

# --- EJ 7 ---
r7 = df.groupby("categoria").agg(
    cant_total=("cantidad", "sum"),
    ingreso_total=("ingreso", "sum"),
    ticket_promedio=("ingreso", "mean"),
    vendedores=("vendedor", "nunique"),
).sort_values("ingreso_total", ascending=False).reset_index()
"""
