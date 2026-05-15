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

**Archivo:** `semana-04/04_pandas_agg_merge.py`  
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

**Archivo:** `semana-04/05_pandas_empleados_revenue.py`  
**Herramienta:** Python — Pandas (groupby + agg)

Al analizar el revenue total, cantidad de pedidos y promedio por pedido de cada empleado se identificaron dos perfiles distintos:

### Perfil 1 — Alto volumen, bajo ticket promedio
**Margaret Peacock** lidera en revenue total y cantidad de pedidos (156), pero al ordenar por promedio cae al puesto 7 ($1.492 por pedido).
**Estrategia sugerida:** trabajar en upselling y productos de mayor valor para aumentar el ticket promedio.

### Perfil 2 — Bajo volumen, alto ticket promedio
**Fuller, King y Dodsworth** tienen entre 3 y 4 veces menos pedidos que Peacock pero superan su promedio.
**Estrategia sugerida:** incentivar con bonos escalonados por cantidad de pedidos, con el desafío de mantener el promedio actual.

> Este tipo de segmentación permite diseñar estrategias comerciales distintas por perfil, en lugar de una política uniforme para todo el equipo.