#Este programa soluciona una ecuación de ssegundo grado
import math

print("Este programa calcula la solución de una ecuación de segundo grado")

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

discriminante = b**2 -4*a*c

if a != 0:
    if discriminante >= 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print("La solución de la ecuación es: x1 = {0} y x2 = {1}".format(x1, x2))
    else:
        print("La ecuación no tiene soluciones reales")
else:
    if b != 0:
        x = -c/b
        print("La solución de la ecuación es: {}".format(x))
    else:
        if c != 0:
            print("La ecuación no tiene solución")
        else:
            print("La ecuación tiene infinitas soluciones")