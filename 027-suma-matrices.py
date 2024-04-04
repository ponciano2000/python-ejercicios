#Este programa suma dos matrices leyendo ambas por teclado
print("Este programa suma dos matrices leyendo ambas por teclado")

m = int(input("Dime el número de filas: "))
n = int(input("Dime el número de columnas: "))

#Creamos dos matrices nulas
A = []
for i in range(m):
    A.append([0]*n)

B = []
for i in range(m):
    B.append([0]*n)

#Leemos su contenido por teclado
print("Lectura de la matriz A")
for i in range(m):
    for j in range(n):
        A[i][j] = float(input(f"Componente ({i}, {j}): "))

print("Lectura de la matriz B")
for i in range(m):
    for j in range(n):
        B[i][j] = float(input(f"Componente ({i}, {j}): "))

#Construimos una matriz nula para el resultado
C = []
for i in range(m):
    C.append([0]*n)

#Hacemos el cálculo de la suma
for i in range(m):
    for j in range(n):
        C[i][j] = A[i][j] + B[i][j]

#Mostramos el resultado por pantalla
print("Suma: ")
for i in range(m):
    for j in range(n):
        print(C[i][j], end = " ")
    print()