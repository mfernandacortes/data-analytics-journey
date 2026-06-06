import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)

# traigo tablas que necesito:

df = pd.read_sql("select ProductID, ProductName, UnitPrice, CategoryID from Products", engine)

# filtrar los precios menor a 10 o categorías igual a 3
df=df[ ( df["UnitPrice"] < 10 ) | (df["CategoryID"]== 3)  ]

print(df)


# filtrar precios mayor a 30 y solo categoria 3

df = df[  (df["UnitPrice"] > 30) & (df["CategoryID"] == 3) ]

print(df)


#  python condiciones_dobles.py