# Ejemplo con slicing 

texto = "PROGRAMACION"

# Ej 1 : Basico -> [inicio : fin]
print(texto[0:4])

# Ej 2 : Basico -> atajo desde el inicio
print(texto[:4])

# Ej 3 : desde atajo hasta el final
print(texto[8:])

# Ej 4 : con indices negativos
print(texto[-4:])

# Ej 5 : invertir el texto usando el paso
print(texto[::-1])

# Ej 6 : invertir el texto usando el paso de 2 pasos
print(texto[::-2])

# Ej 7 : paso o salto normal de 2 
print(texto[::2])

""" Respuesta:
PROG
PROG
CION
CION
NOICAMARGORP
NIAAGR
PORMCO
"""