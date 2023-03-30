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
    


class dataCompuesto():
    def __init__(self, nombreCompuesto, listaCompuestos, numeroCompuesto):
        self.nombreCompuesto = nombreCompuesto
        self.listaCompuestos = listaCompuestos
        self.numeroCompuesto = numeroCompuesto


    def get_listaCompuestos(self):
        return self.listaCompuestos
    
    def get_nombreCompuesto(self):
        return self.nombreCompuesto
    
    def imprimirListaCompuestos(self):
        for x in self.listaCompuestos:
            print(x)
