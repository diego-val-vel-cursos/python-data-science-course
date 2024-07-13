# Curso: Capacitación de Python para Data Science

## Objetivo del repositorio
Diseñado para llevar el curso llamado "Capacitación para Python Data Science". El objetivo de este curso es proporcionar una comprensión profunda de Python y sus aplicaciones en la ciencia de datos, abarcando desde los fundamentos del lenguaje hasta la implementación de ejercicios más complejos.

## Temario

### Módulo 1: Fundamentos de Python
1.1. Estructura y elementos del lenguaje  
1.2. Tipos, operadores, expresiones  
1.3. Control de flujo  
1.4. Colecciones  
1.5. Funciones  
1.6. Estructuras de datos fundamentales  

### Módulo 2: Programación Orientada a Objetos
2.1. Clases, propiedades y métodos  
2.2. Objetos, herencia, herencia múltiple y polimorfismo  
2.3. Acceder a los métodos y propiedades de un objeto  

### Módulo 3: Tipos de datos complejos en Python
3.1. Listas y Tuplas  
3.2. Diccionarios y Conjuntos  

### Módulo 4: Python para ciencia de datos
4.1. Introducción a NumPy  
4.2. Operaciones avanzadas con matrices NumPy  
4.3. Introducción a Pandas  
4.4. Manipulación de datos en Pandas DataFrames  
4.5. Visualización básica de datos con Seaborn  
4.6. Visualización avanzada de datos con Seaborn  

### Módulo 5: Algoritmos en Python
5.1. Algoritmos de clasificación y su implementación  
5.2. Árboles y grafos y su implementación  

## Tecnologías usadas
- Python 3.8
- NumPy
- Pandas
- Seaborn
- Matplotlib
- Scikit-learn
- Plotly

## Explicación del archivo `docker-compose.yml`
Este archivo `docker-compose.yml` configura un ambiente de desarrollo completo para el curso. Contiene el siguiente servicio:

1. **python-env**:
   - **Imagen**: Python 3.8 (basado en Debian Slim)
   - **Volúmenes**: Monta el directorio actual en `/app`
   - **Directorio de trabajo**: `/app`
   - **Comando**: Instala las dependencias listadas en `requirements_python-env.txt` y mantiene el contenedor en ejecución con un shell interactivo.

## Levantando los contenedores
Para levantar los contenedores con el entorno de desarrollo, se deben de seguir estos pasos:

1. Asegurarse de que el motor de Docker esté corriendo.
2. Acceder al directorio raíz del repositorio.
3. Ejecutar el siguiente comando para levantar los contenedores en segundo plano:
   ```sh
   docker-compose up -d
4. Lo anterior le indica a Docker que debe ejecutar el contenido del archivo docker-compose.yml.

## Todos los comandos para entrar al contenedor y corroborar las versiones de las tecnologías

```sh
# Acceder al contenedor
docker exec -it python_env bash

# Verificar Python
python --version

# Verificar pip
pip --version

# Verificar NumPy
python -c "import numpy; print(numpy.__version__)"

# Verificar Pandas
python -c "import pandas; print(pandas.__version__)"

# Verificar Seaborn
python -c "import seaborn; print(seaborn.__version__)"

# Verificar Matplotlib
python -c "import matplotlib; print(matplotlib.__version__)"

# Verificar Scikit-learn
python -c "import sklearn; print(sklearn.__version__)"

# Verificar Plotly
python -c "import plotly; print(plotly.__version__)"
