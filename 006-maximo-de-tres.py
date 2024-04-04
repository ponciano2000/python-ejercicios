#Este programa calcula el máximo de tres números

print("Este programa calcula el máximo de tres números")

a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segungo número: "))
c = int(input("Introduce el tercer número: "))

if a > b:
    if a > c:
        maximo = a
    else:
        maximo = c
else:
    if b > c:
        maximo = b
    else: 
        maximo = c

print("El número máximo es: {}".format(maximo))