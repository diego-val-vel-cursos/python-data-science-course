# Definición de la clase base Organismo
class Organismo:
    def __init__(self, nombre, especie):
        # Inicializa los atributos comunes
        self.nombre = nombre
        self.especie = especie
    
    def mostrar_info(self):
        # Muestra la información del organismo
        print(f"Nombre: {self.nombre}, Especie: {self.especie}")

# Definición de la clase derivada Bacteria
class Bacteria(Organismo):
    def __init__(self, nombre, especie, gram):
        # Inicializa los atributos de la clase base y el específico de Bacteria
        super().__init__(nombre, especie)
        self.gram = gram
    
    def mostrar_info(self):
        # Muestra la información específica de la bacteria
        super().mostrar_info()
        print(f"Tipo de Gram: {self.gram}")

# Definición de la clase derivada Virus
class Virus(Organismo):
    def __init__(self, nombre, especie, tipo_arn):
        # Inicializa los atributos de la clase base y el específico de Virus
        super().__init__(nombre, especie)
        self.tipo_arn = tipo_arn
    
    def mostrar_info(self):
        # Muestra la información específica del virus
        super().mostrar_info()
        print(f"Tipo de ARN: {self.tipo_arn}")

# Definición de la clase derivada Fungus
class Fungus(Organismo):
    def __init__(self, nombre, especie, habitat):
        # Inicializa los atributos de la clase base y el específico de Fungus
        super().__init__(nombre, especie)
        self.habitat = habitat
    
    def mostrar_info(self):
        # Muestra la información específica del hongo
        super().mostrar_info()
        print(f"Hábitat: {self.habitat}")

# Definición de la clase base Experimento
class Experimento:
    def __init__(self, id_experimento):
        # Inicializa el identificador del experimento
        self.id_experimento = id_experimento
    
    def realizar_experimento(self, organismo):
        # Método polimórfico para realizar el experimento
        raise NotImplementedError("Este método debe ser implementado por la subclase")

# Clase Crecimiento hereda de Experimento
class Crecimiento(Experimento):
    def __init__(self, id_experimento, tiempo):
        # Inicializa los atributos de la clase base y el específico de Crecimiento
        super().__init__(id_experimento)
        self.tiempo = tiempo
    
    def realizar_experimento(self, organismo):
        # Implementación del experimento de crecimiento
        print(f"Realizando experimento de crecimiento en {organismo.nombre} por {self.tiempo} días.")

# Clase Mutación hereda de Experimento
class Mutación(Experimento):
    def __init__(self, id_experimento, agente):
        # Inicializa los atributos de la clase base y el específico de Mutación
        super().__init__(id_experimento)
        self.agente = agente
    
    def realizar_experimento(self, organismo):
        # Implementación del experimento de mutación
        print(f"Realizando experimento de mutación en {organismo.nombre} usando {self.agente}.")

# Clase Resistencia hereda de Experimento y otra clase (para herencia múltiple)
class Resistencia(Experimento):
    def __init__(self, id_experimento, antibiotico):
        # Inicializa los atributos de la clase base y el específico de Resistencia
        super().__init__(id_experimento)
        self.antibiotico = antibiotico
    
    def realizar_experimento(self, organismo):
        # Implementación del experimento de resistencia
        print(f"Realizando experimento de resistencia en {organismo.nombre} contra {self.antibiotico}.")

# Crear instancias de los organismos
bacteria = Bacteria("E. coli", "Bacteria", "Gram-negativa")
virus = Virus("Influenza", "Virus", "ARN negativo")
fungus = Fungus("Penicillium", "Fungus", "Tierra")

# Crear instancias de los experimentos
experimento_crecimiento = Crecimiento(1, 7)
experimento_mutacion = Mutación(2, "Radiación")
experimento_resistencia = Resistencia(3, "Penicilina")

# Realizar experimentos usando polimorfismo
for experimento in [experimento_crecimiento, experimento_mutacion, experimento_resistencia]:
    for organismo in [bacteria, virus, fungus]:
        experimento.realizar_experimento(organismo)
