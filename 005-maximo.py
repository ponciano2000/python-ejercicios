#Este programa calcula el máximo de dos números

print("Este programa calcula el máximo de dos números")
a = int(input("Dame el primer número: "))
b = int(input("Dame el segundo número: "))

if a > b:
    maximo = a
else:
    maximo = b

print("El número máximo es {}".format(maximo))