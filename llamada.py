from proceso import Proceso

class Llamada(Proceso):

    def __init__(self,nombre,tiempo,numero,duracion):
        self.id = id
        self.name = nombre
        self.time = tiempo
        self.number = numero
        self.length = duracion

    def getNumber(self):
        return self.number

    def getLength(self):
        return self.length