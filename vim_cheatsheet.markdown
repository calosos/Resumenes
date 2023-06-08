# Cheat Sheet de Vim

## Modos de Vim
- Modo Normal: `Esc` o `Ctrl+[`
- Modo Insertar: `i`
- Modo Visual: `v`

## Movimiento en el archivo
- Moverse hacia arriba: `k`
- Moverse hacia abajo: `j`
- Moverse hacia la izquierda: `h`
- Moverse hacia la derecha: `l`
- Moverse al inicio de la línea: `0`
- Moverse al final de la línea: `$`
- Moverse al inicio del archivo: `gg`
- Moverse al final del archivo: `G`
- Moverse a una línea específica: `:n` (reemplaza `n` por el número de línea)

## Edición de texto
- Insertar antes del cursor: `i`
- Insertar al inicio de la línea: `I`
- Insertar después del cursor: `a`
- Insertar al final de la línea: `A`
- Borrar un carácter: `x`
- Borrar una palabra: `dw`
- Borrar una línea completa: `dd`
- Deshacer la última acción: `u`
- Rehacer la última acción: `Ctrl+r`

## Copiar y pegar
- Copiar (yank) una línea: `yy`
- Copiar (yank) un carácter: `yl`
- Copiar (yank) una palabra: `yw`
- Pegar después del cursor: `p`
- Pegar antes del cursor: `P`

## Guardar y salir
- Guardar el archivo: `:w`
- Guardar y salir: `:wq`
- Salir sin guardar cambios: `:q!`

## Búsqueda y reemplazo
- Buscar una cadena de texto: `/cadena`
- Ir a la siguiente coincidencia: `n`
- Ir a la coincidencia anterior: `N`
- Reemplazar una cadena de texto: `:%s/buscar/reemplazar/g`

## Otras funciones útiles
- Deshacer todas las modificaciones en una línea: `:u` mientras estás en modo Normal
- Cambiar la indentación hacia la derecha: `>>`
- Cambiar la indentación hacia la izquierda: `<<`
- Comentar líneas seleccionadas: `:norm I#`
