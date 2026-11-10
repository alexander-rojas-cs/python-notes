# Buscar subcadena dentro de una cadena - con find 
# con el metodo de find(), devuelve el indice de la primera aparicion 
# de la subcadena, si no encuentra la subcadena devuelve -1


# Ejemplo 1:
cadena = "Hola mundo"
print(f"Cadena:{cadena}")
indice = cadena.find("mundo")
print("Ej 1:")
print(f"Indice de la subcadena mundo: {indice}")

# Ejemplo 2:
indice = cadena.find("Hola")
print("Ej 2:")
print(f"Indice de la subcadena Hola: {indice}")

# Ejemplo 3:
indice = cadena.find("hola")
print("Ej 3: de subcadena no encontrada (Devuelve -1)")
print(f"Indice de la subcadena hola: {indice}")

""" Respuesta : 
Cadena:Hola mundo
Ej 1:
Indice de la subcadena mundo: 5
Ej 2:
Indice de la subcadena Hola: 0
Ej 3: de subcadena no encontrada (Devuelve -1)
Indice de la subcadena hola: -1
 """