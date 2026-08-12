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
Tablas: Employees, Orders, Order Details.
Traer las tres con read_sql (traer OrderDate de Orders, y LastName + EmployeeID de Employees).
Merge encadenado:
  1) Order Details + Orders (por OrderID)
  2) + Employees (por EmployeeID) → para tener LastName

Columna calculada: monto = Quantity * UnitPrice * (1 - Discount)
Columna calculada: anio = usar .dt.year sobre OrderDate

PIVOT:
Con pd.pivot_table, armar una tabla cruzada:
  - index = LastName (empleados en filas)
  - columns = anio (años en columnas)
  - values = monto
  - aggfunc = "sum"
  - fill_value = 0

Guardar el resultado en una variable nueva.

"""
# traer tablas:

e= pd.read_sql("Select EmployeeID, LastName from Employees", engine)
o=pd.read_sql("Select OrderID, EmployeeID, OrderDate from Orders", engine)
od=pd.read_sql("Select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)
# merge:
od_o=pd.merge(od,o,on="OrderID")
df=pd.merge(od_o,e,on="EmployeeID")

# calcular monto:
df["monto"]=df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])
df["anio"]=df["OrderDate"].dt.year



pivot4 = pd.pivot_table(
    df,
    index="LastName",
    columns="anio",
    values= "monto",
    aggfunc="sum",
    fill_value=0
)
print(pivot4)

# python pivot4.py


"""
HALLAZGO:
Con estas comparaciones de años, se ve claramente que el año 1998 tiene
una gran caída de números, esto sucede porque el dataset llegó hasta mayo de 
1998, o sea, es parcial. Este tipo de diferencias en una empresa puede mostrar
la pronta quiebra de la misma.

"""