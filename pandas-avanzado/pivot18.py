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
Generar un reporte por empleado que muestre, en una sola tabla, el monto total 
facturado y el monto promedio de sus líneas de pedido — para poder comparar 
ambas métricas lado a lado.

"""

# traer tablas:
e=pd.read_sql("select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("select OrderID, EmployeeID  from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, CategoryID, ProductName from Products", engine)
# merge:
eo=pd.merge(e,o,on="EmployeeID")
eood=pd.merge(eo,od,on="OrderID")
eood_p=pd.merge(eood,p,on="ProductID")
eo_od=pd.merge(eood_p, ca, on="CategoryID")

# calcular monto:
eo_od["monto"]=eo_od["Quantity"] * eo_od["UnitPrice"] * (1 - eo_od["Discount"])

# pivot:
informe=pd.pivot_table(
    eo_od,
    index=["EmployeeID", "LastName"],
    values="monto",
    aggfunc=["sum","mean"],
    margins=True,
    margins_name="Total",
    fill_value=0
)
print(informe)

"""
Al mismo reporte que ya armaste, agregale el corte por categoría de producto: 
el g además, cuál es el monto total y el monto promedio por cada categoría de 
producto, no solo por empleado.
"""
df=eo_od.copy()


informe2=pd.pivot_table(
    df,
    index=["CategoryID","CategoryName"],
    values="monto",
    aggfunc=["sum","mean"],
    margins=True,
    margins_name="Total",
    fill_value=0

)
print(informe2)
"""
HALLAZGO:
Meat/Poultry tiene el promedio más alto por lejos (942), pero no es la categoría 
que más factura en total (163 mil, lejos de Beverages con 267 mil).
"""

# python pivot18.py
