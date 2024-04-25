#Este programa calcula el factorial de un número usando el concpto de recursión

def factorial (n):
    if n == 0 or n == 1:
        resultado = 1
    elif n > 1:
        resultado = n * factorial(n-1)
    return resultado

n = int(input("Introduce un número: "))
print(f"El factorial {n} es {factorial(n)}")