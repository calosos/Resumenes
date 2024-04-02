# Fases de Power BI
- **GD (Get Data)**
- **DP (Data Preparation)**
- **DM (Data Modeling)**
- **DV(Data Visualization)**
- **DR(Data Reporting)**
## **GD(Get Data)** 
Obtener datos de tablas de Excel, pdf´s, bases de datos, fuentes web, servicios en línea, etc.
**Fuentes de datos:** Cualquier ruta o destino que cuente con registros provenientes de documentos o archivos digitales.  

Cuando las fuentes  cuenten con elementos que no deseamos importar o que tienen inconsistencias que requieren modificaciones será necesario avanzar a la fase de **DP**.  
**Actualizar Datos:** Debido a que PBI está conectado a fuente de datos, al estar alimentado estas fuentes con nuevos registros, puede actualizarse y mostrar esos datos nuevos en el reporte.
### Consideraciones:
- Cambiar la estructura de las fuentes de datos puede afectar en el proceso de **GD**, también cambiar el nombre del archivo o modificaciones a la ruta dónde se encuentren los datos.
- Asignar nombres consistentes y que no vayan  a ser cambiados por el paso del tiempo, como el nombre  de tablas, nombre de archivos, carpetas, rutas, modelos de datos, etc. Para prevenir problemas futuros por este tipo de cambios.


## **DP(Data Preparation)** 
Preparación de los datos obtenidos, limpiar y organizar en query Editor.  
El **Query Editor** o Editor de consultas, es donde se hacer los ajustes correspondientes a las tablas y sus registros para que PBI los reconozca y posteriormente ser utilizados en el reporte. Es para mayormente utilizado para corrección y limpieza de datos. *No para realizar cálculos u operaciones.*
Para abrir el Query Editor, click en `Transform data` desde Home. 
![Transform data](media/imagenes/Transforma_data.png)
Un nuevo apartado aparecerá en otra ventana de PBI:
![Query Editor](media/imagenes/query_editor_vista.png)

**Tipos de datos:** Es importante revisar que cada campo cuente con el tipo de dato que corresponde. Por lo general PBI los asigna en automático, pero en ocasiones pueden no ser el tipo correcto.  
**Pasos aplicados:**
Cada corrección o ajuste realizado queda "grabado" en u paso el Query Editor, y cada uno de estos pasos son realizados en el mismo orden cuando se actualice el reporte.
nuevos registros en fuentes de datos -> click en actualizar -> Se aplican pasos grabados -> Nuevos datos con la estructura esperada.  

En el Query Editor se pueden hacer modificaciones a las tablas de diferentes formas, y ese usan la  3 pestañas principales de la barra de herramientas:  
![Query Editor](media/imagenes/pestanias_query_editor.png)
**Home:** Pestaña principal donde se pueden realizar ajustes y transformaciones generales como modificar fuentes de datos, remover columnas o filas, combinar tablas.  
**Transform:** Los ajustes realizados desde esta pestaña se reflejan para las columnas seleccionadas como reemplazar valores, extraer caracteres, pivot/un-pivot, etc.  
**Add Column:** Se agregan nuevas columnas por lo general con referencia a los datos de otra columna.

### Notas
El Query Editor modifica la estructura a ser utilizada en Power Bi, pero no afecta en lo absoluto a la estructura o registro de las fuentes de los datos. PBI solo se conecta a las fuentes de datos y no provocará ningún cambio en la fuente de datos.
## **DM(Data Modeling)** 
Modelado de datos, crear estructuras o modelos que permitan relacionar datos.  
## **DV(Data Visualization)**
Visualización de datos, la representación de los datos en forma de gráficos, matrices y más visualizaciones.  
## **DR(Data Reporting)** 
Reporte de datos, estructura y formato de visualizaciones y elementos que darán lugar al reporte.
## Notas
- Puede haber proyectos donde no todas las fases sean necesarias. Como una tabla previamente estructurada adecuadamente no requiere **DP** ni **DM**.
- Las fases no son secuenciales, son iterativas. En cada reporte que realicemos vamos a ester pasando de una fase a otra, sin importar la frecuencia de uso u orden.
