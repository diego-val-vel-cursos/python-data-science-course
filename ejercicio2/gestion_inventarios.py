# Importamos el módulo pprint para una mejor presentación de los datos
import pprint

# Inicializamos una lista vacía para almacenar los productos del inventario
inventario = []

# Definimos una función para registrar un nuevo producto
def registrar_producto(nombre, categoria, precio):
    producto = {
        'nombre': nombre,       # Almacenamos el nombre del producto
        'categoria': categoria, # Almacenamos la categoría del producto
        'precio': precio        # Almacenamos el precio del producto
    }
    inventario.append(producto)  # Agregamos el producto al inventario

# Definimos una función para consultar la lista de productos
def consultar_productos():
    pprint.pprint(inventario)  # Usamos pprint para mostrar el inventario de manera legible

# Definimos una función para actualizar el precio de un producto
def actualizar_precio(nombre, nuevo_precio):
    for producto in inventario:  # Recorremos la lista de productos
        if producto['nombre'] == nombre:  # Buscamos el producto por su nombre
            producto['precio'] = nuevo_precio  # Actualizamos el precio
            return f"Precio de {nombre} actualizado a {nuevo_precio}"
    return "Producto no encontrado"  # Mensaje si el producto no se encuentra

# Definimos una función para eliminar un producto del inventario
def eliminar_producto(nombre):
    for producto in inventario:  # Recorremos la lista de productos
        if producto['nombre'] == nombre:  # Buscamos el producto por su nombre
            inventario.remove(producto)  # Eliminamos el producto del inventario
            return f"Producto {nombre} eliminado"
    return "Producto no encontrado"  # Mensaje si el producto no se encuentra

# Definimos una función para calcular el valor total del inventario
def calcular_valor_total():
    total = 0  # Inicializamos el total en 0
    for producto in inventario:  # Recorremos la lista de productos
        total += producto['precio']  # Sumamos el precio de cada producto al total
    return total  # Devolvemos el valor total del inventario

# Función principal para ejecutar el programa
def main():
    while True:
        print("\nOpciones del Sistema de Gestión de Inventarios:")
        print("1. Registrar producto")
        print("2. Consultar productos")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total")
        print("6. Salir")

        opcion = int(input("Seleccione una opción: "))  # Solicitamos la opción al usuario

        if opcion == 1:
            nombre = input("Ingrese el nombre del producto: ")  # Solicitamos el nombre del producto
            categoria = input("Ingrese la categoría del producto: ")  # Solicitamos la categoría del producto
            precio = float(input("Ingrese el precio del producto: "))  # Solicitamos el precio del producto
            registrar_producto(nombre, categoria, precio)  # Registramos el producto
            print(f"Producto {nombre} registrado con éxito")

        elif opcion == 2:
            print("Inventario de productos:")
            consultar_productos()  # Consultamos y mostramos la lista de productos

        elif opcion == 3:
            nombre = input("Ingrese el nombre del producto a actualizar: ")  # Solicitamos el nombre del producto
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))  # Solicitamos el nuevo precio
            mensaje = actualizar_precio(nombre, nuevo_precio)  # Actualizamos el precio del producto
            print(mensaje)  # Mostramos el mensaje de actualización

        elif opcion == 4:
            nombre = input("Ingrese el nombre del producto a eliminar: ")  # Solicitamos el nombre del producto
            mensaje = eliminar_producto(nombre)  # Eliminamos el producto del inventario
            print(mensaje)  # Mostramos el mensaje de eliminación

        elif opcion == 5:
            total = calcular_valor_total()  # Calculamos el valor total del inventario
            print(f"El valor total del inventario es: {total}")  # Mostramos el valor total

        elif opcion == 6:
            print("Saliendo del sistema...")  # Mensaje de salida
            break  # Terminamos el bucle y salimos del programa

        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 6")  # Mensaje para opción no válida

# Ejecutamos la función principal
if __name__ == "__main__":
    main()
