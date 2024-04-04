#Este programa suma dos matrices leyendo ambas por teclado
print("Este programa multitplica dos matrices leyendo ambas por teclado")

p = int(input("Dime el número de filas de A: "))
q = int(input("Dime el número de columnas de A: "))
r = int(input("Dime el número de columnas de B: "))

#Creamos dos matrices nulas
A = []
for i in range(p):
    A.append([0]*q)

B = []
for i in range(q):
    for j in range(r):
        B.append([0]*r)

#Leemos su contenido por teclado
print("Lectura de la matriz A")
for i in range(p):
    for j in range(q):
        A[i][j] = float(input(f"Componente ({i}, {j}): "))

print("Lectura de la matriz B")
for i in range(q):
    for j in range(r):
        B[i][j] = float(input(f"Componente ({i}, {j}): "))

#Construimos una matriz nula para el resultado
C = []
for i in range(p):
    C.append([0]*r)

#Hacemos el cálculo del producto
for i in range(p):
    for j in range(r):
        for k in range(q):
            C[i][j] += A[i][k] * B[k][j]

#Mostramos el resultado por pantalla
print("Producto: ")
for i in range(p):
    for j in range(r):
        print(C[i][j], end = " ")
    print()