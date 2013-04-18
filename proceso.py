class Proceso:

    def __init__(self,id,nombre,tiempo):
        self.id = id
        self.name = nombre
        self.time = tiempo

    def getName(self):
        return self.name

    def getTime(self):
        return self.time

    def getId(self):
        return self.id