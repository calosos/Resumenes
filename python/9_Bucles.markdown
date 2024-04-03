# Bucles 
- Permiten ejecutar un bloque de código de forma repetitiva.
- Son fundamentales para automatizar tareas y realizar operaciones sobre conjuntos de datos.
## Tipos de bucles
- Bucles `for`: Se utiliza para ejecutar un bloque de código un número determinado de veces, generalmente iterando sobre una secuencia como una lista o una cadena.
- Bucle `while`: Se utiliza para ejecutar un bloque de código mientras se cumpla una condición.
## Bucle `for`
```python
for i in range(1, 6):
    print(i)
```
## Bucle `while`
```python
# Pedir un número al usuario hasta que introduzca un número positivo
numero = -1
while numero <= 0:
    numero = int(input("Introduce un número positivo: "))
print('El número  introducido es:', número)
```
## Sentencias adicionales:
- `break`: Se utiliza para salir del bucle de forma anticipada.
```python
# Imprimir los números del 1 al 10, pero salir del bucle al llegar al 5
for i in range(1, 11):
    print(i)
    if i == 5:
        break
```
- `continue`: Se utiliza para pasar a la siguiente iteración del bucle sin ejecutar el resto del código dentro del bucle.
```python
# Imprimir los números pares del 1 al 10
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)
```
## Elección del bucle adecuado

- Depende de la tarea que se desea realizar. 
- Si se conoce de antemano el número de veces que se debe ejecutar el bucle, se suele usar un bucle for. 
- Si no se conoce el número de iteraciones o se desea ejecutar el bucle mientras se cumpla una condición, se utiliza un bucle while.

## Bucles anidados
Un bucle anidado es un bucle que se ejecuta dentro de otro bucle. Esto te permite crear estructuras de control más complejas y realizar tareas más sofisticadas.
```python
# Imprimir la tabla de multiplicar del 2
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
```
**Otros ejemplos:**
- Recorrer una matriz bidimensional.
- Buscar un elemento en una lista de listas.
- Generar todas las combinaciones posibles de dos conjuntos de datos.

**Consejos para usar bucles anidados:**

- Evita anidar bucles demasiado profundamente, ya que puede dificultar la lectura y comprensión del código.
- Utiliza nombres de variables descriptivos para cada bucle.
- Considera usar funciones para encapsular la lógica de cada bucle.