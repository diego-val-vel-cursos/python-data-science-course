# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd

# Leer los datos del archivo CSV
datos = pd.read_csv('/app/ejercicio13/datos_electricos.csv')

# Convertir los datos de las columnas 'corriente' y 'voltaje' a arreglos de NumPy
corriente = datos['corriente'].to_numpy()
voltaje = datos['voltaje'].to_numpy()

# Calcular el valor promedio de la corriente y el voltaje durante el mes
corriente_promedio = np.mean(corriente)
voltaje_promedio = np.mean(voltaje)
print(f'El valor promedio de la corriente durante el mes es: {corriente_promedio} A')
print(f'El valor promedio del voltaje durante el mes es: {voltaje_promedio} V')

# Identificar el día con el valor más alto y el más bajo de corriente
dia_corriente_mas_alta = np.argmax(corriente) + 1  # +1 para ajustar al índice de día
dia_corriente_mas_baja = np.argmin(corriente) + 1
corriente_mas_alta = np.max(corriente)
corriente_mas_baja = np.min(corriente)
print(f'El día con la corriente más alta es el día {dia_corriente_mas_alta} con {corriente_mas_alta} A')
print(f'El día con la corriente más baja es el día {dia_corriente_mas_baja} con {corriente_mas_baja} A')

# Calcular la resistencia diaria utilizando la Ley de Ohm (R = V/I)
resistencia = voltaje / corriente
print(f'Las resistencias diarias calculadas son: {resistencia}')

# Crear un arreglo que contenga los valores de potencia (P = V * I) para cada día
potencia = voltaje * corriente
print(f'Las potencias diarias calculadas son: {potencia}')
