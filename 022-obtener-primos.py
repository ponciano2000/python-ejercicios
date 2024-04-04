#Este programa obtiene los números primos entre 1 y un número dado

print("Este programa obtiene los números primos entre 1 y un número dado")
n = int(input("Introduce el valor máximo: ")) 

primos = []
for numero in range(2, n+1):
    #Determinamos si el número es primo 
    creo_que_es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            creo_que_es_primo = False
            break
    #Si esprimo lo añadimos a la lista
    if creo_que_es_primo:
        primos.append(numero)

print(primos)