class Cola:
    def __init__(self):
        self.items = [] #Constructor, permite que items sea una variable global

    def agregar(self, item):
        # self.items.insert(0,item)
        self.items.append(item)

    def quitar(self):
        if(not self.estaVacia()):
            # return self.items.pop()
            return self.items.pop(0)  #Diferencia con las pilas, se elimina el elemento 0 de la lista

    def inicioCola(self):
        if (not self.estaVacia()):
            return self.items[0]

    def tamano(self):
        return len(self.items)

    def estaVacia(self):
        return self.items == []

    def __str__(self):
        return f"\n items: {self.items}"


"""PROGRAMA PRINCIPAL"""
#c=Cola() #Llama al metodo de constructor
# print(c.estaVacia())
# #
# c.agregar(1)
#
# c.agregar(2)
# c.agregar(3)
# c.agregar(4)
# # print(c)
# c.quitar()
# # print(c)
# ic = c.inicioCola()
# print(ic)
# print(c.tamano())
# # c.quitar()
# #
# #
# #
# # print(c)
# # c.agregar(5)
# # print(c)
# # # print(c.estaVacia())
# # print("tamaño: ",c.tamano())
# #
# # print(c.inicioCola())