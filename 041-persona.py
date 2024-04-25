#Este programa define una clase llamda persona

class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

    def iniciales (self):
        cadena = ""
        for caracter in self.nombre:
            if caracter >= "A" and caracter <= "Z":
                cadena = cadena + caracter + ". "
        return cadena
    
    def __str__(self):
        cadena = f"Nombre: {self.nombre}\n"
        cadena = cadena + f"DNI: {self.dni}\n"
        cadena = cadena + f"Edad: {self.edad}\n"
        return cadena


toni = Persona ("Antono Pérez", "546544656545", 20)

print(toni.nombre)
print(toni.iniciales())
print(toni)