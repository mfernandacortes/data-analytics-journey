import pandas as pd

clientes_arg = pd.DataFrame({
    "CustomerID": ["ARG1", "ARG2", "ARG3"],
    "Country": ["Argentina", "Argentina", "Argentina"],
    "Revenue": [1500, 2300, 800]
})

clientes_bra = pd.DataFrame({
    "CustomerID": ["BRA1", "BRA2"],
    "Country": ["Brazil", "Brazil"],
    "Revenue": [3200, 1100]
})

df_total = pd.concat([clientes_arg, clientes_bra], ignore_index=True)

print(df_total)

#fillna: 
"""
dataframe original:

df_limpio = df.copy()
df_limpio["columna"] = df_limpio["columna"].fillna(valor)

""" 
#  python concat_ej.py