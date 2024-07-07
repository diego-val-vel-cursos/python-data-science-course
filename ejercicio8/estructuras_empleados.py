# Lista de empleados, cada uno representado por una tupla (nombre, departamento, salario)
empleados = [
    ("Juan", "Ventas", 50000),
    ("Ana", "Marketing", 60000),
    ("Luis", "Ventas", 50000),
    ("Marta", "Recursos Humanos", 55000),
    ("Carlos", "Marketing", 60000),
    ("Elena", "Ventas", 70000)
]

# Convertir la lista de empleados a un conjunto para eliminar duplicados
empleados_unicos = set(empleados)

# Crear un diccionario para agrupar a los empleados por departamento
empleados_por_departamento = {}
for empleado in empleados_unicos:
    nombre, departamento, salario = empleado
    if departamento not in empleados_por_departamento:
        empleados_por_departamento[departamento] = []
    empleados_por_departamento[departamento].append(empleado)

# Crear un diccionario para almacenar el salario promedio por departamento
salario_promedio_por_departamento = {}
for departamento, empleados in empleados_por_departamento.items():
    total_salarios = sum(salario for nombre, dep, salario in empleados)
    salario_promedio = total_salarios / len(empleados)
    salario_promedio_por_departamento[departamento] = salario_promedio

# Crear un diccionario para almacenar el empleado con el salario más alto por departamento
empleado_max_salario_por_departamento = {}
for departamento, empleados in empleados_por_departamento.items():
    empleado_max_salario = max(empleados, key=lambda empleado: empleado[2])
    empleado_max_salario_por_departamento[departamento] = empleado_max_salario

# Imprimir los resultados
print("Salario promedio por departamento:")
for departamento, salario_promedio in salario_promedio_por_departamento.items():
    print(f"{departamento}: {salario_promedio}")

print("\nEmpleado con el salario más alto por departamento:")
for departamento, empleado in empleado_max_salario_por_departamento.items():
    nombre, dep, salario = empleado
    print(f"{departamento}: {nombre} con un salario de {salario}")
