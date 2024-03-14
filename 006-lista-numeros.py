#Programa que obtiene un conjunto de números separados por comas y crea una lista

print("Este programa hace una lista con un conjunto de números separados por comas")
entrada = input("Introduce un conunto de números separados por comas: ")

numeros = entrada.split(",")
print(numeros)