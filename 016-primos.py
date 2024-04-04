#Este programa imprime todos los números primos entre el 0 y el número que le indiquemos
print("Este programa imprime todos los números primos entre el 0 y el número que le indiquemos")

limite = int(input("Introduce un número: "))

for numero in range(2, limite+1):
    creo_que_es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            creo_que_es_primo = False
            break
    if creo_que_es_primo:
        print(numero, end=" ")
 
print()