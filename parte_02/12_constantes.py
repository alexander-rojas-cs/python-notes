# constantes 

""" En python no tiene de forma nativa constantes como otros lenguajes
asi que por convencion (por reglas o pautas no obligatorios) las constantes 
se escriben en en mayuscula y no se modifican (aun que python permita 
modificarlas) """

print(" *** Constantes en python ***")

# Constantes convencionales - NO MODIFUCAR AUN QUE PYTHON LO PERMITE
PI = 3.14159
print("El valor de PI es :", PI)

NOMBRE_BASE_DATOS = "cliente_bs"
print("Nombre de la base de datos:",NOMBRE_BASE_DATOS)

# Aca se puede ver como se cambia valor de una constantes , prohibido hacer
NOMBRE_BASE_DATOS = "lista_de_clientes_db"
print("No cambiar el valor de una constante (esto no se debe hacer):",NOMBRE_BASE_DATOS)