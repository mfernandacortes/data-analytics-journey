import pandas as pd
from sqlalchemy import create_engine 

# conexión, descomentar según de donde trabaje, por defecto es la de escritorio
engine = create_engine( 
    # ESCRITORIO:
     "mssql+pyodbc://FERCHUSERVER/AdventureWorks2025?driver=SQL+Server&trusted_connection=yes"
    # NOTEBOOK:
    # "mssql+pyodbc://.\\SQLEXPRESS/AdventureWorks2025?driver=SQL+Server&trusted_connection=yes"

)

"""
CONSIGNA:

"""

# traer tablas:
q_join = """
SELECT COUNT(*) AS con_persona
FROM Sales.Customer c
JOIN Person.Person p ON c.PersonID = p.BusinessEntityID
"""
q_total = "SELECT COUNT(*) AS total FROM Sales.Customer"

print(pd.read_sql(q_join, engine))
print(pd.read_sql(q_total, engine))


print(pd.read_sql("SELECT COUNT(*) AS sin_persona FROM Sales.Customer WHERE PersonID IS NULL", engine))

