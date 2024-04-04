#Este programa determina si un elemento pertenece a una lista dada o no

conjunto = [1, 2, 3]
elemento = int(input("Dame un número: "))
if not elemento in conjunto:
    conjunto.append(elemento)

print(conjunto)