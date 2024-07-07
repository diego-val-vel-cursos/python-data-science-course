# Ejercicio: Análisis de Ventas en una Empresa de Retail

# 1. Simulación de datos de ventas
# La lista de diccionarios representa las ventas. Cada diccionario contiene 'producto', 'tienda' y 'cantidad'.
ventas = [
    {'producto': 'laptop', 'tienda': 'Tienda A', 'cantidad': 5},
    {'producto': 'smartphone', 'tienda': 'Tienda B', 'cantidad': 3},
    {'producto': 'tablet', 'tienda': 'Tienda A', 'cantidad': 2},
    {'producto': 'laptop', 'tienda': 'Tienda C', 'cantidad': 4},
    {'producto': 'smartwatch', 'tienda': 'Tienda B', 'cantidad': 7},
    {'producto': 'laptop', 'tienda': 'Tienda A', 'cantidad': 3},
    {'producto': 'smartphone', 'tienda': 'Tienda A', 'cantidad': 6},
    {'producto': 'tablet', 'tienda': 'Tienda C', 'cantidad': 3},
    {'producto': 'smartwatch', 'tienda': 'Tienda C', 'cantidad': 5}
]

# 2. Inicialización de estructuras de datos
# Diccionario para contar las ventas por producto
ventas_por_producto = {}
# Diccionario para contar las ventas por tienda
ventas_por_tienda = {}
# Conjunto para almacenar los productos únicos vendidos
productos_unicos = set()

# 3. Iterar sobre la lista de ventas para llenar las estructuras de datos
for venta in ventas:
    producto = venta['producto']
    tienda = venta['tienda']
    cantidad = venta['cantidad']
    
    # Contar ventas por producto
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad
    
    # Contar ventas por tienda
    if tienda in ventas_por_tienda:
        ventas_por_tienda[tienda] += cantidad
    else:
        ventas_por_tienda[tienda] = cantidad
    
    # Agregar el producto al conjunto de productos únicos
    productos_unicos.add(producto)

# 4. Encontrar la tienda con mayor y menor número de ventas
tienda_max_ventas = max(ventas_por_tienda, key=ventas_por_tienda.get)
tienda_min_ventas = min(ventas_por_tienda, key=ventas_por_tienda.get)

# 5. Imprimir los resultados
print("Ventas por Producto:")
for producto, cantidad in ventas_por_producto.items():
    print(f"{producto}: {cantidad} unidades")

print("\nVentas por Tienda:")
for tienda, cantidad in ventas_por_tienda.items():
    print(f"{tienda}: {cantidad} unidades")

print("\nProductos Únicos Vendidos:")
for producto in productos_unicos:
    print(producto)

print(f"\nTienda con Mayor Número de Ventas: {tienda_max_ventas} ({ventas_por_tienda[tienda_max_ventas]} unidades)")
print(f"Tienda con Menor Número de Ventas: {tienda_min_ventas} ({ventas_por_tienda[tienda_min_ventas]} unidades)")
