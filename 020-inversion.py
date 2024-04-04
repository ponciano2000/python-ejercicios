#Este programa invierte una cadena

print("Este programa invierte una cadena")
cadena = input("Introduce una cadena: ")

inversion = ""
for caracter in cadena:
    inversion = caracter + inversion

print(f"Su inversión es: {inversion }")