import pandas as pd

df_clientes = pd.DataFrame({
    "cliente_id": [1, 2, 3],
    "nombre": ["Ana", "Carlos", "Marta"]
})

df_pedidos = pd.DataFrame({
    "pedido_id": [100, 101, 102],
    "cliente_id": [1, 2, 1],
    "monto": [500, 800, 300]
})

clientes = pd.merge(df_clientes, df_pedidos, on = "cliente_id")

print(clientes)

#   python dobles4.py