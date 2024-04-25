#Este programa calcula la integral de x**2

def integral_x2(a, b, n):
    if n == 0:
        sumatorio = 0.0
    else:
        deltax = (b-a)/n
        sumatorio = 0.0
        for i in range(n):
            sumatorio += deltax * (a+i*deltax)**2
    return sumatorio 

inicio = float(input("Inicio del intervalo: "))
final = float(input("Final del intervalo: "))
partes = int(input("Número de rectángulos: "))

print(f"La integral de x**2 entre {inicio} y {final}", end=" ")
print(f"vale aproximadamente {integral_x2(inicio, final, partes)}")
