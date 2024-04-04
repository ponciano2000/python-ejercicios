#Este programa convierte un número binario en decimal

print("Este programa convierte un número binario en decimal")

bits = input("Dame un número binario: ")

n = len(bits)
valor = 0

for bit in bits:
    if bit == "1":
        valor = valor + 2**(n-1)
    n -= 1

print(f"Su valor decimal es: {valor}")

