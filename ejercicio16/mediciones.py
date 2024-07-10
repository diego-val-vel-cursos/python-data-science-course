import pandas as pd
import plotly.express as px

# Cargar los datos desde el archivo CSV
df = pd.read_csv('/app/ejercicio16/mediciones_electricas.csv')

# Mostrar las primeras filas del DataFrame para entender su estructura
print(df.head())

# Calcular la potencia eléctrica (P = V * I)
df['potencia'] = df['voltaje'] * df['corriente']

# Mostrar las primeras filas del DataFrame con la nueva columna de potencia
print(df.head())

# Calcular estadísticas descriptivas de la potencia
potencia_promedio = df['potencia'].mean()
potencia_maxima = df['potencia'].max()

print(f"\nPotencia Promedio: {potencia_promedio:.2f} W")
print(f"Potencia Máxima: {potencia_maxima:.2f} W")

# Crear un gráfico de la potencia a lo largo del tiempo para cada dispositivo
fig_potencia = px.line(df, x='tiempo', y='potencia', color='dispositivo', title='Potencia Eléctrica a lo Largo del Tiempo')
fig_potencia.write_image("/app/ejercicio16/potencia_electrica_tiempo.png")
fig_potencia.show()

# Crear un gráfico de barras de la potencia promedio por dispositivo
potencia_promedio_dispositivo = df.groupby('dispositivo')['potencia'].mean().reset_index()
fig_promedio = px.bar(potencia_promedio_dispositivo, x='dispositivo', y='potencia', title='Potencia Promedio por Dispositivo')
fig_promedio.write_image("/app/ejercicio16/potencia_promedio_dispositivo.png")
fig_promedio.show()

# Guardar el DataFrame procesado en un nuevo archivo CSV
df.to_csv('/app/ejercicio16/mediciones_electricas_procesado.csv', index=False)
