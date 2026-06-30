# CONCATENACION: es el proceso de unir 2 o mas cadenas y 
# obtener una sola que repreeta la union de cada cadena

# METODO ANTIGUO

# Ejemplo 1 :
nombre = "pedro "
edad = 25 
print("Me llamo " + nombre + "y mi edad es " + str(edad) + " años")

# Ejemplo 2 : 
print("Hola mi nombre es {}y tengo {} años".format(nombre,edad))


# METODO MODERNO :
# es el metodo mas moderno, facil y rapido
# donde dentro de llaves {} va a ver calculos o txt

# Ejemplo 3 :
nombre = "Maria"
ciudad = "salta"
edad = 25
print(f"Hola me llamo {nombre} soy de {ciudad} y tengo {edad} años")

""" Respuesta : 

Me llamo pedro y mi edad es 25 años
Hola mi nombre es pedro y tengo 25 años
Hola me llamo Maria soy de salta y tengo 25 años

 """