import numpy as np

# Leer datos del archivo CSV usando NumPy
# Asegúrate de tener el archivo "ventas.csv" en el mismo directorio que este script.

nombre_archivo = '/app/ejercicio14/ventas.csv'

# Leer el archivo CSV excluyendo la primera columna (nombres de productos)
datos = np.loadtxt(nombre_archivo, delimiter=',', skiprows=1, usecols=range(1, 13))

# Imprimir la matriz de datos
print("Datos de ventas (sin nombres de productos):\n", datos)

# Calcular el total de ventas por producto (suma por filas)
total_ventas_por_producto = np.sum(datos, axis=1)
print("Total de ventas por producto:\n", total_ventas_por_producto)

# Calcular el promedio de ventas por mes (promedio por columnas)
promedio_ventas_por_mes = np.mean(datos, axis=0)
print("Promedio de ventas por mes:\n", promedio_ventas_por_mes)

# Calcular el producto con mayores ventas totales
indice_producto_mayores_ventas = np.argmax(total_ventas_por_producto)
producto_mayores_ventas = indice_producto_mayores_ventas + 1  # +1 porque los índices empiezan en 0
print(f"El producto con mayores ventas es el Producto {producto_mayores_ventas} con un total de {total_ventas_por_producto[indice_producto_mayores_ventas]} ventas.")

# Calcular la variabilidad de las ventas (desviación estándar por columnas)
variabilidad_ventas = np.std(datos, axis=0)
print("Variabilidad de ventas por mes (desviación estándar):\n", variabilidad_ventas)

# Calcular la matriz de correlación entre los productos
correlacion_productos = np.corrcoef(datos)
print("Matriz de correlación entre productos:\n", correlacion_productos)

# Calcular la matriz de covarianza entre los productos
covarianza_productos = np.cov(datos)
print("Matriz de covarianza entre productos:\n", covarianza_productos)

# Normalizar los datos (escalado de 0 a 1)
datos_min = np.min(datos, axis=0)
datos_max = np.max(datos, axis=0)
datos_normalizados = (datos - datos_min) / (datos_max - datos_min)
print("Datos normalizados:\n", datos_normalizados)

# Guardar los resultados en un nuevo archivo CSV
resultados = np.vstack((promedio_ventas_por_mes, variabilidad_ventas))
np.savetxt('/app/ejercicio14/resultados_ventas.csv', resultados, delimiter=',', header='Promedio,Variabilidad', comments='')

print("Los resultados han sido guardados en 'resultados_ventas.csv'.")
