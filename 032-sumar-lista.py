#Este programa define y una una función que suma los elementos numéricos de una lista

def sumatorio (lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

a = [1, 2, 3]
print(sumatorio(a))