import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

"""
Usar las tablas Customers, Orders y Order Details de Northwind.

1. Merge de las tres tablas.
2. Calcular monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por Country y calcular en un solo agg:
   - monto → sum Y mean
   - OrderID → nunique

"""
# traer tablas:
c=pd.read_sql("Select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("Select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("Select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge de tablas:
co=pd.merge(c, o, on="CustomerID")
co_od=pd.merge(co, od, on="OrderID")

# calcuar el monto por línea de pedido:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])

# agrupar por pais y calcular monto total, promedio y total de pedidos de cada pais:
agrup_pais=co_od.copy()
agrup_pais=agrup_pais.groupby("Country").agg({
    "monto":["sum", "mean"],
    "OrderID":"nunique"
})
print(agrup_pais)

# python practica21.py
"""
4. Ordenar de mayor a menor por monto total (sum).
5. Con apply y def (axis=1), agregar columna "nivel":
   - "Top" si monto sum supera 100000
   - "Medio" si monto sum supera 40000 (y no es top)
   - "Bajo" en cualquier otro caso

"""
#
"""
Hallazgo:

"""