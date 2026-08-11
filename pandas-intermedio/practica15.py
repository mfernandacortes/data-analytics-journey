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


"""
4. Ordenar de mayor a menor por el monto promedio (mean).
5. Con apply y def (axis=1), agregar columna "perfil_categoria":
   - "Premium" si el monto promedio (mean) supera 600
   - "Volumen" si la cantidad total (Quantity sum) supera 5000 (y no es premium)
   - "Estándar" en cualquier otro caso

"""
#punto 4 ordenar de mayor a menor por promedio monto:
agrup_cat=agrup_cat.sort_values(by=("monto", "mean"), ascending=False)
#punto 5 clasificar:
def clasif(row):
    if row["monto", "mean"] > 600:
        return "Premium"
    elif row["Quantity", "sum"] > 5000:
        return "Volúmen"
    else:
        return "Estándar"
    
agrup_cat["perfil_categoria"]= agrup_cat.apply(clasif, axis=1)  
print(agrup_cat)


"""
Hallazgo:
Premium (mean > 600): Meat/Poultry, Produce, Beverages, Dairy — los cuatro de ticket alto
Volumen (Quantity > 5000, sin ser premium): Confections (7906), Condiments (5298), 
Seafood (7681) — venden mucho pero con ticket más bajo
Estándar: solo Grains/Cereals (mean 488, Quantity 4562 — no llega a ninguna de las dos 
condiciones)

El caso más interesante para leer: Seafood. Tiene el ticket promedio más bajo de todos
 (397), pero es de los que más unidades vende (7681). Por eso cae en "Volumen" — su negocio es
vender mucho a precio bajo, lo opuesto a Meat/Poultry (poco volumen, ticket altísimo de 942). 
Las dos tuplas juntas dejan ver esa diferencia de modelo de negocio en la misma tabla.
"""

"""
Sobre el resultado (agrup_cat, el de las 8 categorías con perfil):

1. Mostrar SOLO las categorías "Premium" (filtrá el DataFrame por la columna perfil_categoria).
2. De esas Premium, mostrá solo dos columnas: el monto promedio ("monto","mean") y la cantidad 
de clientes ("CustomerID","nunique").
"""

print(agrup_cat[agrup_cat["perfil_categoria"]=='Premium'])

#print(agrup_cat)

# python practica15.py