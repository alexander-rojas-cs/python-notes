# Inmutabilidad de cadenas:
# si se crea una cadena y se trata de modifcar no se puede

# Ejemplo 0 :  fallido fa un error 
""" texto = "Gato"
texto[0] = "P" """

# Ejemplo 1 : no se puede modificar una caenas pero si contenar 
# y generar un nueva cadena
animal = "Gato"
# concatenacion
plural = animal + "s"
# mostrar la concatenacion en la nueva var
print(plural)

# Ejemplo 2 : alternativa con D-String
plural2 = f"{animal}s"
print(plural2)

""" 
Respuesta:
Gatos
Gatos
"""