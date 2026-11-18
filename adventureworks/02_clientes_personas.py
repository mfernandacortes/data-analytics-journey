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
Ver los clientes y de ellos el top 5.

"""

# traer tablas:
query = """
SELECT TOP 10 c.CustomerID, p.FirstName, p.LastName
FROM Sales.Customer c
JOIN Person.Person p ON c.PersonID = p.BusinessEntityID
"""
df = pd.read_sql(query, engine)

print(df)


