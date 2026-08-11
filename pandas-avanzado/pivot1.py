import pandas as pd
from sqlalchemy import create_engine 

# conexión, descomentar según de donde trabaje, por defecto es la de escritorio
engine = create_engine( 
    # ESCRITORIO:
     "mssql+pyodbc://FERCHUSERVER/Northwind?driver=SQL+Server&trusted_connection=yes"
    # NOTEBOOK:
    # "mssql+pyodbc://.\\SQLEXPRESS/Northwind?driver=SQL+Server&trusted_connection=yes"

)
ca=pd.read_sql("select CategoryID, CategoryName from Categories", engine)
p=pd.read_sql("select ProductID, CategoryID, ProductName from Products", engine)
c= pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID from Orders", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)

"""
CONSIGNA:
Tablas: Orders, Order Details, Customers, Products, Categories.

Traer las cinco con read_sql.
Merge encadenado:
  1) Order Details + Orders (por OrderID)
  2) + Customers (por CustomerID) → para tener Country
  3) + Products (por ProductID) → puente hacia Categories
  4) + Categories (por CategoryID) → para tener CategoryName
"""
# merge:
od_o=pd.merge(od,o,on="OrderID")
od_oc=pd.merge(od_o,c,on="CustomerID")
od_ocp=pd.merge(od_oc,p,on="ProductID")
df=pd.merge(od_ocp,ca,on="CategoryID")

"""




Columna calculada: monto = Quantity * UnitPrice * (1 - Discount)

PIVOT:
Con pd.pivot_table, armar una tabla cruzada:
  - index = Country (países en filas)
  - columns = CategoryName (categorías en columnas)
  - values = monto
  - aggfunc = "sum"   (declararlo siempre, no dejar el default)
  - fill_value = 0    (para que los cruces sin datos queden en 0, no NaN)

Guardar el resultado en una variable nueva.

"""
# monto:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])

print(df)

resultado = pd.pivot_table(
    df,
    index="Country",
    columns="CategoryName",
    values= "monto",
    aggfunc="sum",
    fill_value=0
)
print(resultado)

print(resultado.columns)
print(resultado.index)
# python pivot1.py