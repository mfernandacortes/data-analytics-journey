import pandas as pd
"""
Se ejecutó código con errores para leerlos, detectarlos:

data = {"ProductID": [1, 2, 3], "UnitPrice": [10.5, 25.0, 8.0]}
df = pd.DataFrame(data)

print(df["Precio"])

numeros = [10, 20, 30]
print(numeros[5])


numero = "25"
resultado = numero + 5
print(resultado)

def calcular_promedio(numeros):
    resultado = suma / len(numeros)
    return resultado

print(calcular_promedio([10, 20, 30]))


import pandas as pd


data = {"ProductID": [1, 2, 3], "UnitPrice": [10.5, 25.0, 8.0]}
df = pd.DataFrame(data)

promedio = df["UnitPrice"].mean
print(promedio)


promedio = df["UnitPrice"].mean
"""
data = {"ProductID": [1, 2, 3], "UnitPrice": [10.5, 25.0, 8.0]}
df = pd.DataFrame(data)

df[df["UnitPrice"] > 10 and df["UnitPrice"] < 25]

# python leer_errores.py
