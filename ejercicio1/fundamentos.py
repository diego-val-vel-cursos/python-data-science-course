# Este script solicita una lista de números enteros, clasifica los números en pares e impares,
# y calcula la suma y el promedio de cada grupo, manejando posibles entradas no válidas.

# Solicitar al usuario que ingrese una lista de números enteros separados por comas
entrada = input("Introduce una lista de números enteros separados por comas: ")

# Inicializar listas para números pares e impares
pares = []
impares = []

# Inicializar variables para la suma de pares e impares
suma_pares = 0
suma_impares = 0

# Procesar cada número en la entrada
for numero in entrada.split(','):
    # Eliminar espacios en blanco alrededor del número
    numero = numero.strip()
    try:
        # Intentar convertir el número a entero
        numero = int(numero)
        if numero % 2 == 0:
            # Si el número es par, agregar a la lista de pares y sumar
            pares.append(numero)
            suma_pares += numero
        else:
            # Si el número es impar, agregar a la lista de impares y sumar
            impares.append(numero)
            suma_impares += numero
    except ValueError:
        # Si el número no es válido, imprimir un mensaje de error
        print(f"'{numero}' no es un número entero válido y será ignorado.")

# Calcular el promedio de números pares e impares
# Si no hay números pares o impares, evitar la división por cero
promedio_pares = suma_pares / len(pares) if pares else 0
promedio_impares = suma_impares / len(impares) if impares else 0

# Imprimir los resultados
print("\nResultados:")
print(f"Números pares: {pares}")
print(f"Suma de números pares: {suma_pares}")
print(f"Promedio de números pares: {promedio_pares}")

print(f"\nNúmeros impares: {impares}")
print(f"Suma de números impares: {suma_impares}")
print(f"Promedio de números impares: {promedio_impares}")
