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
   - monto → sum Y mean
   - OrderID → nunique
4. Ordenar de mayor a menor por el monto total (sum).
5. Con apply y def (axis=1), agregar columna "aporte":
   - "Alto" si el monto total (sum) supera 200000
   - "Medio" si supera 120000 (y no es alto)
   - "Bajo" en cualquier otro caso
"""
#tablas:
c=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, ProductName, CategoryID from Products", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

#merge:
cp=pd.merge(c,p, on="CategoryID")
cp_od=pd.merge(cp, od, on="ProductID")
cp_od["monto"]=cp_od["Quantity"] * cp_od["UnitPrice"] * (1 - cp_od["Discount"])
print(cp_od)
agrup_cat=cp_od.copy()
agrup_cat=agrup_cat.groupby(["CategoryID", "CategoryName"]).agg({
    "monto":["sum", "mean"],
    "OrderID":"nunique"
})

agrup_cat=agrup_cat.sort_values(by=("monto", "sum"), ascending=False)
def clasif(row):
    if row["monto", "sum"] > 200000:
        return "Alto"
    elif row["monto", "sum"] > 120000:
        return "Medio"
    else:
        return "Bajo"
    
agrup_cat["aporte"]=agrup_cat.apply(clasif, axis=1)
print(agrup_cat)
# python practica13.py