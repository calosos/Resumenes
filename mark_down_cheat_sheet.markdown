# Cheat Sheet de Markdown

## Encabezados
# Encabezado 1
## Encabezado 2
### Encabezado 3

## Estilos de Texto
*Texto en cursiva*
**Texto en negrita**
~~Texto tachado~~

## Listas
### Lista sin orden
- Elemento 1
- Elemento 2
- Elemento 3

### Lista ordenada
1. Elemento 1
2. Elemento 2
3. Elemento 3

## Enlaces
`[Texto del enlace](url_del_enlace)`

## Imágenes
`![Texto alternativo](ruta/de/la/imagen.png)`
- `![Texto alternativo]`: Es el texto que se mostrará si la imagen no se puede cargar.
- `(ruta/a/la/imagen.png)`: Es la ruta de acceso a la imagen. Puede ser una URL o una ruta local a la imagen en tu ordenador.   

**Tamaño de la imagen**  

`![Texto alternativo](ruta/a/la/imagen.png)(ancho x alto)`
`![Texto alternativo](ruta/a/la/imagen.png)(200x100)` 

**Alineación de la imagen**  

`![Texto alternativo](ruta/a/la/imagen.png){.align-left}`  
`![Texto alternativo](ruta/a/la/imagen.png){.align-right}`    
`![Texto alternativo](ruta/a/la/imagen.png){.align-center}`  

## Citas
> Esto es una cita.

## Línea horizontal
---

## Código
`código en línea`

```python
def funcion_ejemplo():
print("Hola, esto es un bloque de código.")
```