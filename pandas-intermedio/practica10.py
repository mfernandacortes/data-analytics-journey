import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

"""
Usar las tablas Suppliers, Products y Order Details de Northwind.

1. Hacer merge de las tres tablas por sus claves.
2. Calcular la columna monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por SupplierID y CompanyName, y calcular en un solo agg:
   - monto → sum Y mean
   - Quantity → sum
   - ProductID → nunique
4. Ordenar de mayor a menor por la cantidad total vendida (Quantity sum).
5. Con apply y def (axis=1), agregar columna "escala":
   - "Mayorista" si la cantidad total (Quantity sum) supera 1500
   - "Intermedio" si supera 800 (y no es mayorista)
   - "Pequeño" en cualquier otro caso
"""
# tablas:
s=pd.read_sql("select SupplierID, CompanyName from Suppliers", engine)
p=pd.read_sql("select ProductID, ProductName, SupplierID from Products", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)
#merge:
sp=pd.merge(s, p, on="SupplierID")
sp_od=pd.merge(sp, od, on="ProductID")
#monto:
sp_od["monto"]=sp_od["Quantity"] * sp_od["UnitPrice"] * (1 - sp_od["Discount"])
#agrupar:
agrup_sp=sp_od.copy()
agrup_sp=agrup_sp.groupby(["SupplierID", "CompanyName"]).agg({
    "monto":["sum", "mean"],
    "Quantity":"sum",
    "ProductID":"nunique"
})
#ordeno con el argumento quantity sum:
agrup_sp=agrup_sp.sort_values(by=("Quantity", "sum"), ascending=False)

def clasificar(row):
    if row["Quantity", "sum"] > 1500:
        return "Mayorista"
    elif row["Quantity", "sum"] > 800:
        return "Intermedio"
    else:
        return "Minorista"
    
agrup_sp["escala"]=agrup_sp.apply(clasificar, axis=1)
print(agrup_sp)
# python practica10.py