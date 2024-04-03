# SENTENCIAS CONDICIONALES	
---  

**Sentencias condicionales:** Sección del código que dirigen el programa en función de determinadas condiciones.  
- Permite comparar valores 
- Cuando se realizan comparaciones el resultado es un bool.
- Cuando se compara operadores como el siguiente `>`:
```python
print(1 > '1' )
```
El resultado es un type error.  
- Cuando se compara con el operador de `==`: 

```python
print(1 == '1' )
```
El resultado es `False`


*EJEMPLO*
```python
num = 4
if num > 0:
    print(‘El número es positivo’)
elif num != 10000:
    pass
elif num == 0:
    print(‘El número es cero’)
else:
    print(‘El número es negativo’)
```
