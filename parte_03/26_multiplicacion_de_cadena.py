# Multiplicacion de cadenas 
# el operador * si se usa con una cadena crea una cantidad indicada de 
# copias de la cadena

# UTILIDADES :
# 1. separadores visuales
# 2. identacion dinamica
# 3. patrones siemples

# SINTAXIS -> "cadena" * entero 

# Ejemplo 1: separador visual 
linea = "-" * 20
print("Ej 1:")
print(linea)

# Ejemplo 2: idetacion simples -> sangria (equiv 8 espacios)
nivel = 2
sangria = "    " * nivel
print("Ej 2")
print(sangria + "|Definicion de bloque codigo")

# Ejemplo 3: patrones simple
print("Ej 3")
print("1" * 10) # "1111111111" es texto, no un numero

# Ejemplo 4: Error de tipos 
# Comentado pata eviar crash
print("ej 4")
#print("Hola" * 2.5)

""" Respuesta:
Ej 1:
--------------------
Ej 2
        |Definicion de bloque codigo
Ej 3
1111111111
ej 4
Traceback (most recent call last):
  File "/app/parte_03/26_multiplicacion_de_cadena.py", line 30, in <module>
    print("Hola" * 2.5)
          ~~~~~~~^~~~~
TypeError: can't multiply sequence by non-int of type 'float'
 """