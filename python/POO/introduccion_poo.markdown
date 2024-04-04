# INTRODUCCIÓN PROGRAMACIÓN ORIENTADA A OBJETOS
---
- **Programación Orientada a Objetos:** Una forma de pensamiento acerca de como implementar el código.

## Conceptos principales
- **`self`**: Parámetro que representa la instancia sobre la cual se  esta ejecutando el método. Permite acceder a los atributos
de la instancia utilizando la notación de punto, `self.nombre`, que accederá al atributo nombre de esa instancia especifica del objeto de la clase.  
- **Variables de instancia**: Son variables que contienen diferentes valores para diferentes instancias. Van en el init
```py
class Estudiante:
    def __init__(self, nombre, apellido, curso):
        self.nombre=nombre
        self.apellido=apellido
    self.curso=curso
```
- **Variables de clase**: van fuera de las funciones. Es igual para todas las instancias, se podría tomar como un valor por defecto.
```py
class Estudiante:
    horas_por_semana=36
```
**Ejemplo de acceso a las variables de instancia y variables de clase**
```py
class Estudiante:
    
    horas_por_semana=36
    
    def __init__(self, nombre, apellido, curso):
        self.nombre=nombre
        self.apellido=apellido
        self.curso=curso
    def resumen(self):
        return print('Resumen:\n Nombre:{}\n Apellido:{}\n Curso:{}\n Horas por semana:{}'
                     .format(self.nombre,self.apellido,self.curso,Estudiante.horas_por_semana))
```

**Modificar una variable de clase desde las variables de instancia:**
```py
class Estudiante:
    horas_por_semana=36
    numero_estudiantes=0 
    def __init__(self, nombre, apellido, curso):
        self.nombre=nombre
        self.apellido=apellido
        self.curso=curso
        Estudiante.numero_estudiantes+=1
    def resumen(self):
        return print('Resumen:\n Nombre:{}\n Apellido:{}\n Curso:{}\n Horas por semana:{}'
                     .format(self.nombre,self.apellido,self.curso,self.horas_por_semana))
```
- Cada que se cree una instancia el número de estudiantes se le va aumentar 1.  

**LLamando las variables de clase con self**
```py
class Estudiante:
    
    horas_por_semana=36
    
    def __init__(self, nombre, apellido, curso):
        self.nombre=nombre
        self.apellido=apellido
        self.curso=curso
    def resumen(self):
        return print('Resumen:\n Nombre:{}\n Apellido:{}\n Curso:{}\n Horas por semana:{}'
                     .format(self.nombre,self.apellido,self.curso,self.horas_por_semana))
```
*Nota*
A las variables de clase también se le pueden llamar con el self.
**Atributos:** Cualidades que tiene la clase, como el color, etc.
### **Clases:** 
- Son una herramienta fundamental para la POO. 
- Permite crear objetos que encapsulas datos y comportamientos, lo que hace que el código sea más modular y reutilizable.
#### **Ventajas de las clases / Pilares de la POO:**
- **Modularidad:** Permiten dividir el código en módulos independientes.
- **Reutilización:** Permiten reutilizar código en diferentes programas.
- **Encapsulamiento:** Permiten ocultar la implementación de los detalles de un objeto.
- **Herencia:** Permiten crear nuevas clases a partir de clases existentes.
#### **Ejemplos de problemas que se pueden resolver con clases:**
- Simulación de objetos del mundo real (personas, animales, coches, etc.).
- Desarrollo de interfaces gráficas de usuario (GUI).
- Implementación de algoritmos complejos.  

**EJEMPLO DE CLASE**
```python
class Persona:
    # Atributo de la clase
    especie = 'Homo sapiens'

    def __init__(self, nombre, edad, apellido):
        # Atributos de instancia: nombre y edad
        self.nombre = nombre  # Atributo 'nombre'
        self.edad = edad      # Atributo 'edad'

    def mostrar_informacion(self):
        # Método de instancias para mostrar información
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def set_edad(self, edad):
        self.edad = edad

    def get_edad(self)
        return self.edad 
    
    def saludar(self):
        # Método de la clase 
        print(f'Hola mi nombre es {self.nombre} {self.apellido}.')
    
    def cumplir_anios(self):
        self.edad += 1

# Crear instancias de la clase Persona
persona1 = Persona("Juan", 25)   # Instancia con nombre "Juan" y edad 25
persona2 = Persona("Maria", 30)  # Instancia con nombre "Maria" y edad 30

# Llamar al método de instancia para mostrar información
persona1.mostrar_informacion()   # Muestra información de persona1
persona2.mostrar_informacion()   # Muestra información de persona2

# Acceso a los atributos
print(f"Nombre: {persona1.nombre}")
print(f"Apellido: {persona1.apellido}")
print(f"Edad: {persona1.edad}")

# Llamada a los métodos
persona1.saludar()
persona1.cumplir_anios()
print(f"Edad después de cumplir años: {persona1.edad}")

```
**Explicación:**
- La clase Persona define dos atributos de clase: especie y `__init__`.
- El método `__init__` se llama al crear una nueva instancia de la clase y se utiliza para inicializar los atributos de la instancia.
- La clase Persona define 3 métodos: saludar(), cumplir_anios() mostrar_informacion().
- Los métodos de la clase pueden acceder y modificar los atributos de la instancia.  

