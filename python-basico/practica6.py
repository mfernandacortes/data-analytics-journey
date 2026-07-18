import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)



"""
Usar las tablas Products, Categories y Order Details de Northwind.

1. Hacer merge de las tres tablas por sus claves.
2. Calcular la columna monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por CategoryName y calcular en un solo agg:
   - Monto total facturado (monto → sum)
   - Cantidad de productos distintos (ProductID → nunique)
   - Promedio de precio (UnitPrice → mean)
4. Ordenar de mayor a menor por monto total.
5. Con apply y def (axis=1), agregar columna "rendimiento":
   - "Alto" si el monto supera 100000
   - "Medio" si supera 40000 (y no es alto)
   - "Bajo" en cualquier otro caso
"""
#traigo tablas
p=pd.read_sql("Select ProductID, ProductName, CategoryID from Products", engine)
c=pd.read_sql("Select CategoryID, CategoryName from Categories", engine)
od=pd.read_sql("Select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

#merge:
pc=pd.merge(p,c, on="CategoryID")
pc_od=pd.merge(pc, od, on="ProductID")

# calculo la nueva columna monto:
pc_od["monto"]=pc_od["Quantity"]*pc_od["UnitPrice"]*(1-pc_od["Discount"])
print(pc_od)
agrup=pc_od.copy()

agrup=agrup.groupby(["CategoryID","CategoryName"]).agg({
    "monto":"sum",
    "ProductID":"nunique",
    "UnitPrice":"mean"
})

print(agrup)
#  python practica6.py