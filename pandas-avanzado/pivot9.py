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

Cliente: "Quiero ver, por proveedor, cuántos productos distintos 
nos vende y cuál es el precio promedio de esos productos."

Tablas: Products, Suppliers.

Merge: Products + Suppliers (por SupplierID)

PIVOT:
  - index = CompanyName (del proveedor)
  - sin columns (una sola dimensión, no hay cruce)
  - values = ["ProductID", "UnitPrice"]
  - aggfunc = {"ProductID": "nunique", "UnitPrice": "mean"}
  - fill_value = 0

"""

# traer tablas:
s=pd.read_sql("Select SupplierID, CompanyName from Suppliers", engine)
p=pd.read_sql("Select ProductID, SupplierID, ProductName, UnitPrice from Products", engine)


# merge:
sp=pd.merge(s,p,on="SupplierID")
print(sp)
# pivot:
resultado=pd.pivot_table(
    sp,
    index=["SupplierID","CompanyName"],
    values=["ProductID", "UnitPrice"],
    aggfunc={"ProductID":"nunique","UnitPrice":"mean"},
    fill_value=0
)
print(resultado)

"""
HALLAZGO:
"Aux joyeux ecclésiastiques": 3 productos, promedio $99 — 
ese número alto tiene sentido porque uno de sus productos es el 
Côte de Blaye a $263,50, que arrastra el promedio para arriba.

"""
# python pivot9.py
