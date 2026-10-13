import pandas as pd
from scipy.stats import chi2_contingency

# Consigna: Predecir si el valor p será chico (menos de 0.05) o grande con 100 vs 
# 115 compras sobre 1.000 visitantes por grupo, y repetir la predicción con 100 
# vs 160 compras.
# Calcular ambos valores p con chi2_contingency e interpretar en cuál de los dos 
# casos la diferencia es real y no casualidad.


# filas: botón azul y botón verde / columnas: compraron y no compraron
tabla = [[100, 900],
         [115, 885]]

resultado = chi2_contingency(tabla)
# se espera un valor grande:
print(resultado[1])

# otro ejemplo (para contrastar)
tabla2 = [[100, 900],
         [160, 840]]

resultado2 = chi2_contingency(tabla2)
# se espera un valor más chico:
print(resultado2[1])
