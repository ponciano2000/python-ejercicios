#Este programa lee información de un fichero

#Paso 1. Abrir el fichero
fichero = open("ejemplo.txt")

#Paso 2. Leer los datos del fichero
for linea in fichero:
    if linea[-1] == "\n":
        linea = linea[:-1]
    print(linea)

#Paso 3. Cerrar el fichero
fichero.close()