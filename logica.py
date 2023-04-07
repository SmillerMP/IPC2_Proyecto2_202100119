from carga import *
from clasesDatos import *
from nodo import *


colaDirecciones = cola()
colaDireccionesClon = ListaSimple()

lista_ElementosGeneral = get_listaElementosGeneral()
lista_Maquinas = get_listaMaquinas()
lista_Compuestos = get_Compuestos()
listaPasosEspecificos = ListaSimple()
listaPinesUso = ListaSimple()
lisaPrimerosPines = ListaSimple()

listaPasosGenerales = ListaSimple()
def get_listaPasosGenerales():
    return listaPasosGenerales


def logica(compuestoFusionar, maquina):
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
                    if buscador(nodo_actualElementos.dato.elemento) == False:
                        return False

                    nodo_actualElementos = nodo_actualElementos.siguiente
            nodo_actualCompuestos = nodo_actualCompuestos.siguiente

        if encontrado == False:
            print(f"No se ha encontrado el compuesto: {compuesto}")
            return encontrado
            



    # Buscador de elementos en la lista de maquinas
    def buscador(elementoCompuesto):
        encontrado = False
        contador = 0
        nodo_primeroMaquinas = lista_Maquinas.primero
        while nodo_primeroMaquinas != None:
            if nodo_primeroMaquinas.dato.nombreMaquina == maquina:
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
                            colaDireccionesClon._agregar_final(data_temp)
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

        return encontrado

    def existePines(pinBuscar):
            aux = listaPinesUso.primero
            encontrado = False
            while aux != None:
                if aux.dato.pin == pinBuscar:
                    encontrado = True
                    break
                aux = aux.siguiente
            return encontrado

    def recorrerCola():
        direcciones = colaDirecciones.cola
        for x in direcciones:
            print(f"Maquina: {x.numeroMaquina}, Pin: {x.numeroPin}, No. Elemento: {x.contadorElemento}, Elemento: {x.elementoEncontrado}")



    def primerosPinesElementos():
        pines_guardados = set()
        lisaPrimerosPines = ListaSimple()
        cola = colaDirecciones.cola
        for z in cola:
            pin = z.numeroPin
            if pin not in pines_guardados:
                pines_guardados.add(pin)
                data_temp = pinesPrimeros(pin, cola.index(z))
                lisaPrimerosPines._agregar_final(data_temp)

        return lisaPrimerosPines


    def recorerPosicionesPines():
        nodo_actual = listaPinesUso.primero
        while nodo_actual != None:
            print(f"Pin: {nodo_actual.dato.pin}, Posicion: {nodo_actual.dato.posicion}, Uso: {nodo_actual.dato.EnUso}")
            nodo_actual = nodo_actual.siguiente

    if recorridoCompuesto(compuestoFusionar) != False:
        recorrerCola()
        print(colaDirecciones._size())

        listaPinesUso.limpiar()
        for x in colaDirecciones.cola:
            if (existePines(x.numeroPin)) == False:
                data_temp = estadosActuales(x.numeroPin, -1, False)
                listaPinesUso._agregar_final(data_temp)

        recorerPosicionesPines()



        pasos = 0
        fusion = False
        movimiento = -1
        listaPasosGenerales = ListaSimple()
        while colaDirecciones._size() != 0:
            pasos += 1
            pinFusionado = 0

            if fusion == True:
                colaDirecciones._borrarCola()
            #print("\n")
            direcciones = colaDirecciones.cola
            #print("reinicio", pasos)
            fusion = False
            listaPrimeros = primerosPinesElementos()
            listaPasosEspecificos = ListaSimple()
            for x in direcciones:
                
                indice = direcciones.index(x)
                nodoPosicion = listaPinesUso.primero
                while nodoPosicion != None:

                    if nodoPosicion.dato.EnUso == False:
                        #print(f"Maquina: {x.numeroMaquina}, Pin: {x.numeroPin}, No. Elemento: {x.contadorElemento}, Elemento: {x.elementoEncontrado}")
                        if (nodoPosicion.dato.pin == x.numeroPin) and (nodoPosicion.dato.posicion < x.contadorElemento) and pinFusionado != nodoPosicion.dato.pin:
                            nodoPosicion.dato.set_posicion(x.contadorElemento)
                            nodoPosicion.dato.set_EnUso(True)
                            #print("Entro Adelante")
                            movimiento = 1

                            data_temp = datosSalidaEspecificos(nodoPosicion.dato.pin, x.elementoEncontrado, movimiento, nodoPosicion.dato.posicion)
                            listaPasosEspecificos._agregar_final(data_temp)
                            break

                        elif(nodoPosicion.dato.pin == x.numeroPin) and (nodoPosicion.dato.posicion > x.contadorElemento) and pinFusionado != nodoPosicion.dato.pin:
                            nodoPosicion.dato.set_posicion(x.contadorElemento)
                            nodoPosicion.dato.set_EnUso(True)
                            movimiento = 2
                            #print("Entro Atras")

                            data_temp = datosSalidaEspecificos(nodoPosicion.dato.pin, x.elementoEncontrado, movimiento, nodoPosicion.dato.posicion)
                            listaPasosEspecificos._agregar_final(data_temp)
                            break

                        

                    if(nodoPosicion.dato.pin == x.numeroPin) and (nodoPosicion.dato.posicion == x.contadorElemento) and (fusion == False) and  (indice == 0) and colaDirecciones.cola[0].elementoEncontrado == x.elementoEncontrado:
                        nodoPosicion.dato.set_posicion(x.contadorElemento)
                        nodoPosicion.dato.set_EnUso(False)
                        pinFusionado = nodoPosicion.dato.pin
                        direcciones = colaDirecciones.cola
                        fusion = True
                        movimiento = 3
                        #print(f"Entro Fusion Elemento {x.elementoEncontrado} --> Pin: {nodoPosicion.dato.pin}")

                        data_temp = datosSalidaEspecificos(nodoPosicion.dato.pin, x.elementoEncontrado, movimiento, nodoPosicion.dato.posicion)
                        listaPasosEspecificos._agregar_final(data_temp)
                        break
                        

                    elif (nodoPosicion.dato.pin == x.numeroPin) and (nodoPosicion.dato.posicion == x.contadorElemento) :
                        

                        nodoPrimeros = listaPrimeros.primero
                        while nodoPrimeros != None:
                            if nodoPrimeros.dato.pin == nodoPosicion.dato.pin and indice == nodoPrimeros.dato.contador:
                                nodoPosicion.dato.set_posicion(x.contadorElemento)
                                nodoPosicion.dato.set_EnUso(True)
                                #print(f"Entro Espera, pin: {x.numeroPin}")
                                movimiento = 0

                                data_temp = datosSalidaEspecificos(nodoPosicion.dato.pin, x.elementoEncontrado, movimiento, nodoPosicion.dato.posicion)
                                listaPasosEspecificos._agregar_final(data_temp)

                            nodoPrimeros = nodoPrimeros.siguiente
        
                    nodoPosicion = nodoPosicion.siguiente

            data_temp = datosSalidaGeneral(pasos, listaPasosEspecificos)
            listaPasosGenerales._agregar_final(data_temp)
        pasos -= 1

        #print(pasos)
        return listaPasosGenerales

    else:
        return False




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