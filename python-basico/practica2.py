import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)
"""
Usar las tablas Categories, Products y Order Details.

1. Hacer merge de las tres tablas por sus claves (CategoryID y ProductID).
2. Calcular la columna monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por CategoryName y calcular en un solo agg:
   - Monto total facturado (monto → sum)
   - Cantidad de productos distintos (ProductID → nunique)
4. Ordenar de mayor a menor por monto total.
5. Con apply y def (axis=1), agregar columna "peso_categoria":
   - "Alta facturación" si el monto supera 100000
   - "Media" si supera 50000 (y no es alta)
   - "Baja" en cualquier otro caso
"""

# traer tablas que necesito:
c = pd.read_sql("Select CategoryID, CategoryName from Categories", engine)
p = pd.read_sql("Select ProductID, ProductName, CategoryID from Products", engine)
od = pd.read_sql("Select ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# 1 merge
cp = pd.merge(c, p, on="CategoryID")
cp_od = pd.merge(cp, od, on="ProductID")

# 2 Calcular monto:

cp_od["monto"]= cp_od["Quantity"] * cp_od["UnitPrice"] * (1 - cp_od["Discount"])

# 3 Agrupar por categorias y calcular Monto total facturado y cantidad de prod distintos:
agrup_cat = cp_od.copy()

agrup_cat = agrup_cat.groupby(["CategoryID", "CategoryName"]).agg({
    "monto":"sum",
    "ProductID":"nunique"
    })

print(agrup_cat)

#Parte 2: (4 y 5)


# python practica2.py
