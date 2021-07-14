class Pila:
    def __init__(self): #Constructor
        self.items = [] #Inicializar pila

    def apilar(self, item):
        self.items.append(item)  #Se agragan elementos en el append

    def desapilar(self):
        if(not self.estaVacia()):
            return self.items.pop()

    #retorna el dato que eta en la cima
    def cima(self):
        if(not self.estaVacia()):
            return self.items[len(self.items)-1] #En las listas la indexacion va de 0 a n

    def tamanio(self):
        return len(self.items)

    def estaVacia(self):
        if(self.items==[]):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.items}"     #Permite visualizar la pila

# ---------------------------------------------------------------
elem=Pila()   # Se crea un elemento de la clase pila

elem.apilar("Lunes")
elem.apilar("Martes")
elem.apilar("Miércoles")
elem.apilar("Jueves")
print(elem)
elem.desapilar()
print(elem)
# print(elem.cima())
# print(elem)

# print(elem.tamanio())
# print(elem.cima())

#desapilar hasta vaciar
# while not elem.estaVacia():
#    elem.desapilar()


# print(elem)

