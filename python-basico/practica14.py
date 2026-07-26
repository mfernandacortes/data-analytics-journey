import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)
"""
Usar las tablas Employees, Orders y Order Details de Northwind.

1. Hacer merge de las tres tablas por sus claves.
2. Calcular la columna monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por EmployeeID y LastName, y calcular en un solo agg:
   - monto → sum Y mean
   - Quantity → sum
   - OrderID → nunique
4. Ordenar de mayor a menor por el monto promedio (mean).
5. Con apply y def (axis=1), agregar columna "perfil":
   - "Ticket alto" si el monto promedio (mean) supera 650
   - "Ticket medio" si supera 500 (y no es alto)
   - "Ticket bajo" en cualquier otro caso
"""
# tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo=pd.merge(e, o, on="EmployeeID")
eo_od=pd.merge(eo, od, on="OrderID")

#monto:
eo_od["monto"]=eo_od["Quantity"] * eo_od["UnitPrice"] * (1 - eo_od["Discount"])

#agrupar por empleados y calcular métricas, primero salvo el df orig que se pierde al agrupar
agrup_emp=eo_od.copy()
agrup_emp=agrup_emp.groupby(["EmployeeID", "LastName"]).agg({
    "monto":["sum", "mean"],
    "Quantity":"sum",
    "OrderID":"nunique"
})
print(agrup_emp)
# python practica14.py