import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)
"""
Usar las tablas Customers, Orders y Order Details de Northwind.

1. Merge de las tres tablas por sus claves.
2. Calcular monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por Country y calcular en un solo agg:
   - monto → sum Y mean
   - OrderID → nunique

"""


#tablas:
c=pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

#Merge:
co=pd.merge(c, o, on="CustomerID")
co_od=pd.merge(co, od, on="OrderID")

#crear monto:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])

#agrupar por pais:
agrup_pais=co_od.copy()
agrup_pais=agrup_pais.groupby("Country").agg({
    "monto":("sum", "mean"),
    "OrderID": "nunique"
})

"""
4. Ordenar de mayor a menor por monto total (sum).
5. Con apply y def (axis=1), agregar columna "mercado":
   - "Fuerte" si monto sum supera 50000 Y pedidos (OrderID nunique) supera 30
   - "Selecto" si monto mean supera 600 (y no es fuerte)
   - "Menor" en cualquier otro caso
"""

#ordenar de mayor a menor por monto total sum:
agrup_pais=agrup_pais.sort_values(by=("monto","sum"), ascending=False)
#Definir función para clasificar:
def clasif(row):
    if row[("monto", "sum")] > 50000 and row[("OrderID", "nunique")] > 30:
        return "Fuerte"
    elif row["monto", "mean"] > 600:
        return "Selecto"
    else:
        return "Menor"
agrup_pais["mercado"]=agrup_pais.apply(clasif, axis=1)
print(agrup_pais)
# python practica17.py
"""
Hallazgo:
Canada: monto 50196 (justo por encima de 50000) pero solo 30 pedidos. 
La condición pide pedidos > 30, y 30 no es mayor que 30, así que NO cumple "Fuerte" 
por un pelo. Cae a "Selecto" por su ticket (669). El and fue estricto: le faltó un pedido
para ser "Fuerte".
Y Ireland: quedó "Selecto" con ticket altísimo (908) pero solo 19 pedidos y 49979 de
monto — no llega a fuerte, pero su ticket la distingue. El patrón volumen vs ticket de siempre.

"""