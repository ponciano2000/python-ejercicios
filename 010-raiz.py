#Este programa calcula la raíz cuadrada de un número

import math

print("Este programa calcula la raíz cuadrada de un número positivo")

x = -1
while x < 0:
    x = float(input("Introduce un número positivo: "))

print(f"La raíz cuadrada de {x} es {math.sqrt(x)}")