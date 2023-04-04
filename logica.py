from carga import *
from clasesDatos import *
from nodo import *

cargaArchivo()

colaDirecciones = cola()

lista_ElementosGeneral = get_listaElementosGeneral()
lista_Maquinas = get_listaMaquinas()
lista_Compuestos = get_Compuestos()
listaPasosGenerales = ListaSimple()
listaPasosEspecificos = ListaSimple()
listaPinesUso = ListaSimple()

# #---------- RECORRRIDO LISTA ELEMENTOS GENERAL ------------#
# nodo_actual = lista_ElementosGeneral.primero
# while nodo_actual != None:
#     print(f"No. {nodo_actual.dato.contador} --> No. Atomic: {nodo_actual.dato.numeroAtomico} --> Simbolo: {nodo_actual.dato.simbolo} --> Nombre: {nodo_actual.dato.nombreElemento}")
#     nodo_actual = nodo_actual.siguiente


# #---------- RECORRRIDO LISTA MAQUINAS ------------#
# nodo_primeroMaquinas = lista_Maquinas.primero
# while nodo_primeroMaquinas != None:
#     nodo_pines = nodo_primeroMaquinas.dato.listaPines.primero
#     while(nodo_pines != None):
#         nodo_elementos = nodo_pines.dato.listaPin.primero
#         while(nodo_elementos != None):
#             print(f"Maquina: {nodo_primeroMaquinas.dato.numeroDeMaquina} --> Pin: {nodo_pines.dato.contadorPin} --> Elemento: {nodo_elementos.dato.elementoPin}")

#             nodo_elementos = nodo_elementos.siguiente
#         nodo_pines = nodo_pines.siguiente
#     nodo_primeroMaquinas = nodo_primeroMaquinas.siguiente


# #---------- RECORRRIDO LISTA COMPUESTOS ------------#
# nodo_actualCompuestos = lista_Compuestos.primero
# while nodo_actualCompuestos != None:
#     nodo_actualElementos = nodo_actualCompuestos.dato.listaCompuestos.primero
#     while nodo_actualElementos != None:
#         print(f"Compuesto: {nodo_actualCompuestos.dato.nombreCompuesto, nodo_actualCompuestos.dato.numeroCompuesto} --> Elemento: {nodo_actualElementos.dato.elemento} --> No.: {nodo_actualElementos.dato.numeroElemento}")
#         nodo_actualElementos = nodo_actualElementos.siguiente
#     nodo_actualCompuestos = nodo_actualCompuestos.siguiente


"""
Recorre la lista de compuestos en busca de donde esta cada uno
de los elementos en la lista de las maquinas
"""
def recorridoCompuesto(compuesto):
    encontrado = False
    colaDirecciones = cola()
    print(colaDirecciones._size())
    nodo_actualCompuestos = lista_Compuestos.primero
    while nodo_actualCompuestos != None:

        if compuesto == nodo_actualCompuestos.dato.nombreCompuesto:
            encontrado = True
            nodo_actualElementos = nodo_actualCompuestos.dato.listaCompuestos.primero
            while nodo_actualElementos != None:

                #print(f"Compuesto: {nodo_actualCompuestos.dato.nombreCompuesto, nodo_actualCompuestos.dato.numeroCompuesto} --> Elemento: {nodo_actualElementos.dato.elemento} --> No.: {nodo_actualElementos.dato.numeroElemento}")
                buscador(nodo_actualElementos.dato.elemento)

                nodo_actualElementos = nodo_actualElementos.siguiente
        nodo_actualCompuestos = nodo_actualCompuestos.siguiente

    if encontrado == False:
        print(f"No se ha encontrado el compuesto: {compuesto}")



# Buscador de elementos en la lista de maquinas
def buscador(elementoCompuesto):
    encontrado = False
    nodo_primeroMaquinas = lista_Maquinas.primero
    while nodo_primeroMaquinas != None:
        nodo_pines = nodo_primeroMaquinas.dato.listaPines.primero

        while(nodo_pines != None):
            nodo_elementos = nodo_pines.dato.listaPin.primero

            while(nodo_elementos != None):
                #print(f"Maquina: {nodo_primeroMaquinas.dato.numeroDeMaquina} --> Pin: {nodo_pines.dato.contadorPin} --> Elemento: {nodo_elementos.dato.elementoPin}")
                if nodo_elementos.dato.elementoPin == elementoCompuesto:
                    #print(f"Encontrado!!!!!!!! Maquina: {nodo_primeroMaquinas.dato.numeroDeMaquina} --> Pin: {nodo_pines.dato.contadorPin} --> Elemento: {nodo_elementos.dato.elementoPin} --> Contador Elemento: {nodo_elementos.dato.contadorElemento}")
                    encontrado = True
                    data_temp = elementosEncontrados(nodo_primeroMaquinas.dato.numeroDeMaquina, nodo_pines.dato.contadorPin, nodo_elementos.dato.contadorElemento, nodo_elementos.dato.elementoPin)
                    colaDirecciones._agregarCola(data_temp)

                    #estadosActualesElementos._agregar_final(data_temp)

                if encontrado == True:
                    break
                nodo_elementos = nodo_elementos.siguiente

            if encontrado == True:
                break
            nodo_pines = nodo_pines.siguiente

        if encontrado == True:
            break
        nodo_primeroMaquinas = nodo_primeroMaquinas.siguiente


