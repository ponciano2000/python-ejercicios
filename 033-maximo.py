#Este programa define y usa una función que regresa el máximo número de una lista

def maximo (lista):
    if len(lista) > 0:
        candidato = lista[0]
        for elemento in lista:
            if elemento > candidato:
                candidato = elemento
    else:
        candidato = None
    return candidato

a = [10, 0, -15, 22]
print(maximo(a))
    