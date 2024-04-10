# Cheatsheet para Series en Pandas
---
- **Unidimensional:** Es una estructura similar a una lista de Python, pero con la capacidad de almacenar datos etiquetados por un índice.
- **Índices:** Cada elemento de la Serie tiene un índice único que permite acceder a él de forma eficiente.
- **Datos homogéneos:** La Serie almacena un único tipo de datos (enteros, strings, etc.) en todos sus elementos.
- **Análisis básico:** Se utiliza para tareas de análisis de datos básicas como cálculo de medias, varianzas, filtrado y ordenamiento.
- Son similares a las listas en Python, pero ofrecen funcionalidades adicionales para el análisis de datos.

## Llamada a la librería
`import pandas as pd` 

## Creación de Series
- `pd.Series(data)`: crear una Serie a partir de una lista, un diccionario o un array de NumPy.
- `pd.Series(index=index, data=data)`: Crea una Serie con un índice personalizado.
```py
nombres = ['Juan', 'Mario', 'Pablo', 'José']
edades = [20, 21, 19, 22]
serie = pd.Series(data=edades, index=nombres)
```
```py
# con diccionario
personas = {'Juan':20, 'Mario':21, 'Pablo':19, 'José':22}

serie = pd.Series(personas)
nuevas_llaves = ['Juan', 'Mario', 'Pablo', 'José', 'Julio']
serie = pd.Series(personas, index=nuevas_llaves)
# En este caso Julio va a tener el valor NaN
```
## Acceso a datos
- Acceder a los elementos de una Serie por su posición o por su índice.
    - `serie[0]`: Accede al primer elemento de la Serie.
    - `serie.iloc[0]`: Accede al elemento con el índice de ubicación'.
    - `serie['valor']`: Accede al elemento con el índice `'valor'`. 
    - `serie.loc['valor']`: Accede al elemento con el índice `'valor'`.
 - Información del índice
    - `serie.index` da como resultado algo como: `RangeIndex(start=0, stop=4, step =1)`
- Validar que existe un dato en una Serie.
    - `elemento in serie`
- Validar null en la lista.
    - `pd.isnull(serie)`: Devuelve el índice y el valor, si el valor es NaN va a devolver el índice y true en lugar del valor.
    ```py
    personas = {'Juan':20, 'Mario':21, 'Pablo':19, 'José':22}
    nuevas_llaves = ['Juan', 'Mario', 'Pablo', 'José', 'Julio']
    serie = pd.Series(personas, index=nuevas_llaves)
    # resultado en pantalla
    # Juan False
    # Mario False
    # Pablo False
    # Jose  True
    ```
- Validar los que no son null en la lista.
    - `pd.notnull(serie)`: Devuelve el índice y el valor, si el valor es NaN va a devolver el índice y False en lugar del valor.
    ```py
    personas = {'Juan':20, 'Mario':21, 'Pablo':19, 'José':22}
    nuevas_llaves = ['Juan', 'Mario', 'Pablo', 'José', 'Julio']
    serie = pd.Series(personas, index=nuevas_llaves)
    # resultado en pantalla
    # Juan True
    # Mario True
    # Pablo True
    # Jose  False
    ```
    
### Manejo de elementos que no existen
```python
try:
    elemento_no_existe = serie['valor']
    print(elemento_no_existe)
except KeyError:
    print("El índice 'valor' no existe")
```
- Los métodos `head()`y `tail()` para mostrar las primeras o últimas filas de una serie, por defecto muestran 5 resultados.
    - `primeras_filas = serie.head(2)`: Mostrar las primeras dos filas.
    - `ultimas_filas = serie.tail(2)`: Mostrar las primeras dos filas.

## Manipulación de datos:
- Ordenar, filtrar y eliminar valores de una Serie.
    - `serie.sort_values()`: Ordena la Serie por sus valores.
    - `serie.dropna()`: Elimina los valores nulos de la Serie.
- Realizar operaciones matemáticas con las  Series:
    - `serie + 1`: Suma 1 a cada elemento de la Serie.
    - `serie * 2`: Multiplica cada elemento de la Serie por 2.
    - `serie / 3`: Divide cada elemento de la Serie por 3.
- Agregar nuevas columnas a una Serie.
- Eliminar valores específicos
    - `serie_sin_20 = serie.drop(1)`: elimina por el índice.
## Funciones estadísticas:
- `serie.mean()`: Calcula la media de la Serie.
- `serie.meadian()`: Calcula la mediana de la Serie.
- `serie.std()`: Calcula la desviación estándar de la Serie.
- `serie.max()`: Calcula el valor máximo de la Serie.
- `serie.min()`: Calcula el valor máximo de la Serie.
## Filtrado
- `serie[serie > 0]`: Filtra la Serie para obtener solo los valores mayores que 0.
- `serie[serie.isin(['a','b'])]`: Filtra la Serie para obtener solo los valores 'a' y 'b'.
## Concatenación
- `pd.concat([serie1, serie2])`: Concatena dos Series.
## Agrupación
- `serie.groupby(column).mean()`: Calcula la media de la Serie agrupada por la columna 'column'.
## Visualización:
- Crear gráficos de la serie para visualizar los datos.
    - `serie.plot()`: Muestra un gráfico de la Serie.
## Ejemplos de uso
- Almacenar una lista de nombres.
- Almacenar los valores de una columna de una hoja de cálculo.
- Calcular la media de un conjunto de datos.
- Filtrar un conjunto de datos para obtener solo los valores que cumplen una condición.
- Visualizar la distribución de un conjunto de datos.
## Ventajas de usar Series
- Son eficientes para almacenar y manipular datos.
- Ofrecen una amplia gama de funcionalidades para el análisis de datos.
- Son fáciles de usar y aprender.
## Documentación
[Documentación Oficial Pandas - Series](https://pandas.pydata.org/pandas-docs/stable/reference/index.html#)
