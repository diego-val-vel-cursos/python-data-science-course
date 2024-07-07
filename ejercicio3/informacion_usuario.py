# Solicitamos el nombre del usuario
nombre = input("Por favor, ingresa tu nombre: ")

# Solicitamos la edad del usuario y la convertimos a entero
edad_actual = int(input("Por favor, ingresa tu edad: "))

# Calculamos la edad del usuario en 10 años
edad_futura = edad_actual + 10

# Solicitamos tres números enteros al usuario
numero1 = int(input("Ingresa el primer número entero: "))
numero2 = int(input("Ingresa el segundo número entero: "))
numero3 = int(input("Ingresa el tercer número entero: "))

# Calculamos la suma de los tres números
suma = numero1 + numero2 + numero3

# Calculamos el promedio de los tres números
promedio = suma / 3

# Creamos una lista con los números del 1 al 10
lista_numeros = list(range(1, 11))

# Calculamos la suma de todos los elementos de la lista
suma_lista = sum(lista_numeros)

# Creamos un diccionario con la información del usuario
informacion_usuario = {
    "nombre": nombre,
    "edad_actual": edad_actual,
    "edad_futura": edad_futura
}

# Imprimimos la información del diccionario de manera legible
print("\nInformación del usuario:")
print(f"Nombre: {informacion_usuario['nombre']}")
print(f"Edad actual: {informacion_usuario['edad_actual']}")
print(f"Edad en 10 años: {informacion_usuario['edad_futura']}")

# Imprimimos los resultados de los cálculos
print("\nResultados de los cálculos:")
print(f"Suma de los tres números: {suma}")
print(f"Promedio de los tres números: {promedio:.2f}")
print(f"Suma de la lista de números del 1 al 10: {suma_lista}")
