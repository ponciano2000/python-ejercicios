#Este programa calcula las primeras 100 raíces de un número

print("Este programa calcula las primeras 100 raíces de un número")
numero = int(input("Dame un úmero: "))

for n in range (2, 101):
    print(f"La raíz {n}-ésima de {numero} es {numero**(1/n)}")