### **Métodos:**
- Son comportamientos asociados a los parámetros de un objeto que modifica su estado. 
- Son las acciones que puede realizar la clase.
- En python se implementan con la sintaxis de las funciones y pertenecen a una instancia específica de una clase. Esto es llamar a un método de la clase.   
Los métodos tienen varias categorías:
#### **Métodos de instancia:** 
- Son el tipo más común de métodos en Python. Se definen dentro de una clase creando  funciones dentro de la definición de la clase. 
- Cuando instancias objetos de una clase, esas instancias individuales pueden tener sus métodos  lo que permite que el programa controle y modifique esos objetos directamente.
- Pueden tomar un parámetro llamado `self`.

#### **Métodos de clase:** 
- Se llaman para la propia clase en lugar de ser para una instancia específica.
- Están marcados con un decorador `@classmethod`y toman un parámetro `cls` que apunta a la clase, y no a una instancia específica, cuando se llama al método. 
- Un caso de uso común es crear y modificar estructuras de datos que contienen registros para todas las instancias de una clase. 
- Por lo general, los programadores crean un lista dentro de la definición de la clase, y métodos para agregar instancias de clase a esa lista con el fin de realizar  un seguimiento de esa clase.

```python
class Empleado:
    empleados = []  # Lista para realizar un seguimiento de todas las instancias de Empleado

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.empleados.append(self)  # Agregar esta instancia a la lista de empleados

    @classmethod
    def mostrar_empleados(cls):
        print("Lista de empleados:")
        for empleado in cls.empleados:
            print(f"Nombre: {empleado.nombre}, Salario: {empleado.salario}")

# Crear instancias de la clase Empleado
empleado1 = Empleado("Juan", 50000)
empleado2 = Empleado("Maria", 60000)

# Llamar al método de clase para mostrar la lista de empleados
Empleado.mostrar_empleados()

```
```python
class Producto:
    productos_por_categoria = {}  # Diccionario para realizar un seguimiento de productos por categoría

    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.registrar_producto()

    def registrar_producto(self):
        if self.categoria not in Producto.productos_por_categoria:
            Producto.productos_por_categoria[self.categoria] = []
        Producto.productos_por_categoria[self.categoria].append(self)

    @classmethod
    def mostrar_productos_por_categoria(cls):
        print("Lista de productos por categoría:")
        for categoria, productos in cls.productos_por_categoria.items():
            print(f"Categoría: {categoria}")
            for producto in productos:
                print(f"   Nombre: {producto.nombre}, Precio: {producto.precio}")

# Crear instancias de la clase Producto con diferentes categorías
producto1 = Producto("Laptop", 1200, "Electrónica")
producto2 = Producto("Camiseta", 20, "Ropa")
producto3 = Producto("Teléfono", 800, "Electrónica")
producto4 = Producto("Zapatos", 50, "Ropa")

# Llamar al método de clase para mostrar la lista de productos por categoría
Producto.mostrar_productos_por_categoria()
```
#### **Métodos estáticos:** 
- Son marcados por el decorador `@staticmethod`, no toma un parámetro `self` o `cls`. 
- Se comportan como funciones simples, excepto que puedes llamarlos directamente desde la clase. 
- No se necesita instanciar la clase para llamar a estos métodos; los métodos simplemente residen en la clase. Esto se debe a que las definiciones de clase son en sí mismas un objeto (ed decir, una instancia de una base abstracta), lo que reduce la sobrecarga y permite encapsular funciones de manera fácil y accesible. 
- Se usan cuando no necesita acceder a ningún dato específico de la instancia o de la clase.

