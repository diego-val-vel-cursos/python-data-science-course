# Importamos las librerías necesarias
import pandas as pd  # Librería Pandas para manipulación de datos
import seaborn as sns  # Librería Seaborn para visualización de datos
import matplotlib.pyplot as plt  # Matplotlib para gráficos

# Cargamos el conjunto de datos "Titanic" proporcionado por Seaborn
titanic = sns.load_dataset('titanic')

# Exploramos las primeras filas del conjunto de datos
print(titanic.head())

# Exploración inicial de los datos
print(titanic.info())

# Estadísticas descriptivas del conjunto de datos
print(titanic.describe())

# Limpieza de datos: Eliminamos las filas con valores nulos en las columnas 'age' y 'embarked'
# Aquí usamos Pandas para manipular el DataFrame
titanic_clean = titanic.dropna(subset=['age', 'embarked']).copy()  # Uso de pd.dropna() y .copy() para evitar SettingWithCopyWarning

# Imputación: Rellenamos los valores nulos en la columna 'embark_town' con el valor más frecuente
titanic_clean.loc[:, 'embark_town'] = titanic_clean['embark_town'].fillna(titanic_clean['embark_town'].mode()[0])  # Uso de pd.fillna() y pd.mode() con .loc para evitar SettingWithCopyWarning

# Creación de una nueva columna 'family_size' que suma 'sibsp' y 'parch' para indicar el tamaño de la familia
titanic_clean['family_size'] = titanic_clean['sibsp'] + titanic_clean['parch']  # Uso de pd para operaciones en columnas

# 1. Distribución de edades de los pasajeros
plt.figure(figsize=(10, 6))
sns.histplot(titanic_clean['age'], bins=30, kde=True)
plt.title('Distribución de Edades de los Pasajeros')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.savefig('/app/ejercicio18/histograma.png')
plt.close

# 2. Distribución de pasajeros por clase
plt.figure(figsize=(10, 6))
sns.countplot(x='class', data=titanic_clean)
plt.title('Distribución de Pasajeros por Clase')
plt.xlabel('Clase')
plt.ylabel('Número de Pasajeros')
plt.savefig('/app/ejercicio18/countplot.png')
plt.close

# 3. Relación entre el precio del billete y la clase
plt.figure(figsize=(10, 6))
sns.boxplot(x='class', y='fare', data=titanic_clean)
plt.title('Relación entre el Precio del Billete y la Clase')
plt.xlabel('Clase')
plt.ylabel('Precio del Billete')
plt.savefig('/app/ejercicio18/boxplot.png')
plt.close

# 4. Tasa de supervivencia por género y clase
plt.figure(figsize=(10, 6))
sns.barplot(x='class', y='survived', hue='sex', data=titanic_clean)
plt.title('Tasa de Supervivencia por Género y Clase')
plt.xlabel('Clase')
plt.ylabel('Tasa de Supervivencia')
plt.savefig('/app/ejercicio18/barplot.png')
plt.close

# 5. Correlación entre diferentes características
# Seleccionamos solo las columnas numéricas para la matriz de correlación
numeric_cols = titanic_clean.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(12, 10))
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', linewidths=0.5)  # Uso de pd.corr() para calcular correlaciones
plt.title('Matriz de Correlación de las Características del Titanic')
plt.savefig('/app/ejercicio18/heatmap.png')
plt.close
