#Este programa construye una matriz leyendo los elementos por teclado

print("Este programa construye una matriz leyendo los elementos por teclado")

m = int(input("Dime el número de filas: "))
n = int(input("Dime el número de columnas: "))

#Creamos una matriz nula
M = []
for i in range(m):
    M.append([0]*n)

#Leemos su contenido por teclado
for i in range(m):
    for j in range(n):
        M[i][j] = float(input(f"Dame el componente ({i}, {j}): "))