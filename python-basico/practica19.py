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
4. Ordenar de mayor a menor por monto promedio (mean).
5. Con apply y def (axis=1), agregar columna "perfil":
   - "Alto valor" si monto mean supera 700
   - "Volumen" si pedidos (OrderID nunique) supera 100 (y no es alto valor)
   - "Regular" en cualquier otro caso
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

#agrupar por empleados y calcular: monto total, promedio, cantidad de pedidos por cada uno:
agrup_emp=eo_od.copy()
agrup_emp=agrup_emp.groupby(["EmployeeID", "LastName"]).agg({
    "monto":["sum","mean"],
    "OrderID":"nunique"
})
print(agrup_emp)

# python practica19.py