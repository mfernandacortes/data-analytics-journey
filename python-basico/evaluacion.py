"""
Evaluación — Python/Pandas con Northwind
Sin darte pistas de estructura. Resolvé todo en un solo script, sin mirar ejercicios anteriores.
Consigna:
Usando las tablas Orders, Order Details, Products y Customers de Northwind:

Armar un DataFrame único que combine toda la información necesaria (pedidos, detalle de pedidos, productos 
y clientes).
Calcular una columna monto que refleje lo efectivamente facturado por línea de pedido (considerando 
, precio y descuento).
Agrupar por CompanyName (cliente) y obtené en una sola agregación: el monto total facturado, la cantidad 
de pedidos distintos, y la cantidad de productos distintos comprados.
Ordenar de mayor a menor por monto total y quedate con los primeros 15 clientes.
Agregar una columna nueva llamada segmento, calculada con apply, que clasifique a cada cliente de 
ese top 15 en:

"Cliente premium" si el monto total supera $20.000
"Cliente frecuente" si tiene más de 20 pedidos distintos (y no es premium)
"Cliente estándar" en cualquier otro caso
"""

import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traer tablas que necesito:

o = pd.read_sql("Select OrderID, CustomerID from Orders", engine)
od= pd.read_sql("Select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)
p = pd.read_sql("Select ProductID, ProductName from Products", engine)
c = pd.read_sql("Select CustomerID, CompanyName from Customers", engine)

# merge combinando los df
o_od = pd.merge(o, od, on="OrderID")
p_ood= pd.merge(o_od, p, on ="ProductID")
c_pood= pd.merge(p_ood, c, on ="CustomerID")

# ahora voy a crear la columna monto:

c_pood["monto"] = c_pood["Quantity"] * c_pood["UnitPrice"] * (1 - c_pood["Discount"])

print(c_pood)

# siguiente paso: agrupar por clientes y calcular monto total

c_pood_ag= c_pood.groupby("CustomerID")["monto"].sum()


# ahora las métricas:

resultado_final = c_pood.groupby("CustomerID").agg({
    "monto": "sum",
    "OrderID": "nunique",
    "ProductID":"nunique"

})

print(resultado_final)
# continuamos parte 2
#  python evaluacion.py