#Programa que calcula el perímetro de un círculp

from math import pi

print("Este programa calcula el perímetro de un círculo dado el radio")
radio = float(input("Introduce el radio del círculo: "))
perimetro = 2*pi*radio

print("El perímetro del círculo de radio {0} es {1}".format(radio, perimetro))
