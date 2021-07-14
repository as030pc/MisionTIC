#from Nodo import Nodo
class Nodo():
    def __init__(self, dato=None):
        self.dato = dato
        self.enlace=None

    def __str__(self):
        return f" Dato: {self.dato} Enlace:{self.enlace} "
"""Clase ColaE"""


class ColaE:
    """ Crea una cola vacía. """

    def __init__(self):

        self.primero = None #Variables de control
        self.ultimo = None

    """ Agrega el elemento x como último de la cola. """

    def agregar(self, x):
        nuevo = Nodo(x)

        if self.ultimo != None:
            #Permiten que se enlacen
            self.ultimo.enlace = nuevo  # ultimo apunta al primer dato
            self.ultimo = nuevo

        # si estaba vacia el primero es también el ultimo
        else:
            self.primero = nuevo
            self.ultimo = nuevo

    def quitar(self):
        """ Elimina el primer elemento de la cola y devuelve su
            valor. Si la cola está vacía, levanta ValueError. """
        # Si hay un nodo para desencolar
        if self.primero!=None:
            valor = self.primero.dato
            self.primero = self.primero.enlace

            if(self.primero==None):
                self.ultimo=None
                return "eliminado",valor
            else:
                return "eliminado",valor
        else:
            return "no hay para eliminar"

    def print_list(self):
        nodoaux= self.primero
        while nodoaux != None:
            print(nodoaux.dato, end=" => ")
            nodoaux = nodoaux.enlace
        print("\n")

    def tamanio(self):
        nodo = self.primero
        cont=0
        while nodo != None:
            cont+=1
            nodo = nodo.enlace
        return cont

    def inicioCola(self):
        return self.primero.dato

    def es_vacia(self):
        """ Devuelve True si la cola esta vacía, False si no."""
        return self.primero == None


ce = ColaE()
ce.agregar(1)
ce.agregar(2)
ce.agregar(3)
ce.agregar(4)
ce.agregar(5)


print(ce.quitar())
print(ce.quitar())
ce.print_list()
print(ce.inicioCola())


#
# print(ce.quitar())
#
# print(ce.quitar())
# print(ce.quitar())

# print(ce.quitar())
# print(ce.primero)
ce.print_list()

# print(ce.primero.enlace.enlace.dato)
# while ce.primero!=None:
#     print(ce.primero.dato)
#     ce.primero=ce.primero.enlace