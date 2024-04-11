# Cheatsheet para Series en Pandas
---
- Es una herramienta fundamental para el análisis de datos en Python, ya que permite organizar, manipular y analizar conjuntos de datos complejos de manera eficiente.
- **Bidimensional:** Es similar a una hoja de cálculo de Excel, con filas y columnas.
- **Columnas:** Cada columna en un DataFrame es una Serie etiquetada con un nombre.
- **Datos heterogéneos:** Las columnas de un DataFrame pueden almacenar diferentes tipos de datos.
- **Análisis complejo:** Se utiliza para tareas de análisis de datos más complejas como relaciones entre variables, agrupaciones y operaciones matriciales.
## Características de un DataFrame
- **Columnas:** Cada columna en un DataFrame es una Serie con un nombre específico y un tipo de dato.
- **Filas:** Cada fila en un DataFrame representa un registro individual de datos.
- **Índices:** Cada fila tiene un índice único que permite acceder a ella de forma eficiente.
- **Tipo de datos:** Pandas soporta una amplia variedad de tipos de datos, como enteros, strings, fechas y valores booleanos.
## Creación de Data Frames
- `pd.DataFrame(data)`: crea un DataFrame a partir de una lista de listas, un diccionario o un array de NunPy.
- Desde una lista de lista. 
```python
datos = [['Ana', 20],['Jorge', 22],['Julia', 23]]
df = pd.DataFrame(datos, columns=['Nombre', 'Edad'])
```     
- Desde un diccionario.
```python
import pandas as pd
datos = {'Nombre':['Ana', 'Juan', 'María'],
         'Edad':[20,30,25]}
df = pd.DataFrame(datos)
``` 
- `pd.read_csv(ruta_archivo)`: Importa un DataFrame desde una archivo CSV.
- `pd.read_excel(ruta_archivo)`: Importa un DataFrame desde un archivo Excel.
## Acceso a datos:
- `df.head(numero_filas)`: Muestra por defecto las primeras 5 filas del data frame, pero se le puede pasar como parámetro una cantidad de datos a visualizar: `df.head(8)`, devuelve las primeras 8 filas.
- `df.tail(numero_filas)`: Muestra por defecto las últimas 5 filas del data frame, pero se le puede pasar como parámetro una cantidad de datos a visualizar: `df.tail(3)`, devuelve las últimas 3 filas.
- `df.info()`: Información general sobre el DataFrame.
- `df.describe()`: Muestra estadística descriptiva de las columnas numéricas del DataFrame.
- `df[columna]`: Accede a una columna por su nombre.
- `df.nombre_columna`: Regresa lo que tenga en esa columna con un índice y el dato. 
- `df.values`: Regresa todos los calores como un lista de listas.
- `df.index` da como resultado algo como: `RangeIndex(start=0, stop=4, step =1)`
- Nota como el índice es una tupla, el índice es inmutable.
- `df.columns`: Accde a los nombres de las columnas
- `'Nombres' in df.columnas`: Devuelve true si hay una columna que se llame 'Nombres' o False si no esta.
### Resumen de pd.loc y pd.iloc en Pandas
- Son métodos esenciales para acceder y modificar datos en DataFrames. 
- Ambos permiten seleccionar subconjuntos de datos.
#### **pd.loc:**
- **Selección basada etiquetas:** Permite seleccionar filas y columnas por sus nombres o etiquetas.
- **Más intuitivo:** Es más fácil de entender.
- **Más flexible:** Permite usar expresiones booleanas para filtrar datos.
- `df.loc[fila, columna]`: Accede a un elemento por su posición de fila y columna. Si solo se da el índice de la fila devuelve toda la fila.
```python
edad_ana = df.loc[2, 'Edad']
```
- `df.loc[2]`: Seleccionar la fila 2.
- `df.loc[:, 'Nombre']`: Seleccionar la columna 'Nombre'.
- `df.loc[:, ['Nombre', 'edad', 'Nacionalidad']]`: Seleccionar la columna 'Nombre', 'edad' y 'Nacionalidad'.
- `df.loc[df['Edad'] > 25]` Seleccionar las filas donde la edad es mayor a 25.
```python
edad_ana = df.loc[2]
```
- **Usar:** Para seleccionar datos por sus nombres o etiquetas, o cuando se requieran usar expresiones booleanas para filtrar.
##### Filtros
```python
is_male = df.loc[:, 'sex'] == 'Male'
df_male = df.loc[is_male]
df_male.head()
```
```python
total_up_10 = df.loc[:,'total_bill'] > 10
df_total_up_10 = df.loc[total_up_10]
df_total_up_10.head(3)
```
```python
fumador = df.loc[:,'smoker'] == 'Yes'
df_fumador = df.loc[fumador]
df_fumador.head(3)
```
#### **pd.iloc**
- **Selección basada en posición:** Permite seleccionar filas y columnas por su posición numérica.
- **Más rápido:** Puede ser más rápido que pd.loc para operaciones que no requieren filtrado.
- **Útil para bucles:** Es más adecuado para usar dentro de bucles for.
- `df.iloc[2]`: Seleccionar la fila 2.
- `df.iloc[-1]`: Seleccionar la utlima fila.
- `df.iloc[: ,1]`: Seleccion la columna 1.
- `df.iloc[: -1 ,]`: Seleccion la última columna.
- `df.iloc[-5:]`: Seleccionar las últimas 5 filas.
- `df.iloc[0:2]`: Seleccionar las filas 0 y 1.
- `df.iloc[:, 0:2]`: Seleccionar las columnas 0 y 1.
- `df.iloc[[1, 3, 5]]`: Seleccionar la fila con índice 1 3 y 5.
- `df.iloc[:, [0, 3, 2]]`: Seleccionar las columnas 0, 3 y 2.
- **Usar:** para seleccionar datos por su posición numérica,o para usar bucles para iterar sobre el DataFrame.

## Filtrado de datos
`df_filtrado = df[df['Edad'] > 25]`
## Manipulación de datos:
- `df.sort_values(columna)`: Ordena el DataFrame por una columna.
- `df.dropna()`: Elimina los valores nulos del DataFrame.
- `df.fillna(valor)`:Rellena los valores nulos del DataFrame con un valor específico-
- `df.groupby(columna)[:funcion]`: Agrupa el DataFrame por una columna y aplica una función a cada grupo.
- `df.merge(otro_df, on= columna)`: Combina dos DataFrames por una columna común.
`df['Total'] = df['Edad' + 10]` : agrega una nueva columna.
```python
nuevos_datos = [10, 25, 15, 14]
df['Nuevos_datos'] = nuevos_Satos
# Si los nuevos datos no son del mismo tamaño del índice al que se quieren agregar va a marcar error 
```
- `df.T`: Es la transpuesta de la tabla. 
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