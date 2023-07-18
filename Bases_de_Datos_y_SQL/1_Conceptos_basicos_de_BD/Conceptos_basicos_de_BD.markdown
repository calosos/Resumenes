# Conceptos básicos de Bases de datos

**Datos**: Del latín "datum", significa lo que se da. Es la representación simbólica de un atributo o variable cuantitativa o cualitativa. Puede ser números, figuras, letras, etc. Representa una entidad, un hecho o un momento de la vida real. Sin embargo, un dato por sí solo no tiene ningún sentido y no genera información, sino que requiere un contexto para ser interpretado.

**Dato cuantitativo**: Son datos que representan cantidades o cualidades de las cosas, como 1 metro, 4 años, 3 kilos, etc.

**Dato cualitativo**: Describe cómo es el dato, por ejemplo, redondo, dulce, colorido, etc.

**Metadatos**: Son información adicional que proporciona detalles sobre otros datos. Son "datos sobre datos".

**Metadatos descriptivos**: Son datos que describen al dato en sí mismo y proporcionan información sobre su contenido. Ayudan a comprender y categorizar los datos.

Ejemplo:
Para el campo "Nombre" en la tabla "Clientes", el metadato descriptivo podría ser:

- **Nombre**: "Nombre"
- **Descripción**: Nombre del cliente.
- **Tipo de dato**: Cadena de caracteres.
- **Longitud máxima**: 50 caracteres.

Este metadato descriptivo proporciona información sobre el contenido del campo "Nombre", indicando que se espera que almacene el nombre del cliente y que tiene una longitud máxima de 50 caracteres.

**Metadatos estructurales**: Son datos que describen la estructura o formato en el que se almacenan los datos, como la organización de tablas, columnas y relaciones.

Ejemplo:
Para la tabla "Clientes", los metadatos estructurales podrían ser:

- **Tabla**: "Clientes"
- **Descripción**: Almacena información de los clientes de la empresa.
- **Columnas**:
  - **"ID"**:
    - **Tipo de dato**: Entero.
    - **Longitud**: 10 dígitos.
    - **Clave primaria**.
  - **"Nombre"**:
    - **Tipo de dato**: Cadena de caracteres.
    - **Longitud máxima**: 50 caracteres.
  - **"Apellido"**:
    - **Tipo de dato**: Cadena de caracteres.
    - **Longitud máxima**: 50 caracteres.
  - **"Correo electrónico"**:
    - **Tipo de dato**: Cadena de caracteres.
    - **Longitud máxima**: 100 caracteres.
  - **"Teléfono"**:
    - **Tipo de dato**: Cadena de caracteres.
    - **Longitud máxima**: 15 caracteres.

Estos metadatos estructurales describen la tabla "Clientes" y sus columnas, incluyendo los nombres de las columnas, los tipos de datos y las longitudes máximas permitidas para cada campo. También se indica que la columna "ID" es la clave primaria de la tabla.

**Información**:

**Entidad**: Se refiere a un objeto o concepto que se representa en una base de datos. Se representa como una tabla en una base de datos relacional. Cada fila representa una instancia o entidad específica, y cada columna representa un atributo o propiedad de la entidad.

**Relación**: Es una asociación entre dos o más entidades. Representa una conexión lógica o dependencia entre las entidades. Se definen mediante claves primarias y claves foráneas.

**Instancia**: Un único ejemplar de una entidad o un conjunto completo de datos en un momento específico. Es decir, una fila o registro individual en una tabla.

**Atributo o Propiedad**: Una pieza de información que describe una entidad o una instancia en una tabla. Cada columna representa un atributo de la entidad.

**Base de Datos**: Un conjunto de datos o una colección de información organizada de manera que sea fácil de acceder, gestionar y actualizar. Los datos pertenecen a un mismo contexto y se pueden clasificar según su organización, sus tipos de datos, su finalidad, su tamaño, su tasa de cambio de datos, su ámbito o alcance, y otros criterios.

SQL no es una base de datos, sino un lenguaje de consulta estructurado utilizado para comunicarse con las bases de datos y realizar operaciones en ellas.

Una base de datos no es un software.

**Modelo de Datos**: Es un lenguaje de modelado que define la estructura y las relaciones de los datos en una base de datos. Proporciona una representación abstracta de cómo interactúan los datos entre sí y cómo se relacionan. Un modelo de datos es una estructura abstracta que documenta y organiza los elementos de información, estandarizando cómo se relacionan entre sí y con las propiedades de las entidades del mundo real. Determina explícitamente la estructura de los datos y proporciona reglas claras y no ambiguas. Además, es independiente de los dispositivos, estable, flexible y reutilizable.

Un modelo de datos:

- Define un lenguaje común.
- Identifica entidades (sustantivos).
- Establece reglas del negocio.

**Cardinalidad**: Se refiere al número de elementos en un conjunto de datos. Indica cuántos elementos puede tener un conjunto en particular.
