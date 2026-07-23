import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)


"""
Usar las tablas Shippers, Orders y Order Details de Northwind.

Ojo con la clave: Orders se une a Shippers por ShipVia (no por ShipperID).

1. Hacer merge de las tres tablas.
2. Calcular la columna monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por ShipperID y CompanyName, y calcular en un solo agg:
   - monto → sum Y mean
   - OrderID → nunique
   - Quantity → sum
"""
# traigo las tablas:
s= pd.read_sql("Select ShipperID, CompanyName from Shippers", engine)
o= pd.read_sql("Select OrderID, ShipVia from Orders", engine)
od=pd.read_sql("Select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:left_on → cómo se llama la columna en el DataFrame izquierdo (el primero que paso)
# right_on → cómo se llama en el derecho (el segundo), en este caso en el merge no se puede
# utilizar on porque las columnas tienen distinto nombre

so=pd.merge(s, o, left_on="ShipperID", right_on="ShipVia")
so_od=pd.merge(so, od, on="OrderID")

# calculo monto:
so_od["monto"]=so_od["Quantity"] * so_od["UnitPrice"] * (1 - so_od["Discount"])
# agrupar por shipperID y CompanyName:
agrup_ship=so_od.copy()
agrup_ship=agrup_ship.groupby(["ShipperID", "CompanyName"]).agg({
    "monto":["sum", "mean"],
    "OrderID":"nunique",
    "Quantity":"sum"
})

print(agrup_ship)
"""
4. Ordenar de mayor a menor por el monto promedio (mean).
5. Con apply y def (axis=1), agregar columna "tipo_envio":
   - "Envíos grandes" si el monto promedio (mean) supera 600
   - "Envíos medianos" si supera 450 (y no es grande)
   - "Envíos chicos" en cualquier otro caso
"""
# python practica11.py