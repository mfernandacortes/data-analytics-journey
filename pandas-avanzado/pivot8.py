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
Cliente: "Para cada empleado, quiero ver cuántos clientes distintos atendió 
y cuánto facturó en total, comparando trimestre a trimestre."
.dt.quarter
"""

# traer tablas:
e=pd.read_sql("Select EmployeeID, LastName from Employees", engine)
c=pd.read_sql("Select CustomerID, CompanyName from Customers", engine)
o=pd.read_sql("Select OrderID, EmployeeID, CustomerID, OrderDate from Orders", engine)
od=pd.read_sql("Select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
od_o=pd.merge(o,od,on="OrderID")
od_oe=pd.merge(od_o,e,on="EmployeeID")
df=pd.merge(od_oe,c,on="CustomerID")


# calcular monto:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])
# trimestre=
df["trimestre"]=df["OrderDate"].dt.quarter

# pivot:
informe=pd.pivot_table(
    df,
    index=["EmployeeID","LastName"],
    columns="trimestre",
    values=["monto", "CustomerID"],
    aggfunc={"monto": "sum", "CustomerID": "nunique"},
    fill_value = 0
)
print(informe)
# python pivot8.py
"""
HALLAZGO:

"""