# Cheatsheet para Series en Pandas
---
- Es una herramienta fundamental para el análisis de datos en Python, ya que permite organizar, manipular y analizar conjuntos de datos complejos de manera eficiente.
- **Bidimensional:** Es similar a una hoja de cálculo de Excel, con filas y columnas.
- **Columnas:** Cada columna en un DataFrame es una Serie etiquetada con un nombre.
- **Datos heterogéneos:** Las columnas de un DataFrame pueden almacenar diferentes tipos de datos.
- **Análisis complejo:** Se utiliza para tareas de análisis de datos más complejas como relaciones entre variables, agrupaciones y operaciones matriciales.
# Ultima consulta de Gemini 
## Creación de Data Frames
- `pd.DataFrame(data)`: crea un DataFrame a partir de una lista de listas, un diccionario o un arry de NunPy.
- `pd.read_csv(ruta_archivo)`: Importa un DataFrame desde una archivo CSV.
- `pd.read_excel(ruta_archivo)`: Importa un DataFrame desde un archivo Excel.
## Acceso a datos:
- `df.head(numero_filas)`: Muestra por defecto las primeras 5 filas del data frame, pero se le puede pasar como parámetro una cantidad de datos a visualizar: `df.head(8)`, devuelve las primeras 8 filas.
- `df.tail(numero_filas)`: Muestra por defecto las últimas 5 filas del data frame, pero se le puede pasar como parámetro una cantidad de datos a visualizar: `df.tail(3)`, devuelve las últimas 3 filas.
- `df.info()`: Información general sobre el DataFrame.
- `df.describe()`: Muestra estadística descriptiva de las columnas numéricas del DataFrame.
- `df[columna]`: Accede a una columna por su nombre.
- `df.loc[fila, columna]`: Accede a un elemento por su posición de fila y columna.
## Manipulación de datos:
- `df.sort_values(columna)`: Ordena el DataFrame por una columna.
- `df.dropna()`: Elimina los valores nulos del DataFrame.
- `df.fillna(valor)`:Rellena los valores nulos del DataFrame con un valor específico-
- `df.groupby(columna)[:funcion]`: Agrupa el DataFrame por una columna y aplica una función a cada grupo.
- `df.merge(otro_df, on= columna)`: Combina dos DataFrames por una columna común.
## Operaciones matemáticas
- `df + df2`: Suma dos DataFrames con las mismas dimensiones.
- `df * df2`: Multiplica dos DataFrames con las mismas dimensiones.
- `df.mean()`: Calcula la media de las columnas numéricas del DataFrame.
- `df.sum()`: Calcula la suma de las columnas numéricas del DataFrame.
## Visualización
- `df.plot()`: Muestra un gráfico simple del DataFrame.
- `df.hist()`: Muestra un histograma de las columnas numéricas del DataFrame.
- `df.boxplot()`: Muestra un diagrama de caja de las columnas numéricas del DataFrame.
```python
#Creación de un DataFrame
import pandas as pd
df = pd.DataFrame({
        'Nombre': ['Ana', 'Juan', 'María'],
        'Edad': [20, 30, 40]
})

# Acceso a datos
print(df.head())
print(df['Nombre'])
print(df.loc[1, 'Edad'])

# Manipulación de datos
df.sort_values('Edad', inplace=True)
df.dropna(inplace=True)
df.fillna('Desconocido', inplace=True)

# Operaciones matemáticas
df['Total'] = df['Edad'] + 10

# Visualización
df.plot()
df.hist()

```