""" Entrda de datos

funcion input() permite al usuario ingresar datos por teclado,
el valor ingresado es de tipo string, si se desea otro tipo de dato
se debe convertir el valor ingresado a otro tipo de dato, por ejemplo
int(), float(), bool() etc  

estructura basica
variable = input("mensaje para el usuario")

aclaracion el valor ingresado en el imput siempre es de tipo string
 """

# ejemplo 1

nombre = input ("ingrese tu nombre: ")
print(f"el nombre ingresado es: {nombre}")

# ejemplo 2 conversion de tipo de dato
edad = int(input("ingrese su edad: "))
print(f"la edad ingresada es: {edad}")

# comprobacion que edad es de tipo int con operacion de suma
print(f"tu edad + 10 años es: {edad + 10}")

# ejemplo 3 
altura = float(input("ingrese su altura: "))
print(f"la altura ingresada es: {altura:.2f}")


""" respuesta

ingrese tu nombre: alex 
el nombre ingresado es: alex 
ingrese su edad: 30
la edad ingresada es: 30
tu edad + 10 años es: 40
ingrese su altura: 1.69999
la altura ingresada es: 1.70
 """