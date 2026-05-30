from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ============================================
# EDA - Digital Burnout & Productivity Dataset
# ============================================

# SECCIÓN 1: Carga y descripción del dataset
# SECCIÓN 2: Calidad de datos
# SECCIÓN 3: Distribuciones
# SECCIÓN 4: Relaciones entre variables
# SECCIÓN 5: Hallazgos y conclusiones


# Conexión
engine = create_engine(
    "mssql+pyodbc://FERCHUSERVER/burnout_analytics"
    "?driver=SQL+Server&trusted_connection=yes"
)

data_burnout = pd.read_sql("SELECT * FROM small_bournout", engine)

# ============================================
# SECCIÓN 1: Carga y descripción del dataset
# ============================================
# shape, dtypes, info: como está compuesto el dataset: filas, columnas, datos
print(data_burnout.head())
print(data_burnout.shape)
print(data_burnout.dtypes)
print(data_burnout.info())


# ============================================
# SECCIÓN 2: Calidad de datos
# ============================================

print(data_burnout.isnull().sum())

# Nulos detectados: 4 columnas con ~2% de nulos cada una
# social_media_hours: 198 | deep_work_hours: 203 | sleep_hours: 201 | motivation_level: 212
# Porcentaje bajo — no afecta el análisis


# ============================================
# SECCIÓN 3: Distribuciones
# ============================================

# Gráfico 1 - boxplot
sns.boxplot(data=data_burnout, x="stress_level", y="burnout_risk")
plt.show()

# Gráfico 2 - barplot  gráfico con work_mode
# con el gráfico por modalidad de trabajo confirmamos el hallazgo en sql:
# la modalidad de trabajo no afecta el riesgo de burnout

sns.barplot(data=data_burnout, x="work_mode", y="burnout_risk")
plt.title("Burnout promedio por modalidad de trabajo")
plt.xlabel("Modalidad")
plt.ylabel("Burnout promedio")
plt.show()

# ============================================
# SECCIÓN 4: Relaciones entre variables
# ============================================

correlacion = data_burnout.select_dtypes(include="number").corr()
plt.figure(figsize=(12, 10))
sns.heatmap(data=correlacion, annot=True, fmt=".1f")
plt.show()

# ============================================
# SECCIÓN 5: Hallazgos y Conclusiones
# ============================================

# 1. # Promedio de burnout_risk agrupado por stress_level
     # Resultado: relación lineal — a mayor stress, mayor burnout
     # Stress 1 → 35.7 | Stress 10 → 62.7
# 2. Distribución: 52% nivel medio, 26% bajo, 21% alto
# 3. Modalidad de trabajo: sin diferencia entre remoto, híbrido y presencial
# 4. Sueño: menos horas → más burnout
# 5. Stress: relación lineal — stress 1 → burnout 35.7 / stress 10 → burnout 62.7 — hallazgo principal
# 6. Fatiga mental y ocupación: sin relación clara con el burnout

# python EDA_burnout.py