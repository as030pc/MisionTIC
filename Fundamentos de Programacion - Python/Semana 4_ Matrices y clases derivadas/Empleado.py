"""Clase Padre"""
class Empleado:
    def __init__(self, nom,id,suel):
        self.nombre=nom
        self.id=id
        self.sueldo=suel

    def devolverSueldo(self):
        return self.sueldo
        # print(self.sueldo)

    def __str__(self):
        return f"nombre: {self.nombre} id: {self.id} sueldo:{self.sueldo}"


"""Clase Hija - Gerente"""
class Gerente(Empleado):

    def sueldoGerente(self):
        self.sueldo=self.sueldo+100
        #s1=super().devolverSueldo()+100
        print(self.sueldo)

"""PROGRAMA PRINCIPAL"""
# em=Empleado("em1","10",10)
ger1=Gerente("ger1","20",500)
ger1.sueldoGerente()

ger2=Gerente("ger2","10",300)

em=Empleado("em1","10",200)
print(em)
# print(ger1)
# ger1.devolverSueldo()
