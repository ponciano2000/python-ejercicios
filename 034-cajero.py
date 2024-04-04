#Este programa simula la actividad de un cajero autmático 

#Número de billetes inicial de tres denominaciones 

carga50 = 100    
carga20 = 100
carga10 = 100

def sacar_dinero(cantidad):
    global carga50, carga20, carga10
    if cantidad <= 50*carga50 + 20*carga20 + 10*carga10:
        de50 = cantidad // 50
        cantidad = cantidad % 50
        if de50 >= carga50: #Si no hay suficientes billetes de a 50 
            cantidad = cantidad + (de50 - carga50) * 50
            de50 = carga50
        de20 = cantidad // 20
        cantidad = cantidad % 20
        if de20  >= carga20: #Si no hay suficientes billetes de a 20 
            cantidad = cantidad + (de20 - carga20) * 20
            de20 = carga20
        de10 = cantidad // 10
        cantidad = cantidad % 10
        if de10 >= carga10:
            cantidad = cantidad + (de10 - carga10)*10
            de10 = carga10
        #Si todo ha ido bien, la cantidad que resta por entregar es nula 
        if cantidad == 0:
            #Así que hacemos efectiva la extracción 
            carga50 = carga50 - de50
            carga20 = carga20 -de20
            carga10 = carga10 - de10
            return [de50, de20, de10]
        else: #Y si no, devolvemos la lista con tres ceros
            return [0, 0, 0]
    else: 
        return [0, 0, 0]
    
c = int (input("Cantidad a extraer: "))
print(sacar_dinero(c))


