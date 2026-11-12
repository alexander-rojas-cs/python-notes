""" Receta de cocina

Crear un porgrama para solicitar algunos valores
importntes para una receta de cocina

Los valore a introducir por elusario debe ser : 

- nombre de la receta
- ingredientes
- tiempo de preparacion (en minutos)
- dificultad de la receta (facil, media, dificil)

y por ultimo mandar imprimir la receta.
 """

print("*** Receta de cocina ***")
nombre_receta = input("ingrese nombre de la receta: ")
ingredientes = input("ingrese los ingredientes: ")
tiempo = int(input("ingrese el tiempo de preparacion: "))
dificultad = input("¿dificultad?(facil|media|dificil): ")

print("\n*** RECETA ***")
print(f"nombre de la receta: {nombre_receta}")
print(f"lista de ingredientes: {ingredientes}")
print(f"tiempo de preparacion: {tiempo} min")
print(f"¿dificultad? : {dificultad}")

""" respuesta:
*** Receta de cocina ***
ingrese nombre de la receta: pizza
ingrese los ingredientes: harina, queso, salsa de tomate, etc                 
ingrese el tiempo de preparacion: 14
¿dificultad?(facil|media|dificil): facil

*** RECETA ***
nombre de la receta: pizza
lista de ingredientes: harina, queso, salsa de tomate, etc
tiempo de preparacion: 14 min
¿dificultad? : facil
"""