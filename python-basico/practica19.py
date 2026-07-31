import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)
"""
Usar las tablas Employees, Orders y Order Details de Northwind.

1. Merge de las tres tablas.
2. Calcular monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por EmployeeID y LastName y calcular en un solo agg:
   - monto → sum Y mean
   - OrderID → nunique
"""

# traigo las tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge de tablas:
eo=pd.merge(e, o, on="EmployeeID")
eo_od=pd.merge(eo, od, on="OrderID")

# calculo el monto agregando una nueva columna:
eo_od["monto"]=eo_od["Quantity"] * eo_od["UnitPrice"] * (1 - eo_od["Discount"])

# agrupar por empleados y calcular: monto total, promedio, cantidad de pedidos distintos por cada uno:
agrup_emp=eo_od.copy()
agrup_emp=agrup_emp.groupby(["EmployeeID", "LastName"]).agg({
    "monto":["sum","mean"],
    "OrderID":"nunique"
})
"""
4. Ordenar de mayor a menor por monto promedio (mean).
5. Con apply y def (axis=1), agregar columna "perfil":
   - "Alto valor" si monto mean supera 700
   - "Volumen" si pedidos (OrderID nunique) supera 100 (y no es alto valor)
   - "Regular" en cualquier otro caso
"""
# ordeno de mayor a menor por promedio de monto:
agrup_emp=agrup_emp.sort_values(by=("monto", "mean"), ascending=False)
# agrego columna perfil y clasifico conuna función
def clasif(row):
    if row["monto", "mean"] > 700:
        return "Alto valor"
    elif row["OrderID", "nunique"] > 100:
        return "Volumen"
    else:
        return "Regular"
agrup_emp["perfil"]=agrup_emp.apply(clasif, axis=1)
print(agrup_emp)

"""
Alto valor (mean > 700): Dodsworth (722) y King (707) — ticket alto aunque no facturen tanto en total
Volumen (>100 pedidos, sin ser alto valor): Leverling (127), Davolio (123), Peacock (156), 
Callahan (104) — hacen muchos pedidos
Regular: Fuller, Buchanan, Suyama — ni ticket alto ni +100 pedidos

Y un caso interesante: Fuller quedó "Regular" con ticket 691 — le faltaron 9 puntitos para "Alto 
valor" (>700). Tan cerca. Y como tiene 96 pedidos (no más de 100), tampoco entró en Volumen. 
Cayó justo en el medio de las dos condiciones. Otro caso borde de los que muestran que la lógica
discrimina bien.
"""

# python practica19.py