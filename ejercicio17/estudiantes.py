# Paso 1: Importar las bibliotecas necesarias
import seaborn as sns  # Biblioteca para visualización de datos
import pandas as pd    # Biblioteca para manipulación de datos
import matplotlib.pyplot as plt  # Biblioteca para visualización de gráficos

# Paso 2: Cargar el conjunto de datos
# Usamos pd.read_csv para leer el archivo CSV con los datos de los estudiantes
data = pd.read_csv('/app/ejercicio17/student_scores.csv')

# Paso 3: Visualización de la distribución de las puntuaciones de matemáticas
# Utilizamos sns.histplot para crear un histograma de las puntuaciones de matemáticas
plt.figure(figsize=(10, 6))  # Configuramos el tamaño de la figura
sns.histplot(data['math_score'], kde=True, bins=10, color='blue')  # Histograma con densidad estimada y color azul
plt.title('Distribución de las Puntuaciones de Matemáticas')  # Título del gráfico
plt.xlabel('Puntuación de Matemáticas')  # Etiqueta del eje X
plt.ylabel('Frecuencia')  # Etiqueta del eje Y
plt.savefig('/app/ejercicio17/histograma.png')
plt.close

# Paso 4: Comparación de las puntuaciones de matemáticas entre géneros
# Utilizamos sns.boxplot para crear un gráfico de caja de las puntuaciones de matemáticas por género
plt.figure(figsize=(10, 6))
sns.boxplot(x='gender', y='math_score', data=data, palette='Set2')  # Gráfico de caja con una paleta de colores predefinida
plt.title('Comparación de Puntuaciones de Matemáticas por Género')
plt.xlabel('Género')
plt.ylabel('Puntuación de Matemáticas')
plt.savefig('/app/ejercicio17/boxplot.png')
plt.close

# Paso 5: Correlación entre las puntuaciones de matemáticas y lectura
# Utilizamos sns.scatterplot para crear un gráfico de dispersión entre las puntuaciones de matemáticas y lectura
plt.figure(figsize=(10, 6))
sns.scatterplot(x='math_score', y='reading_score', data=data, hue='gender', palette='Set1')  # Gráfico de dispersión con color basado en género
plt.title('Correlación entre Puntuaciones de Matemáticas y Lectura')
plt.xlabel('Puntuación de Matemáticas')
plt.ylabel('Puntuación de Lectura')
plt.savefig('/app/ejercicio17/scatterplot.png')
plt.close

# Paso 6: Variación de las puntuaciones de escritura entre géneros
# Utilizamos sns.violinplot para crear un gráfico de violín de las puntuaciones de escritura por género
plt.figure(figsize=(10, 6))
sns.violinplot(x='gender', y='writing_score', data=data, palette='Set3')  # Gráfico de violín con una paleta de colores predefinida
plt.title('Variación de las Puntuaciones de Escritura por Género')
plt.xlabel('Género')
plt.ylabel('Puntuación de Escritura')
plt.savefig('/app/ejercicio17/violinplot.png')
plt.close
