import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traer tablas que necesito:

p = pd.read_sql("Select ProductID, ProductName from Products", engine)
od = pd.read_sql("Select ProductID, Quantity, OrderID from [Order Details]", engine)


"""
Usar las tablas Products y Order Details.

1. Hacer merge entre ambas por ProductID.
2. Agrupar por ProductID y ProductName, y calcular en una sola agregación:
   - Total de unidades vendidas (Quantity)
   - Cantidad de pedidos distintos en los que aparece el producto (OrderID)
3. Ordenar de mayor a menor por unidades vendidas y quedarse con los primeros 10.
4. Con apply y una función def (axis=1), agregar una columna "clasificacion" que devuelva:
   - "Estrella" si las unidades vendidas superan 1000
   - "Popular" si aparece en más de 40 pedidos distintos (y no es Estrella)
   - "Normal" en cualquier otro caso

"""
# hacer el merge:
p_od = pd.merge(p, od, on="ProductID")
print(p_od)

# agrupar:


agrup_pod=p_od.groupby(["ProductID", "ProductName"]).agg({
    "Quantity": "sum",
    "OrderID": "nunique"
})


print(agrup_pod)

# seguir con lo que falta: item 3 y 4
# top 10
top_10 = agrup_pod.sort_values(by="Quantity", ascending=False).head(10)
print(top_10)

#clasificación de productos:
"""
   - "Estrella" si las unidades vendidas superan 1000
   - "Popular" si aparece en más de 40 pedidos distintos (y no es Estrella)
   - "Normal" en cualquier otro caso
"""
clasif= top_10.copy()

def clasificacion(row):
    if row["Quantity"] > 1000:
        return "Estrella"
    elif row["OrderID"] > 40:
        return["Popular"]
    else:
        return "Normal"
    
clasif["clasificacion"]= clasif.apply(clasificacion, axis=1)

print(clasif)

#  python practica1.py