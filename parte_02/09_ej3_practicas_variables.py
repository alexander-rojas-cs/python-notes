# Ejercicio: registro de explorador espacial 

# aisgnacion de las variables 

nombre_explorador = "luna vega"
planeta_origen = "Tierra"
edad_explorador = 29
misiones_completadas = 4
nivel_energia = 87.5

# Explicacion de malas practicas 
# for = 25 # arroja un error(no se puede asignar sobre palabras reservadas)
Nivel_Energia = 99.5 # No es una buena practica
NIVEL_ENERGIA = 100 # No arroja error pero se consdera como una constante en python una convencion
nivel_energía = 88.5 # No se be usar caracteres espciles como tilde o ñ 

print("=== Registro espacial ===")
print("nombre del explorador:", nombre_explorador)
print("planeta de origen:", planeta_origen)
print("edad del explorador:", edad_explorador)
print("misiones completadas:", misiones_completadas)
print("nivel de energia:", nivel_energia)

print("NIVEL DE ENERGIA:", NIVEL_ENERGIA)