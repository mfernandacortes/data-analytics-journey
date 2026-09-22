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
Analizar el total vendido por país de cliente y trimestre, armando un pivot 
con index="Trimestre", columns="Country", values="monto", y graficarlo con 
.plot(kind="bar").

"""

# traer tablas:
c=pd.read_sql("select CustomerID, CompanyName, Country from Customers", engine)
o=pd.read_sql("select OrderID, CustomerID, OrderDate from Orders", engine)
od=pd.read_sql("select OrderID, Quantity, UnitPrice, Discount from [Order Details]", engine)

# merge:
co=pd.merge(c,o,on="CustomerID")
co_od=pd.merge(co,od,on="OrderID")

# calcular monto:
co_od["monto"]=co_od["Quantity"] * co_od["UnitPrice"] * (1 - co_od["Discount"])
co_od["trimestre"]=co_od["OrderDate"].dt.quarter
# pivot:
print(co_od)
informe=pd.pivot_table(
    co_od,
    index="Country",
    columns="trimestre",
    values="monto",
    aggfunc="sum",
    fill_value=0
)

print(informe)
# para el gráfico voy a invertir el pivot:
informe2=pd.pivot_table(
    co_od,
    index="trimestre",
    columns="Country",
    values="monto",
    aggfunc="sum",
    fill_value=0
)

# gráfico:
import matplotlib.pyplot as plt
informe["total"] = informe.sum(axis=1)
top5 = informe.sort_values("total", ascending=False).head(5)
top5 = top5.drop(columns="total")

top5.plot(kind="bar")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()



"""
HALLAZGO:
## Top 5 paises por venta y trimestre — Grafico de barras filtrado

**Pregunta:** ¿Cuales son los 5 paises con mayor facturacion en Northwind, y como 
se distribuye esa venta a lo largo de los 4 trimestres?

**Metodo:** pivot_table con index="Country", columns="trimestre", values="monto", 
aggfunc="sum". Se calculo el total por pais con sum(axis=1), se ordeno con 
sort_values y se tomaron los 5 primeros con head(5). Se elimino la columna auxiliar 
"total" antes de graficar con plot(kind="bar"), y se movio la leyenda afuera del 
grafico con bbox_to_anchor.

**Resultado:** USA es el pais con mayor facturacion total, con un trimestre 1 
particularmente fuerte (mas de $80.000). Germany es el segundo, con ventas mas 
parejas entre trimestres. Austria, Brazil y France completan el top 5, bastante 
mas atras.

**Conclusion:** Con 21 paises el grafico de barras agrupadas se vuelve ilegible 
- filtrar al top N antes de graficar es clave para que el grafico comunique algo 
util. La eleccion del grafico correcto depende tanto de los datos como de cuantas 
categorias se van a comparar.
"""