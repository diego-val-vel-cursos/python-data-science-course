import pandas as pd
import matplotlib.pyplot as plt

# Paso 1: Lectura de Datos
# ========================
# Leemos el archivo CSV `consumo_energia.csv` y creamos un DataFrame
df = pd.read_csv('/app/ejercicio15/consumo_energia.csv')

# Paso 2: Exploración de Datos
# ============================
# Imprimimos las primeras filas del DataFrame para entender su estructura
print("Primeras filas del DataFrame:")
print(df.head())

# Imprimimos información general del DataFrame
print("\nInformación del DataFrame:")
print(df.info())

# Imprimimos estadísticas descriptivas del DataFrame
print("\nEstadísticas descriptivas del DataFrame:")
print(df.describe())

# Paso 3: Limpieza de Datos
# =========================
# Verificamos y manejamos valores nulos
print("\nVerificamos si hay valores nulos:")
print(df.isnull().sum())

# Suponiendo que hay valores nulos en 'Consumo_kWh' y 'Costo_Total', los rellenamos con la media
df['Consumo_kWh'].fillna(df['Consumo_kWh'].mean(), inplace=True)
df['Costo_Total'].fillna(df['Costo_Total'].mean(), inplace=True)

# Verificamos nuevamente los valores nulos
print("\nVerificamos nuevamente si hay valores nulos después de la limpieza:")
print(df.isnull().sum())

# Paso 4: Manipulación de Datos
# =============================
# Creamos una nueva columna 'Costo_por_kWh' que es el resultado de Costo_Total / Consumo_kWh
df['Costo_por_kWh'] = df['Costo_Total'] / df['Consumo_kWh']

# Agrupamos los datos por 'Ciudad' y calculamos la suma de 'Consumo_kWh' y 'Costo_Total', y la media de 'Costo_por_kWh'
resumen = df.groupby('Ciudad').agg({
    'Consumo_kWh': 'sum',
    'Costo_Total': 'sum',
    'Costo_por_kWh': 'mean'
}).reset_index()

# Ordenamos el resumen por 'Consumo_kWh' en orden descendente
resumen = resumen.sort_values(by='Consumo_kWh', ascending=False)

# Paso 5: Análisis Descriptivo y Visualización
# ============================================
# Imprimimos el resumen de consumo de energía por ciudad
print("\nResumen de consumo de energía por ciudad:")
print(resumen)

# Generamos un gráfico de barras del consumo de energía por ciudad
plt.figure(figsize=(10, 6))
plt.bar(resumen['Ciudad'], resumen['Consumo_kWh'], color='skyblue')
plt.xlabel('Ciudad')
plt.ylabel('Consumo de Energía (kWh)')
plt.title('Consumo de Energía por Ciudad')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/app/ejercicio15/consumo_energia_por_ciudad.png')
plt.show()

# Paso 6: Escritura de Datos
# ==========================
# Guardamos el resumen en un nuevo archivo CSV `resumen_energia.csv`
resumen.to_csv('/app/ejercicio15/resumen_energia.csv', index=False)
