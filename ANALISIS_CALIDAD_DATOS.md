# 🔍 Análisis de Calidad de Datos — Northwind

## Hallazgo: Pedido sin detalles (registro huérfano)

Durante el análisis de ventas detecté una inconsistencia entre las métricas 
de volumen (cantidad de pedidos) y revenue (ventas totales).

## ¿Qué encontré?

Un pedido existía en la tabla `Orders` pero no tenía registros asociados 
en `Order Details`. Esto generaba que:
- El pedido se contaba en el total de órdenes
- Pero no aportaba nada al revenue
- Las métricas quedaban inconsistentes entre tablas

## ¿Por qué pasó?

Northwind permite crear un pedido sin detalles porque la integridad 
referencial es unidireccional:

- `Order Details` → tiene FK hacia `Orders` ✅ No podés crear un detalle sin pedido
- `Orders` → NO obliga a tener registros en `Order Details` ✅ Podés crear un pedido vacío

## ¿Cómo lo resolví?
## Contexto

El registro huérfano fue generado durante una prueba propia para ejecutar 
una query. Sin embargo, el hallazgo es válido: en bases de datos reales 
este escenario puede ocurrir y afectar las métricas si no se controla.
Validé mediante consultas SQL la existencia de pedidos sin detalles 
y los identifiqué para limpiarlos antes del análisis.

## Impacto en el análisis

Este tipo de inconsistencia afecta directamente cualquier dashboard 
que compare volumen de pedidos con revenue. Sin esta validación, 
los números no cierran.

## Aprendizaje

> "Northwind permite órdenes sin detalles porque la integridad referencial 
> es unidireccional. Detecté registros huérfanos que afectaban métricas 
> y los identifiqué para asegurar consistencia en el análisis."