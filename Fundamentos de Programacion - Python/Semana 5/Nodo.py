class Nodo():
    def __init__(self, dato=None):
        self.dato = dato
        self.enlace=None

    def __str__(self):
        return f" Dato: {self.dato} Enlace:{self.enlace} "

"""
-crear nodos
-mostrar con str y directamente
-enlazar 2 nodos y mostrar con __str y directo
-enlazar 2,3,4 nodos y mostrar con __str y directo
-Eliminar un nodo

"""
#
n1=Nodo(10)

n2=Nodo(20)


n2.enlace=n1
n3=Nodo(30)
n3.enlace=n2

ultimo =  n3
while (ultimo!=None):
    print(ultimo.dato,end=" ")
    ultimo=ultimo.enlace
print()
#
# n4=Nodo(40)
# #

#
# n3.enlace=n2
#
# n4.enlace=n3
# #
# # print(n4)
# # print(n4.enlace.enlace.enlace.enlace)
# # print(n4)
# # n3.enlace=n1
# # print(n4)
# # print(n2)
# # n2=None
# # print(n2)
#
#
# # print(n4)
# # ultimo=n4

