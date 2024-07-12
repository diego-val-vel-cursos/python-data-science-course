# Importar las bibliotecas necesarias
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el conjunto de datos "penguins"
penguins = sns.load_dataset("penguins")

# Exploramos las primeras filas del conjunto de datos
print(penguins.head())

# Exploración inicial de los datos
print(penguins.info())

# Estadísticas descriptivas del conjunto de datos
print(penguins.describe())

# Crear un gráfico de dispersión (scatter plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species")
plt.title("Relación entre la longitud y profundidad del pico de los pingüinos")
plt.xlabel("Longitud del pico (mm)")
plt.ylabel("Profundidad del pico (mm)")
plt.savefig('/app/practica4/scatterplot.png')
plt.close

# Crear un diagrama de caja (box plot)
plt.figure(figsize=(10, 6))
sns.boxplot(data=penguins, x="species", y="flipper_length_mm")
plt.title("Distribución de la longitud de las aletas por especie")
plt.xlabel("Especie")
plt.ylabel("Longitud de las aletas (mm)")
plt.savefig('/app/practica4/boxplot.png')
plt.close

# Crear un diagrama de violín (violin plot)
plt.figure(figsize=(10, 6))
sns.violinplot(data=penguins, x="species", y="body_mass_g", hue="sex", split=True)
plt.title("Distribución del peso corporal por especie y sexo")
plt.xlabel("Especie")
plt.ylabel("Peso corporal (g)")
plt.savefig('/app/practica4/violinplot.png')
plt.close
