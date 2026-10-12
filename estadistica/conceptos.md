# Estadística descriptiva — Conceptos básicos

## Media
Suma todos los valores y divide por la cantidad. 

## Mediana
ordena todos los valores de menor a mayor, y es el que queda justo en el medio.

La diferencia importa cuando hay outliers. Por ej: UnitPrice: la mayoría de productos cuestan poco, pero Côte de Blaye está a $263,50, bien lejos del resto. Ese outlier tira la media para arriba (la tironea hacia él), pero la mediana casi ni se mueve, porque solo le importa cuál está "en el medio", no cuánto valen los extremos.

## Moda
es simplemente el valor que más se repite en el grupo. A diferencia de media y mediana, que casi siempre dan un número que no está literalmente en los datos, la moda sí es un valor real que aparece.

## Desvío estándar
mide qué tan dispersos están los datos respecto a la media — o sea, en promedio, cuánto se aleja cada valor del centro.

Desvío bajo: los valores están todos parecidos, cerca de la media.
Desvío alto: hay mucha variedad, valores muy distintos entre sí.

Pensado con el histograma de UnitPrice: la mayoría está apretado cerca de $0-$30, pero están Côte de Blaye ($263) y algún otro caro estirando. Eso da un desvío estándar alto — porque aunque la mayoría esté cerca, esos pocos casos extremos abren mucho el promedio de distancias.