import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)
"""
Usar las tablas Products y Order Details de Northwind.

1. Merge por ProductID.
2. Calcular monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por ProductName y calcular en un solo agg:
   - monto → sum Y mean
   - Quantity → sum

"""
# traigo las tablas:
p=pd.read_sql("select ProductID, ProductName from Products", engine)
od= pd.read_sql("select ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
p_od=pd.merge(p, od, on="ProductID")
#calcular monto:
p_od["monto"]=p_od["Quantity"] * p_od["UnitPrice"] * (1 - p_od["Discount"])
# agrupar por productos:
agrup_prod=p_od.copy()
agrup_prod=agrup_prod.groupby(["ProductID", "ProductName"]).agg({
    "monto":["sum","mean"],
    "Quantity":"sum"
})
"""
4. Ordenar de mayor a menor por monto total (sum) y quedarte con el top 10.
5. Con apply y def (axis=1), agregar columna "clase":
   - "Estrella" si monto sum supera 40000 Y Quantity sum supera 1000
   - "Nicho" si monto mean supera 50 (y no es estrella)
   - "Común" en cualquier otro caso
"""
print(agrup_prod)
# python practica16.py