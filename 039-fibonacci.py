#Este programa calcula los n números de la serie de Fibonacci
def fibonacci(n):
    if n == 1 or n == 2:
        resultado = 1
    elif n > 2:
        resultado = fibonacci(n-1) + fibonacci(n-2)
    return resultado

n = int(input("Introduce un número: "))
print(f"El {n} ésimo número de Fibonacci es {fibonacci(n)}")