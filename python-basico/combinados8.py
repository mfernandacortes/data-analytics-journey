"""
 Sobre la tabla Products de Northwind, traé ProductName, UnitPrice y UnitsInStock.
Con apply() y axis=1, creá una columna categoria_precio que diga:

"Económico" si UnitPrice es menor a 15
"Medio" si UnitPrice es entre 15 y 50
"Premium" si UnitPrice es mayor a 50

"""

import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traigo tablas que necesito:

prod= pd.read_sql("Select ProductID, ProductName, UnitPrice, UnitsInStock from Products", engine)

#st["estado_stock"]=st.apply(lambda row : "Sin Stock" if row["UnitsInStock"] == 0 else "Stock bajo" if row["UnitsInStock"] <= 10 else "Stock normal", axis = 1)

prod["columna_categoria"] = prod.apply(lambda row: "Económico" if row["UnitPrice"] <= 15 else "Medio" if (row["UnitPrice"] > 15) & (row["UnitPrice"] <= 50) else "Premium", axis = 1)

print(prod)