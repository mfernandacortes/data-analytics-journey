import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)
"""
Usar las tablas Employees, Orders y Order Details de Northwind.

1. Hacer merge de las tres tablas por sus claves (EmployeeID y OrderID).
2. Calcular la columna monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por EmployeeID y LastName, y calcular en un solo agg:
   - Monto total facturado (monto → sum)
   - Cantidad de pedidos distintos (OrderID → nunique)
4. Ordenar de mayor a menor por monto total.
5. Con apply y def (axis=1), agregar columna "categoria_vendedor":
   - "Top" si el monto supera 150000
   - "Medio" si supera 80000 (y no es Top)
   - "Base" en cualquier otro caso

"""
# tablas:
e = pd.read_sql("Select EmployeeID, LastName from Employees", engine)
o = pd.read_sql("Select OrderID, EmployeeID from Orders", engine)
od = pd.read_sql("Select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo = pd.merge(e, o, on ="EmployeeID")
eo_od=pd.merge(eo, od, on ="OrderID")

print(eo_od)

# calcular monto:
eo_od["monto"]= eo_od["Quantity"] * eo_od["UnitPrice"] * (1 - eo_od["Discount"])
print(eo_od)

# agrupar por empleado:
agrup_emp= eo_od.copy()
agrup_emp=agrup_emp.groupby(["EmployeeID", "LastName"]).agg({
    "monto":"sum",
    "OrderID": "nunique"

})
"""
Con apply y def (axis=1), agregar columna "categoria_vendedor":
   - "Top" si el monto supera 150000
   - "Medio" si supera 80000 (y no es Top)
   - "Base" en cualquier otro caso

"""

agrup_emp=agrup_emp.sort_values(by="monto", ascending=False)

def clasificar(row):
    if row["monto"] > 150000:
        return "Top"
    elif row["monto"] > 80000:
        return "Medio"
    else:
        return "Base"

# agregar categoria vendedor:
agrup_emp["categoria_vendedor"] = agrup_emp.apply(clasificar, axis=1)

print(agrup_emp)

#  python practica4.py