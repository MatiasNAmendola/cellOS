from proceso import Proceso

class Message(Proceso):

    def __init__(self,id, attributes, numero,texto):
        
        Process.__init__(self, id, attributes)
        self.id = id
        self.name = nombre
        self.time = tiempo
        self.number = numero
        self.text = texto

    def getNumber(self):
        return self.number

    def getText(self):
        return self.text