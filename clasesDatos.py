class datosElementos():

    def __init__(self,maquina, pin, indice, simboloElemento):
        self.maquina = maquina
        self.pin = pin
        self.indice = indice
        self.simboloElemento = simboloElemento



    def get_maquinaElemento(self):
        return self.maquina
    
    def get_pinElemento(self):
        return self.pin
    
    def get_simboloElemento(self):
        return self.simboloElemento
    
