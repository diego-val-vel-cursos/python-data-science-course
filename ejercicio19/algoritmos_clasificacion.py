# Importamos las bibliotecas necesarias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Cargamos el conjunto de datos Iris desde scikit-learn
from sklearn.datasets import load_iris

# Cargamos los datos y los convertimos en un DataFrame de pandas
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Mostramos las primeras filas del DataFrame para entender su estructura
print(df.head())

# Definimos las características (X) y la etiqueta (y)
X = df.iloc[:, :-1]  # Todas las columnas menos la última (species)
y = df['species']    # La columna 'species'

# Dividimos los datos en conjunto de entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Mostramos la forma de los conjuntos de datos para verificar la división
print("Tamaño del conjunto de entrenamiento:", X_train.shape, y_train.shape)
print("Tamaño del conjunto de prueba:", X_test.shape, y_test.shape)

# Inicializamos el clasificador K-NN con k=3
knn = KNeighborsClassifier(n_neighbors=3)

# Entrenamos el clasificador con el conjunto de entrenamiento
knn.fit(X_train, y_train)

# Realizamos predicciones en el conjunto de prueba
y_pred = knn.predict(X_test)

# Calculamos la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")

# Mostramos las predicciones y las etiquetas reales para comparar
print("Predicciones:", y_pred)
print("Etiquetas reales:", y_test.values)
