# Hallazgos del análisis — Northwind

## Señal de churn — Cliente ALFKI

**Archivo:** [`semana-02/05_lag_dias_entre_pedidos_clientes.sql`](https://github.com/mfernandacortes/data-analytics-journey/blob/main/semana-02/05_lag_dias_entre_pedidos_clientes.sql)  
**Herramienta:** SQL — LAG + DATEDIFF

Usando `LAG` y `DATEDIFF` para calcular los días entre pedidos por cliente,
encontré un patrón inusual en el cliente **Alfred Futterkiste (ALFKI)**:

- En 1997: pedidos cada 10–60 días (comportamiento normal)
- Entre abril 1998 y enero 1999: **gap de casi un año**
- Enero 1999 fue su **último pedido**

> Este tipo de brecha es una señal clásica de churn.
> Próxima pregunta a investigar: *¿Cambió el vendedor asignado antes de que apareciera el gap?*

Un dashboard que muestre solo el total de pedidos nunca detectaría este patrón.

---

## Riesgo de concentración de revenue — USA y Alemania

**Archivo:** semana-04/04_pandas_agg_merge.py
**Herramienta:** Python — Pandas (groupby + agg)

Calculando el revenue total por país uniendo Customers, Orders y Order Details,
encontré que USA y Alemania concentran una porción desproporcionada del total:

- USA: $245.584 — puesto 1
- Alemania: $230.284 — puesto 2
- Austria: $128.003 — puesto 3 (menos de la mitad que USA)

> Esta brecha representa un riesgo de concentración.
> Un negocio tan dependiente de dos mercados queda muy expuesto
> si los clientes clave de esos países reducen sus compras.

## Análisis de performance de empleados por revenue

**Archivo:** semana-04/05_pandas_empleados_revenue.py 
**Herramienta:** Python — Pandas (groupby + agg)

Al analizar el revenue total, cantidad de pedidos y promedio por pedido de cada empleado se identificaron dos perfiles distintos:

### Perfil 1 — Alto volumen, bajo ticket promedio
**Margaret Peacock** lidera en revenue total y cantidad de pedidos (156), pero al ordenar por promedio cae al puesto 7 ($1.492 por pedido).
**Estrategia sugerida:** trabajar en upselling y productos de mayor valor para aumentar el ticket promedio.

### Perfil 2 — Bajo volumen, alto ticket promedio
**Fuller, King y Dodsworth** tienen entre 3 y 4 veces menos pedidos que Peacock pero superan su promedio.
**Estrategia sugerida:** incentivar con bonos escalonados por cantidad de pedidos, con el desafío de mantener el promedio actual.

> Este tipo de segmentación permite diseñar estrategias comerciales distintas por perfil, en lugar de una política uniforme para todo el equipo.

## Merge fino — clientes sin pedidos

**Archivo:** pandas-avanzado/practica3.py
**Herramienta:** Python — Pandas (merge left + isna)

Usando un left join entre Customers y Orders, detecté 2 clientes dados de alta
que nunca hicieron un pedido:

- FISSA Fabrica Inter. Salchichas S.A.
- Paris spécialités

> Son clientes activos en el sistema pero sin revenue generado nunca — 
> candidatos directos para una campaña de reactivación del equipo de marketing.

## Categoría vs trimestre: volumen y ticket promedio (pivot_table aggfunc múltiple)

Comparando suma total y promedio (ticket) por categoría y trimestre, se repite el 
patrón visto antes con empleados (Peacock vs Dodsworth): Beverages es la categoría 
con mayor facturación total en todos los trimestres, pero no necesariamente la de 
mayor ticket promedio por pedido — categorías como Meat/Poultry muestran promedios 
más altos por pedido individual pese a facturar menos en volumen total.

Conclusión: la categoría que más vende no es necesariamente la de mayor valor por pedido.
## Merge left + indicator — productos sin ventas (Northwind)
**Fecha:** 12/9/2026 
**Archivo:** pandas-avanzado/merge_fino.py

Se encontró el producto Yerba Mate Tradicional que no está asociado a ningún pedido
(ID 1078), es decir: nunca se vendió, capital parado. Propuesta urgente: una promo
muy atractiva para poder vender, revisar precio, preguntar a los vendedores.

## Merge left + indicator — clientes sin pedidos (Northwind)
**Fecha:** 13/9/2026
**Archivo:** pandas-avanzado/merge_fino2.py

Se detectaron 2 clientes registrados sin ningún pedido asociado: FISSA Fábrica
Inter. Salchichas S.A. y Paris Spécialités. Posibles causas: falta de seguimiento
comercial o ausencia de vendedor asignado. Propuesta: identificar si tienen
vendedor a cargo, indagar el motivo de la inactividad y evaluar un descuento de
reactivación como incentivo.

## Merge left + indicator — empleados sin pedidos (Northwind)
**Fecha:** 14/9/2026
**Archivo:** pandas-avanzado/merge_fino3.py

Se encontró un único registro sin match: EmployeeID 11 ("Prueba"), que corresponde
a un registro de testing dentro del dataset y no a un empleado real. Esto confirma
que no existe ningún empleado real sin pedidos asignados, y que la consulta
funciona correctamente.

## Merge left + indicator=True — Suppliers vs Products
**Fecha:** 16/9/2026
**Archivo:** pandas-avanzado/merge_fino5.py

**Pregunta:** ¿Hay proveedores cargados en el sistema que no tengan ningún producto asociado?

**Método:** Merge left entre Suppliers y Products con indicator=True, filtrando por _merge == 'left_only'.

**Resultado:** DataFrame vacío — los 29 suppliers del dataset tienen al menos un producto asociado. No hay proveedores "huérfanos" para depurar.

**Conclusión:** A diferencia del caso Products vs Order Details (donde sí apareció un producto sin ventas), acá no hay inconsistencias de este tipo entre Suppliers y Products.

## Ventas por categoria y anio — Grafico de barras agrupadas
**Fecha:** 21/9/2026
**Archivo:** pandas-avanzado/grafico3.py

**Pregunta:** ¿Como evolucionaron las ventas de cada categoria de producto a lo largo de los años en Northwind?

**Metodo:** pivot_table con index="Anio", columns="CategoryName", values="monto", aggfunc="sum". Luego reset_index() + set_index("CategoryName") para graficar con df.plot(kind="bar").

**Resultado:** 1997 fue el año pico de ventas en practicamente todas las categorias, con una caida notoria en 1998 (posiblemente por ser un año incompleto en el dataset). Beverages y Dairy Products son las categorias con mayor facturacion en los tres años.

**Conclusion:** El grafico de barras agrupadas es ideal para comparar una metrica a traves de multiples categorias y periodos simultaneamente, mucho mas claro que una tabla numerica para detectar patrones temporales.

## Evolucion ventas top 3 empleados por trimestre — Grafico de lineas
**Fecha:** 23/9/2026
**Archivo:** pandas-avanzado/grafico5.py

**Pregunta:** ¿Como evoluciono la facturacion de los 3 empleados con mayor venta 
total, a lo largo del tiempo?

**Metodo:** pivot_table con index=["anio","trimestre"], columns=["EmployeeID",
"LastName"], values="monto", aggfunc="sum". Filtrado a los 3 empleados de mayor 
venta total con sum(axis=0) + sort_values + head(3). Graficado con informe.plot() 
(lineas) + plt.legend().

**Resultado:** Con granularidad mensual el grafico de lineas resulto ilegible por 
la volatilidad de los datos. Agrupando por trimestre en lugar de mes, la tendencia 
se ve clara: Leverling tuvo un pico fuerte en Q1 1998 (63.605), superando a Peacock
que venia liderando en los trimestres anteriores.

**Conclusion:** La eleccion de la granularidad temporal (mes vs trimestre) es tan 
importante como el tipo de grafico para que una visualizacion comunique una tendencia
real en vez de ruido.

## Hallazgo — Precios concentrados en lo económico (Northwind)

**Fecha:** 28/9/2026
**Archivo:** pandas-avanzado/grafico9.py y top10precios.py


En Northwind los precios están muy concentrados en lo económico. Más de 50 de los 78 productos cuestan menos de unos $28, y hay un caso extremo: **Côte de Blaye**, a $263,50, más del doble que el segundo más caro (Thüringer Rostbratwurst, $123,79).

Cruzando con el top 10 de cantidades, Côte de Blaye no figura entre los más vendidos por unidades. En cambio **Raclette Courdavault** ($55) y **Tarte au sucre** ($49,30) aparecen en las dos listas: están entre los más caros y también entre los más vendidos. Con estos gráficos no se puede saber cuál pesa más en la facturación, porque eso pide combinar precio y cantidad (`Quantity * UnitPrice`).

## Hallazgo — Sesgo en tamaño de pedidos (Northwind)

**Fecha:** 06/10/2026
**Archivo:** estadistica/practica3.py

Quantity (Order Details): media 23.81 vs mediana 20 — la media queda por encima porque hay pedidos grandes (máx. 130) mezclados con la mayoría de pedidos chicos (Q1=10, Q3=30). Mismo patrón de sesgo que se vio en UnitPrice con Côte de Blaye.

## Hallazgo — Sesgo en tamaño de pedidos (Northwind)

**Fecha:** 07/10/2026
**Archivo:** estadistica/distribucion.py

UnitPrice (Products) — sesgo: skew() = 4.97, confirma numéricamente el sesgo a la derecha ya visto en el histograma y en la brecha media-mediana (28.70 vs 19.48). Sesgo fuerte, no sutil.

**Fecha:** 08/10/2026
**Archivo:** estadistica/distribucion3.py

Sesgo de precios por categoría (Northwind): skew() de UnitPrice por categoría, de mayor a menor: Beverages (3.49) y Seafood (2.09) con los precios más estirados hacia arriba; Produce (-0.07) y Dairy Products (-0.15) casi simétricas. El sesgo global de 4.97 no se reparte parejo entre categorías: se concentra en unas pocas.

**Fecha:** 09/10/2026
**Archivo:** estadistica/precios.py
Sesgo de Beverages (Northwind): el skew() de 3.49 en Beverages lo explica un solo producto: Côte de Blaye ($263.50), casi 6 veces más caro que el segundo (Ipoh Coffee, $46.00). El resto de la categoría se concentra entre $4.50 y $19. Un único outlier alcanza para sesgar toda la categoría.

## Hallazgo — Muestras al azar de Quantity (Northwind)

**Fecha:** 10/10/2026
**Archivo:** estadistica/sample.py

Con 3 muestras de 100 filas (más una de 100 previa) los promedios dieron entre 24.3 y 25.61, y la media real (23.81) quedó afuera. Con 3 muestras de 1000 filas dieron entre 23.445 y 24.024, y la media real quedó adentro. A mayor tamaño de muestra, los promedios se parecen más entre sí y se acercan al de la población (ley de los grandes números).


## Hallazgo — Tamaño de muestra y dispersión (Quantity, Northwind)

**Fecha:** 11/10/2026
**Archivo:** estadistica/sample2.py

Con muestras de 30 filas los promedios se dispersan mucho (de 18.07 a 30.83 en dos corridas), con 100 filas van de 24.3 a 25.61 y con 1000 filas de 23.445 a 24.024, cerca de la media real (23.81). A menor tamaño de muestra, mayor dispersión de los promedios y un intervalo de confianza más ancho.

## Hallazgo — Intervalo de confianza de Quantity (Northwind)
**Fecha:** 12/10/2026
**Archivo:** estadistica/inferencial.py

Con una sola muestra de 100 filas, el intervalo de confianza de la media (media ± 1.96 * std / raíz de n) dio de 18.2 a 25.5, y la media real (23.81) cayó adentro. Con una sola muestra se puede estimar un rango para la media de toda la población, y ese rango se angosta al agrandar la muestra.

## Hallazgo — A/B testing con valor p (ejemplo de botón azul vs verde)
**Fecha:** 13/10/2026
**Archivo:** estadistica/testing.py

Con 1.000 visitantes por grupo, 100 vs 115 compras dio un valor p de 0.31, que es compatible con el azar y no alcanza para decir que el verde es mejor. Con 100 vs 160 compras el valor p fue de 0.0000875, y una diferencia así casi nunca aparece por casualidad. Valor p chico (menos de 0.05) indica una diferencia probablemente real. Datos de ejemplo, calculado con chi2_contingency de scipy.

## Hallazgo — Ventas por empleado y año (Northwind)
**Fecha:** 14/10/2026
**Archivo:** pandas-avanzado/pivot22.py

En 1997 Peacock fue el empleado con más ventas ($128.810), seguido por Leverling ($108.026). Peacock también encabezó 1996 ($49.945), pero en 1998 Leverling pasó a primer lugar ($76.563). Los datos de 1998 llegan solo hasta mayo, así que los montos de ese año no son comparables con los anteriores.

## Hallazgo — Ventas por categoría y año (Northwind)
**Fecha:** 15/10/2026
**Archivo:** pandas-avanzado/pivot23.py

Beverages es la categoría que más creció: de $47.919 en 1996 a $103.924 en 1997, y llegó a $116.025 en 1998 con el año incompleto, siendo la única que sigue subiendo ese año. En 1997 la categoría líder fue Dairy Products ($115.388). Las otras 7 categorías bajan en 1998, pero los datos de ese año llegan solo hasta principios de mayo, así que no son comparables con los años completos.

## Hallazgo — Ventas por empleado y categoría (Northwind, 1996-1998)
**Fecha:** 16/10/2026
**Archivo:** pandas-avanzado/pivot24.py

Peacock lidera cuatro categorías: Beverages ($50.308), Condiments ($23.315), Meat/Poultry ($30.867) y Seafood ($27.316). Leverling lidera Confections ($33.622) y Davolio lidera Produce ($19.706). Dodsworth casi no vendió Produce ($315). Quedan por revisar Dairy Products y Grains/Cereals, que el resultado oculta.

## Hallazgo — Unidades vendidas por país y año (Northwind)
**Fecha:** 17/10/2026
**Archivo:** pandas-avanzado/pivot25.py

Alemania y USA son los dos mercados más grandes, muy por encima del resto. Alemania lidera 1996 (1.910 unidades) y 1997 (4.756), y USA lidera 1998 (3.152), con el año incompleto (llega hasta principios de mayo). Sumando los tres años, USA queda apenas arriba: 9.330 unidades contra 9.213 de Alemania. Argentina no registra ventas en 1996 y recién aparece en 1997.

## Hallazgo — Ventas por transportista y año (Northwind):
**Fecha:** 18/10/2026
**Archivo:** pandas-avanzado/pivot26.py

United Package es el transportista que más monto movió en total ($533.548 sumando los tres años) y lidera 1997 ($237.146) y 1998 ($219.629). Federal Shipping lideraba en 1996 ($81.221), pero pasa al último lugar en 1998 ($102.549), aunque ese año está incompleto (llega hasta principios de mayo). Speedy Express fue el de menor monto en 1996 y 1997.

## Hallazgo — Unidades vendidas por empleado y año (Northwind):
**Fecha:** 19/10/2026
**Archivo:** pandas-avanzado/pivot27.py

Peacock lidera 1996 (2.212 unidades) y 1997 (5.273), y también el total de los tres años (9.798). En 1998 Leverling pasa al primer lugar (2.476), con Peacock cayendo a 2.313. Dodsworth es el único empleado que crece todos los años (575, 955 y 1.140), mientras los otros 8 bajan en 1998. Ese año está incompleto (los datos llegan hasta principios de mayo), así que el resto no necesariamente vendió menos. El patrón coincide con el del monto vendido: Peacock lidera 1996 y 1997, y Leverling 1998.

## Hallazgo — Monto vendido por país y transportista (Northwind):
**Fecha:** 21/10/2026
**Archivo:** pandas-avanzado/pivot28.py

United Package es el transportista que más monto movió en 15 de los 21 países, incluida USA ($100.791, con Federal Shipping cerca en $91.057). Speedy Express lidera solo en Alemania ($94.847, el monto más alto de un transportista en un país tras USA) e Italia. Federal Shipping lidera en Dinamarca, México, Portugal y Suiza. Alemania es el único mercado grande donde United Package no es primero.

## Hallazgo — Monto vendido por país y transportista (Northwind):
**Fecha:** 22/10/2026
**Archivo:** pandas-avanzado/pivot29.py

Monto vendido por categoría y transportista (Northwind): United Package lidera 7 de las 8 categorías. La única excepción es Condiments, donde Speedy Express gana por muy poco ($39.675 contra $38.863). El monto más alto del pivot es Beverages con United Package ($118.621). La ventaja más marcada está en Meat/Poultry, donde United Package ($84.281) vende unas 2,7 veces más que Speedy Express ($31.139). Coincide con el pivot por país, donde United Package también lidera en 15 de 21 países.

## Hallazgo — Monto vendido por empleado y transportista (Northwind):
**Fecha:** 23/10/2026
**Archivo:** pandas-avanzado/pivot30.py

United Package lidera en 8 de los 9 empleados. La única excepción es Fuller, donde Speedy Express gana por poco ($63.300 contra $61.960). El monto más alto es Peacock con United Package ($106.643), y Peacock es también el empleado con mayor monto total ($232.891). En King la diferencia entre United Package ($52.099) y Federal Shipping ($50.430) es mínima. Coincide con los pivots por país y por categoría, donde United Package también es el transportista que más monto mueve.

## Hallazgo — Monto vendido por país y categoría (Northwind):
**Fecha:** 24/10/2026
**Archivo:** pandas-avanzado/pivot31.py

USA y Alemania se reparten el primer lugar entre las seis categorías visibles. USA lidera Beverages ($60.521), Confections ($36.315), Meat/Poultry ($41.635) y Seafood ($23.507). Alemania lidera Condiments ($16.737) y Produce ($16.013). En Meat/Poultry USA vende el doble que Alemania ($21.456), y en Condiments, Confections y Seafood la diferencia entre los dos es mínima. Irlanda vende $20.914 en Meat/Poultry, unas 3 veces más que en su siguiente categoría visible (Seafood, $6.899). Brasil concentra Beverages ($37.193), también unas 3 veces más que en su siguiente categoría. Argentina no registra ventas de Meat/Poultry. El resultado oculta Dairy Products y Grains/Cereals, así que el hallazgo vale solo para las otras seis.

## Hallazgo — Unidades vendidas por país de proveedor y categoría (Northwind):
**Fecha:** 25/10/2026
**Archivo:** pandas-avanzado/pivot32.py

USA (6.828), Alemania (6.120) y Australia (6.045) son los países de proveedor con más unidades vendidas. La celda más alta es Francia en Dairy Products (3.073), y esa categoría solo tiene proveedores en cuatro países (Francia, Italia, Noruega y España). Alemania y Australia son los más diversificados, con proveedores en 7 de las 8 categorías, mientras que Brasil, Dinamarca, Países Bajos, Noruega y España concentran todo en una sola categoría. Los 0 del pivot indican que el país no tiene proveedores de esa categoría, no que no se vendió.

## Hallazgo — Unidades vendidas por categoría y año (Northwind):
**Fecha:** 26/10/2026
**Archivo:** pandas-avanzado/pivot33.py

Dairy Products lidera 1996 (2.086 unidades) y 1997 (4.374). En 1998 pasa a liderar Beverages (3.694), con el año incompleto (los datos llegan hasta principios de mayo, cerca de un tercio del año). Beverages vendió en esos pocos meses casi lo mismo que en todo 1997 (3.996), y su monto por unidad subió de unos $26 a unos $31. Meat/Poultry y Produce son las categorías con menos unidades en 1997 (2.189 y 1.583). Los totales por año (9.581, 25.489 y 16.247) coinciden con los del pivot de unidades por empleado.

## Hallazgo — Unidades enviadas por transportista y año (Northwind):
**Fecha:** 27/10/2026
**Archivo:** pandas-avanzado/pivot34.py

United Package es el transportista con más unidades en total (19.945) y lidera 1997 (9.253) y 1998 (7.345). Federal Shipping lideraba 1996 (3.680), pero pasa al último lugar en 1997 (7.874) y se mantiene último en 1998 (3.899). Speedy Express queda en el medio en 1997 y 1998. Los datos de 1998 llegan hasta principios de mayo, así que ese año no es comparable con los anteriores. El patrón coincide con el pivot de monto por transportista y año.

## Hallazgo — Monto vendido por país de proveedor y año (Northwind): 
**Fecha:** 28/10/2026
**Archivo:** pandas-avanzado/pivot35.py

Francia lidera los tres años (1996: $47.871, 1997: $112.031, 1998: $117.652) y concentra cerca del 22% del monto total. Es el único país grande que sigue creciendo en 1998, con el año incompleto (los datos llegan hasta principios de mayo). En 1997 le siguen Alemania ($95.152) y Australia ($91.943). Brasil también sube los tres años, pero con montos muy chicos (de $557 a $2.318). A diferencia del país del cliente, donde lideran USA y Alemania, el país de proveedor que más vende es Francia.

## Hallazgo — Monto vendido por país de proveedor y transportista (Northwind):  
**Fecha:** 29/10/2026
**Archivo:** pandas-avanzado/pivot36.py

United Package lidera en 9 de los 16 países de proveedor, incluidos los de mayor monto: Francia ($124.842, la celda más alta), Alemania ($93.658) y Australia ($67.455). Speedy Express lidera en 5 (Brasil, Dinamarca, Italia, Países Bajos y Noruega), tres de ellos con montos muy chicos, y Federal Shipping en 2 (Canadá y España). En Italia la diferencia es mínima: Speedy Express $38.764 contra $36.276 de United Package. Coincide con los pivots por país del cliente y por categoría, donde United Package también es el transportista que más monto mueve.

## Hallazgo — Monto vendido por empleado y país del cliente (Northwind): 
**Fecha:** 30/10/2026
**Archivo:** pandas-avanzado/pivot37.py

 En USA lidera Peacock ($46.385), seguido muy de cerca por Davolio ($43.761). Peacock también lidera Bélgica ($13.597), Davolio el Reino Unido ($10.946), King Austria ($25.745), Callahan Argentina ($2.751) y Leverling Venezuela ($11.246). Hay celdas en 0: Buchanan no vendió en Argentina ni en Austria, y Callahan no vendió en Bélgica. El resultado oculta 15 de los 21 países, así que el hallazgo vale solo para los seis visibles.