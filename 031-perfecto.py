#Este programa determina si un número es perfecto
def es_perfecto(n):
    sumatorio = 0
    for i in range(1, n):
        if n % i == 0:
            sumatorio += i
    return sumatorio
    