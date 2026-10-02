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
subplots con histogramas, uno al lado del otro: UnitPrice de productos y 
de Order Details

"""

# traer tablas:
p=pd.read_sql("select ProductID, ProductName, UnitPrice from Products", engine)
od=pd.read_sql("select OrderID, ProductID, Quantity from [Order Details]", engine)

# merge:
df=pd.merge(p,od,on="ProductID")
print(df)
# gráfico:

"""
python histograma4.py

"""