import random

class ElementosColores:
    
    def __init__(self, numeroAtomico=None, simbolo=None, elemento=None):
        self.numeroAtomico = numeroAtomico
        self.simbolo = simbolo
        self.elemento = elemento
        self.color = "%06x" % random.randint(0,0xFFFFFF)


    def getNumeroAtomico(self):
        return self.numeroAtomico
    
    def getSimbolo(self):
        return self.simbolo
    
    def getElemento(self):
        return self.elemento