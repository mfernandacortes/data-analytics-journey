import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

"""
Usar las tablas Orders, Order Details y Employees de Northwind.

1. Hacer merge de las tres tablas por sus claves.
2. Calcular la columna monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por EmployeeID y LastName, y calcular en un solo agg:
   - Monto total (monto → sum)
   - Monto promedio por línea de pedido (monto → mean)
   - Cantidad de pedidos distintos (OrderID → nunique)
4. Ordenar de mayor a menor por monto total.
5. Con apply y def (axis=1), agregar columna "eficiencia":
   - "Alta" si el monto promedio por línea supera 700
   - "Media" si supera 500 (y no es alta)
   - "Baja" en cualquier otro caso
"""

o=pd.read_sql("select OrderID, CustomerID, EmployeeID from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, UnitPrice, Quantity, Discount from [Order Details]", engine)
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)

# merge:
o_od=pd.merge(o, od, on="OrderID")
p_od_e=pd.merge(o_od, e, on="EmployeeID")

#ahora calculo el monto facturado agregando columna nueva:
p_od_e["Monto"]=p_od_e["Quantity"]*p_od_e["UnitPrice"]*(1-p_od_e["Discount"])
print(p_od_e)

#agrupo por empleados:
agrup_emp=p_od_e.copy()
agrup_emp=agrup_emp.groupby(["EmployeeID", "LastName"]).agg({
    "Monto":["sum","mean"],
    "OrderID":"nunique"
})

# hacer puntos 4 y 5:
agrup_emp=agrup_emp.sort_values(by=("Monto", "sum"), ascending=False)
# defino la función que los clasifica, esta vez utilizamos tupla para distinguir si quiero la suma o el promedio del Monto:
def clasifica(row):
    if row[("Monto", "mean")] > 700:
        return "Alta"
    if row[("Monto", "mean")] > 500:
        return "Media"
    else:
        return "Baja"
# agrego la columna eficiencia para llamar a la función y mostrar la clasificación:
agrup_emp["eficiencia"]=agrup_emp.apply(clasifica, axis=1)

print(agrup_emp)

# python practica7.py