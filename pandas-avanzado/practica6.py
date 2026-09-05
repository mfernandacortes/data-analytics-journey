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
El gerente quiere una columna que clasifique cada pedido como "con descuento" o "sin 
descuento", pero además marque como "descuento alto" si el descuento supera el 15%.

"""

# traer tablas:

o=pd.read_sql("select OrderID, EmployeeID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
df=pd.merge(o,od, on="OrderID")

df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])

#     python practica6.py
# tengo que redondear a 2 decimales porque por un bug de los lenguajes no pueden hacerlo solo,
# 
def descuento(row):
    d = round(row["Discount"], 2)
    if d > 0.15:
        return "Descuento alto"
    elif d !=0:
        return "Con descuento"
    else:
        return "sin descuento"
df["tipo_descuento"] = df.apply(descuento, axis=1)

# print(df)
print(df[df["tipo_descuento"] == "Descuento alto"])
"""
HALLAZGO:
Error de punto flotante en comparaciones de Discount: al filtrar Discount > 0.15, 
pedidos con descuento exacto de 15% aparecían como "Descuento alto" por error. La 
base guarda 0.15 como 0.150000005960... internamente. Solución: redondear con 
round(row["Discount"], 2) antes de comparar. 
Con esto se bajó de 472 a 315 filas.

"""