import math

# 1. PREPARACIÓN DE DATOS:
# Crear las colecciones necesarias: listas para ventas mensuales y precios base, y un diccionario para los descuentos.
# Asegurar que todos los datos estén alineados por mes.

# Datos de ventas mensuales en unidades
ventas_mensuales = [120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230]

# Precios base del producto por mes
precios_base = [10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5]

# Descuentos aplicados durante el año (porcentaje)
descuentos = {
    'Enero': 0.10,
    'Febrero': 0.05,
    'Marzo': 0.00,
    'Abril': 0.15,
    'Mayo': 0.20,
    'Junio': 0.10,
    'Julio': 0.05,
    'Agosto': 0.00,
    'Septiembre': 0.10,
    'Octubre': 0.15,
    'Noviembre': 0.20,
    'Diciembre': 0.10
}

# Lista de meses para alinear datos
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# 2. CÁLCULO DE VENTAS NETAS MENSUALES:
# Aplicar los descuentos a las ventas mensuales utilizando los precios base y el diccionario de descuentos.

# Calcular las ventas netas mensuales aplicando los descuentos
ventas_netas_mensuales = []
for i in range(12):
    mes = meses[i]
    descuento = descuentos[mes]
    ventas_netas = ventas_mensuales[i] * precios_base[i] * (1 - descuento)
    ventas_netas_mensuales.append(ventas_netas)

print("Ventas netas mensuales: ", ventas_netas_mensuales)

# 3. ANÁLISIS TRIMESTRAL:
# Dividir las ventas netas en trimestres.
# Calcular las ventas totales por trimestre y determinar el trimestre con mayores ventas.

# Dividir las ventas netas en trimestres
trimestres = {
    'Q1': ventas_netas_mensuales[:3],
    'Q2': ventas_netas_mensuales[3:6],
    'Q3': ventas_netas_mensuales[6:9],
    'Q4': ventas_netas_mensuales[9:12]
}

# Calcular las ventas totales por trimestre
ventas_trimestrales = {k: sum(v) for k, v in trimestres.items()}

# Determinar el trimestre con mayores ventas
trimestre_max_ventas = max(ventas_trimestrales, key=ventas_trimestrales.get)

print("Ventas trimestrales: ", ventas_trimestrales)
print("Trimestre con mayores ventas: ", trimestre_max_ventas)

# 4. CÁLCULO DE ESTADÍSTICAS ANUALES:
# Calcular la media de ventas netas anuales.
# Calcular la desviación estándar de las ventas mensuales.

# Calcular la media de ventas netas anuales
total_ventas_anuales = sum(ventas_netas_mensuales)
media_ventas_anuales = total_ventas_anuales / len(ventas_netas_mensuales)

# Calcular la desviación estándar de las ventas mensuales
# Primero, calcular la media
media_ventas_mensuales = sum(ventas_netas_mensuales) / len(ventas_netas_mensuales)

# Luego, calcular la suma de los cuadrados de las diferencias respecto a la media
sum_squares_diff = sum((x - media_ventas_mensuales) ** 2 for x in ventas_netas_mensuales)

# Finalmente, calcular la desviación estándar
desviacion_estandar_ventas = math.sqrt(sum_squares_diff / len(ventas_netas_mensuales))

print("Media de ventas netas anuales: ", media_ventas_anuales)
print("Desviación estándar de ventas mensuales: ", desviacion_estandar_ventas)

# 5. CONCLUSIÓN:
# Resumir los resultados obtenidos.

print("Resumen:")
print(f"Ventas netas mensuales: {ventas_netas_mensuales}")
print(f"Ventas trimestrales: {ventas_trimestrales}")
print(f"Trimestre con mayores ventas: {trimestre_max_ventas}")
print(f"Media de ventas netas anuales: {media_ventas_anuales}")
print(f"Desviación estándar de ventas mensuales: {desviacion_estandar_ventas}")
