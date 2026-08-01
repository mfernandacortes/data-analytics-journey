import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

"""
Usar las tablas Categories, Products y Order Details de Northwind.

1. Merge de las tres tablas.
2. Calcular monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por CategoryName y calcular en un solo agg:
   - monto → sum Y mean
   - Quantity → sum

"""

# traer tablas:
c=pd.read_sql("Select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("Select ProductID, CategoryID, ProductName from Products", engine)
od=pd.read_sql("Select ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge de tablas:
cp=pd.merge(c,p,on="CategoryID")
cp_od=pd.merge(cp,od,on="ProductID")
# creo el campo monto:
cp_od["monto"]=cp_od["Quantity"]*cp_od["UnitPrice"]*(1-cp_od["Discount"])


# Agrupo por Categorias y calculo monto total, promedio y cantidades vendidas
agrup_cat=cp_od.copy()
agrup_cat=agrup_cat.groupby(["CategoryID","CategoryName"]).agg({
    "monto":["sum","mean"],
    "Quantity":"sum"
})
"""
4. Ordenar de mayor a menor por monto total (sum).
5. Con apply y def (axis=1), agregar columna "tipo":
   - "Alta" si monto sum supera 150000
   - "Media" si monto sum supera 100000 (y no es alta)
   - "Baja" en cualquier otro caso

"""
agrup_cat=agrup_cat.sort_values(by=("monto","sum"), ascending=False)
# defino la función que clasifica y agrego columna "tipo":
def clasific(row):
    if row["monto","sum"] > 150000:
        return "Alta"
    elif row["monto","sum"] > 100000:
        return "Media"
    else:
        return "Baja"
agrup_cat["tipo"]=agrup_cat.apply(clasific, axis=1)
print(agrup_cat)
"""
Hallazgo:
Produce con 99984 quedó "Baja" por 16 pesos — casi toca los 100000 de "Media". Tan 
cerca. Ese tipo de detalle es bueno notarlo: un umbral es un corte duro, y a veces 
algo queda de un lado por muy poco. En un análisis real, cuando algo cae tan al límite, 
vale la pena mencionarlo ("Produce está al borde de Media").
"""