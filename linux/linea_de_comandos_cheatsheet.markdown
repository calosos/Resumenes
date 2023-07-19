# Cheat Sheet de Comandos de Bash

## Navegación y Manipulación de Directorios
- Directorio actual: `pwd`
- Cambiar de directorio: `cd ruta/directorio`
- Listar archivos y directorios: `ls`
- Crear un directorio: `mkdir nombre_directorio`
- Crear un archivo: `touch nombre_archivo`
- Eliminar un archivo: `rm nombre_archivo`
- Eliminar un directorio (vacío): `rmdir nombre_directorio`
- Eliminar archivos y directorios: `rm [opciones] [archivo(s) o directorio(s)]`
  - Opciones:
    - -r : Elimina directorios y su contenido de forma recursiva.
    - -f : Forzar la eliminación sin pedir confirmación.
    - -i : Solicita confirmación antes de eliminar cada archivo o directorio.
    - -v : Muestra información detallada sobre los archivos eliminados.
    - -d : Elimina solo los directorios vacíos.
    - --preserve-root : Evita la eliminación accidental de archivos del directorio raíz.
- Copiar un archivo: `cp archivo_origen archivo_destino`
- Mover un archivo o directorio: `mv origen destino`
- Cambiar el nombre de un directorio: `mv ruta/mi_directorio ruta/nuevo_directorio`


## Operaciones de Archivos
- Mostrar el contenido de un archivo: `cat archivo`
- Mostrar el contenido de un archivo página por página: `less archivo`
- Mostrar las primeras líneas de un archivo: `head [opciones] [archivo(s)]`
  - Opciones:
    - -n NUM : Muestra las primeras NUM líneas del archivo(s).
    - -c NUM : Muestra los primeros NUM bytes del archivo(s).
    - -q : No muestra encabezado de archivo al procesar múltiples archivos.
    - -v : Muestra siempre el encabezado de archivo al procesar múltiples archivos.

- Mostrar las últimas líneas de un archivo: `tail archivo`
- Buscar texto en un archivo: `grep texto archivo`
- Filtrar y manipular texto: `awk 'patrón {acción}' archivo`
- Concatenar archivos: `cat archivo1 archivo2 > archivo_final`
- Mostrar información sobre el uso de espacio en disco de los sistemas de archivos montados en el sistema: `df [opciones] [archivo o directorio]`
  - Opciones:
    - -a : Muestra todos los sistemas de archivos, incluyendo aquellos que tienen tamaño 0.
    - -h : Muestra los tamaños en un formato legible por humanos (ejemplo: "1K", "1M", "1G").
    - -T : Muestra el tipo de sistema de archivos.
    - -i : Muestra información sobre inodos en lugar de bloques de disco.
    - -x tipo : Excluye los sistemas de archivos del tipo especificado.
## Variables y Entorno
- Crear una variable: `variable=valor`
- Mostrar el valor de una variable: `echo $variable`
- Variables de entorno predefinidas:
  - `$HOME`: Directorio del usuario actual
  - `$PATH`: Ruta de búsqueda de comandos
  - `$USER`: Nombre del usuario actual

## Comandos de Procesos
- Ejecutar un comando en segundo plano: `comando &`
- Mostrar los procesos en ejecución: `ps`
- Finalizar un proceso: `kill PID`

## Redireccionamiento y Tuberías
- Redireccionar la salida a un archivo: `comando > archivo`
- Redireccionar la salida y la salida de errores a un archivo: `comando > archivo 2>&1`
- Redireccionar la entrada desde un archivo: `comando < archivo`
- Conectar la salida de un comando con la entrada de otro: `comando1 | comando2`

## Permisos y Propietarios de Archivos
- Cambiar el propietario de un archivo o directorio: `chown nuevo_propietario archivo_o_directorio`
- Cambiar el grupo de un archivo o directorio: `chgrp nuevo_grupo archivo_o_directorio`

## Ayuda y Documentación
- Mostrar el manual de un comando: `man comando`
- Mostrar información sobre un comando: `info comando`
- Mostrar la descripción de un comando: `comando --help`

## Gestión de Paquetes

- Instalar un paquete: `apt-get install [nombre_paquete]`
- Desinstalar un paquete: `apt-get remove [nombre_paquete]`
- Actualizar la lista de paquetes disponibles: `apt-get update`
- Actualizar los paquetes instalados: `apt-get upgrade`
- Buscar paquetes disponibles: `apt-cache search [palabra_clave]`

## Compresión y Descompresión

- Comprimir archivos o directorios en un archivo tar.gz: `tar -czvf [nombre_archivo.tar.gz] [archivos/directorios]`
- Descomprimir un archivo tar.gz: `tar -xzvf [nombre_archivo.tar.gz]`
- Comprimir archivos o directorios en un archivo zip: `zip [nombre_archivo.zip] [archivos/directorios]`
- Descomprimir un archivo zip: `unzip [nombre_archivo.zip]`

## Otros
- Mostrar el historial de comandos ejecutados: `history`
- Ejecutar un comando con privilegios de administrador: `sudo [comando]`
- Mostrar la estrutura de las carpetas de forma gráfica: `tree`



