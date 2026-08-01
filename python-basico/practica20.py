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
4. Ordenar de mayor a menor por monto total (sum).
5. Con apply y def (axis=1), agregar columna "tipo":
   - "Alta" si monto sum supera 150000
   - "Media" si monto sum supera 100000 (y no es alta)
   - "Baja" en cualquier otro caso

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
print(agrup_cat)
# python practica20.py