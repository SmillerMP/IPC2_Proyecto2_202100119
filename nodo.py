from clasesDatos import *

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
        self.contador += 1

    def _recorrer_adelante(self):
        aux = self.primero
        while aux != None:
            print(aux.dato.maquina, aux.dato.pin, aux.dato.indice, aux.dato.simboloElemento)
            aux = aux.siguiente

    def _recorrer_atras(self):
        aux = self.ultimo
        while aux != None:
            print(aux.dato)
            aux = aux.anterior


    def _size(self):
        print(self.contador)



class ListaSimple():
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


    def _recorrer(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

    def _size(self):
        return(self.contador)
        




# lista = listaDoble()
# lista2 = listaDoble()

# lista._agregar_inicio(1)
# lista._agregar_inicio(2)
# lista._agregar_inicio(3)
# lista._agregar_inicio(5)
# lista._agregar_inicio(6)
# lista._recorrer_adelante()
# lista._size()

# lista2._agregar_inicio(22)
# lista2._agregar_inicio(33)
# lista2._agregar_inicio(44)
# lista2._agregar_inicio(55)
# lista2._agregar_inicio(66)
# lista2._recorrer_adelante()
# lista2._size()




# lista = listaCompuesto()
# lista._agregar_final(1)
# lista._agregar_final(2)
# lista._agregar_final(3)
# lista._agregar_final(5)
# lista._agregar_final(6)
# lista._recorrer()
# lista._size()


class colaCompuestos():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cola = []

    def _getPrimero(self):
        return self.primero
    
    def _getUltimo(self):
        return self.ultimo
    
    def _agregarCola(self, dato):
        self.cola.append(dato)
        self.final = dato
        return self.ultimo
    
    def _borrarCola(self):
        self.cola.pop(0)
        self.primero = self.cola[0]
        return self.primero
    
    def _size(self):
        print(len(self.cola))
    
    def _recorrer(self):
        return 
