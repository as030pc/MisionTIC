# Creamos la clase node
class Nodo:
    def __init__(self, dato = None, enlace = None):
        self.dato = dato
        self.enlace = enlace

# Creamos la clase linked_list
class ListaE:
    def __init__(self):
        self.cabeza = None

    # Método para agregar elementos en el frente de la linked list
    def agregarAlFrente(self, dato):

        nuevo=Nodo(dato)
        if self.cabeza != None:

            nuevo.enlace = self.cabeza  # ultimo apunta al primer dato
            self.cabeza = nuevo

        # si estaba vacia el primero es también el ultimo
        else:
            self.cabeza = nuevo


    def estaVacia(self):
        return self.cabeza == None

    # Método para agregar elementos al final de la linked list
    def agregarAlFinal(self, dato):
        if not self.cabeza:
            self.cabeza = Nodo(dato=dato)
            return
        actual = self.cabeza
        while actual.enlace:
            actual = actual.enlace
        actual.enlace = Nodo(dato=dato)

    # Método para agregar elementos en una posición especifica de la lista
    def agregarEnPosicion(self, data, position):
        actual = self.cabeza
        acutal_pos = 0
        if not self.estaVacia():
            while actual and acutal_pos != position:
                node_replace = actual
                actual = actual.enlace
                acutal_pos += 1
            node_replace.enlace = Nodo(dato=data, enlace=actual)
        else:
            self.agregarAlFrente(data)



    def buscarDato(self,valor):
        nodo = self.cabeza
        con=0
        while (nodo != None):
            if(nodo.dato==valor):
                return con
            nodo = nodo.enlace
            con+=1

        return -1

    def obtenerPrimerNodo(self):
        return self.cabeza.dato

    # Método para obtener el ultimo nodo
    def obtenerUltimoNodo(self):
        nodo = self.cabeza
        while(nodo.enlace !=None):
            nodo = nodo.enlace
        return nodo.dato

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.cabeza
        while node != None:
            print(node.dato, end =" => ")
            node = node.enlace
        print("\n")


l = ListaE() # Instancia de la clase
l.agregarAlFrente(1) # Agregamos un elemento al frente del nodo
l.agregarAlFrente(2)
l.agregarAlFrente(3)
l.print_list()
l.agregarEnPosicion(10,2)
l.agregarEnPosicion(20,1)
l.agregarAlFinal(100)
l.agregarAlFinal(200)
print("primer",l.obtenerPrimerNodo())

l.print_list()
print("pos:",l.buscarDato(1))



# l.add_at_end(1)
# l.add_at_end(2)
# l.add_at_end(3)
# l.add_at_end(8)
l.print_list()
# print(l.obtenerUltimoNodo())


#
# s.add_at_end(8) # Agregamos un elemento al final del nodo
# s.add_at_front(9) # Agregamos otro elemento al frente del nodo
# s.add_at_position(18,2) # Agregamos un elemento en la posición 1
# s.print_list() # Imprimimos la lista de nodos
# s.delete_node(18) #Borrar nodo por valor
# s.print_list() # Imprimimos la lista de nodos