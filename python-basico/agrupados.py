"""
Ejercicio de repaso — GroupBy + Agg (Northwind):
Usando el DataFrame de Orders combinado con Order Details (podés partir del merge que ya tenés armado), 
calculá:

El total facturado (Quantity * UnitPrice * (1 - Discount)) agrupado por CustomerID.
Además del total, agregá en la misma agregación la cantidad de pedidos distintos que hizo cada cliente
 y el promedio de unidades por pedido.
Ordená el resultado de mayor a menor facturación y mostrá los primeros 10 clientes.

Como pista de estructura (sin darte la sintaxis completa, porque esto ya lo sabés hacer): pensá en un solo 
.groupby().agg({...}) con un diccionario que combine varias funciones de agregación, y después el
 reset_index(), sort_values() y head().
"""

import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)




# traigo tablas que necesito:

o = pd.read_sql("select OrderID, CustomerID from Orders", engine)
od = pd.read_sql("select OrderID, Quantity, ProductID, UnitPrice, Discount from [Order Details]", engine)

# unir tablas con merge
o_od=pd.merge(o, od, on="OrderID")

# agrupar por OrderID, primero creo la columna monto, ejemplo para un solo resultado:
o_od["monto"]= o_od["Quantity"]* o_od["UnitPrice"] * (1- o_od["Discount"])
#o_od= o_od.groupby("CustomerID")["monto"].sum()

# para más de un cálculo necesito agg:

# agrupo con agg: total facturado, cantidad de pedidos distintos, promedio de unidades
resultado = o_od.groupby("CustomerID").agg({
    "monto": "sum",
    "OrderID": "nunique",
    "Quantity": "mean"
})

# muestro el resultado
print(resultado)

#  python agrupados.py