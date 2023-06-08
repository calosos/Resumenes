# Cheat Sheet de Comandos de Git

## Configuración
- Configurar el nombre de usuario: `git config --global user.name "Nombre"`
- Configurar el correo electrónico: `git config --global user.email "correo@ejemplo.com"`
- Configurar el editor de texto: `git config --global core.editor "nombre_editor"`

## Iniciar un Repositorio
- Inicializar un nuevo repositorio: `git init`
- Clonar un repositorio existente: `git clone url_repositorio`

## Registrar Cambios
- Añadir cambios al área de preparación: `git add archivo(s)`
- Añadir todos los cambios al área de preparación: `git add .`
- Confirmar los cambios: `git commit -m "Mensaje del commit"`

## Ramas (Branches)
- Crear una nueva rama: `git branch nombre_rama`
- Cambiar a una rama existente: `git checkout nombre_rama`
- Crear una nueva rama y cambiar a ella: `git checkout -b nombre_rama`
- Listar todas las ramas: `git branch`
- Eliminar una rama: `git branch -d nombre_rama`

## Sincronización Remota
- Agregar un repositorio remoto: `git remote add nombre_remoto url_repositorio`
- Listar los repositorios remotos: `git remote -v`
- Obtener cambios del repositorio remoto: `git pull nombre_remoto nombre_rama`
- Enviar cambios al repositorio remoto: `git push nombre_remoto nombre_rama`

## Historial y Diferencias
- Ver el historial de commits: `git log`
- Ver el resumen del historial de commits: `git log --oneline`
- Ver las diferencias entre commits: `git diff commit1 commit2`
- Ver las diferencias entre el área de preparación y el último commit: `git diff`

## Deshacer Cambios
- Deshacer los cambios en el área de preparación: `git restore --staged archivo(s)`
- Deshacer los cambios en un archivo modificado: `git restore archivo`
- Descartar los cambios locales y restaurar el último commit: `git checkout -- archivo(s)`

## Etiquetas (Tags)
- Crear una etiqueta ligera: `git tag nombre_etiqueta`
- Crear una etiqueta anotada: `git tag -a nombre_etiqueta -m "Mensaje de la etiqueta"`
- Listar las etiquetas: `git tag`
- Mostrar información de una etiqueta: `git show nombre_etiqueta`
- Enviar etiquetas al repositorio remoto: `git push nombre_remoto --tags`

## Otras Funciones
- Ver el estado actual del repositorio: `git status`
- Crear un archivo .gitignore: `touch .gitignore`
- Fusionar cambios de una rama a otra: `git merge nombre_rama`
- Actualizar y descargar los cambios más recientes: `git fetch`
- Crear y aplicar un parche: `git diff > archivo.patch` / `git apply archivo.patch`



