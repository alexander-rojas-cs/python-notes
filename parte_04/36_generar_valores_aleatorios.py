""" Generar valores aleatorios

usando la funcion randint() del modulo random podemos generar valores aleatorios
se debera importar el modulo random para poder usar la funcion randint()

como se usa : random.randint(a, b) donde devuelve un numero entero aleatorio N tal que a <= N <= b

"""

from random import randint

# Ejemplo 1
# Genera un numero aleatorio entre 1 y 100

numero = randint(1,100)
print(f"numero aleatoro entre 1 y 100: {numero}")

# ejemplo 2 : dado de 6 caras
dado = randint(1,6)
print(f"resultado de lanzar el dado: {dado}")