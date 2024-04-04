#Este programa calcula el volumen de una esfera

from math import pi

print("Este programa calcula el volumen de una esfera dado su radio")
radio = float(input("Introduce el radio de la esfera: "))

volumen = 4 /3 * pi* radio**3
print("El volumen de la esfera de radio {0} es {1}".format(radio, volumen))

