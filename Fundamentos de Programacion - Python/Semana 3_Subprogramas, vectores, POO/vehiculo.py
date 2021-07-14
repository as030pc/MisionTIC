"""Estructura de datos"""
class Vehiculo:
    # color = 'ROJO'
    # matricula= 'f22fa'
    # gasolina = 20
    # gasolinaentanque = 3
    # paseactivo = True


# Metodo especial constructor: init, permite que las variables sean mas dinamicas
    def __init__(self, col, matri, gasol, pa):
        self.color = col
        self.matricula = matri
        self.gasolinaentanque = gasol
        self.paseactivo = pa

    def __str__(self):
        return "Color: " + self.color + "Matricula: "+ self.matricula+ 'Pase: '+ str(self.paseactivo)




    def verColor(self):
        print(self.color)


    def cambiarColor(self, cl):
        self.color = cl

    def devolverColor(self):
        return self.color

    def verGasolina(self):
        print(self.gasolinaentanque)


    def cargarGasolina(self,galonesacargar):
        self.gasolinaentanque = self.gasolinaentanque + galonesacargar
        return self.gasolinaentanque

    def hayGasolina(self, kilometros):

        aux = self.gasolinaentanque - kilometros
        if(aux >=0):
            return True
        else:
            return False
    def avanzarCincoKm(self):
        if(self.hayGasolina(5)):
            self.gasolinaentanque = self.gasolinaentanque-5
        else:
            print('No alcanza para llegar')

"""fin de estructura de datos"""

"""PROGRAMA PRINCIPAL"""

#Mostrar variables de la clases
# carro1 = Vehiculo()  #Asignacion
# print(carro1.color)
# print(carro1.matricula)
# print(carro1.paseactivo)


# Operaciones de asignacion

# carro1 = Vehiculo()
# print(carro1.color)
# carro1.color = 'Amarillo'
# print(carro1.color)


#Subprogramas en las clases
#----------------------------------------
# carro1 = Vehiculo()
# # # carro1.verColor()
# # # carro1.cambiarColor("Azul")
# # # carro1.verColor()
# # col = carro1.devolverColor()
# # print(col)
# ----------------------------------------
# carro1.verGasolina()
# #gasolinaentanque1 = carro1.cargarGasolina(30)
# carro1.verGasolina()

# ----------------------------------------
# Llega = carro1.hayGasolina(10)
# print(Llega)
# carro1.avanzarCincoKm()
# carro1.verGasolina()

#----------------------------------------
# Declaracion con init

carro1 = Vehiculo('Plateado', 'ff23', 30, True)
print(carro1)



