# Ejercicio - Generador de email
""" Generador de email se tiene que normalizar 
Datos 
- mombre : Ubaldo Acosta Soto
- empresa : Global Mentoring
- Dominio : com.mx

Resultado 
- email: ubaldo.acosta.soto@globalmentoring.com.mx
 """


# Datos : 
nombre_usuario = " Ubando Acosta Soto "
nombre_empresa = " Global Mentoring "
dominio_email = "com.mx"

# 1. normalizar nombre de usuario -> sin espacio incial y final, en  minuscula y con punto
#print(nombre_usuario)
nombre_usuario = nombre_usuario.strip()
#print(nombre_usuario)
nombre_usuario = nombre_usuario.lower()
#print(nombre_usuario)
nombre_normalizado = nombre_usuario.replace(" ", ".")
#print(nombre_normalizado)

# 2. normalizar nombre empresa -> Minuscula y todo junto.
#print(nombre_empresa)
# se puede usar 2 metodos seguido para no escribir tanto
empresa_normalizado = nombre_empresa.replace(" ", "").lower()
#print(empresa_normalizado)

# 3. concatenacion de partes normalizadas e imprimir
email = nombre_normalizado + "@" + empresa_normalizado + "." + dominio_email
print("*** Generador de email ***")
print(f"email:{email}")

"""
Respuesta:
*** Generador de email ***
email:ubando.acosta.soto@globalmentoring.com.mx
 """