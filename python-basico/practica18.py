import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)
"""
Usar las tablas Suppliers, Products y Order Details de Northwind.

Recordá: Products se une a Suppliers por SupplierID.

1. Merge de las tres tablas.
2. Calcular monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por Country (el país del proveedor) y calcular en un solo agg:
   - monto → sum Y mean
   - ProductID → nunique
"""
# traigo las tablas que necesito:
s=pd.read_sql("Select SupplierID, CompanyName, Country from Suppliers", engine)
p=pd.read_sql("Select ProductID, ProductName, SupplierID from Products", engine)
od=pd.read_sql("Select ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge de tablas:
sp=pd.merge(s, p, on="SupplierID")
sp_od=pd.merge(sp, od, on="ProductID")


# calculo monto agregando la columna:
sp_od["monto"]=sp_od["Quantity"] * sp_od["UnitPrice"] * (1 - sp_od["Discount"])

# agrupo por pais del proveedor y calculo las métricas: sumas y promedios y cada producto:
agrup_pais=sp_od.copy()
agrup_pais=agrup_pais.groupby("Country").agg({
    "monto":["sum", "mean"],
    "ProductID":"nunique"
})

print(agrup_pais)
# python practica18.py

"""
4. Ordenar de mayor a menor por monto total (sum).
5. Con apply y def (axis=1), agregar columna "origen":
   - "Clave" si monto sum supera 60000 Y productos (ProductID nunique) supera 5
   - "Especializado" si monto mean supera 500 (y no es clave)
   - "Menor" en cualquier otro caso
   
"""