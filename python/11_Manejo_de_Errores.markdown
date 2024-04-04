# Manejo de Errores
---
El bloque `try/except/finally/else` proporciona una estructura completa para el manejo de errores en Python. Permite ejecutar código de forma controlada en caso de que ocurra un error, evitando que el programa se bloquee y liberando recursos adecuadamente.
## Estructura
```python
try:
    # Bloque de código que puede generar errores
except Exception1 as e1:
    # Bloque de código que se ejecuta si se produce un error de tipo Exception1
except Exception2 as e2:
    # Bloque de código que se ejecuta si se produce un error de tipo Exception2
else:
    # Bloque de código que se ejecuta si NO se produce ningún erro
...
finally:
    # Bloque de código que se ejecuta siempre, haya o no haya error
```
**Ejemplo**
```python
try:
    archivo = open("ejemplo.txt", "r")
    contenido = archivo.read()
except FileNotFoundError as e:
    print(f"Error: el archivo no existe. {e}")
finally:
    if archivo is not None:
        archivo.close()
        print("Archivo cerrado.")
```
**Explicación:**
- El bloque `try` contiene el código que puede generar errores.
- El bloque `except` se ejecuta si se produce un error en el bloque `try`.
- La variable `e` contiene información sobre el error.
- El bloque `else` se ejecuta solamente **si NO se produce ningún error** en el bloque `try`. Se suele usar para realizar acciones que dependen de la ejecución exitosa del código del bloque `try`.
- El bloque `finally` se ejecuta siempre, independientemente de si se produce un error o no. Se suele usar para liberar recursos como archivos abiertos, conexiones de red, etc.

## **Tipos de excepciones:**
- **ValueError:** Se produce cuando se introduce un valor no válido.
- **TypeError:** Se produce cuando se utiliza un tipo de dato incorrecto.
- **IndexError:** Se produce cuando se accede a un índice fuera de rango.
- **ZeroDivisionError:** Se produce cuando se divide por cero.
## Módulo `sys`
- El módulo `sys` proporciona acceso a variables y funciones del intérprete de Python.
- La función `sys.exc_info()` devuelve información sobre la última excepción que se ha producido.  
**Ejemplo**
```python
try:
    numero = int(input("Introduce un número: "))
except ValueError as e:
    tipo_excepcion, valor_excepcion, traza_excepcion = sys.exc_info()
    print(f"Tipo de excepción: {tipo_excepcion}")
    print(f"Valor de la excepción: {valor_excepcion}")
    print(f"Traza de la excepción: {traza_excepcion}")
```
## Mensaje de error
El mensaje de error debe responder:
- ¿Qué paso?
- ¿Dónde paso?
- ¿Cuándo paso?
- ¿Qué se debe hacer?

## Notas Adicionales
**Múltiples excepciones:** Puedes usar varios bloques except para manejar diferentes tipos de excepciones.
**Excepciones personalizadas:** Puedes crear tus propias excepciones para manejar errores específicos de tu programa.
