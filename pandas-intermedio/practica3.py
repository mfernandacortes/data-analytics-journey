import pandas as pd
from sqlalchemy import create_engine 

# conexion
engine = create_engine( 
    "mssql+pyodbc://FERCHUSERVER/Northwind"    
    "?driver=SQL+Server&trusted_connection=yes"

)
"""
Usar las tablas Customers y Orders de Northwind.

1. Hacer merge entre ambas por CustomerID.
2. Agrupar por Country y calcular en un solo agg:
   - Cantidad de pedidos distintos (OrderID → nunique)
   - Cantidad de clientes distintos (CustomerID → nunique)
3. Ordenar de mayor a menor por cantidad de pedidos.
4. Mostrar los primeros 10 países.
"""
# traigo las tablas que necesito:
c = pd.read_sql("Select * from Customers", engine)
o = pd.read_sql("Select * from Orders", engine)

# merge:
co = pd.merge(c, o, on="CustomerID")
# agrupo por pais:
ag_co = co.copy()
ag_co = ag_co.groupby("Country").agg({
    "OrderID":"nunique",
    "CustomerID":"nunique"
})
print(ag_co.sort_values(by="OrderID", ascending=False).head(10))


# python practica3.py