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


df["tiene descuento"]= df.apply(lambda row: "No" if row["Discount"] == 0 else "Sí", axis = 1)

print(df)
"""
Sobre Employees de Northwind — traé FirstName, LastName y BirthDate. Con apply() y lambda, creá una 
columna nombre_completo que una FirstName y LastName con un espacio.
Pista: en Python los strings se unen con +.

"""

emp["nombre_completo"] = emp.apply(lambda row : row["FirstName"] + " " + row["LastName"], axis = 1)

print(emp)

