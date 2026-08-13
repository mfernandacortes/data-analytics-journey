import pandas as pd
from sqlalchemy import create_engine 

# conexión, descomentar según de donde trabaje, por defecto es la de escritorio
engine = create_engine( 
    # ESCRITORIO:
     "mssql+pyodbc://FERCHUSERVER/Northwind?driver=SQL+Server&trusted_connection=yes"
    # NOTEBOOK:
    # "mssql+pyodbc://.\\SQLEXPRESS/Northwind?driver=SQL+Server&trusted_connection=yes"

)


c= pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

"""
CONSIGNA:
Merge: Order Details + Orders (OrderID) + Customers (CustomerID)
monto = Quantity * UnitPrice * (1 - Discount)
.groupby("Country").agg({"monto": ["sum", "mean"]})
sort_values(by=("monto","sum"), ascending=False)
apply(axis=1): columna nivel — "Alto" si sum>100000, "Bajo" si no
"""
# merge:
co=pd.merge(c,o,on="CustomerID")
od_oc=pd.merge(co,od,on="OrderID")


# monto:
od_oc["monto"]=od_oc["Quantity"] * od_oc["UnitPrice"] * (1 - od_oc["Discount"]) 

# promedio y suma de montos:
df=od_oc.copy()
df=df.groupby("Country").agg({
    "monto":["sum","mean"]
})
print(df)

"""
Mismas tablas + columna anio (.dt.year sobre OrderDate)
pd.pivot_table(df, index="LastName", columns="anio", 
values="monto", aggfunc="sum", fill_value=0)


"""

# python pivot3.py
