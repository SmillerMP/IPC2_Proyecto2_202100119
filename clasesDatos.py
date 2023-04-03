
# ------------ CLASES PARA LA LISTA DE COMPUESTO ---------------- #
class dataCompuesto():
    def __init__(self, nombreCompuesto, numeroCompuesto, listaCompuestos):
        self.nombreCompuesto = nombreCompuesto
        self.numeroCompuesto = numeroCompuesto
        self.listaCompuestos = listaCompuestos

class dataCompuestoElemento():
    def __init__(self, elemento, numeroElemento):
        self.elemento = elemento
        self.numeroElemento = numeroElemento



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



# ------------ CLASES PARA LA LISTA DE ELEMENTOS PRINCIPAL ---------------- #
class dataElementosGeneral():
    def __init__(self, contador, numeroAtomico, simbolo, nombreElemento):
        self.contador = contador
        self.numeroAtomico = numeroAtomico
        self.simbolo = simbolo
        self.nombreElemento = nombreElemento
# ---------------------------------------------------------------------------




# ------------ DATOS DE ELEMENTOS ENCONTRADOS EN LOS PINES  ---------------- #
class elementosEncontrados():
    def __init__(self, numeroMaquina, numeroPin, contadorElemento, elementoEncontrado):
        self.numeroMaquina = numeroMaquina
        self.numeroPin = numeroPin
        self.contadorElemento = contadorElemento
        self.elementoEncontrado = elementoEncontrado

class estadosActuales():
    def __init__(self, pin, posicion, EnUso):
        self.pin = pin
        self.posicion = posicion
        self.EnUso = EnUso

    def set_EnUso(self, estado):
        self.EnUso = estado

    def set_posicion(self, nuevo):
        self.posicion = nuevo

        
# -----------------------------------------------------------------------------