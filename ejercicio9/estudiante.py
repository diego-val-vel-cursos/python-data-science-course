# Definición de la clase Estudiante
class Estudiante:
    # Método constructor para inicializar los atributos nombre y calificaciones
    def __init__(self, nombre):
        self._nombre = nombre  # Nombre del estudiante
        self._calificaciones = []  # Lista de calificaciones del estudiante

    # Propiedad para obtener el nombre del estudiante
    @property
    def nombre(self):
        return self._nombre

    # Propiedad para establecer el nombre del estudiante
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Propiedad para obtener las calificaciones del estudiante
    @property
    def calificaciones(self):
        return self._calificaciones

    # Propiedad para establecer las calificaciones del estudiante
    @calificaciones.setter
    def calificaciones(self, nuevas_calificaciones):
        if isinstance(nuevas_calificaciones, list):
            self._calificaciones = nuevas_calificaciones
        else:
            raise ValueError("Las calificaciones deben ser una lista")

    # Método para agregar una calificación a la lista
    def agregar_calificacion(self, calificacion):
        self._calificaciones.append(calificacion)

    # Método para calcular el promedio de las calificaciones
    def calcular_promedio(self):
        if len(self._calificaciones) == 0:
            return 0
        return sum(self._calificaciones) / len(self._calificaciones)


# Creación de una instancia de la clase Estudiante
estudiante = Estudiante("Juan")

# Uso de la propiedad nombre para obtener el nombre del estudiante
print("Nombre del estudiante:", estudiante.nombre)

# Uso del método agregar_calificacion para añadir calificaciones
estudiante.agregar_calificacion(85)
estudiante.agregar_calificacion(90)
estudiante.agregar_calificacion(78)

# Uso de la propiedad calificaciones para obtener las calificaciones del estudiante
print("Calificaciones del estudiante:", estudiante.calificaciones)

# Uso del método calcular_promedio para obtener el promedio de las calificaciones
print("Promedio del estudiante:", estudiante.calcular_promedio())

# Cambio del nombre del estudiante usando la propiedad nombre
estudiante.nombre = "Pedro"
print("Nuevo nombre del estudiante:", estudiante.nombre)

# Cambio de las calificaciones usando la propiedad calificaciones
estudiante.calificaciones = [92, 88, 95]
print("Nuevas calificaciones del estudiante:", estudiante.calificaciones)
print("Nuevo promedio del estudiante:", estudiante.calcular_promedio())
