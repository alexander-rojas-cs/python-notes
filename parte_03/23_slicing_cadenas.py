# Slicing o manejo de subcadenas 
# slicing es la tecnica para extraer una parte de un texto o 
# cadena sin modifcar la cadena original

# formula texto[inicio : fin : paso]
# Donde :
# inicio -> indice donde idnica el corte de la cadena (lo incluye)
# fin -> indice donde terina el corte de la cadena (no lo incluye)
# paso -> salto o como avanzar, por defecto es de 1

# Ejemplo 1 : Basico
texto = "Python"

txt_1 = texto[0:2] 
print(f"cadena cortada 1: {txt_1}")

# Ejmeplo 2 : Basico 
txt_2 = texto[2:6]
print(f"cadena cortada 2: {txt_2}")

# Ejemplo 3 : con  indice negativos 
# como funciona :
#  0   1   2   3   4   5   (indice normal de izq a der)
# -6  -5  -4  -3  -2  -1   (ind negativo de der a izq)
#  P   y   t   h   o   n

# En var txt_3 se guarda del -4 en adelante hasta -1
txt_3 = texto[-4:]
print(f"cadena cortada 3 con ind negativo: {txt_2}")

""" Respuesta:
cadena cortada 1: Py
cadena cortada 2: thon
cadena cortada 3 con ind negativo: thon
"""