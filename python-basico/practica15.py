import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)
"""
Usar las tablas Categories, Products, Order Details y Orders de Northwind.

1. Hacer merge de las cuatro tablas por sus claves.
2. Calcular la columna monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por CategoryName y calcular en un solo agg:
   - monto → sum Y mean
   - Quantity → sum
   - OrderID → nunique
   - CustomerID → nunique
"""
# traigo las tablas en distintos df:
c = pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p = pd.read_sql("select ProductID, CategoryID, ProductName from Products", engine)
o = pd.read_sql("select OrderID, CustomerID from Orders", engine)
od = pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge
cp = pd.merge(c, p, on="CategoryID")
cp_od = pd.merge(cp, od, on="ProductID")
cp_ood=pd.merge(cp_od, o, on="OrderID")

# calcular monto:
cp_ood["monto"]=cp_ood["Quantity"] * cp_ood["UnitPrice"] * (1 - cp_ood["Discount"])

agrup_cat=cp_ood.copy()
agrup_cat=agrup_cat.groupby(["CategoryID", "CategoryName"]).agg({
    "monto":["sum", "mean"],
    "Quantity":"sum",
    "OrderID":"nunique",
    "CustomerID":"nunique"
})

print(agrup_cat)
"""
4. Ordenar de mayor a menor por el monto promedio (mean).
5. Con apply y def (axis=1), agregar columna "perfil_categoria":
   - "Premium" si el monto promedio (mean) supera 600
   - "Volumen" si la cantidad total (Quantity sum) supera 5000 (y no es premium)
   - "Estándar" en cualquier otro caso

"""

# python practica15.py