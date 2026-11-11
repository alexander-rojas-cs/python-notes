""" conversion de tipo de dato en python 

Hearramientas de python
- int () -> convierte un texto a entero
- float () -> convierte un texto o entero a decimal
- str () -> convierte cualquier tipo de dato a texto
"""

# ejemplo 1 operacion de suma variables
numero_txt= "55"

total = int(numero_txt) + 10
print(f"el total es: {total}")

# ejemplo 2 concatenacion de texto
contaneacion = numero_txt + str(10)
print(f"el total es: {contaneacion}")

""" respuesta 
el total es: 65
el total es: 5510
"""