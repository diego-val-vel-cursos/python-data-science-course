class Grafo:
    def __init__(self):
        self._adjacencia = {}

    @property
    def adjacencia(self):
        return self._adjacencia

    def agregar_operacion(self, nodo1, nodo2, operacion):
        if nodo1 not in self._adjacencia:
            self._adjacencia[nodo1] = []
        if nodo2 not in self._adjacencia:
            self._adjacencia[nodo2] = []
        self._adjacencia[nodo1].append((nodo2, operacion))
        self._adjacencia[nodo2].append((nodo1, operacion))

    def calcular_resultado(self, nodo1, nodo2):
        for (nodo, operacion) in self._adjacencia[nodo1]:
            if nodo == nodo2:
                if operacion == "suma":
                    return nodo1 + nodo2
                elif operacion == "resta":
                    return nodo1 - nodo2
        return None

# Crear un grafo y realizar operaciones
grafo = Grafo()
operaciones = [
    (10, 5, "suma"),
    (10, 15, "resta"),
    (5, 3, "suma"),
    (15, 12, "suma")
]

for nodo1, nodo2, operacion in operaciones:
    grafo.agregar_operacion(nodo1, nodo2, operacion)

print(operaciones)
print(grafo.adjacencia)

print("Resultados de las operaciones:")
print("10 + 5 =", grafo.calcular_resultado(10, 5))  # Imprime 15
print("10 - 15 =", grafo.calcular_resultado(10, 15))  # Imprime -5
print("5 + 3 =", grafo.calcular_resultado(5, 3))  # Imprime 8
print("15 + 12 =", grafo.calcular_resultado(15, 12))  # Imprime 27
