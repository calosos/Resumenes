Métodos y Funciones de Listas en Python

## Manipulación de Listas
### Lisa de ejemplo:
`lista = ["manzana", "banana", "pera", "uva"]`
- `append(elemento)`: Agrega un elemento al final de la lista.
- `extend(iterable)`: Extiende la lista agregando elementos de otro iterable.
- `insert(indice, elemento)`: Inserta un elemento en un índice específico de la lista.
- `remove(elemento)`: Elimina la primera aparición de un elemento de la lista.
    - Ejemplo :
    1. Eliminar la cadena "banana" de la lista
    `lista.remove("banana")`

- `pop([indice])`: Elimina y devuelve el elemento en el índice especificado. Si no se proporciona un índice, elimina y devuelve el último elemento.
- `clear()`: Elimina todos los elementos de la lista.
- `index(elemento[, inicio[, fin]])`: Devuelve el índice de la primera aparición de un elemento en la lista dentro del rango especificado.
    - Ejemplo :
    1.Encontrar el ídice de "banana"
    `lista.index('banana')`\
    - Devolvera como resultado 1
    
- `count(elemento)`: Devuelve el número de veces que un elemento aparece en la lista.
- `sort([key][, reverse])`: Ordena los elementos de la lista en orden ascendente. Se puede proporcionar una función de clave opcional para personalizar el orden. El parámetro `reverse` se puede establecer en `True` para ordenar en orden descendente.
- `reverse()`: Invierte el orden de los elementos en la lista.

## Acceso a Elementos de la Lista

- `len(lista)`: Devuelve la longitud (número de elementos) de la lista.
- `lista[indice]`: Accede al elemento en el índice especificado de la lista.
- `lista[inicio:fin]`: Accede a una porción de la lista desde el índice de inicio hasta el índice de fin (exclusivo). Si no se proporciona el índice de inicio, se asume como 0. Si no se proporciona el índice de fin, se asume como el final de la lista.
- `elemento in lista`: Verifica si un elemento está presente en la lista.

## Creación de Listas

- `lista = []` o `lista = list()`: Crea una lista vacía.
- `lista = [elemento1, elemento2, ...]`: Crea una lista con elementos predefinidos.
