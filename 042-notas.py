#Este programa crea la clase estudiante y algunos métodos

class Estudiante:
    def __init__ (self, nombre, grupo, nota, practica):
        self.nombre = nombre
        self.grupo = grupo
        self.nota = nota
        self.practica = practica 

    def __str__ (self):
        cadena = f"Nombre: {self.nombre}"
        cadena = cadena + f"Grupo: {self.grupo}"
        cadena = cadena + f"Nota examen: {self.nota}"
        if self.practica:
            cadena = cadena + "Práctica entregada"
        else:
            cadena = cadena + "Práctica no entregada"
        return cadena 
        
    def calificacion(self):
        if not self.practica:
            return "Suspenso"
        else:
            if self.nota < 5:
                return "Suspenso"
            elif self.nota < 7:
                return "Aprobado"
            elif self.nota < 8.5:
                return "Notable"
            elif self.nota < 10:
                return "Sobresaliente"
            else:
                return "Matrícula de honor"


def lee_estudiante ():
    nombre = input("Nombre: ")
    grupo = input("Grupo (A, B o C): ")
    nota = float(input("Nota del examen: "))
    entregada = input("Práctica entregada (s/n): ")
    practica = entregada == "s"
    return Estudiante (nombre, grupo, nota, practica)

def lee_y_añade_estudiante(lista):
    estudiante = lee_estudiante()
    lista.append(estudiante)

def acta(lista):
    for estudiante in lista:
        print(estudiante.nombre, estudiante.calificacion())

def nota_media(lista):
    suma = 0
    cantidad = 0
    for estudiante in lista:
        if estudiante.practica:
            suma += estudiante.nota
            cantidad += 1
        if cantidad != 0:
            return suma / cantidad
        else:
            return 0.0
        
def procentaje_de_practicas_entregadas(lista):
    if len(lista) != 0:
        cantidad = 0
        for estudiante in lista:
            if estudiante.practica:
                cantidad += 1
        return cantidad  / len(lista) * 100
    else:
        return 0.0
    
def mejores_estudiantes(lista):
    nota_mas_alta = 0
    mejores = []
    for estudiante in lista:
        if estudiante.practica:
            if estudiante.nota > nota_mas_alta:
                mejores = [estudiante]
                nota_mas_alta = estudiante.nota
            elif estudiante.nota == nota_mas_alta:
                mejores.append(estudiante)
    return mejores

#----------------Programa principal----------------
pepe = lee_estudiante()
print(pepe.calificacion())