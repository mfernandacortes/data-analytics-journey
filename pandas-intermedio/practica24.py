import pandas as pd
from sqlalchemy import create_engine 

# conexión, descomentar según de donde trabaje, por defecto es la de escritorio
engine = create_engine( 
    # ESCRITORIO:
     "mssql+pyodbc://FERCHUSERVER/Northwind?driver=SQL+Server&trusted_connection=yes"
    # NOTEBOOK:
    # "mssql+pyodbc://.\\SQLEXPRESS/Northwind?driver=SQL+Server&trusted_connection=yes"

)

"""
CONSIGNA:
Usar las tablas Orders, Order Details y Customers de Northwind.

1. Merge de las tres tablas.
2. Calcular monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por City (la ciudad del cliente) con TUPLAS, en un solo agg:
   - monto → sum Y mean
   - OrderID → nunique
"""
# tablas:
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)
c=pd.read_sql("select CustomerID, CompanyName, City from Customers", engine)

# merge:
co=pd.merge(c,o,on="CustomerID")
co_od=pd.merge(co,od,on="OrderID")

# monto:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])

# agrupar por ciudad y calcular monto total, promedio y total pedidos:
co_od=co_od.groupby("City").agg({
    "monto":["sum","mean"],
    "OrderID":"nunique"
})


"""
4. Ordenar de mayor a menor por monto total ("monto","sum").
5. Mostrar el top 10 con head(10).

"""
# ordenar de mayor a menor
co_od=co_od.sort_values(by=("monto","sum"), ascending=False)

# Mostrar el top 10:

print(co_od.head(10))

"""
HALLAZGO:
Cunewalde lidera en facturación (110K) con ticket altísimo (1282) pero solo 28 pedidos — o sea, 
es una ciudad con pocos clientes pero que compran muchísimo. Comparala con London: 4º en 
facturación (52K) pero con 46 pedidos y ticket mucho más bajo (471). London vende por volumen
 (muchos pedidos chicos), Cunewalde por ticket (pocos pedidos enormes).
 
"""

# python practica24.py