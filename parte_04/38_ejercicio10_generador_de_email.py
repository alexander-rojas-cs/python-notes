""" sistema de generador de email

Se solicita crear una nueva version del sistema de emails

para solictar un email se debe solciitar:

- nombre: juan carlos
- apellido: gomez lara
- nombre de empresa: global mentoring
- extension de dominio: .com.mx

El resultado debe ser :
juan.carlos.gomez.lara@globalmentoring.com.mx

"""

nombre = input("ingrese nombre: ")
apellido = input("ingrese apeellido: ")
nombre_empresa = input("ingrese nombre de la empresa: ")
extension = input("ingrese dominio de la empresa: ")

# Normalizacion de los valores recibidos
nombre = nombre.strip().lower().replace(" ", ".")
apellido = apellido.strip().lower().replace(" ", ".")
nombre_empresa = nombre_empresa.strip().lower().replace(" ", "")
extension = extension.strip().lower().replace(" ", "")

# concatenacion y guardado
email = f"{nombre}.{apellido}@{nombre_empresa}{extension}"

# imprimir el ressultado
print(f"El email generado: {email}")

""" respuesta :
ingrese nombre: juan carlos 
ingrese apeellido: gomez lara
ingrese nombre de la empresa: global mentoring
ingrese dominio de la empresa: .com.mx
El email generado: juan.carlos.gomez.lara@globalmentoring.com.mx
 """