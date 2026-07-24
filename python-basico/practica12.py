import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

"""
Usar las tablas Products y Order Details de Northwind.

1. Hacer merge por ProductID.
2. Calcular la columna monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por ProductID y ProductName, y calcular en un solo agg:
   - monto → sum Y mean
   - Quantity → sum
   - OrderID → nunique
4. Ordenar de mayor a menor por el monto promedio (mean) y quedarse con los primeros 15.
5. Con apply y def (axis=1), agregar columna "rotacion":
   - "Alta" si la cantidad total (Quantity sum) supera 800
   - "Media" si supera 400 (y no es alta)
   - "Baja" en cualquier otro caso
"""
# tablas:
p=pd.read_sql("select ProductID, ProductName from Products", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

#merge:
pod=pd.merge(p, od, on="ProductID")
#monto:
pod["monto"]= pod["Quantity"] * pod["UnitPrice"] * (1 - pod["Discount"])

#metricas: montos, cantidad pedidos, promedio de monto:
pod_ag=pod.copy()
pod_ag=pod_ag.groupby(["ProductID", "ProductName"]).agg({
    "monto":["sum", "mean"],
    "Quantity":"sum",
    "OrderID":"nunique"
})

"""
Para una decisión de stock real, esto importa muchísimo: los de ticket alto 
y rotación baja te inmovilizan capital, aunque cada venta sea grande.
"""
pod_ag=pod_ag.sort_values(by=("monto", "mean"), ascending=False).head(15)

def clasif(row):
    if row["Quantity","sum"] > 800:
        return "Alta"
    elif row["Quantity","sum"] > 400:
        return "Media"
    else:
        return "Baja"


pod_ag["rotacion"]=pod_ag.apply(clasif, axis=1)
print(pod_ag)
# python practica12.py