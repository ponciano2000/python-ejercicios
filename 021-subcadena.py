#Este programa hace sub cadenas

print("Este programa hace subcadenas dados una cadena y dos índices")

cadena = input("Dame una cadena: ")
i = int(input("Dame el índice i: "))
j = int(input("Dame el índice j: "))

if j > len(cadena):
    final = len(cadena)
else: 
    final = j

subcadena = ""
for k in range(i, final):
    subcadena += cadena[k]

print(f"La sub cadena entre {i} y {j} es: {subcadena}")
