""" Error comunes 

La funcion bool revisa si en caso de string si esta vacio o no
si esta vacio devuelve False, si tiene contenido devuelve True

"""

# ejemplo 1
respuesta_usuario = "False"
es_verdadero = bool(respuesta_usuario)
print(f"el valor de la variable es: {es_verdadero}")                

# ejemplo 2
respuesta_usuario2 = False
es_verdadero2 = bool(respuesta_usuario2)
print(f"el valor de la variable es: {es_verdadero2}")

# ejemplo 3 : forma correcta para validar vacio
respuesta_usuario3 = ""
print(f"el valor de la variable es: {bool(respuesta_usuario3)}")

""" respeusta
el valor de la variable es: True
el valor de la variable es: False
el valor de la variable es: False
"""