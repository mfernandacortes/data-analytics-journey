import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

"""
Ejercicio:
Usando Northwind:

Cargar Orders y Employees
Hacer merge por EmployeeID
Calcular cuántos pedidos hizo cada empleado (groupby + count)
Mostrar el resultado ordenado de mayor a menor

Pasos:

Cargar las dos tablas
Merge
Groupby + count
Ordenar

"""

# traigo tablas que necesito:
od= pd.read_sql("Select OrderID, EmployeeID from Orders", engine)
emp= pd.read_sql("Select EmployeeID, LastName from Employees", engine)

od_emp=pd.merge(od, emp, on="EmployeeID")
od_emp=od_emp.groupby(["EmployeeID", "LastName"])["OrderID"].count()
#print(od_emp.sort_values(ascending=False))






"""
Calcular el monto total vendido por categoría, mostrando el nombre de la categoría, 
ordenado de mayor a menor.Calcular el monto total vendido por categoría, mostrando el nombre de la 
categoría, ordenado de mayor a menor.
Tablas:

Order Details: OrderID, ProductID, UnitPrice, Quantity, Discount
Products: ProductID, CategoryID
Categories: CategoryID, CategoryName
"""
odet=pd.read_sql("select OrderID, ProductID, Quantity, UnitPrice, Discount from [Order Details]", engine)
prod= pd.read_sql("select ProductID, ProductName, CategoryID from Products", engine)
cat= pd.read_sql("select CategoryID, CategoryName from Categories", engine)

od_prod=pd.merge(odet, prod, on ="ProductID")
od_prod_cat= pd.merge(od_prod, cat, on ="CategoryID")
od_prod_cat["monto"] = od_prod_cat["Quantity"] * od_prod_cat["UnitPrice"] * (1 - od_prod_cat["Discount"])


print(od_prod_cat["monto"])

od_prod_cat=od_prod_cat.groupby(["CategoryID", "CategoryName"])["monto"].sum().sort_values(ascending=False)

print(od_prod_cat)
# python combinados9.py