def existePines(pinBuscar):
        aux = listaPinesUso.primero
        encontrado = False
        while aux != None:
            if aux.dato.pin == pinBuscar:
                encontrado = True
                break
            aux = aux.siguiente
        return encontrado

def completo():
    contador = 0
    nodo_actual = listaPinesUso.primero
    while nodo_actual != None:
        if nodo_actual.dato.EnUso == True:
            contador += 1

        nodo_actual = nodo_actual.siguiente

    if listaPinesUso._size() == contador:
        return True
    else:
        return False


def recorerPosicionesPines():
    nodo_actual = listaPinesUso.primero
    while nodo_actual != None:
        print(f"Pin: {nodo_actual.dato.pin}, Posicion: {nodo_actual.dato.posicion}")
        nodo_actual = nodo_actual.siguiente

recorridoCompuesto("Micol")

def recorrerCola():
    direcciones = colaDirecciones.cola
    for x in direcciones:
        print(f"Maquina: {x.numeroMaquina}, Pin: {x.numeroPin}, No. Elemento: {x.contadorElemento}, Elemento: {x.elementoEncontrado}")

recorrerCola()
# colaDirecciones._borrarCola()

# print("\n")
# recorrerCola()

print(colaDirecciones._size())


for x in colaDirecciones.cola:
    if (existePines(x.numeroPin)) == False:
        data_temp = estadosActuales(x.numeroPin, 0, False, -1)
        listaPinesUso._agregar_final(data_temp)

recorerPosicionesPines()

# nodo_actual = estadosActualesElementos.primero
# while nodo_actual != None:
#     print(f"Elemento: {nodo_actual.dato.elemento}, Posicion: {nodo_actual.dato.posicion}")
#     nodo_actual = nodo_actual.siguiente

print(colaDirecciones.cola[0].elementoEncontrado)
print("\n\n")

pasos = 0
fusion = False
fusionar = 0
movimiento = -1
while colaDirecciones._size() != 0:
    pasos += 1

    if fusion == True:
        colaDirecciones._borrarCola()
    print("\n")
    direcciones = colaDirecciones.cola
    print("reinicio", pasos)
    fusion = False
    for x in direcciones:
        
        indice = direcciones.index(x)
        nodoPosicion = listaPinesUso.primero
        while nodoPosicion != None:
            if nodoPosicion.dato.EnUso == False:
                #print(f"Maquina: {x.numeroMaquina}, Pin: {x.numeroPin}, No. Elemento: {x.contadorElemento}, Elemento: {x.elementoEncontrado}")
                if (nodoPosicion.dato.pin == x.numeroPin) and (nodoPosicion.dato.posicion < x.contadorElemento) and fusion == False:
                    nodoPosicion.dato.set_posicion(x.contadorElemento)
                    nodoPosicion.dato.set_contadorCola(indice)
                    nodoPosicion.dato.set_EnUso(True)
                    print("Entro Adelante")
                    movimiento = 1
                    break

                elif(nodoPosicion.dato.pin == x.numeroPin) and (nodoPosicion.dato.posicion > x.contadorElemento) and fusion == False:
                    nodoPosicion.dato.set_posicion(x.contadorElemento)
                    nodoPosicion.dato.set_contadorCola(indice)
                    nodoPosicion.dato.set_EnUso(True)
                    movimiento = 2
                    print("Entro Atras")
                    break

            if(nodoPosicion.dato.pin == x.numeroPin) and (nodoPosicion.dato.posicion == x.contadorElemento) and (fusion == False) and colaDirecciones.cola[0].elementoEncontrado == x.elementoEncontrado:
                nodoPosicion.dato.set_posicion(x.contadorElemento)
                nodoPosicion.dato.set_EnUso(False)
                direcciones = colaDirecciones.cola
                fusion = True
                movimiento = 3
                print(f"Entro Fusion Elemento {x.elementoEncontrado} --> Pin: {nodoPosicion.dato.pin}")
                break
                

            elif (nodoPosicion.dato.pin == x.numeroPin) and (nodoPosicion.dato.posicion == x.contadorElemento) and (fusion == True or fusion == False):
                nodoPosicion.dato.set_posicion(x.contadorElemento)
                nodoPosicion.dato.set_EnUso(True)
                print("Entro Espera")
                movimiento = 0

            nodoPosicion = nodoPosicion.siguiente
pasos -= 1

print(pasos)




""""
PSEUDOCODIGO
1 adelante, 2 atras, 0 esperar, 3 fusionar
si momento actual es menor que no. elemento, resultado 1
si momento actual es mayor que no. elemento, resultado 2
si momento actual es == que no. elemento fusionar

hacer una lista para ver que pines ya estan en uso,
en caso de que el pin ya este en uso esperar en caso de que
se fucione el elemento borrar de la lista el pin en uso

"""