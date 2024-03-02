#Programa que calcula el área de un círculo
from math import pi

print("Este programa calcula el area de un circulo")
r = float(input("Escribe el radio del circulo: "))
A = pi*r**2

print("El área del círculo de radio {0} es {1}".format(r, A))