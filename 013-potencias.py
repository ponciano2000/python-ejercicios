#Este programa imprime las primeras 5 potencias de un número

print("Este programa imprime las primeras 5 potencias de un número")

numero = int(input("Dame un número:"))

for potencia in [2, 3, 4, 5]:
    print(f"{numero} elevado a la potencia {potencia} es {numero**potencia}")