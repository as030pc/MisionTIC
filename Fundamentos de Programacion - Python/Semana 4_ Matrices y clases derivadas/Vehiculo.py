"""Estructura de datos"""
class Vehiculo:
    # color="Rojo"
    # matricula="f22fa"
    # gasolinaentanque=3
    # paseactivo=False

    def __init__(self,col,matri,gasol,pa):
        self.color=col
        self.matricula=matri
        self.gasolinaentanque=gasol
        self.paseactivo=pa

    def __str__(self):
        return "Color: "+self.color+" Matricula: "+self.matricula+ "gasolina: "+str(self.gasolinaentanque) +"pase: "+str(self.paseactivo)


    def verColor(self):
        # print("Hola desde verColor")
        print(self.color)
        # print(self.gasolina)
        # print(self.paseactivo)
        # print(self.matricula)

    def ponerColor(self,cl):
        self.color=cl

    def devolverColor(self):
        return self.color

    def verGasolina(self):
        print(self.gasolinaentanque)

    def devolverGasolina(self):
        return self.gasolinaentanque

    def cargarGasolina(self,galonesacargar):
        self.gasolinaentanque=self.gasolinaentanque+galonesacargar

    def gastarGasolina(self,galonesagastar):
        self.gasolinaentanque=self.gasolinaentanque-galonesagastar

    def avanzarCincokm(self):
        if(self.hayGasolinaparallegar(5)):
            self.gasolinaentanque=self.gasolinaentanque-5
        else:
            print("No alcanza para llegar")

    def avanzarDiezkm(self):
        self.gasolinaentanque=self.gasolinaentanque-10

    def hayGasolinaparallegar(self,galonesagastar):
        aux=self.gasolinaentanque-galonesagastar
        #aux=5-5= 0
        if(aux>=0):
            return True
        else:
            return False


"""fin de estructura de Datos"""
"""----------------------------"""
"""PROGRAMA PRINCIPAL"""
carro1=Vehiculo("Plateado","ff233",30,True)
print(carro1)




#crear 3 carros con metodo especial constructor
carro2=Vehiculo("Negro","gga33",10,False)
carro3=Vehiculo("Verde","eeadf",20,True)

carro1.avanzarDiezkm()
# carro1.verGasolina()

carro2.avanzarCincokm()
# carro2.verGasolina()

carro3.avanzarDiezkm()
# carro3.verGasolina()

print(carro1)
print(carro2)
print(carro3)







#avanzarCincokm
# carro1.verGasolina()
# carro1.avanzarCincokm()
# carro1.verGasolina()
# carro1.cargarGasolina(10)
# carro1.avanzarCincokm()
# carro1.verGasolina()



# carro1.avanzarCincokm()
# carro1.verGasolina()
# carro1.avanzarDiezkm()
# carro1.avanzarDiezkm()
# carro1.avanzarDiezkm()
# carro1.verGasolina()











#GASOLINA


# carro1.cargarGasolina(20)
# carro1.verGasolina()
# carro1.cargarGasolina(5)
# carro1.verGasolina()
# carro1.gastarGasolina(10)
# carro1.verGasolina()
# n=15
# carro1.gastarGasolina(n)
# carro1.verGasolina()


# gasol=carro1.devolverGasolina()
# print(gasol)




# carro1.verColor()
# col=carro1.devolverColor()


# carro1.cambiarColor("Azul")
# carro1.ponerColor("Plateado")
# carro1.verColor()







"""Asignar valores y mostrar"""
# print(carro1.color,carro1.matricula,carro1.gasolina,carro1.paseactivo)
# carro1.color="Amarillo"
# carro1.matricula="ggg233"
# carro1.gasolina=10
# carro1.paseactivo=True
#
# print(carro1.color,carro1.matricula,carro1.gasolina,carro1.paseactivo)





"""MOSTRAR VARIABLES"""
# print(carro1.color)
# print(carro1.matricula)
# print(carro1.gasolina)
# print(carro1.paseactivo)