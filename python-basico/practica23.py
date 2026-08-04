import pandas as pd
from sqlalchemy import create_engine 

# conexión, descomentar según de donde trabaje, por defecto es la de escritorio
engine = create_engine( 
    # ESCRITORIO:
     "mssql+pyodbc://FERCHUSERVER/Northwind?driver=SQL+Server&trusted_connection=yes"
    # NOTEBOOK:
    # "mssql+pyodbc://.\\SQLEXPRESS/Northwind?driver=SQL+Server&trusted_connection=yes"

)

"""
CONSIGNA:
Usar las tablas Products, Categories y Order Details de Northwind.

1. Merge de las tres tablas.
2. Calcular monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por CategoryName y calcular en un solo agg (CON TUPLAS, no named):
   - monto → sum Y mean
   - Quantity → sum Y mean
4. Ordenar de mayor a menor por el promedio de monto ("monto","mean").
5. Mostrar SOLO las columnas ("monto","mean") y ("Quantity","mean") usando doble corchete.

"""


# traer tablas:
p=pd.read_sql("Select ProductID, CategoryID, ProductName from Products", engine)
c=pd.read_sql("Select CategoryID, CategoryName from Categories", engine)
od=pd.read_sql("Select ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)
# merge:
pc=pd.merge(p,c,on="CategoryID")
pc_od=pd.merge(pc,od,on="ProductID")


# calcular monto:
pc_od["monto"]=pc_od["Quantity"] * pc_od["UnitPrice"] * (1 - pc_od["Discount"])



# agrupar y agg:
agrup_cat=pc_od.copy()
agrup_cat=agrup_cat.groupby(["CategoryID", "CategoryName"]).agg({
    "monto":["sum","mean"],
    "Quantity":["sum","mean"]
})

# ordenar:

print(agrup_cat)
# clasificar (apply):
# python practica23.py


"""
HALLAZGO:

"""