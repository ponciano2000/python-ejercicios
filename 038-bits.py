#Este programa calcula el número de bits necesarios para representar un número en 
#base dos usando el concepto de recursividad

def bits(n):
    if n == 0 or n == 1:
        resultado = 1
    else:
        resultado = 1 + bits(n//2)
    return resultado

n = int(input("Introduce un número: "))
print(f"Para representar el número {n} en base dos se necesitan {bits(n)} bits")