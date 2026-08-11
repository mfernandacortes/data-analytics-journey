import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)
"""

Usar las tablas Categories, Products y Order Details de Northwind.

1. Hacer merge de las tres tablas por sus claves.
2. Calcular la columna monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por CategoryName y calcular en un solo agg:
   - monto → sum Y mean (las dos funciones sobre la misma columna)
   - Quantity → sum
4. Ordenar de mayor a menor por el monto total (sum).
5. Con apply y def (axis=1), agregar columna "ticket":
   - "Alto" si el monto promedio (mean) supera 600
   - "Medio" si supera 350 (y no es alto)
   - "Bajo" en cualquier otro 
   
"""

# traigo las tablas:
c= pd.read_sql("Select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("Select ProductID, CategoryID, ProductName from Products", engine)
od=pd.read_sql("Select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
cp=pd.merge(c, p, on="CategoryID")
cp_od=pd.merge(cp, od, on="ProductID")

# calcular la columna monto:
cp_od["monto"]=cp_od["Quantity"] * cp_od["UnitPrice"] * (1 - cp_od["Discount"])


#agrupar por categorias:
agrup_cat=cp_od.copy()
agrup_cat=agrup_cat.groupby(["CategoryID", "CategoryName"]).agg({
    "monto":["sum", "mean"],
    "Quantity":"sum"
})

agrup_cat=agrup_cat.sort_values(by=("monto", "sum"), ascending=False)

def categorizar(row):
    if row["monto","mean"] > 600:
        return "Alto"
    elif row["monto", "mean"] > 350:
        return "Medio"
    else:
        return "Bajo"
    
agrup_cat["ticket"]=agrup_cat.apply(categorizar, axis=1)
print(agrup_cat)
# python practica8.py