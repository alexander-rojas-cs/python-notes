# funcion de reenplazo en python .replace()
# 1. Buscar las coincidencias dentro de una cadena
# 2. Cambia lo viejo por lo nuevo
# 3. Las cadenas en python son inmutables por lo tanto
# ... no reemplaza sino que crea una nueva cadena con el cambio

# Uso de replace():
# A) limpieza :  de espacios extras, simbolos raroso errores
# B) plantilla : se puede buscar dentro de una strtura y 
# cambiar un campo especifico

# SINTAXIS   ->  texto.replace("viejo", "nuevo")
# SINTAXIS 2 ->  texto.replace("viejo", "nuevo", 2)

# el 3er parametros es opcional para indicar cuentas veces 
# hacer el reemplzazo cada vez que ebcutre coincidencia 
# ej si encutra coincidencia 5 txt viejos y se poner de 3er 
# parametro 2, solo se reemplzan las 2 primeras coincidencias 


# Ejemplo 1 : Basico
txt = "Es sal"
print("Ej 1")
print(f"Sin replace : {txt}")
txt_replace =txt.replace("sal", "dulce")
print(f"Con replace : {txt_replace}")

# Ejemplo 2 : Reemplazar todas las veces de las apariciones
mensaje = "Hola Mundo, Mundo"
print("Ej 2")
print(mensaje)
nuevo_msj = mensaje.replace("Mundo","Python")
print(nuevo_msj)

#Ejemplo 3 : Reemplazar 1 sola vez
print("Ej 3")
print(mensaje)
mensaje_nuevo = mensaje.replace("Mundo", "Dev", 1)
print(mensaje_nuevo)

""" Respuesta 
Ej 1
Sin replace : Es sal
Con replace : Es dulce
Ej 2
Hola Mundo, Mundo
Hola Python, Python
Ej 3
Hola Mundo, Mundo
Hola Dev, Mundo
 """
