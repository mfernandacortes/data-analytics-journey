import pandas as pd
from sqlalchemy import create_engine 
"""
Sobre Order Details de Northwind — traé UnitPrice, Quantity y Discount. Con lambda y axis=1, 
agregá una columna tiene_descuento que diga "Sí" si Discount > 0 y "No" si Discount == 0.
Pista: vas a necesitar un if/else dentro de la lambda — eso se escribe así: "Sí" if condicion else "No".
"""
# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traigo tablas que necesito:
df = pd.read_sql("Select UnitPrice, Quantity, Discount from [Order Details]", engine)
emp = pd.read_sql("Select EmployeeID, FirstName, LastName from Employees", engine)
cli = pd.read_sql("Select CustomerID, CompanyName, Country from Customers", engine)

df["tiene descuento"]= df.apply(lambda row: "No" if row["Discount"] == 0 else "Sí", axis = 1)

print(df)
"""
Sobre Employees de Northwind — traé FirstName, LastName y BirthDate. Con apply() y lambda, creá una 
columna nombre_completo que una FirstName y LastName con un espacio.
Pista: en Python los strings se unen con +.

"""

emp["nombre_completo"] = emp.apply(lambda row : row["FirstName"] + " " + row["LastName"], axis = 1)

print(emp)
"""
Un caso corto de repaso. Sobre Customers de Northwind, traé CompanyName y Country. Con 
lambda y axis=1 (o sin axis si es una sola columna), creá una 
columna es_europa que diga "Sí" si el país está en ["Germany", "France", "Spain", "Italy"] y "No" si no.

"""
# probé verificando solo si eran de Alemania:

cli["es_alemania"] = cli.apply(lambda row : "Si" if row["Country"] == "Germany" else "No", axis = 1)

print(cli)

# acá verifico la lista, si son de Europa: 

cli["es_europa"] = cli["Country"].apply(lambda x: "Sí" if x in ["Germany", "France", "Spain", "Italy"] else "No")

print(cli)

# python combinados6.py