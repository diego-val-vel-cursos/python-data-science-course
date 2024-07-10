# Definición de una lista de números
numeros_lista = [1, 2, 3, 4, 5]
print("Lista inicial:", numeros_lista)

# Añadir un elemento a la lista
numeros_lista.append(6)
print("Lista después de añadir 6:", numeros_lista)

# Insertar un elemento en una posición específica
numeros_lista.insert(2, 10)  # Insertar 10 en la posición 2
print("Lista después de insertar 10 en la posición 2:", numeros_lista)

# Eliminar un elemento de la lista
numeros_lista.remove(4)
print("Lista después de eliminar el 4:", numeros_lista)

# Modificar un elemento de la lista
numeros_lista[0] = 100
print("Lista después de modificar el primer elemento:", numeros_lista)

# Definición de una tupla de números
numeros_tupla = (1, 2, 3, 4, 5)
print("Tupla inicial:", numeros_tupla)

# Acceder a un elemento de la tupla
print("Elemento en la posición 1 de la tupla:", numeros_tupla[1])

# Intentar modificar un elemento de la tupla (esto causará un error)
try:
    numeros_tupla[0] = 100
except TypeError as e:
    print("Error al intentar modificar un elemento de la tupla:", e)

# Análisis simple de datos: Calcular la media de una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
media = sum(numeros) / len(numeros)
print("La media de los números es:", media)

# Uso de listas y tuplas en análisis de datos: Crear una tupla con los resultados
resultados = (min(numeros), max(numeros), media)
print("Resultados del análisis de datos (mínimo, máximo, media):", resultados)
