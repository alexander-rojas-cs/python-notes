# Explicacion rapida de como se alamcenan en python las variables 

""" una variables esta formada por : 

- nombre o etiqueta 
- asignacion = 
- valor o  dato 

ejemplo:  """

numero = 7 

print(numero)

""" ¿ COO FUNCIONAN INTERNAMENTE ?

exiten 2 partes en la memoria (Ram) una llamada stack y otra heap
donde en el stack se almacenan las referecias, variables locales, 
funciones, etc. y en el heap se almacenan los objetos y estructuras
de datos, tomando el ejemplo anterior,
cuando se ejecuta la linea numero = 7, se crea un objeto con el
valor 7, en el heap y se asigna la referencia de ese objeto a 
la variable numero en el stack.

en resumen : 

stack -> numero 

heap -> 7

donde se dice que el numero apunta al objeto 7 en el heap.
"""
