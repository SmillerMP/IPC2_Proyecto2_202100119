

class dataCompuesto():
    def __init__(self, nombreCompuesto, listaCompuestos, numeroDeElementos):
        self.nombreCompuesto = nombreCompuesto
        self.listaCompuestos = listaCompuestos
        self.numeroDeElementos = numeroDeElementos


    def get_listaCompuestos(self):
        return self.listaCompuestos
    
    def get_nombreCompuesto(self):
        return self.nombreCompuesto
    
    def imprimirListaCompuestos(self):
        for x in self.listaCompuestos:
            print(x)



# ------------ CLASES PARA LA LISTA DE MAQUINAS ---------------- #
class dataMaquina():
    def __init__(self, nombreMaquina, numeroDePines, numeroDeElementos, numeroDeMaquina, listaPines):
        self.nombreMaquina = nombreMaquina
        self.numeroDePines = numeroDePines
        self.numeroDeElementos = numeroDeElementos
        self.numeroDeMaquina = numeroDeMaquina
        self.listaPines = listaPines

class dataPin():
    def __init__(self, listaPin, contadorPin):
        self.listaPin = listaPin
        self.contadorPin = contadorPin

class dataElementoPin():
    def __init__(self, elementoPin, contadorElemento):
        self.elementoPin = elementoPin
        self.contadorElemento = contadorElemento

# ---------------------------------------------------------