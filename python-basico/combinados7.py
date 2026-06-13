import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traigo tablas que necesito:

emp = pd.read_sql("Select EmployeeID, FirstName, LastName, HireDate, BirthDate from Employees", engine)
st = pd.read_sql("Select ProductID, ProductName, UnitPrice, UnitsInStock from Products", engine)

""" 
Sobre Employees de Northwind — traer FirstName, LastName y BirthDate. Con apply() y lambda, creá una 
columna nombre_completo que una FirstName y LastName con un espacio.
Pista: en Python los strings se unen con +.


Sobre Employees de Northwind, traer HireDate y BirthDate. Con apply() y axis=1, calcular la edad que tenía 
cada empleado al momento de ser contratado (en años, aproximado).
Pista: la diferencia entre dos fechas en días se obtiene restando, y para convertir 
a años aproximados dividir por 365.
"""

#emp["nombre_completo"] = emp.apply(lambda row : row["FirstName"] + " " + row["LastName"], axis = 1)

# emp["anios_contrato"] = emp.apply(lambda row : row["HireDate"] - row["BirthDate"], axis = 1)

#emp["anios_contrato"] = emp.apply(lambda row: (row["HireDate"] - row["BirthDate"]).days / 365, axis=1)

#print(emp)

"""
Ahora el caso nuevo — abrir un archivo nuevo combinados7.py. Sobre Products, traer UnitPrice y UnitsInStock. 
Con axis=1, calcul valor_inventario = UnitPrice * UnitsInStock. 
"""


st["valor_inventario"] = st.apply(lambda row : (row["UnitPrice"] * row["UnitsInStock"]), axis = 1)

#print(st)
"""
Ahora el caso con axis=0 — sobre el mismo DataFrame, calculá el promedio de UnitPrice y
de valor_inventario usando apply() sin axis (o axis=0). 

"""

# pedidos[["UnitPrice", "Quantity"]].apply(lambda col: col.mean())

print(st[["UnitPrice", "valor_inventario"]].apply(lambda col: col.mean()))
