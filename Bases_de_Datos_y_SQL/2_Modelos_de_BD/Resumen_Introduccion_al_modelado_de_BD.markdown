# Introducción al Modelado de Datos

## Breve Historia del Modelado de Datos

- En 1948, surgió la Teoría de la Información y el Álgebra de la Información, técnicas matemáticas para el manejo de datos.
- En los años 60, IBM desplegó computadoras en empresas para gestionar datos (MIS).
- Charles Madman lanzó el primer sistema de bases de datos (IDS) antes de los modelos actuales.
- Modelo Jerárquico: Relacionaba datos por estructuras jerárquicas, pero tenía limitaciones en transacciones.
- Modelo de Redes: Más complejo, manejo de transacciones, no desarrollado por IBM.
- En 1969, Edgar Codd presentó el Modelo de Bases de Datos Relacionales.

## Modelo de Archivos Planos:

- Base del almacenamiento de datos, sin formato específico, a menudo con CSV.
- Desventaja: ausencia de metadatos en el archivo.
- Lenguajes de marcado: Estándares, metadatos para información adicional.
- Archivos de texto plano con formato: Fáciles de leer, comprimir y transferir datos.

## Modelo Jerárquico:

- Organiza datos en árbol invertido.
- Nodos conectados por relaciones, caminos entre nodos.
- Permite relaciones 1:N, no muchas a muchas (N:M).
- Redundancia de datos causa problemas en bases de datos.

## Modelo de Redes:

- Permite relaciones N:M.
- Basado en teoría matemática de grafos.
- Sin restricciones para unir nodos.

## INTEGRIDAD DE LOS DATOS:

- Mantener y asegurar exactitud y consistencia en toda la vida de los datos es crucial para la calidad y utilidad de la información almacenada.
