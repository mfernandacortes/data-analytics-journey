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
Ejercicio de tuplas (misma base de siempre — Orders, Order Details,
 Customers, columna monto):

Agrupar por Country. En un solo .agg() con sintaxis de diccionario 
(no named aggregation): sobre monto, calcular sum y mean.
Ordenar de mayor a menor por el sum, referenciándolo como tupla en el by=.


"""

# traer tablas:
c= pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity,UnitPrice, Discount from [Order Details]", engine)

# merge:
co=pd.merge(c,o,on="CustomerID")
co_od=pd.merge(co,od,on="OrderID")

# calcular monto:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])
# agrupar y agg:

agrup_pais=co_od.copy()
agrup_pais=agrup_pais.groupby("Country").agg({
    "monto":["sum", "mean"]
})

# ordenar:
agrup_pais=agrup_pais.sort_values(by=("monto","sum"), ascending=False)

# clasificar (apply):

"""
Con apply + def (axis=1), agregar columna categoria: "Top" si el sum 
supera 
100000, "Medio" si supera 30000, "Chico" en el resto — accediendo al 
valor con la tupla dentro del row.
"""
def clasificar(row):
    if row["monto","sum"] > 100000:
        return "Top"
    elif row["monto","sum"] > 30000:
        return "Medio"
    else:
        return "Chico"

agrup_pais["categoria"]=agrup_pais.apply(clasificar, axis=1)
print(agrup_pais)
# python practica27.py
"""
HALLAZGO:

"""