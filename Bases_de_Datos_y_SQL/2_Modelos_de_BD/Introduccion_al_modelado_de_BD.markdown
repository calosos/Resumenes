# Introducción al Modelado de Datos

## Breve Historia del Modelado de Datos

En 1948, surgió la Teoría de la Información y el Álgebra de la Información, que son un conjunto de técnicas matemáticas dedicadas al manejo de la información.

Durante la década de 1960, IBM desplegó computadoras en grandes empresas para gestionar sus datos a través de hardware. En esa misma época, nació el primer sistema para el manejo de la información conocido como MIS (Management Information System).

Charles Madman, en General Electric, lanzó el primer sistema para el manejo de bases de datos, conocido como IDS (Information Data Store). Antes de la aparición de los modelos de bases de datos, la información se almacenaba en archivos planos.

## Modelo Jerárquico

Por primera vez, se hizo posible relacionar los datos entre sí mediante estructuras jerárquicas que incluían entidades, atributos y relaciones. Aunque fue apoyado por IBM, presentaba dificultades para resolver transacciones comunes de la vida real.

Posteriormente, el Modelo de Redes permitió modelar de manera más compleja y manejar transacciones cotidianas. Sin embargo, este modelo resultaba complicado y difícil de implementar, y no fue desarrollado por IBM.

En 1969, Edgar Codd presentó el revolucionario Modelo de Bases de Datos Relacionales.

## Modelo de Archivos Planos

Aunque no se considera un modelo completo, es la base del almacenamiento de datos. No requiere un formato específico, siendo común la separación de datos mediante caracteres, como las comas en los archivos CSV. Una desventaja de estos archivos es la ausencia de metadatos dentro del archivo, lo que implica que los usuarios deben conocer las reglas para dar sentido a los datos.

Los lenguajes de marcado rodean la información con una gran cantidad de marcadores conocidos por los involucrados, estableciendo un estándar. Estos marcadores se convierten en metadatos que proporcionan información adicional sobre los datos del archivo. Los archivos de texto plano con formato son fáciles de leer, comprimir y facilitan la transferencia de datos.

## Modelo Jerárquico

Este modelo organiza los datos en una estructura jerárquica de tipo árbol invertido (tree-like structure). La raíz representa el primer nivel, las ramas los subsiguientes y las hojas el último nivel. Los nodos contienen información y se conectan mediante relaciones. Siguiendo estas relaciones, se pueden establecer caminos que representan conjuntos de relaciones entre nodos. En cualquier nivel, dos nodos relacionados se denominan Padre e Hijo, Maestro y Detalle, Antecesor y Predecesor. Nodos del mismo nivel se llaman Hermanos. Los árboles que tienen una estructura equilibrada se conocen como árboles balanceados. Este modelo permite relaciones de 1:N de la raíz a las hojas, siempre siendo relaciones de uno a uno (1 a 1), pero no permite relaciones de muchos a muchos (N:M).

La redundancia de los datos es la raíz de muchos problemas en una base de datos.

## Modelo de Redes

Este modelo permite relaciones de N:M y se basa en la teoría matemática de los grafos. Un grafo es un diagrama que representa relaciones entre pares de elementos mediante puntos y líneas. No existen restricciones sobre cómo unir un nodo con otro.

## INTEGRIDAD DE LOS DATOS

Mantener y asegurar la exactitud y consistencia durante toda la vida de los datos es crucial para garantizar la calidad y utilidad de la información almacenada.
