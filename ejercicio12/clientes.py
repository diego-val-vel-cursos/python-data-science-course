# Definir el diccionario principal con los clientes y sus compras
compras = {
    'Alice': {'manzanas', 'naranjas', 'plátanos'},
    'Bob': {'manzanas', 'peras', 'uvas'},
    'Carlos': {'plátanos', 'uvas', 'manzanas'},
    'Diana': {'naranjas', 'peras', 'manzanas'}
}

# Función para obtener el resumen de compras por cliente
def resumen_compras(compras):
    for cliente, productos in compras.items():
        print(f"{cliente} ha comprado: {productos}")

# Función para encontrar productos comprados por todos los clientes
def productos_comunes(compras):
    productos_todos = set.intersection(*compras.values())
    return productos_todos

# Función para encontrar productos exclusivos de un cliente
def producto_exclusivo(cliente, compras):
    productos_cliente = compras[cliente]
    productos_otros = set.union(*(productos for key, productos in compras.items() if key != cliente))
    exclusivos = productos_cliente - productos_otros
    if exclusivos:
        return exclusivos.pop()
    else:
        return "No hay productos exclusivos"

# Mostrar el resumen de compras por cliente
print("Resumen de compras por cliente:")
resumen_compras(compras)

# Mostrar productos comprados por todos los clientes
print("\nProductos comprados por todos los clientes:")
comunes = productos_comunes(compras)
print(comunes)

# Mostrar un producto exclusivo de cada cliente
print("\nProducto exclusivo por cliente:")
for cliente in compras:
    exclusivo = producto_exclusivo(cliente, compras)
    print(f"{cliente}: {exclusivo}")
