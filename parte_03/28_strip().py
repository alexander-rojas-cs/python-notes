# strip(): con el uso de metodo se puede eliminar o limpiar los espacios en blanco 
# al inicio  y final de una cadena 

nombre_carrera = " licenciatura en matematica aplicada "
print(nombre_carrera)
nombre_carrera_corregido = nombre_carrera.strip()
print("nombre corregido sin espacios al inicio y ni final:")
print(nombre_carrera_corregido)

""" Respuesta:
 licenciatura en matematica aplicada 
nombre corregido sin espacios al inicio y ni final:
licenciatura en matematica aplicada
 """