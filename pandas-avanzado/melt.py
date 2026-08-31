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
df_largo = df_ancho.melt(
    id_vars=["EmployeeID", "LastName"],   # columnas que se mantienen fijas
    value_vars=["1996", "1997", "1998"],  # columnas que se van a apilar
    var_name="anio",                       # nombre de la nueva columna con los años
    value_name="monto_total"               # nombre de la nueva columna con los valores
)

"""

# traer tablas:
e=pd.read_sql("Select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("Select OrderID, EmployeeID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo=pd.merge(e,o,on="EmployeeID")
eo_od=pd.merge(eo,od,on="OrderID")

# calcular monto:
eo_od["monto"]=eo_od["Quantity"] * eo_od["UnitPrice"] * (1 - eo_od["Discount"])
eo_od["anio"]=eo_od["OrderDate"].dt.year
print(eo_od)
# pivot:
informe=pd.pivot_table(
    eo_od,
    index=["EmployeeID", "LastName"],
    columns="anio",
    values="monto",
    aggfunc="sum",
    fill_value=0
)
print(informe)
informe = informe.reset_index()
df_largo = informe.melt(
    id_vars=["EmployeeID", "LastName"],
    var_name="anio",
    value_name="monto_total"
)
print(df_largo)
# python melt.py
