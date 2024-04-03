# Listas en Python
---
- Son una estructura de datos que se usa para almacenar colecciones de elementos ordenados.
- Son mutables, es decir se puede modificar su contenido después de crearlas.  
**Creación de Listas**
- `lista = []` o `lista = list()`: Crea una lista vacía.
- `lista = [elemento1, elemento2, ...]`: Crea una lista con elementos predefinidos.

**Ejemplo:**
```python
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "pera", "uva"]
lista_mezclada = [True, "banana", None, 1]
```
## Métodos
- **`append(elemento)`**: Agrega un elemento al final de la lista.

```python
numeros = [1, 2, 3, 4, 5]
numeros.append(6)  # numeros se convierte en [1, 2, 3, 4, 5, 6]
```
- **`extend(iterable)`**: Extiende la lista agregando elementos de otro iterable.
```python
frutas = ["manzana", "plátano", "naranja"]
verduras = ["zanahoria", "papa"]
frutas.extend(verduras)  # frutas se convierte en ["manzana", "plátano", "naranja", "zanahoria", "papa"]
```
- **`insert(indice, elemento)`**: Inserta un elemento en un índice específico de la lista.
```python
frutas = ["manzana", "plátano", "naranja"]
frutas.insert(1, "mango")  # frutas se convierte en ["manzana", "mango", "plátano", "naranja"]
```
- **`remove(elemento)`**: Elimina la primera aparición de un elemento de la lista.
```python
frutas = ["manzana", "mango", "plátano", "naranja"]
frutas.remove("mango")  # frutas se convierte en ["manzana", "plátano", "naranja", "zanahoria", "papa"]
```
- **`pop([indice])`**: Elimina y devuelve el elemento en el índice especificado. Si no se proporciona un índice, elimina y devuelve el último elemento.
```python
frutas = ["manzana", "mango", "plátano", "naranja"]
frutas.pop(2)
# Regresa plátano
# Al imprimir frutas regresar lo siguiente
print(frutas)
# ['manzana', 'mango', 'naranja']
```
- **`clear()`**: Elimina todos los elementos de la lista.

- **`index(elemento[, inicio[, fin]])`:** Devuelve el índice de la primera aparición de un elemento en la lista dentro del rango especificado. 
```python
# Encontrar el índice de "banana"
frutas = ["manzana", "banana", "pera", "uva"]
print(frutas.index('banana'))
# Devolverá como resultado 1
```
- **`count(elemento)`**: Devuelve el número de veces que un elemento aparece en la lista.
```python
frutas = ["manzana", "banana", "pera", "uva"]
print(frutas.count('banana'))
# Devolverá como resultado 1
```
- **`sort([key][, reverse])`**: Ordena los elementos de la lista en orden ascendente. Se puede proporcionar una función de clave opcional para personalizar el orden. El parámetro `reverse` se puede establecer en `True` para ordenar en orden descendente.
- **`reverse()`**: Invierte el orden de los elementos en la lista.

## Acceso a Elementos de la Lista
- **`lista[indice]`**: Accede al elemento en el índice especificado de la lista.
- **`lista[inicio:fin]`**: Accede a una porción de la lista desde el índice de inicio hasta el índice de fin (exclusivo). Si no se proporciona el índice de inicio, se asume como 0. Si no se proporciona el índice de fin, se asume como el final de la lista.
- **`elemento in lista`:** Comprueba si un elemento existe utilizando el operador in
```python
lista = ["manzana", "banana", "pera", "uva"]
elemento  = "uva"
resultado = elemento in lista
# Resulado tendría "True"
if "manzana" in frutas:
    print("La manzana está presente")
```
## Modificación de la Lista
```python
lista = ["manzana", "banana", "pera", "uva"]
lista[1] = 'cereza'
print(lista)
```
El resultado sera:
`["manzana", "cereza", "pera", "uva"]`

## Operaciones Comunes de Listas
- **`len(lista)`**: Devuelve la longitud (número de elementos) de la lista.
- **Concatenación (+)**: Combina listas para crear una nueva.
```python
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "mango", "plátano", "naranja"]
todos_elementos = numeros + frutas  # todos_elementos contendrá tanto números como frutas
```
- **Iteración**: Recorre elementos usando un bucle for.
```python
for fruta in frutas:
    print(fruta)
```
## Comprensión de listas

```python
cuadrados = [x * x for x in range(1, 6)]  # Crea una lista de cuadrados del 1 al 5
```
## Uso de range  y generación de listas
```python
lista_rango = list(range(10))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


lista_rango_inversa = list(range(0,100, 3))
# va a ser del 0 al 99
lista_rango_inversa = list(range(20,0, -2))
#[20, 18, 16, 14, 12, 10, 8,6, 4, 2]
```
- El rango no llega al último valor que se da como limite
## Notas
- Las listas pueden contener elementos de cualquier tipo de dato, incluidas otras listas (listas anidadas) u objetos personalizados.


