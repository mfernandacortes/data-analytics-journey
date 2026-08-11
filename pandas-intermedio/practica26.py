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
CONSIGNA:
Tablas: Orders, Order Details, Customers.
Calcular monto en nueva columna
Agrupar por Country. En un solo agg con sintaxis de diccionario
(NO named aggregation): {"monto": ["sum", "mean"]}.
Ordenar de mayor a menor por el promedio, referenciándolo como tupla en el by=.


"""

# traer tablas:
c=pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
co=pd.merge(c,o,on="CustomerID")
co_od=pd.merge(co,od,on="OrderID")


# calcular monto:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])

print(co_od)                                                        


# agrupar y agg:
agrup_pais=co_od.copy()
agrup_pais=agrup_pais.groupby("Country").agg({
    "monto":["sum","mean"],

})

# ordenar:
agrup_pais=agrup_pais.sort_values(by=("monto","mean"), ascending=False)

# clasificar (apply):
"""
Con apply + def (axis=1), agregar columna nivel:
"Alto" si el promedio supera 800, "Bajo" en caso contrario
(accediendo al promedio con la tupla dentro del row).

"""
# clasifico por ticket promedio; corté en 800 y 500 para separar mercados 
# de alto ticket
def clasi(row):
    if row["monto","mean"] > 800:
        return "Alto"
    elif row["monto","mean"] > 500:
        return "Medio"
    else:
        return "Bajo"

agrup_pais["nivel"]=agrup_pais.apply(clasi, axis=1)
print(agrup_pais)

# python practica26.py
