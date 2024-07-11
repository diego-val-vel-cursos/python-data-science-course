# Ejercicio: Análisis de Calificaciones en una Escuela

# 1. Simulación de datos de calificaciones
# La lista de diccionarios representa las calificaciones. Cada diccionario contiene 'estudiante', 'materia' y 'calificacion'.
calificaciones = [
    {'estudiante': 'Juan', 'materia': 'Matemáticas', 'calificacion': 85},
    {'estudiante': 'María', 'materia': 'Ciencias', 'calificacion': 90},
    {'estudiante': 'Carlos', 'materia': 'Literatura', 'calificacion': 78},
    {'estudiante': 'Ana', 'materia': 'Matemáticas', 'calificacion': 92},
    {'estudiante': 'Luis', 'materia': 'Ciencias', 'calificacion': 74},
    {'estudiante': 'Pedro', 'materia': 'Matemáticas', 'calificacion': 88},
    {'estudiante': 'Sofía', 'materia': 'Literatura', 'calificacion': 95},
    {'estudiante': 'Laura', 'materia': 'Ciencias', 'calificacion': 82},
    {'estudiante': 'Juan', 'materia': 'Literatura', 'calificacion': 80}
]

# 2. Inicialización de estructuras de datos
# Diccionario para sumar y contar las calificaciones por materia
calificaciones_por_materia = {}
# Diccionario para registrar las calificaciones de cada estudiante
calificaciones_por_estudiante = {}
# Conjunto para almacenar las materias únicas evaluadas
materias_unicas = set()

# 3. Iterar sobre la lista de calificaciones para llenar las estructuras de datos
for calificacion in calificaciones:
    estudiante = calificacion['estudiante']
    materia = calificacion['materia']
    nota = calificacion['calificacion']

    # Sumar y contar las calificaciones por materia
    if materia in calificaciones_por_materia:
        calificaciones_por_materia[materia]['total'] += nota
        calificaciones_por_materia[materia]['conteo'] += 1
    else:
        calificaciones_por_materia[materia] = {'total': nota, 'conteo': 1}
    
    # Registrar las calificaciones de cada estudiante
    if estudiante in calificaciones_por_estudiante:
        calificaciones_por_estudiante[estudiante].append(nota)
    else:
        calificaciones_por_estudiante[estudiante] = [nota]
    
    # Agregar la materia al conjunto de materias únicas
    materias_unicas.add(materia)

# 4. Calcular el promedio de calificaciones por materia
promedio_por_materia = {materia: datos['total'] / datos['conteo'] for materia, datos in calificaciones_por_materia.items()}

# 5. Encontrar el estudiante con la calificación más alta y más baja
estudiante_max_calificacion = max(calificaciones_por_estudiante, key=lambda est: max(calificaciones_por_estudiante[est]))
estudiante_min_calificacion = min(calificaciones_por_estudiante, key=lambda est: min(calificaciones_por_estudiante[est]))

# 6. Imprimir los resultados
print("Promedio de Calificaciones por Materia:")
for materia, promedio in [promedio_por_materia].items():
    print(f"{materia}: {promedio:.2f}")

print("\nCalificaciones por Estudiante:")
for estudiante, notas in [calificaciones_por_estudiante].items():
    print(f"{estudiante}: {notas}")

print("\nMaterias Únicas Evaluadas:")
for materia in [materias_unicas]:
    print(materia)

print(f"\nEstudiante con la Calificación Más Alta: {estudiante_max_calificacion} (Calificación: {max(calificaciones_por_estudiante[estudiante_max_calificacion])})")
print(f"Estudiante con la Calificación Más Baja: {estudiante_min_calificacion} (Calificación: {min(calificaciones_por_estudiante[estudiante_min_calificacion])})")
