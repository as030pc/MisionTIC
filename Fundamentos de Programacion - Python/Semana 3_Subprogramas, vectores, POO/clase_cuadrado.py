class Cuadrado:
    def __init__(self, lado):
        self.a = lado

    def area(self):
        ar = self.a**2
        return ar
        #print('el area es: ',ar)
    def perimetro(self):
        per = 4*self.a
        return per
    def __str__(self):
        return f"el cuadrado tiene un lado de {self.a}"


class Rectangulo:
    def __init__(self, lado1, lado2):

        self.a1 = lado1
        self.b = lado2
    def areaR(self):
        arR = self.a1 * self.b
        return arR
    def perimetroR(self):
        perR = 2*self.a1 + 2*self.b
        return perR

"""Programa principal"""

#CUADRADO
#Area
c1 = Cuadrado(10)
c2 = Cuadrado(20)
areac1 = c1.area()
print(areac1)



# LISTAS CON OBJETOS
lista = []
lista.append(c1)
lista.append(c2)
print(lista)

for i in range(0,2):
    area = int(input("area: "))
    cua = Cuadrado(area)
    lista.append(cua)

for i in lista:
    print(i.area())

#Perimetro
#
# perimetro = c1.perimetro()
# print(perimetro)
# #Leer
# print(c1)


#RECTANGULO
#R1 = Rectangulo(3,4)
#print(f'El area del rectangulo es {R1.areaR()} y el perimetro es {R1.perimetroR()}')