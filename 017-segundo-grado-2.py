#Este programa calcula las raices de una ecuación de segundo grado
#Es la segunda versión del programa, usando try-except en lugar de if para manejar las excepciones

import math

print("Este programa calcula las raices de una ecuación de segundo grado")

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

try:
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    if x1 == x2:
        print(f"La solución es: x = {x1}")
    else:
        print(f"La solución es: x1 = {x1}, x2 = {x2}")
        
except ZeroDivisionError:
    if b != 0:
        print("La ecuación no tiene solución")
    else:
        print("La ecuación tiene infinitas soluciones")
except ValueError:
    print("No hay soluciones reales")