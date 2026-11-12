""" Sistema de generador de id unico

Con los datos recibidos el sistema debera realizar lo siguiente: 

1. del valor recibido de nombre, usar solo las 2 primera letras y 
convertirlas a mayusculas

2. del valor de apellido, usar las 2 primeras letras y convertirlas
a mayusculas

3. del valor de año, tomar los 2 ultimos digitos

Ademas el sistema debera generar un valor aleatrio de 4 digito, con ayuda
de la funcion randint

Finalmente, con los datos obtenidos generar un ID unico uniendo los valores
como sigue: 

ejemplo : 
nombre -> juan -> JU
apellido -> perez -> PE
año nacimiento -> 1995 -> 95
valor aleatorio -> randint -> 7886

Resultado ID unico : JUPE957886
"""

from random import randint 

print("*** Generador de id unico ***")
nombre = input("ingrese su nombre: ")
apellido = input("ingrese sua apellido: ")
ano_nacimiento = input("ingrese su año de nacimiento: ")

# conversion y validacion 
nombre_id = nombre.strip().upper()[:2]
apellido_id = apellido.strip().upper()[:2]
ano_id = ano_nacimiento.strip()[-2:] # toma el anteultimo valor de string hacia adelante
# generar el valor aleatorio
num_aleatorio = randint(0, 9999)
num_id = f"{num_aleatorio:04d}" # genera un string con 4 digitos, rellenando con ceros a la izquierda si es necesario
# concatenacion 
id_unico = nombre_id + apellido_id + ano_id + num_id

# imprimir id unico
print(f"id unico generado es: {id_unico}")

""" respuesta:
*** Generador de id unico ***
ingrese su nombre: juan
ingrese sua apellido: perez
ingrese su año de nacimiento: 1995
id unico generado es: JUPE951041
"""