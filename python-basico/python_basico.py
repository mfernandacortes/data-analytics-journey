import pandas as pd


productos = ["Chai", "Chang", "Tofu"]
print(productos[0])
print(productos[1])
print(productos[2])
# print(productos[3]) #indice fuera de rango...IndexError: list index out of range

print(len(productos))

for elemento in productos:
    print(elemento)


# definir función:
def duplicar(parametro):
    resultado = parametro * 2
    return resultado

print(duplicar(4))


precios = pd.Series([10, 20, 30, 40])
resultado = precios.apply(duplicar)
print(resultado)
# python python_basico.py