#Programa que resuelve una ecuación de primer grado

print("Este programa resuelve una ecuación del tipo ax + b = 0")

a = float(input("Introuce el valor de a: "))
b = float(input("Introuce el valor de b: "))

if a != 0:
    x = -b / a
    print("La solución de la ecuación es: x = {}".format(x))

if a == 0:
    if b != 0:
        print("La ecuación no tiene solución")
    if b == 0:
        print("La ecuación tiene infinitas soluciones")