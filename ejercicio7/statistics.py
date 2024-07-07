# Función para calcular la media
def calcular_media(numeros):
    """Calcula la media de una lista de números."""
    suma = sum(numeros)  # Suma todos los elementos de la lista
    cantidad = len(numeros)  # Cuenta la cantidad de elementos en la lista
    media = suma / cantidad  # Calcula la media
    return media  # Retorna la media

# Función para calcular la mediana
def calcular_mediana(numeros):
    """Calcula la mediana de una lista de números."""
    numeros_ordenados = sorted(numeros)  # Ordena la lista de números
    cantidad = len(numeros_ordenados)  # Cuenta la cantidad de elementos en la lista
    
    # Si la cantidad de elementos es impar, devuelve el elemento del medio
    if cantidad % 2 == 1:
        mediana = numeros_ordenados[cantidad // 2]
    else:  # Si la cantidad de elementos es par, devuelve el promedio de los dos elementos del medio
        mediana = (numeros_ordenados[cantidad // 2 - 1] + numeros_ordenados[cantidad // 2]) / 2
    return mediana  # Retorna la mediana

# Función para calcular la moda
def calcular_moda(numeros):
    """Calcula la moda de una lista de números."""
    frecuencias = {}  # Diccionario para almacenar la frecuencia de cada número
    for numero in numeros:
        if numero in frecuencias:
            frecuencias[numero] += 1  # Incrementa la frecuencia del número
        else:
            frecuencias[numero] = 1  # Inicializa la frecuencia del número

    # Encuentra el número con la mayor frecuencia
    moda = max(frecuencias, key=frecuencias.get)
    return moda  # Retorna la moda

# Función principal
def main():
    """Función principal que solicita una lista de números al usuario y calcula estadísticas básicas."""
    # Solicitar al usuario que ingrese una lista de números
    numeros = input("Ingrese una lista de números separados por comas: ")
    
    # Convertir la entrada en una lista de números
    numeros = list(map(float, numeros.split(',')))
    
    # Calcular y mostrar la media
    media = calcular_media(numeros)
    print(f"La media de los números es: {media}")
    
    # Calcular y mostrar la mediana
    mediana = calcular_mediana(numeros)
    print(f"La mediana de los números es: {mediana}")
    
    # Calcular y mostrar la moda
    moda = calcular_moda(numeros)
    print(f"La moda de los números es: {moda}")

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
