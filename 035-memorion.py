#Este programa crea un memorion
import random
import turtle

#Estados posibles de las celdas
CeldaCerrada = 0
CeldaAbierta = 1
CeldaTemporalmenteAbierta = 2


#Definimos funciones
def crea_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([None]*columnas)
    return matriz

def rellena_simbolos (simbolo):
    numsimbolo = 0
    for i in range(len(simbolo)):
        for j in range(len(simbolo[0])):
            simbolo[i][j] = chr(ord("a")) + numsimbolo // 2
            numsimbolo += 1