# Strings
---
**String:** o cadena de caracteres es *una secuencia ordenada de caracteres* que se utilizan para representar texto.
Ejemplo de formas de definir strings en python:
```python
saludo = "Hola mundo"  # Comillas simples
mensaje = '¿Cómo estás?'  # Comillas dobles (pueden incluir comillas simples)
parrafo = """Este es un 
párrafo con varias líneas"""  # Comillas triples para strings multilínea

```
## Indexación en Strings:** 
Es un método para acceder a caracteres específicos dentro de un string, se consideran como secuencia y cada carácter tiene un índice asociado que comienza en 0.
```python
nombre = "Julio César Castillo"

# Acceder al primer caracter
primer_caracter = nombre[0]  # "J"

# Acceder al último caracter
ultimo_caracter = nombre[-1]  # "o"

# Acceder al quinto caracter
quinto_caracter = nombre[4]  # "l"

```
Rango de caracteres con la notación de *"rebanadas"*
```python
# Acceder a los primeros 5 caracteres
primeros_cinco = nombre[:5]  # "Julio"

# Acceder a los últimos 4 caracteres
ultimos_cuatro = nombre[-4:]  # "illo"

# Acceder a los caracteres del 2 al 7
subcadena = nombre[2:7]  # "ulio "

# Acceder a cada dos caracteres
salteado = nombre[::2]  # "Jio Csaio"

# Acceder a cada tercer caracter
cada_tercero = nombre[::3]  # "Jl Csl"

# Acceder al penúltimo caracter
penultimo = nombre[-2]  # "t"

# Acceder al tercer caracter desde el final
tercero_final = nombre[-3]  # "l"

#Invertir la cadena
nombre_invertido = nombre[::-1]  # "oltiC asréJ oiluJ"

```

## **Concatenación:** 
Es la unión de dos o más strings para formar un nuevo string:  
- Usando el operador: `+`
```python
nombre = "Julio"
apellido = "César"
nombre_completo = nombre + " " + apellido

print(nombre_completo)  # Output: Julio César
```
- Usando el método join():
```python
nombres = ["Julio", "César"]
nombre_completo = " ".join(nombres)

print(nombre_completo)  # Output: Julio César
```
- Usando el f-string(Python 3.6+)
```python
edad = 30
saludo = f"Hola, {nombre_completo}! Tienes {edad} años."

print(saludo)  # Output: Hola, Julio César! Tienes 30 años.
```
- Ejemplos adicionales:
```python
mensaje = "El total es: " + str(100)
print(mensaje)  # Output: El total es: 100

descripcion = "Esta es la primera línea\nEsta es la segunda línea"
print(descripcion)

```
### Notas
- La concatenación crea una nueva cadena. Las cadenas originales permanecen sin cambios.
- Puedes concatenar strings con otros tipos de datos como números, pero Python los convertirá a strings antes de la unión.
- Las f-strings son especialmente útiles para formatear texto con variables y expresiones.
## Comparación de Strings
Verificar si dos cadenas de caracteres son iguales o diferentes.
- Usando el operador: `==`
```python
palabra1 = "Hola"
palabra2 = "hola"

print(palabra1 == palabra2)  # False (distingue mayúsculas/minúsculas)

palabra3 = "Mundo"

print(palabra1 == palabra3)  # False (cadenas diferentes)
```
- Comparación sin distinción de mayúsculas/minúsculas:
```python
# Opción 1: convertir a minúsculas
print(palabra1.lower() == palabra2.lower())  # True

# Opción 2: convertir a mayúsculas
print(palabra1.upper() == palabra2.upper())  # True
```
- Operadores de desigualdad (!=):
```python
print(palabra1 != palabra2)  # True
```
- Operadores de orden (<, >, <=, >=):  
Los operadores de orden te permiten comparar strings alfabéticamente.
```python
print(palabra1 < palabra2)  # False 
print(palabra2 < palabra3)  # True
print(palabra1 <= palabra2)  # True (igualdad también se considera menor o igual)
```
- Pertenencia (in):
```python
oracion = "Hola Mundo, ¿cómo estás?"
print("Mundo" in oracion)  # True
print("adios" in oracion)  # False
```
- Comparación con Condicionales):
```python
cadena_uno= "Hola"
cadena_dos = "HOLA"
if cadena_uno[2:] == cadena_dos[2:].lower():
    print('Los elementos son iguales')
else:
    print('Los elementos no son iguales')
```
## Métodos de las string
**len()**:  
Cantidad de caracteres en un string.
```python
string = '   Esta string tiene 45        caracteres    '
print (len(string))
```
El resultado es:
`45`
Los caracteres vacíos o espacios también se cuentan.  

**strip():**  
Eliminar los espacios al principio y al final en un string:
```python
string = '   Esta string tiene 45        caracteres    '
print (string.strip())
print('La cantidad de caracteres que tiene la cadena ahora es de: '+ str(len(string.strip())))
```
El resultado es:  
```
Esta string tiene 45        caracteres     
La cantidad de caracteres que tiene la cadena ahora es de: 38
```
**startswith():**
Valida que la cadena empiece con cierta cadena de texto:
```python
correo = "micorreo@ejemplo.com"

print(correo.startswith("micorreo"))  # True
print(correo.startswith("ejemplo"))  # False

# La cadena comienza con "Hola"
nombre = "Hola Mundo"
if nombre.startswith("Hola"):
    print("El nombre comienza con 'Hola'")
else:
    print("El nombre no comienza con 'Hola'")
```
El resultado es:  
```
El nombre comienza con 'Hola'
```
**endswith():**
Valida que la cadena termine con cierta cadena de texto:
```python
archivo = "imagen.png"

print(archivo.endswith(".png"))  # True
print(archivo.endswith(".jpg"))  # False

# La cadena termina con "Mundo"
ciudad = "Buenos Aires, Argentina"

if ciudad.endswith("Argentina"):
    print("La ciudad termina con 'Argentina'")
else:
    print("La ciudad no termina con 'Argentina'")
```
El resultado es:  
```
La ciudad termina con 'Argentina'
```
### Notas
- `endswith()` y `startswith()` son sensibles a las mayúsculas y minúsculas.
- Puedes usar los métodos `upper()` o `lower()` para convertir las cadenas a minúsculas o mayúsculas antes de usar `startswith()` o `endswith()`.