**EJEMPLO**
```python
class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

# Llamar a métodos estáticos directamente desde la clase, sin instanciar
resultado_suma = Calculadora.sumar(5, 3)
resultado_resta = Calculadora.restar(10, 4)

print(f"Resultado de la suma: {resultado_suma}")
print(f"Resultado de la resta: {resultado_resta}")

```
**EJEMPLO 2:**
```py
class FileManager:
    allowed_extensions = ['.txt', '.csv', '.pdf', '.docx']

    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def is_valid_extension(filename):
        # Obtener la extensión del archivo
        _, file_extension = filename.rsplit('.', 1) if '.' in filename else (None, None)
        # Verificar si la extensión está en la lista de extensiones permitidas
        return file_extension.lower() in FileManager.allowed_extensions

# Crear instancias de la clase FileManager
file1 = FileManager("documento.txt")
file2 = FileManager("imagen.jpg")

# Usar el método estático para verificar extensiones válidas
result1 = FileManager.is_valid_extension(file1.filename)
result2 = FileManager.is_valid_extension(file2.filename)

# Imprimir resultados
print(f"¿'{file1.filename}' tiene una extensión válida?: {result1}")
print(f"¿'{file2.filename}' tiene una extensión válida?: {result2}")

```
#### **Eligiendo un tipo de método**
El tipo de método que elijas usar, ya sea instancia, clase o estático, depende de qué datos necesita acceder el método.
- Los métodos de instancia son para datos individuales de objetos.
- Los métodos de clase son para datos compartidos.
- Los métodos estáticos son para tareas relacionadas que no necesitan acceder o modificar datos de objetos o clases.
#### **Puntos clave a tener en cuenta**
- Recuerda, en Python, los métodos son una forma de agrupar comportamientos con objetos, permitiéndote interactuar y modificar el estado de esos objetos. Sin embargo, los métodos estáticos ofrecen una manera de agrupar funciones juntas, para ser utilizadas en general en cualquier otro tipo de objeto. Agrupar funciones de esta manera ayuda a organizarlas de manera limpia y las empaqueta para su reutilización en otros proyectos de codificación.

**EJEMPLO 1:**
```py
class Calculadora:
    # Método de instancia
    def sumar(self, a, b):
        return a + b

    # Método de clase
    @classmethod
    def multiplicar(cls, a, b):
        return a * b

    # Método estático
    @staticmethod
    def calcular_promedio(lista):
        return sum(lista) / len(lista)

# Uso de los métodos en una instancia de la clase Calculadora
calc = Calculadora()

# Método de instancia
resultado_suma = calc.sumar(5, 3)

# Método de clase
resultado_multiplicacion = Calculadora.multiplicar(4, 6)

# Método estático
lista_numeros = [2, 4, 6, 8, 10]
resultado_promedio = Calculadora.calcular_promedio(lista_numeros)

# Imprimir resultados
print(f"Resultado de la suma: {resultado_suma}")
print(f"Resultado de la multiplicación: {resultado_multiplicacion}")
print(f"Promedio de la lista: {resultado_promedio}")

```
**EJEMPLO 2**
```py
class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def calcular_salario_total(self):
        return sum(empleado.salario for empleado in self.empleados)

    @classmethod
    def mostrar_departamento_con_mas_empleados(cls):
        max_empleados = max(cls.departamentos, key=lambda dept: len(dept.empleados))
        return max_empleados.nombre

    @staticmethod
    def verificar_edad_valida(edad):
        return 18 <= edad <= 65

class Empleado:
    departamentos = []

    def __init__(self, nombre, edad, salario, departamento):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.departamento = departamento
        departamento.agregar_empleado(self)

    @staticmethod
    def calcular_aumento_salarial(salario_actual, porcentaje_aumento):
        return salario_actual * (1 + porcentaje_aumento / 100)

# Crear instancias de la clase Departamento
departamento1 = Departamento("Desarrollo")
departamento2 = Departamento("Ventas")

# Crear instancias de la clase Empleado
empleado1 = Empleado("Juan", 30, 50000, departamento1)
empleado2 = Empleado("Maria", 25, 60000, departamento1)
empleado3 = Empleado("Carlos", 35, 55000, departamento2)

# Llamar a métodos de instancia y estáticos
salario_total_desarrollo = departamento1.calcular_salario_total()
aumento_nuevo_salario = Empleado.calcular_aumento_salarial(empleado1.salario, 10)
edad_valida = Departamento.verificar_edad_valida(empleado2.edad)

# Imprimir resultados
print(f"Salario total del departamento de Desarrollo: {salario_total_desarrollo}")
print(f"Nuevo salario después del aumento: {aumento_nuevo_salario}")
print(f"¿La edad es válida?: {edad_valida}")

# Llamar al método de clase para mostrar el departamento con más empleados
departamento_con_mas_empleados = Departamento.mostrar_departamento_con_mas_empleados()
print(f"Departamento con más empleados: {departamento_con_mas_empleados}")

```