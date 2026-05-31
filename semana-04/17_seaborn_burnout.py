from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Conexión
engine = create_engine(
    "mssql+pyodbc://FERCHUSERVER/burnout_analytics"
    "?driver=SQL+Server&trusted_connection=yes"
)

data_burnout = pd.read_sql("SELECT * FROM small_bournout", engine)

# gráfico de burnout_risk: riesgo de burnout:

#sns.histplot(data=data_burnout, x="burnout_risk")
#plt.show()

# segundo gráfico: burnout_risk por stress_level:

#sns.boxplot(data=data_burnout, x="stress_level", y="burnout_risk")
#plt.show()

#correlacion = data_burnout.select_dtypes(include="number").corr()
#plt.figure(figsize=(12, 10))
#sns.heatmap(data=correlacion, annot=True, fmt=".1f")
#plt.show()


# Gráfico 1 - boxplot
sns.boxplot(data=data_burnout, x="stress_level", y="burnout_risk")
plt.show()

# Gráfico 2 - barplot  gráfico con work_mode
# con el gráfico por modalidad de trabajo confirmamos el hallazgo en sql:
# la modalidad de trabajo no afecta el riesgo de burnout
plt.title("Burnout promedio por modalidad de trabajo")
plt.xlabel("Modalidad")
plt.ylabel("Burnout promedio")
sns.barplot(data=data_burnout, x="work_mode", y="burnout_risk")
plt.show()
