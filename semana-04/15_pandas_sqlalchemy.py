from sqlalchemy import create_engine
import pandas as pd

# Conexión
engine = create_engine(
    "mssql+pyodbc://FERCHUSERVER/burnout_analytics"
    "?driver=SQL+Server&trusted_connection=yes"
)

# Query
df = pd.read_sql("SELECT burnout_risk, stress_level FROM small_bournout", engine)
print(df.head())

# Promedio de burnout_risk agrupado por stress_level
# Resultado: relación lineal — a mayor stress, mayor burnout
# Stress 1 → 35.7 | Stress 10 → 62.7

df = df.groupby("stress_level")["burnout_risk"].mean()

print(df)

