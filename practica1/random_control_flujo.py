# Inicializar variables para la suma de números pares e impares
suma_pares = 0
suma_impares = 0

# Inicializar variables para el número más grande y más pequeño
numero_mas_grande = numeros[0]
numero_mas_pequeno = numeros[0]

# Recorrer la lista de números
for numero in numeros:
    # Verificar si el número es par
    if numero % 2 == 0:
        print(f"{numero} es par")
        suma_pares += numero  # Sumar al total de números pares
    else:
        print(f"{numero} es impar")
        suma_impares += numero  # Sumar al total de números impares
    
    # Actualizar el número más grande
    if numero > numero_mas_grande:
        numero_mas_grande = numero
    
    # Actualizar el número más pequeño
    if numero < numero_mas_pequeno:
        numero_mas_pequeno = numero

# Imprimir las sumas de números pares e impares
print(f"Suma de números pares: {suma_pares}")
print(f"Suma de números impares: {suma_impares}")

# Imprimir el número más grande y más pequeño
print(f"El número más grande es: {numero_mas_grande}")
print(f"El número más pequeño es: {numero_mas_pequeno}")
