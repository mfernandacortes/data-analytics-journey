# Hallazgos del análisis — Northwind

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