class Fecha:
    def __init__ (self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.año}"
    
    def en_año_bisiesto(self):
        return self.año % 4 == 0 and (self.año % 100 != 0 or self.año % 400  == 0)
    
def lee_fecha():
    dia = 0
    while dia < 1 or dia > 31:
        dia = int(input("Día: "))
    mes = 0
    while mes < 1 or mes > 12:
        mes = int(input("Mes: "))
    año = int(input("Año: "))
    return Fecha (dia, mes, año)


    
