#Proyecto video club
class Socio:
    def __init__ (self, dni, nombre, telefono, domicilio):
        self. dni = dni
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio

    def __str__ (self):
        return f"DNI: {self.dni}\nNombre: {self.nombre}\nTeléfono: {self.telefono}\nDomicilio: {self.domicilio}"

class Pelicula:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def __str__ (self):
        return f"Título: {self.titulo}\nGénero: {self.genero}\n"
    
class VideoClub:
    def __init__ (self):
        self.socios = []
        self.peliculas = []


    



















