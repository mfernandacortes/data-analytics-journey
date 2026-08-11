import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)


"""
Usar las tablas Customers, Orders y Order Details de Northwind.

1. Hacer merge de las tres tablas por sus claves.
2. Calcular la columna monto (Quantity * UnitPrice * (1 - Discount)).
3. Agrupar por Country y calcular en un solo agg:
   - Monto total facturado
   - Cantidad de pedidos distintos
   - Cantidad de clientes distintos
4. Ordenar de mayor a menor por monto total y quedarse con los primeros 10.
5. Con apply y def (axis=1), agregar columna "tipo_mercado":
   - "Mercado clave" si el monto supera 100000
   - "Mercado medio" si supera 30000 (y no es clave)
   - "Mercado chico" en cualquier otro caso

"""
# tablas que necesito:
c=pd.read_sql("Select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("Select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("Select OrderID, ProductID, UnitPrice, Quantity, Discount from [Order Details]", engine)

# merge:
co=pd.merge(c, o, on="CustomerID")
co_od=pd.merge(co, od, on="OrderID")

# calcular monto:
co_od["monto"]= co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])

agrup_pais=co_od.copy()

agrup_pais=agrup_pais.groupby("Country").agg({
    "monto":"sum",
    "OrderID":"nunique",
    "CustomerID":"nunique"
})
# el head siempre después del sort values sino corta a los primeros 10 antes de ordenar
agrup_pais=agrup_pais.sort_values(by="monto", ascending=False).head(10)

def clasificar(row):
    if row["monto"] > 100000:
        return "Mercado clave"
    elif row["monto"] > 30000:
        return "Mercado medio"
    else:
        return "Mercado chico"
agrup_pais["tipo_mercado"]=agrup_pais.apply(clasificar, axis = 1)

print(agrup_pais)

# python practica5.py