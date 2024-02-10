# OPERADORES EN PYTHON
---  
**Operadores:** Símbolos para realizar operaciones en objetos y valores.  

## Operadores Matemáticos
---
**`x + y`:** Operador de suma retorna la suma de x más y.
**`x - y`:** Operador de resta retorna la resta de x menos y.
**`x*y:`** Operador de multiplicación.
**`x/y:`** Operador de división.
**`x**e:`** El operador ** de potencia, en este caso x elevado a la e.
**`x**2:`** El operador ** de potencia, en este caso x elevado a cuadrado.
**`x**3:`** El operador ** de potencia, en este caso x elevado al cuadrado.
**`x**(1/2):`** De esta forma se realza el cálculo de la raíz cuadrada.
**`x//y:`** Regresa la parte entero del resultado.
**`x%y:`** Operador modulo retorna el residuo de la división. 

## Operadores Relacionales   
---
Los siguientes operadores son usados para los int y flotantes las comparaciones van a regresar un bool (`True` o `False`).  
**`==`:** Operador de comparación de igualdad.
**`!=`:** Operador que compara que haya desigualdad.  
**`>`:** Mayor que.  
**`<`:** Menor que.
**`>=`:** Mayor o igual que.  
**`<=`:** Menor o igual que.  

## Operador de Asignación
---
**`=`:** Operador que permite la asignación de un objeto a variables.
**`+=`:** Operador de asignación incrementada. Agrega el valor del operando del lado derecho al operando del lado izquierdo. 
```python
x = 5
x +=3 # Ahora, x es igual a 8
x = x + 3 # Es la misma expresión de la anterior
```
**`-=`:** Operador de asignación decrementada. Resta el valor del operando del lado derecho al operando del lado izquierdo.
```python
x = 5
x -= 3 # Ahora, x es igual a 2
x = x - 3 # Es la misma expresión de la anterior
```
**`*=`:** Operador de asignación multiplicativa. Multiplica el operando del lado izquierdo por el valor del operando del lado derecho.
```python
x = 5
x *= 3 # Ahora, x es igual a 6
x = x * 3 # Es la misma expresión de la anterior
```
**`/=`:** Operador de asignación divisiva. Divide el operando del lado izquierdo por el valor del operando del lado derecho.
```python
x = 10
x /=2 # Ahora, x es igual a 5
x = x / 2 # Es la misma expresión de la anterior
```
**`%=`:** Operador de asignación modular. Asigna al operando del lado izquierdo el resultado del módulo entre el operando del lado izquierdo y el operando del lado derecho.
```python
x = 10
x %=3 # Ahora, x es igual a 1
x = x / 3 # Es la misma expresión de la anterior
```
**`**=`:** Operador de asignación exponencial. Eleva el operando del lado izquierdo a la potencia del operando del lado derecho y asigna el resultado al operando del lado izquierdo.
```python
x = 2
x **=3 # Ahora, x es igual a 8
x = x ** 3 # Es la misma expresión de la anterior
```
**`//=`:** Operador de asignación de división entera. Realiza la división entera entre el operando del lado izquierdo y el operando del lado derecho, y asigna el resultado al operando del lado izquierdo.
```python
x = 12
x //=5 # Ahora, x es igual a 2
x = x // 3 # Es la misma expresión de la anterior
```

## Operadores Lógicos
---
**`and`**: para evaluar como verdadero este operador necesita que ambas expresiones sean verdaderas al mismo tiempo.  
**`or`:** el resultado de la comparación será verdadero cuando alguna de las dos sea verdadera o falso solo cunado las expresiones sean ambas falsas.  
**`not`**:  es el valor contrario a la expresión que lleve  después de este operador.

## Operadores  de Pertenencia
---
`in` y `not in` son operadores de pertenencia.  
El operador `in` devuelve `True` si el valor que mencionas está presente en el iterable que se esta revisando. Por otro lado, `not in` devuelve `True` si el valor no está presente en el iterable. En resumen, in verifica si está adentro, y not in verifica si no está adentro. Ambos devuelven `True` o `False` según el caso.  
**Ejemplo con `in`**
```python
# Lista de frutas
frutas = ['manzana', 'plátano', 'uva', 'naranja']
# Verificar si 'uva' está en la lista de frutas
resultado = 'uva' in frutas
# Imprimir el resultado
print(resultado)  # Devolverá True, ya que 'uva' está en la lista de frutas
```
**Ejemplo con `not in`**
```python
# Lista de colores
colores = ['rojo', 'azul', 'verde', 'amarillo']
# Verificar si 'negro' no está en la lista de colores
resultado = 'negro' not in colores
# Imprimir el resultado
print(resultado)  # Devolverá True, ya que 'negro' no está en la lista de colores
```

## Orden de las operaciones
---
Las operaciones se deben calcular de izquierda a derecha siguiendo el siguiente orden:

**Paréntesis:**  `( )`, `{ }`, `[ ]`
**Exponentes:** `x^e`, `(x**e)`
**Multiplicación:** `*` 
**División:** `/`
**Suma:** `+` 
**Resta:** `-`
Puede resultar útil recordar este orden utilizando el dispositivo mnemotécnico **`PEMDAS`**.