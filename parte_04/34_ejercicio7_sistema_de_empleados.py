""" Ejercicio de sistema de empleados

Se debera crear un programa para solicitarla informacionde un empleado, 
introduciendo, los datos por consola 

- nombre del empleado
- edad del empleado (en entero)
- salario del empleado (con dos decimales)
- es jefe de departamento (si o no)
 """

print("*** Sistema de empleados ***")
nombre = input("ingrese el nombre del empleado: ")
edad = int(input("ingrese la edad del empleado: "))
salario = float(input("ingrese salario del empleado: "))
es_jefe = input("es jefe de departamento (si o no): ")


""" 
Aclaracion ¿porque no usamos en la variable es_jefe un booleano?

es_jefe= bool(input("es jefe de departamento (Si o No): "))"

si se usara NO nos daria el valor esperado ya si trabajamos con
string y boolanos, cuando es string sea vacio nos daria False y
cuando es string tenga algun valor nos daria True
"""

# conversion de string a booleano
# tomamos el sring ingresado y lo convertimos a minuscula, 
# luego comparamos si es igual a "si" , devolviendo True o False
es_jefe = es_jefe.lower() == "si"

print("\n*** Datos del empleado ***")
print(f"el nombre del empleado es: {nombre}")
print(f"la edad del empleado es: {edad}")
print(f"el salario del empleado es: {salario:.2f}")
print(f"¿es jefe de departamento?: {es_jefe}")


""" respuesta
*** Sistema de empleados ***
ingrese el nombre del empleado: mateo 
ingrese la edad del empleado: 30
ingrese salario del empleado: 750000.999
es jefe de departamento (si o no): NO

*** Datos del empleado ***
el nombre del empleado es: mateo 
la edad del empleado es: 30
el salario del empleado es: 750001.00
¿es jefe de departamento?: False
 """