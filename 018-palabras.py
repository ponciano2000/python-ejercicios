#Este programa cuenta las palabras de una oración

print("Este programa cuenta las palabras de una oración")
cadena = input("Escribe una frase: ")

while cadena != "":
    cambios = 0
    anterior = " "
    for caracter in cadena:
        if caracter == " " and anterior != " ":
            cambios += 1
        anterior = caracter

    if cadena[-1] == " ":
        cambios -= 1

    palabras = cambios + 1
    print(f"Palabras: {palabras}")

    cadena = input("Escribe una frase: ")    
