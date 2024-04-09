# Herencia 
---
- Es un mecanismo que permite a una clase heredar los atributos y métodos de otra clase. 
- La clase que hereda se llama **clase hija** o **subclase**, mientras que la clase de la que se hereda se llama clase padre o superclase.
## Beneficios
- **Reutilización de código:** Permite evitar la duplicación de código al heredar de una clase padre que ya implementa la funcionalidad deseada.
- **Modularidad:** Permite dividir el código en módulos independientes y reutilizables.
- **Extensibilidad:** Permite crear nuevas clases a partir de clases existentes, extendiendo su funcionalidad.
## Tipos de Herencia
- **Herencia simple:** Una clase hija hereda de una única clase padre.
- **Herencia múltiple:** Una clase hija hereda de dos o más clases padre.
- **Herencia jerárquica:** Las clases se organizan en una jerarquía de herencia.

## Implmentación
```python
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def saludar(self):
        print(f'Hola, mi nombre es: {nombre} {apellido}')

class Estudiante(Persona):
    def __init__(self, nombre, apellido, matricula):
        super().__init__(nombre, apellido,)
        self.matricula = matricula
    def estudiar(self):
        print(f'El estudiante: {nombre} {apellido} está estudiando')

# Creación de una instancia de la clase Estudiante
estudiante1 = Estudiante("Ana", "Pérez", 57473451235)
# Acceso a los métodos heredados
estudiante1.saludar()
estudiante1.estudiar()
```
## Temas adicionales de la Herencia 
- **Modificación de métodos heredados:** Puedes modificar el comportamiento de un método heredado en la clase hija.
- **Sobrecarga de métodos:** Puedes definir un método con el mismo nombre que un método heredado, pero con una firma diferente:
```python
class Persona:
    def hablar(self):
        print("Hola, soy una persona.")

class Estudiante(Persona):
    def hablar(self, idioma: str):
        print(f"Hola, soy un estudiante y hablo {idioma}.")

# Creación de una instancia de la clase Estudiante
estudiante1 = Estudiante()

# Llamada al método hablar() sin argumentos
estudiante1.hablar()

# Llamada al método hablar() con un argumento
estudiante1.hablar("español")
```
- **Super clase abstractas:** Puede definir una clase padre como abstracta, lo que significa que no se pueden crear instancias de ella.
### Características:
- **No se pueden instanciar:** No es posible crear objetos directamente de una super clase abstracta.
- **Contienen métodos abstractos:** Definen métodos que no tienen implementación y que las clases hijas deben implementar.
- **Actúan como una plantilla:** Permiten definir una estructura común para un conjunto de clases.
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    especie = "Animal"

    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")

# Creación de una instancia de la clase Perro
perro1 = Perro()

# Llamada al método hablar()
perro1.hablar()

# Creación de una instancia de la clase Gato
gato1 = Gato()

# Llamada al método hablar()
gato1.hablar()

# No se puede crear una instancia de la clase Animal
try:
    animal1 = Animal()
except TypeError as e:
    print(f"Error: {e}")

```