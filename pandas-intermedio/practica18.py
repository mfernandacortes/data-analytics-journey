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


# 
"""
4. Ordenar de mayor a menor por monto total (sum).
5. Con apply y def (axis=1), agregar columna "origen":
   - "Clave" si monto sum supera 60000 Y productos (ProductID nunique) supera 5
   - "Especializado" si monto mean supera 500 (y no es clave)
   - "Menor" en cualquier otro caso
   
"""
# ordenar de mayor a menor por monto total:
agrup_pais=agrup_pais.sort_values(by=("monto","sum"), ascending=False)
# clasificar:
def clasificar(row):
    if (row["monto","sum"] > 60000) and (row["ProductID", "nunique"] > 5):
        return "Clave"
    elif row["monto", "mean"] > 500:
        return "Especializado"
    else:
        return "Menor"

agrup_pais["origen"]=agrup_pais.apply(clasificar, axis=1)

print(agrup_pais)

"""
Hallazgo:
France — factura MÁS que nadie (277K) con el ticket MÁS alto (1568), pero solo 5 productos 
"Especializado", no "Clave". Depende de pocos productos caros (el Côte de Blaye). Es el 
ejemplo perfecto de concentración.
Germany, Australia, USA, UK → "Clave": monto alto Y diversificados (7-12 productos). Estos
 son los proveedores-país sólidos.
USA es el caso opuesto a France: ticket bajo (440) pero 12 productos — el más diversificado 
de todos. Factura por variedad, no por concentración.

France vs USA es la historia completa en dos filas: uno concentra (pocos productos carísimos), 
el otro diversifica (muchos productos accesibles).

"""