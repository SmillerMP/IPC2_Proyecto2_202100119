
class nodo():

    def __init__(self, dato, siguiente = None, anterior = None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior


class listaDoble():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.contador = 0

    def _vacia(self):
        return self.primero == None
    
    def _agregar_final(self, dato):
        if self._vacia():
            self.primero = self.ultimo = nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodo(dato)
            self.ultimo.anterior = aux
        self.contador += 1

    def _agregar_inicio(self, dato):
        if self._vacia():
            self.primero = self.ultimo = nodo(dato)
        else:
            aux = nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux

    def _recorrer_adelante(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

    def _recorrer_atras(self):
        aux = self.ultimo
        while aux != None:
            print(aux.dato)
            aux = aux.anterior


    def _size(self):
        return self.contador
        
lista = listaDoble()

# lista._agregar_inicio(1)
# lista._agregar_inicio(2)
# lista._agregar_inicio(3)
# lista._agregar_inicio(5)
# lista._agregar_inicio(7)
# lista._recorrer_adelante()





