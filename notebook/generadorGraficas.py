import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dataFrameAsistencia = pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#Graficando
colors=["#8d66cd","#3078da","#0083d2","#0088ba","#008997","#008671"]


#Grafica de barras

plt.figure(figsize=(8,5))
sns.countplot(x='estado', data=dataFrameAsistencia,palette=colors)
plt.title("Cantidad de registros por estado de asistencia")
plt.xlabel("Estado de asistencia")
plt.ylabel("Cantidad de registros")
plt.tight_layout()
plt.show()

#GRAFICA DE TORTA
#Mostrar proporciones entre dos columnas del DF (proporcion de estudiantes x medio de transporte)

conteoMedioTransporte=dataFrameAsistencia['medio_transporte'].value_counts()

plt.figure(figsize=(5,5))
plt.pie(
    conteoMedioTransporte,
    labels=conteoMedioTransporte.index,
 
    autopct='%1.1f%%',
    colors=sns.color_palette("Blues")
)

plt.title("Distribucion de estudiantes por medio de transporte")
plt.tight_layout()
plt.show()

#Grafico de barras agrupadas
#Se aplica cuando hice cruces en el dataframe

conteoEatadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size().unstack(fill_value=0)

conteoEatadoMedioTransporte.plot(
    kind='bar',
    figsize=(10,6),
    color=colors
)
plt.title("Cantidad de registros por estado de asistencia")
plt.xlabel("Estado de asistencia")
plt.ylabel("Cantidad de registros")
plt.legend(title="Medio de transporte")
plt.tight_layout()
plt.show()