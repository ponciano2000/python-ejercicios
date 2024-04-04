#Este programa es una mejora del programa 007-circulo.py

import math

print("Este programa calcula los elementos de un círculo a partir de su radio")
radio = float(input("Introduce el radio del círculo: "))

opcion = ""
while opcion != "d":
    print("¿Qué quieres calcular")
    print("a) Calcular el diámetro")
    print("b) Calcular el perímetro")
    print("c) Calcular el área")
    print("d) Finalizar")
    opcion = input("Teclea a, b o c y pulsa Enter: ")
    if opcion == "a": 
        diametro = radio * 2
        print("El diámetro del círculo es: {}".format(diametro))
    elif opcion == "b":
        perimetro = 2* math.pi * radio
        print("El perímetro del círculo es: {}".format(perimetro))
    elif opcion == "c": 
        area = math.pi * radio** 2
        print("El área del círculo es: {}".format(area))
    elif opcion != "d":
        print("Sólo hay tres opciónes: a, b o c.")
        print("Tú has tecleado {}".format(opcion))
        print("")


print("Gracias por usar el programa")