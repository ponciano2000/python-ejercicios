#Programa que invierte una cadena dada por teclado

print("Este programa regresa el inverso de una cadena")
str = input("Introduce la cadena: ")

for i in range(len(str)-1, -1, -1):
    print(str[i], end="")

#Programa alternativo
print()
print(str[::-1])