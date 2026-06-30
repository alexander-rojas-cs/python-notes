# Ejemplo de caracteres especiales enn python

# 1. Salfo de linea \n
print("Ej 1 : salto de linea")
mensaje1 = "Hola \nmundo"
print(mensaje1)

# 2. Tabulacion \t
print("Ej 2 y 3 : tabulacion")
## indice de tabulacion
print("1234123412341234\n")
mensaje2 = "\tJuan Perez"
print(mensaje2)
mensaje3 = "\t\tJuan peralta"
print(mensaje3)
    
# 3. Comillas dentro de cadena 
print("Ej 4 : comillas dentro de cadena")
mensaje4 = "Ella dijo \"Hola a todo\""
print (mensaje4)

# 4. Barra invertida
print("Ej 5 : barra invertida")
mensaje5 = "C:\\Usuario\\Juan\\Documentos"
print(mensaje5)

# 5. Cadena cruda(raw string) r"..."
# Las cadnas crudas toman literalmente lo que escbriste 
# ignorando cualquier tipo de caracter especial como 
# salto de linea \n  o tabulacion \t , entre otros. 
print("Ej 6 : cadena cruda")
mensaje6 = r"C:\Usuario\Pedro\Descargas"
print(mensaje6)

""" Respuesta :
Ej 1 : salto de linea
Hola 
mundo
Ej 2 y 3 : tabulacion
1234123412341234

        Juan Perez
                Juan peralta
Ej 4 : comillas dentro de cadena
Ella dijo "Hola a todo"
Ej 5 : barra invertida
C:\Usuario\Juan\Documentos
Ej 6 : cadena cruda
C:\Usuario\Pedro\Descargas
 """