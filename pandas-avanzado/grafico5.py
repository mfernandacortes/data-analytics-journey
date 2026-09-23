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
Analizar la evolución mensual de ventas de los 3 empleados con mayor 
facturación total, usando pivot_table con index="Mes", columns="LastName", 
="monto", y graficando con .plot() (línea, no barras).

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
eo=pd.merge(e,o,on="EmployeeID")
eo_od=pd.merge(eo,od,on="OrderID")

# calcular monto:
eo_od["monto"]=eo_od["Quantity"] * eo_od["UnitPrice"] * (1 - eo_od["Discount"])

# crear columna mes:
eo_od["anio"]=eo_od["OrderDate"].dt.year
eo_od["mes"]=eo_od["OrderDate"].dt.month

df=eo_od.copy()
# pivot:
informe=pd.pivot_table(
    df,
    index=["anio","mes"],
    columns=["EmployeeID","LastName"],
    values="monto",
    aggfunc="sum",
    fill_value=0
)
print(informe)

# ahora me quedo con los 3 empleados que más facturaron:
totales = informe.sum(axis=0)
top3 = totales.sort_values(ascending=False).head(3).index
informe = informe[top3]
print(informe)
"""
python grafico5.py

"""