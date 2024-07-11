import numpy as np
import matplotlib.pyplot as plt
import json

# Ruta del archivo JSON
json_file_path = '/app/practica3/sincrofasores.json'
# Ruta donde se guardarán los gráficos
save_path_magnitudes = '/app/practica3/serie_temporal_magnitudes.png'
save_path_angulos = '/app/practica3/serie_temporal_angulos.png'
save_path_frecuencia = '/app/practica3/analisis_frecuencia.png'

# Leer los datos del archivo JSON
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Obtener magnitudes y ángulos de los datos leídos
magnitudes = np.array(data['magnitudes'])
angulos = np.array(data['angulos'])

# Representación polar
polar_representation = magnitudes * np.exp(1j * np.radians(angulos))

print("Representación polar de las mediciones de sincrofasores:")
print(polar_representation)

# Crear una serie temporal
tiempo = np.arange(len(magnitudes))
series_temporal = polar_representation

# Graficar y guardar la serie temporal de magnitudes
plt.figure()
plt.plot(tiempo, np.abs(series_temporal), label='Magnitud')
plt.xlabel('Tiempo')
plt.ylabel('Magnitud')
plt.legend()
plt.title('Serie Temporal de Magnitudes de Sincrofasores')
plt.savefig(save_path_magnitudes)
plt.close()

# Graficar y guardar la serie temporal de ángulos
plt.figure()
plt.plot(tiempo, np.angle(series_temporal, deg=True), label='Ángulo')
plt.xlabel('Tiempo')
plt.ylabel('Ángulo (grados)')
plt.legend()
plt.title('Serie Temporal de Ángulos de Sincrofasores')
plt.savefig(save_path_angulos)
plt.close()

# Realizar la transformada de Fourier para analizar las frecuencias
from scipy.fft import fft, fftfreq

N = len(magnitudes)
T = 1.0  # Asumimos que las mediciones se toman cada 1 segundo
yf = fft(np.abs(polar_representation))
xf = fftfreq(N, T)[:N//2]

# Graficar y guardar el análisis de frecuencia
plt.figure()
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.title('Análisis de Frecuencia de las Mediciones')
plt.savefig(save_path_frecuencia)
plt.close()

# Determinar si hay componentes fuera de banda (ejemplo: fuera de 0-60 Hz)
fuera_de_banda = xf[(xf > 60) & (np.abs(yf[0:N//2]) > 0.01)]
if len(fuera_de_banda) > 0:
    print("Se detectaron componentes fuera de banda en las frecuencias:", fuera_de_banda)
else:
    print("Todas las componentes están dentro de banda.")
