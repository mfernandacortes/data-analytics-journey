import pandas as pd
import pyodbc
import numpy as np

#pd.set_option('display.max_rows', None) #para no mostrar todas las filas...

# 1. CONEXIÓN
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=FERCHUSERVER;'
    'DATABASE=Northwind;'
    'Trusted_Connection=yes;'
)

"""
Ejercicio: descubrir los productos que no se vendieron:

"""
# 1: traigo las tablas que necesito
products    = pd.read_sql("SELECT ProductID, ProductName FROM Products", conn)
order_details = pd.read_sql("SELECT OrderID, ProductID FROM [Order Details]", conn)

# 2: merge entre productos y order details

prod_no_vendidos = pd.merge(products, order_details, on = 'ProductID', how='left')
prod_no_vendidos = prod_no_vendidos[prod_no_vendidos['OrderID'].isna()]


print(prod_no_vendidos)

# python 11_pandas_joins.py