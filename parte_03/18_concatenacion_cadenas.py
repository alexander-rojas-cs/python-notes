# Ejemplo de concatenacion 

## 1. usando el operador + 
nombre = "Lucia"
apellido = "Garcia"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

## 2. usando el metodo print
edad = 28 
print("Usando comas:", "nombre", nombre_completo, "Edad:", edad)

## 3. usando metodo F-String
ciudad = "Barcelona"
pais = "España"
profesion = "Ingeniera"
presentacion = f"Hola soy {nombre}, tengo {edad + 1} años, soy {profesion} en {ciudad}, {pais}"
print(presentacion)

""" Repuesta 
Lucia Garcia
Usando comas: nombre Lucia Garcia Edad: 28
Hola soy Lucia, tengo 29 años, soy Ingeniera en Barcelona, España
 """