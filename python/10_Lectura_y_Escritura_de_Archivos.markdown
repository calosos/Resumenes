# Lectura y Escritura de Archivos
---
## Lectura de archivos
- **Lectura línea por línea:** Puede usarse el método `readline()` del objeto *"file"* para leer el archivo línea por línea.
```python
archivo = open("ejemplo.txt", "r")
linea = archivo.readline()
while linea:
    print(linea)
    linea = archivo.readline()
archivo.close()
```
- **Lectura por caracteres:** Puede usarse el método `read(n)`del objeto *"file"* para leer una cantidad específica de caracteres del archivo.
```python
archivo = open("ejemplo.txt", "r")
caracteres = archivo.read(10)
print(caracteres)
archivo.close()
```
- **Manejo de errores:** Es importante usar el bloque `with` para asegurar que el archivo se cierre correctamente, incluso si se produce una excepción.
```python
with open("ejemplo.txt", "r") as archivo:
    try:
        contenido = archivo.read()
    except IOError as e:
        print(f'Error al leer el archivo: {e}')
print(contenido)
```
## Escritura de archivos
- **Escritura con formato:** Puedes usar el método format() para escribir cadenas con formato en el archivo.
```python
edad  = 22
archivo = open('ejemplo.txt', 'w')
archivo.write('Hola Mundo, mi nombre es {0} y tengo: {0} años'.format("Juan", edad))
archivo.close()
```
-- **Escritura binaria:** Puede usar el modo `"wb"` para escribir datos binarios en el archivo.
```python
archivo = open('ejemplo.txt', 'w')
archivo.write(bytes_de_la_imagen)
archivo.close()
```

## Modos de apertura
- **"r":** Abre el archivo en modo lectura.
- **"w":** Abre el archivo en modo escritura.
- **"a":** Abre el archivo en modo escritura, agregando el nuevo contenido al final del archivo.
- **"r+":** Abre el archivo en modo lectura y escritura.
- **"x":** Crea el archivo.
# Códigos de Error:
- **`IOError`:** Se produce si no se encuentra el archivo o si hay un error al abrirlo.

## Comprensión de archivos
- Se pueden usar los módulos `gzip` o `bz2` para comprimir archivos antes de escribirlos.
```python
import gzip

with open("ejemplo.txt", "r") as archivo_origen:
    contenido = archivo_origen.read()

with gzip.open("ejemplo.gz", "wb") as archivo_comprimido:
    archivo_comprimido.write(contenido.encode("utf-8"))
```
# Lectura y escritura de archivos CSV

El módulo csv ofrece una forma más sencilla de leer y escribir archivos CSV.
```python
import csv

# Lectura
with open("ejemplo.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

# Escritura
with open("ejemplo.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Nombre", "Apellido", "Edad"])
    escritor.writerow(["Ana", "López", 25])
    escritor.writerow(["Juan", "Pérez", 30])
```