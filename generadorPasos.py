from graphviz import Digraph
from logica import get_listaPasosGenerales
import os

listaPasos = get_listaPasosGenerales()

dot = Digraph(name='grafos.dot', format='png', engine='dot')


# nodo_actual = listaPasos.primero
# while nodo_actual != None:
#     print(nodo_actual.dato)
#     nodo_actual = nodo_actual.siguiente

def graficarGrafo(lista):

    
    grafo_dot = open("grafos.dot", "w")
    grafo_dot.write('digraph { \n')
    grafo_dot.write('rankdir = LR \n' )
    grafo_dot.write('node[shape=record, fontname="Arial", fontsize=15] \n')


            
    grafo_dot.write("} \n")
    grafo_dot.close()


    dot.render("grafos.dot", view=True)




    