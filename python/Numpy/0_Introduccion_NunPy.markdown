# Introducción a NunPy
---
- Es una biblioteca de código abierto que tiene funcionalidades para la computación científica.
- **Creación y manipulación de arrays multi dimensionales:** Permite crear, modificar y acceder a arrays de datos de forma eficiente.
- **Operaciones matemáticas:** Cuenta con varias funciones matemáticas para operar con arrays, como sumas, restas, multiplicaciones, divisiones, cálculo de raises, etc,
- **Álgebra lineal:** Permite realizar operaciones de álgebra lineal como la multiplicación de matrices, la inversión de matrices y la resolución de sistemas de ecuaciones lineales.
- **Análisis estadístico:**: Ofrece funciones para calcular medias, varianzas, correlaciones, histogramas y otras estadísticas descriptivas.
- **Ficheros y E/S:** Permite leer y escribir datos desde y hacia archivos de diferentes formatos.
## Beneficios
- **Eficiencia:** Ofrece un alto rendimiento para operaciones matemáticas y computacionales con arrays.
- **Facilidad de uso:** Soporta una amplia variedad de tarareas de computación científica, como análisis de datos, aprendizaje automático, simulación numérica y procesamiento de imágenes.
# Conceptos básicos
- **Arrys:** Son estructuras de datos multi dimensionales que pueden almacenar datos de diferentes tipos.
- **Tipos de datos:** Soporta una amplia variedad de tipos de datos, como enteros, flotantes, strings, fechas y valores booleanos.
- **Funciones:** Tiene una amplia gama de funciones para realizar operaciones matemáticas, estadísticas y de álgebra líneal con arrays.
- **Módulos:** Está organizado en módulos que agrupan funciones relacionadas.

## Arrays
### Crear un array
```python
import numpy as np
array = np.array([1, 2, 3, 4]) 
```
- `np.zeros(n)`: n es el número de  0
- `np.zeros([10, 10])`: matriz de 10 * 10 de 0s
- `np.zeros((3 , 7 , 5))`:3  matrices de 7 * 5 de 0s
- `np.ones(n)`: es el número de  1
- `np.arange()`: de un rando (0 ,n) hasta uno antes del limite, por defecto.(inicio, fin, pasos)
- `np.linespace()`; (inicio, fin, número de elemetnos)
### Accede a elemetnos usando índices
- `array[0]`
- `array[1, 2]`
- `array[1:4]`: Slicing para sub-arrays.
- `array.reshape()`: Cambia la forma de un array.
- `array.ravel()`: De matriz a vector.
- `array_multiplicado = np.dot(array1, array2)`: Multiplicar dos arreglos.
- `array.dtype`: verificar el tipo de datos.
- `array.shpe`: Cantidad de elementos.
### Funciones de array:
- `np.sum()`: Suma de elementos.
- `np.mean()`: Media de elementos.
- `np.std()`: Desviación estándar.
- `np.min()`: Elemento mínimo.
- `np.max()`: Elemento máximo.
- `np.sort()`: Ordena elementos.
- `np.sin()`: Función seno.
- `np.cos()`: Función  cos seno.
- `np.exp()`: Función exponente.
- `np.exp()`: Función logaritmo.
### Broadcasting
- Operaciones entre arrays de diferentes formas compatibles.
- Se realiza alineación automática de elementos.
### Álgebra lineal
- `np.dot(A, B)`: Producto punto de matrices.
- `np.linalg.inv(A)`: Inversa de una matriz.
### Lectura y escritura de archivos:
- `np.savetext(archivo, array)`: Guarda un array en un archivo de texto.
- `no.loadtxt(archivo)`: Carga un array desde un archivo de texto.
### Arrasys Random
- `no.random.rand(n)`: genera m números aleatorios uniformes entre 0 y 1.
- `np.random.randn(n)`; Genera n número aleatorios con distribución normal.