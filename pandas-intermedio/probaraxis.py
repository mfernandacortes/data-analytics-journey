import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://FERCHUSERVER/Northwind"
    "?driver=SQL+Server&trusted_connection=yes"
)

productos = pd.read_sql("Select ProductID, ProductName, UnitPrice, UnitsInStock from Products", engine)

# axis=0 → recorre COLUMNA por columna
# la función recibe una columna entera (una Series)
resultado_0 = productos[["UnitPrice", "UnitsInStock"]].apply(lambda columna: columna.sum(), axis=0)
print("axis=0 (por columna):")
print(resultado_0)
# UnitPrice          suma de TODOS los precios juntos
# UnitsInStock       suma de TODO el stock junto
# Dos resultados: uno por columna


# axis=1 → recorre FILA por fila
# la función recibe una fila entera (un producto completo)
resultado_1 = productos.apply(lambda fila: fila["UnitPrice"] * fila["UnitsInStock"], axis=1)

print(resultado_1)
# 0    702.00   (precio * stock del producto 1)
# 1    323.00   (precio * stock del producto 2)
# 2    130.00   (precio * stock del producto 3)
# ...
# 78 resultados: uno por cada producto (valor total de inventario de ese producto)