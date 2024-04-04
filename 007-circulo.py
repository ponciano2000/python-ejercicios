#Este programa calcula el diametro, perímetro y área de un círculo
import math

print("Este programa calcula el diametro, perímetro y área de un círculo")

radio = float(input("Introduce el radio de círculo: "))

#Menú
print("Escoge una opción: ")
print("a) Calcular el diámetro: ")
print("b) Calcular el perímetro: ")
print("c) Calcular el área: ")
opcion = input("Escoge una opción: ")

if opcion == "a": 
    diametro = radio * 2
    print("El diámetro del círculo es: {}".format(diametro))
elif opcion == "b":
    perimetro = 2* math.pi * radio
    print("El perímetro del círculo es: {}".format(perimetro))
elif opcion == "c": 
    area = math.pi * radio** 2
    print("El área del círculo es: {}".format(area))
else:
    print("Sólo hay tres opciónes: a, b o c.")
    print("Tú has tecleado {}".format(opcion))