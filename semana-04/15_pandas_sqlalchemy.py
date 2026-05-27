from sqlalchemy import create_engine
import pandas as pd

# Conexión
engine = create_engine(
    "mssql+pyodbc://FERCHUSERVER/burnout_analytics"
    "?driver=SQL+Server&trusted_connection=yes"
)

# Query
df = pd.read_sql("SELECT * FROM small_bournout", engine)
print(df.head())
