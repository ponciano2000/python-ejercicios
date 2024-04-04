#Este programa determina si un número es primo o no

print("Este programa determina si un múmero es primo o no")
numero = int(input("Introduce un número: "))

creo_que_es_primo = True

if numero > 1:
    for divisor in range(2, numero):
        if numero % divisor == 0:
            creo_que_es_primo = False
            break
else:
    creo_que_es_primo = False
    

if creo_que_es_primo:
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")