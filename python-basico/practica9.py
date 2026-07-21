"""
Usar las tablas Customers, Orders y Order Details de Northwind.

1. Hacer merge de las tres tablas por sus claves.
2. Calcular la columna monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por Country y calcular en un solo agg:
   - monto → sum Y mean (las dos sobre la misma columna)
   - OrderID → nunique
4. Ordenar de mayor a menor por el monto promedio (mean) — ojo, hoy es por mean, no por sum.
5. Con apply y def (axis=1), agregar columna "perfil_compra":
   - "Ticket alto" si el monto promedio (mean) supera 800
   - "Ticket medio" si supera 500 (y no es alto)
   - "Ticket bajo" en cualquier otro caso
"""

import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

c= pd.read_sql("Select CustomerID, CompanyName, Country from Customers", engine)
o= pd.read_sql("Select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("Select OrderID, UnitPrice, Quantity, Discount from [Order Details]", engine)

# merge=
co=pd.merge(c, o, on="CustomerID")
co_od=pd.merge(co, od, on="OrderID")

# calcular monto:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])

# agrupar y promediar:
agrup_pais=co_od.copy()
agrup_pais=agrup_pais.groupby("Country").agg({
    "monto":["sum", "mean"],
    "OrderID":"nunique"

})

#ordenar por promedio de mayor a menor
agrup_pais=agrup_pais.sort_values(by=("monto","mean"), ascending=False)
#definir perfil:
#primero creo la función:
def definir(row):
    if row["monto", "mean"] > 800:
        return "Ticket alto"
    elif row["monto", "mean"] > 500:
        return "Ticket medio"
    else:
        return "Ticket bajo"
    
agrup_pais["perfil_compra"]=agrup_pais.apply(definir, axis=1)
print(agrup_pais)
#  python practica9.py