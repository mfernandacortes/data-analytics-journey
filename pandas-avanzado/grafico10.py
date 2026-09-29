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
mostrar monto total y cantidad total, mes a mes, en paneles separados pero en la 
misma ventana.

"""

# traer tablas:
o=pd.read_sql("select OrderID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
o_od=pd.merge(o,od,on="OrderID")

# calcular monto:
o_od["monto"]=o_od["Quantity"] * o_od["UnitPrice"] * (1 - o_od["Discount"])

# año y mes:
o_od["anio"]=o_od["OrderDate"].dt.year
o_od["mes"]=o_od["OrderDate"].dt.month

monto_mensual = o_od.groupby(["anio","mes"])["monto"].sum()
quantity_mensual = o_od.groupby(["anio","mes"])["Quantity"].sum()

# gráfico:
import matplotlib.pyplot as plt

quantity_mensual = o_od.groupby(["anio", "mes"])["Quantity"].sum()

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

monto_mensual.plot(ax=ax[0], title="Monto total mensual")
quantity_mensual.plot(ax=ax[1], title="Cantidad total mensual")

plt.tight_layout()
plt.show()


"""
python grafico10.py

"""